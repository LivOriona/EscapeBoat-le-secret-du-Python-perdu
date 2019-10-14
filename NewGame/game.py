from menu import * #importe tout, Menu et Option
from key_events_listener import waitForKey
from item import Item
from time import time
from console_visual import *
from character import Character

class Game:
    def __init__(self, firstRoom, timer):
        self.currentRoom = firstRoom #firstRoom sera la 1ère salle du jeu, mais currentRoom sera amenée à changer
        self.currentMenu = self.createMenu()
        self.mainMenu = self.currentMenu
        self.inventory = {}
        self.currentAction = None
        self.timer = timer

    def run(self):
        print("Règles du jeu :\nPour quitter le jeu, appuyez sur la touche \"échap\" ou \"esc\"\nVous êtes un voleur, aléché par les trésors d'une épave perdue dans le triangle des Bermudes. On dit qu'il recèles les trésors les plus incroyables... c'est le Titpanic.\nVous allez découvrir des salles cachées, des objets cachés, et des montagnes de trésors vous l'espérez.\nN'oubliez pas que votre temps est limité. Vous n'avez presque plus d'oxygène après avoir eu tant de difficultés à trouver l'épave. C'est la dernière ligne droite !\nBonne aventure ;)\nAppuyez sur \"Entrée\" pour démarrer le jeu.")
        while waitForKey() is None:
            pass

        startTime = time()
        step = time()
        while True:
            if time() - step > 0.2:
                self.printScreen() #afficher l'écran de ce jeu Game
                step= time()

            # timer -- ici

            currentTime = time()
            timeGone = currentTime - startTime
            self.timer-=timeGone
            startTime = currentTime

            if self.timer <= 0:
                print("Vous n'avez plus d'oxygène ... l'asphyxie aura eu raison de vous. \nGAME OVER")
                break

            key = waitForKey()  # bloque le programme jusqu'à ce qu'une touche soit appuyée et me retourne le nom de cette touche

            if key is None: #tant qu'aucune touche reconnue par le jeu n'est appuyée
                continue

            if key == "d":
                self.currentMenu.nextOption()
            elif key == "q":
                self.currentMenu.previousOption()
            elif key == "\r":
                self.currentMenu.enterOption()
            elif key == "s" or key == "z":
                if self.currentMenu.parent is not None:
                    self.currentMenu = self.currentMenu.parent #remet le menu parent en tant que menu actuel
            elif key == "escape":
                break



    def createMenu(self):
        mainMenu = Menu("Actions :", self)

        mainMenu.addOption(Option("Aller à", Game.goToAction)) #j'appelle la fonction addOption sur mainMenu (en lui
        # donnant option1 comme paramètre)
        mainMenu.addOption(Option("Inspecter", Game.inspectAction))
        mainMenu.addOption(Option("Prendre", Game.takeItemAction))
        mainMenu.addOption(Option("Déposer", Game.dropItemAction))
        mainMenu.addOption(Option("Parler à", Game.speakToAction))
        return mainMenu

    def addItemToInventory(self, itemId, occurence):
        nbInInventory = self.inventory.get(itemId, 0)  # récupère valeur associée à la clef qu'on lui donne (dans
        #  un dictionnaire), et s'il n'y a rien il me retourne ici 0 (pour éviter que ça explose
        nbInInventory += occurence
        self.inventory[itemId] = nbInInventory #ajouter l'item dans mon inventaire


    @staticmethod
    def goToAction(game):
        varRoom = game.currentRoom  # récupérer salle dans laquelle je suis actuellement
        varexits = varRoom.exits  # récupérer les sorties de cette salle
        exitsMenu = Menu("Sorties :", game,
                         game.mainMenu)  # création d'un nouveau menu, son parent est game.currentMenu
        for exitName in varexits:  # je boucle sur la liste des sorties de la salle actuelle // rappel : exitName est une var comme i
            destination = varexits[exitName].destination
            def changeRoom(game, destination=destination):
                game.currentRoom = destination  # dans la salle actuelle du jeu est stocké la destination
                # de la sortie associée à la clef du dictionnaire varexits
                game.currentMenu = game.mainMenu  # dans le menu actuel de ce jeu est stocké le menu principal mainMenu ?
                game.currentAction = None
            exitsMenu.addOption(Option(exitName, changeRoom))  # ajout d'options dans mon nouveau menu
        game.currentMenu = exitsMenu  # mon nouveau menu actuel currentMenu correspond à exitsMenu (nouveau menu
        # avec pour parent game.currentMenu)


        # def __init__(self, name, game, parent=None, options=None):
        # créer menu, et je le remplis avec la liste des objets qu'on peut décrire

    @staticmethod #je suis une fonction normale, je ne fonctionne pas avec Game, ça ne décrit pas un comportement de game,
    # c'est juste plus rangé de le mettre là
    def inspectAction(game):  # création du sous menu Inspecter avec 2 options
        newMenu = Menu("Inspecter un objet dans :", game, game.mainMenu)  # création du sousmenu en lui-même
        newMenu.addOption(Option("la salle", Game.inspectRoomAction))
        newMenu.addOption(Option("mon inventaire", Game.inspectInventoryAction))
        game.currentMenu = newMenu  # mon nouveau menu actuel currentMenu correspond à newMenu


    @staticmethod
    def inspectRoomAction(game): #création de la fonction qui dit ce qu'il se passe quand on appuie sur inspecter la salle
        newSousMenu = Menu("Les objets de la salle que tu peux inspecter sont :", game, game.currentMenu)
        pickableItems = game.currentRoom.pickables #je stocke dans pickableItems les objets récupérables dans la salle de jeu
        # actuelle
        inspectableItems = game.currentRoom.inspectables
        itemsToInspect = list(map(lambda i: (i, 1), inspectableItems)) #lambda est là pour écrire en une ligne une fonction simple.
        # ici def matransformation(i): / return (i, 1)
        for itemId, nbOfThisItem in itemsToInspect + list(pickableItems.items()): #je boucle sur ma liste (qui est en fait, qui
            # constituée de deux listes, chaque élement de ma liste me renvoyant un couple clef (inspectables) et valeur (pickables)
            # (un tuple)
            #j'ajoute une option, et chaque option représentera un des objets
            # pickable de la salle. items() permet de renvoyer un couple clef-valeur et non pas juste une clef, comme le fait
            # normalement un dictionaire
            itemToInspect = Item.items[itemId]
            optionName = itemToInspect.name
            def inspectItem(game, itemToInspect=itemToInspect): #executer la fonction correspondante
                itemToInspect.inspectAction(game)
            if nbOfThisItem > 1:
                optionName += " ("+str(nbOfThisItem)+")"
            newSousMenu.addOption(Option(optionName, inspectItem)) #j'ajoute une option qui a pour nom le nom de mon item
            #(et je récupère le nom de cet item par l'identifiant récupéré dans la salle via les id) et une action
        game.currentMenu = newSousMenu

    @staticmethod
    def inspectInventoryAction(game):
        newSousMenu = Menu("Les objets de ton inventaire que tu peux inspecter sont :", game, game.currentMenu)
        for itemId, nbOfThisItem in game.inventory.items(): #j'ajoute une option, et chaque option représentera un des objets de
        # mon inventaire
            itemToInspect = Item.items[itemId]
            optionName = itemToInspect.name
            if nbOfThisItem > 1:
                optionName += " (" + str(nbOfThisItem) + ")"
            def inspectItem(game, itemToInspect=itemToInspect): #afficher la description d'un objet inspecté
                itemToInspect.inspectAction(game)
            newSousMenu.addOption(Option(optionName, inspectItem)) #j'ajoute une option qui a pour nom le nom de mon item
        game.currentMenu = newSousMenu


    @staticmethod
    def speakToAction(game):
        newSousMenu = Menu("Les personnages de cette pièce à qui tu peux parler sont :", game, game.currentMenu)
        for character in game.currentRoom.characters:
            #écrire en options du menu
            def speakTo (game, character=character):
                character.speakToAction(game)
            newSousMenu.addOption(Option(character.name, speakTo))
        game.currentMenu = newSousMenu
            #def communicateWith(game, answers)

    @staticmethod
    def takeItemAction(game):
        newSousMenu = Menu("Objets ramassables :", game, game.mainMenu)
        pickableItems = game.currentRoom.pickables  # je stocke dans pickableItems les objets récupérables dans la salle de jeu
        # actuelle
        for itemId, nbOfThisItem in pickableItems.items():
            itemToTake = Item.items[itemId]
            optionName = itemToTake.name
            def takeItem(game, itemToTake=itemToTake):
                game.currentAction = "Vous prenez \""+itemToTake.name+"\""
                pickableItems[itemToTake.id] -= 1
                if pickableItems[itemToTake.id] == 0:
                    del pickableItems[itemToTake.id] #supprime cet item
                game.addItemToInventory(itemToTake.id, 1)
                Game.takeItemAction(game) #à chaque fois qu'on prend un objet, on rappelle le même menu, car sans
                # rafraichissement des boutons du menu, on vera toujours les mêmes objets pickables, tandis que là
                # on rappelle le menu et donc on regénère le bon nombre d'objets (moins l'objet pris du coup)

            if nbOfThisItem > 1:
                optionName += " (" + str(nbOfThisItem) + ")"
            newSousMenu.addOption(Option(optionName, takeItem))
        game.currentMenu = newSousMenu


    def removeItemInventory(self, itemId, occurence):
        self.inventory[itemId] -= occurence
        if self.inventory[itemId] <= 0:
            del self.inventory[itemId]


    @staticmethod
    def dropItemAction(game):
        newSousMenu = Menu("Objets déposables :", game, game.mainMenu)
        inventoryItems = game.inventory

        for itemId, nbOfThisItem in inventoryItems.items():
            itemToDrop = Item.items[itemId]
            optionName = itemToDrop.name
            def dropItem(game, itemToDrop=itemToDrop):
                game.currentAction = "Vous déposez \"" + itemToDrop.name + "\""
                game.removeItemInventory(itemToDrop.id, 1)
                nbPickableInRoom = game.currentRoom.pickables.get(itemToDrop.id, 0)
                nbPickableInRoom += 1
                Game.dropItemAction(game)
            if nbOfThisItem > 1:
                optionName += " (" + str(nbOfThisItem) + ")"
            newSousMenu.addOption(Option(optionName, dropItem))
        game.currentMenu = newSousMenu


    def clearScreen(self): #clear la console
        import os
        os.system('cls' if os.name == 'nt' else 'clear')


    def printScreen(self): #afficher mes options
        self.clearScreen() #efface la console

        currentRoomsName = buildPrintBloc(self.currentRoom.name+"\n", 150)
        currentRoomsDescription = buildPrintBloc(self.currentRoom.description+"\n", 150)
        minutesLeft = self.timer // 60
        secondsLeft = self.timer % 60
        currentTimer = buildPrintBloc("Il vous reste " + str(round(minutesLeft)) + " minutes et " + str(round(secondsLeft)) +" secondes.", 150)
        descriptionsBloc = currentRoomsName+currentRoomsDescription+currentTimer
        descriptionsBloc = addBorderToBloc(descriptionsBloc)
        printBloc(descriptionsBloc)
        #print(self.currentRoom.name+"\n") #afficher le nom de la salle actuelle
        #print(self.currentRoom.description+"\n") #affiche sa description
        #print("Il vous reste " + str(round(minutesLeft)) + " minutes et " + str(round(secondsLeft)) +" secondes.")
        if self.currentAction is not None:
            print(" → "+self.currentAction+"\n")
        print(self.currentMenu.name+"\n") #affiche le nom du menu actuel

        for i in range(len(self.currentMenu.options)):
            currentOption = self.currentMenu.options[i]
            if i == self.currentMenu.cursor:
                print("["+currentOption.name+"]", end=" ")
            else:
                print(currentOption.name, end=" ")
        print("\n")





