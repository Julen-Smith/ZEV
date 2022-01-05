from xml.dom import minidom
import os

#Función que comprueba que el xml donde se guardará toda la información esta creado en caso contrario llama a otra función para crearlo.
def checkRootXml():
    rootxmlName = "data.xml"   
    path = os.getcwd() + "\Stored"
    elements = os.listdir(path)
    for registry in elements:
        if  registry == rootxmlName:
            pass
    createXml('Zev', path, rootxmlName)
 
####
# 
# Funciones generícas
#
### 

#Función que crea un xml en el path deseado y con el nombre del nodo central modificados según parametros.
def createXml(rootElementName, path, rootxmlName):
    root = minidom.Document()
    xml = root.createElement(rootElementName)
    root.appendChild(xml)
    xml_str = root.toprettyxml(indent ="\t") 
    path += "/" + rootxmlName
    with open(path, "w") as f:
        f.write(xml_str)

