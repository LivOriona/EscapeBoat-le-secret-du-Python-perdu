from room import Room

class Item:
    items = {}

    def __init__(self, id, name, description, inspectAction):  # self = this en js
        Item.items[id] = self #nouvelle association entre un identifiant et l'objet (l'item) en lui-même // Je crée une référence (ex       : qu'est-ce qu'une peluche, qu'est-ce qu'un cutter ?, ils ont un id, un nom, une description et une action quand on les utilise)
        self.id = id
        self.name = name
        self.description = description
        self.inspectAction = inspectAction

    @staticmethod
    def changeTimerActionBuilder(timeModification): #Option d'action de l'item qui retire ou ajoute du temps au timer
        def changeTimer(game, timeModification=timeModification):
            game.timer += timeModification
        return changeTimer


#action = Item.changeTimerActionBuilder(-30) #exemple pour utilisation dans main
#couteau = Item("couteau", "", "", action)

    #pour la dernière action qui consiste à ajouter un item (qui n'est pas dans la salle) dans l'inventaire (item caché), voir la fonction addItemToInventory dans game.py
    @staticmethod
    def changeInventoryActionBuilder(itemId, occurence): #Option d'action de l'item qui ajoute ou retire un item à l'inventaire (que
        #l'item soit présent ou non dans la salle
        item = Item.items[itemId]
        def changeInventory(game, item=item, occurence=occurence):
            if occurence > 0:
                game.addItemToInventory(itemId, occurence)
            else:
                game.removeItemInventory(itemId, occurence)
        return changeInventory

