# Generador de páginas interiores

Las 10 páginas interiores (3 legales + 7 de servicio) se generan desde aquí
para que compartan cabecera, píldora de navegación y pie. Si cambia la
identidad de la clínica, el teléfono o el pie, se toca **un solo sitio** y se
reconstruye todo:

```bash
python .build/build.py
```

- `pagegen.py` — cabecera, navegación, pie y banner de cookies compartidos.
- `legal.py` — textos de aviso legal, privacidad y cookies.
- `servicios.py` — contenido de cada uno de los siete servicios.
- `build.py` — ensambla y escribe los `.html` en la raíz.

> Si editas un `.html` generado a mano, el siguiente `build.py` lo sobrescribe.
> Los cambios van en los archivos de datos de esta carpeta.
