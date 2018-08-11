# coding: utf-8
#         app: Generador de Modelos
#      módulo: main
# descripción: Generar modelos usando Python
#       autor: Javier Sanchez Toledano
#       fecha: martes, 19 de mayo de 2015


import yaml
MIEMBRO = 'josa'
VERSION = 1.0

IMPORTS = """# coding: utf-8
from django.conf import settings
from django.db import models
from core.models import Pipol, PUESTOS
from django.contrib.contenttypes.models import ContentType
from django import forms

from metas.models import Evidencia
from metas.models import subir_archivo
from metas.forms import FormEvidenciaBase

from django.contrib.auth import get_user_model
User = get_user_model()
"""


class Generador:
    def __init__(self, goal):
        self.miembro = goal['miembro']
        self.id = goal['id']
        self.nombre = goal['nombre']
        self.campos = goal['campos']

    def get_campos(self):
        return self.campos

    def get_meta(self):
        return '%s%02d' % (self.miembro.upper(), self.id)

    def get_model(self):
        clase = """class %s(Evidencia):""" % self.get_meta()
        for c in self.get_campos():
            for k, v in c.items():
                blank = u'blank=True, null=True' if v[1] else ''
                clase += u"\n    %s = models.FileField('%s', upload_to=subir_archivo, %s)" % (k, v[0], blank)
        clase += u"""\n
    class Meta:
        app_label = 'metas'
        """
        return clase

    def get_form(self):
        clase = """
class Formulario%s(FormEvidenciaBase):
    class Meta:
        model = %s\n\n'""" % (self.get_meta(), self.get_meta())
        return clase


if __name__ == '__main__':
    file = '%s.yml' % MIEMBRO.lower()
    metas = yaml.load_all(open(file).read())
    print(IMPORTS)
    for meta in metas:
        m = Generador(meta)
        print(m.get_model())
        print(m.get_form())

