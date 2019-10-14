from exit import Exit

class Room: #objet room
    def __init__(self, id, name, description): #rappel : self est mon objet qui suit le plan Room
        self.id = id
        self.name = name
        self.description = description
        self.pickables = {} #les objets ramassables (pickables) sont actuellement un dictionnaire vide, qu'on va remplir plus tard, on        ne les retrouve pas dans les paramètres de ma fonction init
        self.inspectables = []
        self.exits = {}
        self.characters = []


    def addPickable(self, itemId, nbOfThisItem): #méthode ajouter un objet dans une salle
        numberOfThisItem = self.pickables.get(itemId, 0) #fonction get me retourne la valeur associée à la clef itemId,
        # et s'il n'y en a pas, il me retourne ici 0
        numberOfThisItem += nbOfThisItem #j'ajoute x item de plus au nombre d'items
        self.pickables[itemId] = numberOfThisItem #numberfThisItem est stocké dans le pickable de ma 'cuisine' qui a pour clef itemId

    def addInspectable(self, inspectableItem):
        self.inspectables.append(inspectableItem)

    def addCharacter(self, charactersName):
        self.characters.append(charactersName)


    def addExit(self, destination, exitName): #méthode ajouter une sortie (d'un seul côté)
        newExit = Exit(self, destination) #self ici se trouve dans Room, il ne fait référence qu'à une Room du coup (ex 'cuisine')
        #Création d'un nouvel objet de type Exit (ex : new Exit en JS) en lui donnant les paramètres attendus par le contructeur
        #init //// = je stocke ma nouvelle sortie dans newExit
        self.exits[exitName] = newExit #dans le dico exits{} de mon objet ('cuisine'), je stocke newExit (associé à la clef qui
        # vaut exitName)

    def addDoubleExit(self, destination, exitName1, exitName2): #méthode ajouter la même sortie des deux côtés
        self.addExit(destination, exitName1) #exécution méthode addExit() sur 'cuisine'
        destination.addExit(self, exitName2) #destination est associé à la classe Room. A la destination de ma salle
        # actuelle 'cuisine', je lui ajoute une sortie


    @staticmethod
    def addDoubleExitBuilder(source, destination, exitName1, exitName2):
        def hiddenDoubleExit(game, source=source, destination=destination, exitName1=exitName1, exitName2=exitName2):
            source.addDoubleExit(destination, exitName1, exitName2)
        return hiddenDoubleExit


    def __repr__(self):
        return "Room("+self.name+")"



