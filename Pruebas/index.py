import xml.etree.ElementTree as xml


servernumber  = 55555555

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



with open("items.xml","wb") as files:
    tree.write(files,encoding="UTF-8", xml_declaration=True)