from key_events_listener import waitForKey

class Character:
    def __init__(self, name, description, dialogue, speakToAction):
        self.name = name
        self.description = description
        self.dialogue = dialogue
        self.speakToAction = speakToAction

    @staticmethod
    def showDescriptionCharacter(game, character):
        game.currentAction = "Voici \"" + character.name + "\" : " + character.description

    @staticmethod
    def answersMenuBuilder(character, menu):
        def actionOnMenu(game, character=character, menu=menu):
            Character.showDescriptionCharacter(game, character)
            menu.parent = game.currentMenu
            game.currentMenu = menu
        return actionOnMenu

    @staticmethod
    def showDescriptionBuilder (description):
        def charactersReaction(game, desc=description):
            game.currentAction = desc
        return charactersReaction

    @staticmethod
    def conditionalAnswersBuilder(itemId, actionTrue, actionFalse):
        def conditionalAnswers (game, itemId=itemId, actionTrue=actionTrue, actionFalse=actionFalse):
            if itemId in game.inventory:
                actionTrue(game)
            else:
                actionFalse(game)
        return conditionalAnswers

    @staticmethod
    def removeItemBuilder(itemId, occurence): #Option d'action de l'item qui ajoute ou retire un item à l'inventaire (que
        #l'item soit présent ou non dans la salle
        def removeItem(game, itemId=itemId, occurence=occurence):
            game.removeItemInventory(itemId, occurence)
        return removeItem

    @staticmethod
    def multipleActionBuilder(*actions): #liste de tous les paramètres donnés, il peut il y en avoir 1 à autant qu'on veut
        actionsToExecute = actions
        def executeActions(game, actionsToExecute=actionsToExecute):
            for action in actionsToExecute:
                action(game)
        return executeActions