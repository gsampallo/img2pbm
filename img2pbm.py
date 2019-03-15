import glob, os
import sys
from PIL import Image
import struct

def main(argv):

    subir = "upload.bat"
    if os.path.exists(subir):
        os.remove(subir)
    
    for file in glob.glob(argv[0]):
        print(file)
        procesarArchivo(file,'archivo')

def procesarArchivo(archivo,output):
    nombre = archivo.split(".")[0]
    archivoPbm = nombre+".pbm"
    
    img = Image.open(archivo).convert('1')
    size = 64, 64
    img.thumbnail(size)
    img.save(nombre+"1.jpg","JPEG")

    img.save(archivoPbm, "PPM")    
    
    generarBat(archivoPbm)

def generarBat(archivo):
    file = open("upload.bat","a")
    file.write("ampy --port COM4 -b 115200 put "+archivo+"\n")    

if __name__ == "__main__":
    main(sys.argv[1:])