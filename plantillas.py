# coding: utf-8

#         app: Generador de Modelos
#      módulo: main
# descripción: Generar modelos usando Python
#       autor: Javier Sanchez Toledano
#       fecha: martes, 19 de mayo de 2015

HEADER = """{% extends "2014/metas/forms/evidencia.html" %}
{% load sgc %}

{% block formulario %}
"""

FOOTER: str = """
{% endblock formulario %}"""


class Plantilla:
    def __init__(self, meta):
        self.miembro = meta['miembro']
        self.id = meta['id']
        self.nombre = meta['nombre']
        self.repeticiones = meta['repeticiones']
        self.campos = meta['campos']

    def get_campos(self):
        return self.campos

    def get_meta(self):
        return '%s%02d' % (self.miembro.upper(), self.id)


if __name__ == '__main__':
    import yaml
    import codecs

    MIEMBRO = 'josas'

    file = '%s.yml' % MIEMBRO.lower()
    metas = yaml.load_all(open(file, encoding='utf-8').read(), Loader=yaml.Loader)

    for m in metas:
        control = ''
        file = "forms/%s%02d.html" % (m['miembro'].lower(), m['id'])
        f = codecs.open(file, mode="w", encoding="utf-8-sig")
        cam = m['campos']
        f.write(HEADER)
        for c in cam:
            for k, v in c.items():
                control += '''
    <div class="form-group">
      <label class="col-sm-2 control-label" for="id_{campo}">{nombre}</label>
      <div class="col-sm-8">
        {{{{ form.{campo} }}}}
        <p class="help-block">
          Seleccione el archivo para esta evidencia, 
          <em>preferentemente <strong>en formato PDF</strong></em>
        </p>
      </div>
    </div>
    '''.format(campo=k, nombre=v[0])
        f.write(control)
        f.write(FOOTER)
        f.close()
