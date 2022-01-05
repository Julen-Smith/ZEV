class Jugador:
    def __init__(self, nombre, lv, exp, rol, lasthunt, lastfish, lastdungeon, lastsupport, inv):
        self.nombre = nombre
        self.lasthunt = lasthunt
        self.lv = lv
        self.exp = exp
        self.rol = rol
        self.lastfish = lastfish
        self.lastdungeon = lastdungeon
        self.lastsupport = lastsupport
        self.inv = inv

colm = Jugador("Colm",99,1000000,"Monk",None,None,None,None,None)