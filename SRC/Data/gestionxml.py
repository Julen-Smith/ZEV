from xml.dom import minidom
import xml.etree.ElementTree as xml
import os



#Función que comprueba que el xml donde se guardará toda la información esta creado en caso contrario llama a otra función para crearlo.
def checkRootXml():
    rootxmlName = "data.xml"   
    path = os.getcwd() + "\Data\Stored"
    elements = os.listdir(path)
    for registry in elements:
        if  registry == rootxmlName:
            return
    createXml('Zev', path, rootxmlName)

####
# 
# Funciones generícas
#
### 

#Función que crea un xml en el path deseado y con el nombre del nodo central modificados según parametros.
def createXml(rootElementName, path, rootxmlName):
    root = minidom.Document()
    path += "/" + rootxmlName
    with open(path, "w") as f:
        f.write()

#Falta checkear que el servidor no exista.

def init_xml_structure(serverid):
    #if exist return 0 si no 1
    root = xml.Element("Servers")
    elementServer = xml.Element("Server")
    serveridentity = xml.Element("Serverid")
    serveridentity.insert(serverid, elementServer)
    root.append(elementServer)
    elementPlayers = xml.Element("Players")
    elementServer.append(elementPlayers)
    elementPlayer = xml.Element("Player")
    elementPlayers.append(elementPlayer)
    tree = xml.ElementTree(root)
    with open("Data\Stored\data.xml","wb") as files:
        tree.write(files,encoding="UTF-8", xml_declaration=True)

def read_xml():
  filename= "Data\Stored\data.xml"
  tree = xml.parse(filename)
  root = tree.getroot()
  myArray=[]
  for x in root.findall('Server'):
    myArray.append(x.text)
  print(myArray)  


