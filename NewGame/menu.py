class Menu:
    def __init__(self, name, game, parent=None, options=None): #on s'attend à recevoir un paramètre parent,
        # mais si on ne le lui donne pas, il vaut none
        self.game = game #ça va stocker l'état actuel du jeu, comme le menu actuel, etc
        self.name = name
        self.parent = parent
        self.cursor = 0
        self.options = options if options is not None else [] #contient des fonction. condition ternaire
        #maVariable = conditionEstVraie ? valeurSiVraie : valeurSiFausse, mais en python :
        #valeurSiVraie if conditionEstVraie else valeurSiFausse'''

    def nextOption(self): #méthode sélectionner prochaine option
        length = len(self.options) #longueur de la liste options[]
        if length == 0:
            return #ça return none par défaut, donc ça ne retourne strictement rien et ça arrête la fonction
        if self.cursor == length-1: #différence entre longueur de la liste et numéro de ma clef. list begin 0
            self.cursor = 0
        else:
            self.cursor += 1

    def previousOption(self):
        length = len(self.options) #si ma liste a 5 éléments, sa longueur vaut 5, par contre le dernier self.cursor vaut 4
        if length == 0:
            return
        if self.cursor == 0:
            self.cursor = length-1 #ma longueur vaut 5, hors le 5e élément a pour id 4
        else:
            self.cursor -= 1

    def enterOption(self):
        if len(self.options) == 0:
            return

        selectOption = self.options[self.cursor] #stocker dans selectOption la position du curseur de ce menu (self)
        # 'currentMenu' dans la liste options[] de ce menu (self) 'currentMenu' // l'objet en position self.cursor dans
        # la liste self.options
        selectOption.run(self.game)

    def addOption(self, option):
        self.options.append(option) #j'ajoute une option à la liste option

    def __repr__(self):
        return "Menu "+str(self.options)+""

class Option:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def run(self, game): #méthode qui est appelée quand une option est choisie avec la touche enter
        self.action(game) #action() est une fonction qui est comme paramètre de la méthode init

    def __repr__(self):
        return "Option(action="+str(self.action)+")"
