import pandas as pd
from docxtpl import DocxTemplate
import re, json, sys, request, ssh


def generateWord(nadEstudio):
   
    data = request.Logos(nadEstudio)
    try:
        config = ssh.clientSSH(data)
    except:
        print('error al obtener datos del equipo directamente')
        config = {'config':{'ppal':'', 'bck':'', 'diba':''}}

    data = data | config
    try:
	doc = DocxTemplate("d:/User/Desktop/AVTPython/Plantilla.docx")
	doc.render(data)

	PATH = "[" +  data['ppal']['cif'] + "][" + str(data['ppal']['nuAdministrativo']) + "][" + data['ppal']['mnemonico'] + "]"
	doc.save("d:/User/Desktop/AVTPython/avt/" + PATH + ".docx")
	print('documento generado')
    except:
	print('Error generar doc')

for nad in sys.argv[1:]:
    generateWord(nad)