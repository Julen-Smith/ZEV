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

#Chekea que el servidor no exista ya dentro del xml, sencillito.
def check_for_server_id(servernumber):
    tree = xml.parse("Data\Stored\data.xml")
    root = tree.getroot()   
    all_text = root.findall('.//Serverid')
    for texts in all_text:
        dummy = str("".join(texts.itertext()))
        if dummy == str(servernumber):
            return 1
    return 0
    

def register_new_server(servernumber):
    try:
        tree = xml.parse("Data\Stored\data.xml")
        root = tree.getroot()  
        nuevoServer = xml.Element("Server")
        root.append(nuevoServer)
        serverid = xml.Element("Serverid")
        serverid.text = str(servernumber)
        nuevoServer.append(serverid)
        players = xml.Element("Players")
        nuevoServer.append(players)
        player = xml.Element("Player")
        players.append(player)
        tree.write('Data\Stored\data.xml')
        return 1
    except:
        return 0
    


def init_xml_structure(servernumber):
    #if exist return 0 si no 1
    root = xml.Element("Servers")
    tree = xml.ElementTree(root)
    server = xml.Element("Server")
    root.append(server)
    serverid = xml.Element("Serverid")
    serverid.text = str(servernumber)
    server.append(serverid)
    players = xml.Element("Players")
    server.append(players)
    player = xml.Element("Player")
    players.append(player)
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


