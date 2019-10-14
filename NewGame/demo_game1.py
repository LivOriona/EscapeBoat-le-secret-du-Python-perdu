from room import Room
from item import Item
from exit import Exit
from game import Game
from character import Character
from menu import Menu, Option


saloon = Room("saloon", "Saloon du bateau", "Vous êtes dans un saloon qui n'a pas vu la lumière du jour depuis des lustres ! Oui, comme celui tout éclaté qui devait éclairer cette pièce autrefois. La dernière fête qui s'est déroulée ici a dû faire salle comble : les bouteilles jonchent pêle-même de grandes tables. Une immense tapisserie habille le mur du fond.")
myGame = Game(saloon, 300)


cuisine =  Room("cuisine", "Cuisine du bateau", "Cette cuisine a connu de meilleurs jours... Mais on y trouve quelques restes !")
bureau = Room("bureau", "Bureau du commandant", "Ce bureau semble être la pièce qui a conservé le mieux sa grandeur d'antan. Des objets de valeur s'étalent sur le bureau, quelques feuilles dépassent encore d'un tiroir du bureau, et une peluche décousue vous regarde d'un oeil morne.")
balais = Room("balais", "Placard à balais", "Dans cette pièce, vous avez à peine la place de vous retourner. Des outils ménagers y ont été jetés et oubliés.")


#ajouter quelques sorties entre ces pièces
saloon.addDoubleExit(cuisine, "Cuisine du saloon", "Saloon")
saloon.addDoubleExit(bureau, "Bureau du commandant Jackson", "Saloon")
bureau.addDoubleExit(balais, "Placard étroit", "Bureau du commandant Jackson")

#définition d'items dans mon jeu
cutter = Item("cutter", "cutter tranchant", "En voilà un cutter qu'il tranche bien Bondiou !", Item.showDescriptionAction)
clope = Item("clope", "Lucky clope", "Vous tirez une de vos fameuses Lucky clope de son étuit.", Item.changeTimerActionBuilder(-10))
tissus = Item("tissus", "tissus déchiré", "Ce bout de tissus vert déchiré a une bien drôle d'odeur...", Item.showDescriptionAction)
carte = Item("carte", "carte grandeur nature", "Cette tapisserie représente une immense carte du monde, tel que connu à l'époque. Le travail est vraiment très soigné", Item.changeInventoryActionBuilder("tissus", 1))
bouteilleVide = Item("bVide", "bouteille d'alcool vide", "Ce n'est qu'une bouteille d'alcool vide. Aucun intérêt donc.", Item.showDescriptionAction)
bouteillePleine = Item("bPleine", "bouteille d'alcool pleine", "Voilà qui est intéressant. Une petite rassade ne fait jamais de mal dit-on !", Item.changeTimerActionBuilder(-50))
photoEquipage = Item("photoEquipage", "photo de l'équipage", "photo de l'équipage du bateau lors d'une de ces soirées de saloon endiablées.", Item.showDescriptionAction)
aretePoisson = Item("aretePoisson", "arête de poisson", "C'est une vieille arête d'un poisson de bonne taille. Qui fût de bonne taille tout du moins, ça n'a pas dû durer longtemps.", Item.showDescriptionAction)
fromage = Item("fromage", "fromage encore consommable", "Merveilleux ! Ce fromage est encore mangeable, et avec son odeur puante à souhait, il a l'air bien délicieux", Item.changeTimerActionBuilder(-50))
papier = Item("papier", "message à moitié caché", "Vous tirez sur une feuille de papier qui était encore mordue par ce tiroir et vous la lisez. \nJeminreno, mon ami, vous savez que l'heure est grave, je vous écris ce message aussi vite que possible, remontez vers la côte, par tous les moyens possible et prévenez Germina qu'il y a un ... et le message se termine par un trait de stylo relevé brutalement de la feuille, comme si la personne qui l'avait écrit s'était fait tirer par les jambes... ça fait froid dans le dos.", Item.showDescriptionAction)
globe = Item("globe", "globe sur pied", "Votre regard est attiré par ce magnifique globe terrestre sur pied. Il est recouvert d'un revêtement noir, et les contours des îles et pays sont dessinés à l'aide d'un trait doré finement ciselé. Vous avez toujours été attiré par les cartes, et une si belle ne peut que retenir votre attention. Vous perdez quelques précieuses secondes à jouer et le faire tourner.", Item.changeTimerActionBuilder(-30))
clef = Item("clef", "clef mystérieuse", "Vous trouvez une petite clef lourde en or, que vous trouvez bien mystérieuse.", Item.showDescriptionAction)
peluche = Item("peluche", "peluche d'ours bleu décousue", "Cette peluche d'ours décousue semble vous regarder d'un regard suppliant avec le seul oeil qu'il lui reste.", Item.changeInventoryActionBuilder("clef", 1))
pieceDOr = Item("pieceDOr", "pièce d'or", "Quelle pièce bien brillante que vous avez là !", Item.showDescriptionAction)
balaisBrosse = Item("balaisBrosse", "balais brosse usé", "Voici un balais brosse qui a connu de meilleurs jours.", Item.changeInventoryActionBuilder("pieceDOr", 2))
commode = Item("commode", "commode ancienne", "Vous laissez votre main courrir sur une magnifique commode ancienne, qui vous rappelle quelques souvenirs.", Item.showDescriptionAction)

#ajout de ces items (pickables) à mes différentes pièces et mon inventaire
saloon.addPickable(carte.id, 1)
saloon.addPickable(photoEquipage.id, 3)
saloon.addPickable(bouteilleVide.id, 15)
saloon.addPickable(bouteillePleine.id, 2)
cuisine.addPickable(aretePoisson.id, 5)
cuisine.addPickable(fromage.id, 1)
bureau.addPickable(papier.id, 1)
bureau.addPickable(globe.id, 1)
bureau.addPickable(peluche.id, 1)
balais.addPickable(balaisBrosse.id, 1)

#ajout des réponses possibles à faire à chaque personnage
dorisAnswersMenu = Menu("Vous répondez à Dori :", myGame, myGame.currentMenu)
dorisAnswersMenu.addOption(Option("Merci Dori", Character.showDescriptionBuilder("De rien, je t'aime.")))
dorisAnswersMenu.addOption(Option("Vas te faire voir Dori", Character.showDescriptionBuilder("Bah d'accord, je vais à la Hackerhouse de Poupet.")))
dorisAnswersMenu.addOption(Option("Allez viens Dori, on se fait un python", Character.showDescriptionBuilder("C'est quand tu veux Bouffi !")))
dorisAnswersMenu.addOption(Option("Fromaaaaaaaaage !!", Character.removeItemBuilder(fromage.id, 1)))
#ajout des personnages par pièces
dori = Character("Dori", "Vous voyez un poisson bleu, à petite nageoire adorable aux bouts jaunes, qui vous semble un peu perdu.", "Hey salut toi ! Tu sais où je suis ? Oui parce que moi je sais pas hein. Je nageais, je nageais, et je me suis retrouvée ... devine où ? Devine où ? ... Non ? Eh bah LA ! Oui, oui, là tu comprends bien. Bon, c'est pas tout ça, mais tu veux quoi toi ?", None)

bobMarley = Character("Bob Marley", "Vous voyez un jeune homme avec un joint et un bonnet jaune, vert et rouge", "Hey bro", None)
bobMarley.speakToAction = Character.multipleActionBuilder(Item.changeInventoryActionBuilder(clope.id, 5), Character.showDescriptionBuilder("Comme je suis un peu en colère, même si j'en ai pas l'air, parce que je suis shooté H24, je te file des clopes")) #grâce à multipleActionBuilder je peux effectuer plusieurs actions en même temps (il suffit d'en mettre autant que je peux en tant que paramètres)
dori.speakToAction = Character.conditionalAnswersBuilder(fromage.id,
                       Character.answersMenuBuilder(dori, dorisAnswersMenu),
                       Character.showDescriptionBuilder("Vas me chercher du fromage stp :) ") )


saloon.addCharacter(dori)
cuisine.addCharacter(bobMarley)

#ajout des items uniquement inspectables (et non pickables), tels que des meubles
bureau.addInspectable(commode.id)

#ajout des personnages par pièces
bureau.addCharacter(dori)

#cuisine = Room("cuisine", "Cuisine de charme", "Vous arrivez dans une petite cuisine pleine de charme.", {})
#chambre = Room("chambre", "Chambre jaune", "Vous êtes maintenant dans une pièce gaiement peinte en jaune.", {})
#cuisine.addDoubleExit(chambre, "Porte des Lilas roses", "Porte des Lilas bleus")
#pieceDOr = Item("pieceDOr", "pièce d'or", "Quelle pièce bien brillante que vous avez là !", Item.showDescriptionAction)
#peluche = Item("peluche", "peluche bleue de Hannah", "Cette peluche vous regarde avec de grands yeux bleus nuits innocents.", Item.changeInventoryActionBuilder("pieceDOr", 2))
#cutter = Item("cutter", "Cutter de Mamie bricoleuse", "Vous avez dans les mains un cutter très tranchant. Avec un peu de prudence, il fera des miracles de découpage.", Item.changeTimerActionBuilder(-30)) #pas besoin de sauvegarder mes items dans des variables parce que les références sont déjà conservées dans Item.items[id] du fichier item.py

#chambre.addPickable(peluche.id, 1) # dans l'objet chambre, j'ajoute un pickable, qui (est) a pour itemId l'identifiant (id) de l'objet (ici peluche)
#cuisine.addPickable(cutter.id, 2)


myGame.addItemToInventory(cutter.id, 2)
myGame.addItemToInventory(clope.id, 10)
