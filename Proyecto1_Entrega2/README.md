<h1>Guía de instalación API Turismo</h1>
<h2>Creación de ambiente en Python</h2>
Ubiquese en la carpeta del proyecto y abra la consola de Visual Studio Code.

Escriba el siguiente comando en la consola:
``` python -m venv environment ```

Cuando se genere el ambiente ejecute:

1. ``` CTRL + Shift + P ```
2. Escriba en el buscador *Python: Select Interpeter* y seleccione el interprete con el nombre "Environment".
3. Elimine y vuelva a abrir su consola en Visual Studio Code.

<h2>Instalar librerias</h2>
Luego de haber seleccionado el ambiente, ejecute el siguiente comando en consola:

``` pip install -r requirements.txt ```

<h2>Correr el servidor con el API</h2>
Ubiquese en la carpeta con el código fuente del API, para esto ejecute el siguiente comando en consola:


``` cd turismo_site ```

Para ejecutar el servidor en el localhost:8000 ejecute el siguiente comando:

``` python manage.py runserver ```

Este comando ejecutará el servidor y expondrá su acceso en http://127.0.0.1:8000/

Para salir del servidor ejecute ``` CTRL + C ```

<h1>Guía de instalación interfaz gráfica</h1>

NOTA: Es necesario que tenga instalado node en su equipo.

Ejecute otra consola aparte de la consola del API.

Ubiquese en la carpeta con el código fuente del GUI, para esto ejecute el siguiente comando en consola:


``` cd  hotel-calification-ui```

Digite el siguiente comando en consola: ``` npm install```

Cuando la instalación de los modulos haya terminado, ejecute el siguiente comando: ``` npm start ```

El servidor se estará ejecutando en: http://localhost:4200/