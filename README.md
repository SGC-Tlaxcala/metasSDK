# metasSDK

El generador de modelos para las metas del SPEN usa un archivo
especial de definiciones en (YAML)[1] para especificar como
se forma un ciclo de evidencias para una meta.

### Ejemplo

Para este ejemplo vamos a trabajar con la meta INFOMAC del Jefe
de Monitoreo de Módulos. Esta meta consiste en reportar en el
INFOMAC cada inicio de campaña la información de los módulos.

Como son dos campañas al año, consideramos dos ciclos o repeticiones
para esta meta. Cada ciclo o repetición debe constar de tres evidencias:

- Reporte de validación
- Oficio o correo electrónico al VRL
- Oficio o correo de la DOS

Todas las evidencias son obligatorias.

Con estos datos construimos el archivo de definiciones.

```yaml
miembro: String
id: Int
nombre: String
campos:
  - String: [String, Boolean]
```

Estos son los elementos del archivo de definiciones:

- __`miembro`__: Es la clave del puesto, tal como aparece en las metas del SPEN.
- __`id`__: El identificador de la meta, que también determina el SPEN.
- __`nombre`__: Un nombre corto para identificar a la meta.
- __`campos`__: Es la lista de evidencias que deben incluirse en cada ciclo. Cada campo tiene tres elementos:
    - _nombre del campo_: Es el nombre del campo, en minúsculas de preferencia, sin espacios.
    - _descripción_: Un texto que describa la evidencia.
    - _obligatorio_: Es una marca _booleana_ para indicar que el campo es obligatorio. True o true, False o false

```yaml
miembro: JMM
id: 1
nombre: INFOMAC
campos:
  - reporte: ['Reporte de validación', false]
  - correo: ['Oficio o correo electrónico al VRL', false]
  - oficioDOS: ['Oficio o correo de la DOS', false]
```

[1]: http://yaml.org/spec/1.2/spec.html