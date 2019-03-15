# img2pbm

Script en Python que permite convertir imagenes a formato pbm para poder mostrarlas en el display Oled con MicroPython.

## Instalación

Es necesario instalar la libreria Pillow para poder manipular las imagenes por medio de pip:

```sh
pip install Pillow
```
## Forma de uso

img2pbm acepta un solo archivo o especificar varios por medio del comodin.
Si se desea convertir el archivo dog.jpg podemos hacer:

```sh
python img2pbm.py dog.jpg
```
En cambio si queremos convertir todos los archivos de la carpeta seria:
```sh
python img2pbm.py *.jpg
```

img2pbm no solo genera un archivo .pbm por cada imagen, sino tambien crear un archivo upload.bat que contiene las instrucciones necesarias para subir los archivos .pbm al dispositivo por medio de ampy. 

En el caso que se tenga un mensaje de error al subir el archivo, revisar cual es el puerto que se esta utilizando, puede que sea necesario modificarlo por el adecuado. Es posible hacerlo directamente sobre upload.bat, para el caso recomiendo utilizar "reemplazar" de su editor; o directamente editando img2pbm.py dentro de la funcion generarBat().

## Ejemplo

Dentro de la carpeta example encontrara:
- Una imagen llamada dog.png
- El archivo de salida pbm generado por el script para mostrarlo en el display
- upload.bat que contiene la instruccion de ampy para subir el archivo pbm
- dog.py el ejemplo de como mostrar una imagen en MicroPython.