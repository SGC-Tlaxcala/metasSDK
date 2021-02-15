# coding: utf-8
#         app: Generador de Modelos
#      módulo: main
# descripción: Generar modelos usando Python
#       autor: Javier Sanchez Toledano
#       fecha: martes, 19 de mayo de 2015

import sys

class Generador:
    def __init__(self, goal):
        self.miembro = goal['miembro']
        self.id = goal['id'].replace('-', '')
        self.campos = goal['campos']

    def get_campos(self):
        return self.campos

    def get_meta(self):
        return '%s' % (self.id.upper())

    def get_model(self):
        clase = """class %s(Evidencia):""" % self.get_meta()
        for c in self.get_campos():
            for k, v in c.items():
                try:
                    blank = u'blank=True, null=True' if v[1] else ''
                except IndexError:
                    blank = ''
                clase += \
                    u"\n    %s = models.FileField('%s', upload_to=subir_archivo, %s)" %\
                        (k, v[0], blank)
        clase += u"""\n
    class Meta:
        app_label = 'metas'
        """
        return clase

    def get_form(self):
        clase = """
class Formulario%s(FormEvidenciaBase):
    class Meta:
        model = %s\n\n""" % (self.get_meta(), self.get_meta())
        return clase


if __name__ == '__main__':
    import yaml

    IMPORTS = """
# coding: utf-8
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

    MIEMBRO = 'all'

    file = '%s.yml' % MIEMBRO.lower()
    salida = f'./mspe/{MIEMBRO.lower()}.py'
    f = None

    try:
        f = open(salida, 'w', encoding='utf-8')
    except FileNotFoundError:
        print("No puedo escribir el archivo de salida")
        sys.exit()

    try:
        metas = yaml.load_all(open(file, encoding='utf-8').read(), Loader=yaml.Loader)
        f.write(IMPORTS)
        for meta in metas:
            m = Generador(meta)
            f.write(m.get_model())
            f.write(m.get_form())
        print("Archivo generado con éxito")
    except FileNotFoundError:
        print('No puedo abrir el archivo')
