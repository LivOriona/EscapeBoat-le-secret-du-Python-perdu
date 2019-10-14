from room import Room
from item import Item
from exit import Exit
from game import Game
from character import Character
from menu import Menu, Option

#création de la salle de départ (salle de réception ici) :
#myRoom = Room("id", "nom affiché dans le jeu", "description")
salleReception = Room("reception",
                      "Salle de réception",
                      "Vous pénétrez dans une gigantesque salle, ornée de décorations toutes plus luxueuses les unes que les autres. Elles ne sont bien sûr plus aussi brillantes qu'autrefois, et sont couvertes de mousse après avoir passé tant de temps sous l'eau. Les tables de réception s'accordent en rond, et laisse la place pour ce qui fut certainement une piste de danse. Plusieurs portes s'offrent à vous, c'est le moment d'explorer pour amasser le butin du célèbre navire Titpanic."
                      )

#création du jeu (salle de départ et timer) :
#myGame = Game(Room, timerEnSecondes)
myGame = Game(salleReception, 600)







#création des autres pièces du bateau :
#myRoom = Room("id", "nom affiché dans le jeu", "description")
cuisine = Room("cuisine",
               "cuisine du bateau",
               "Vous entrez dans une cuisine qui a connu de meilleurs jours. La mousse des profondeur marines a pris possession de chaque recoin de la pièce, et des sortes de plantes grimpantes poussent sur ce qui ressemble de près ou de loin à des barres. Tout a été laissé pêle-mêle sur les grands plans de travail. Vous vous approchez : des fois qu’il y ait encore de la nourriture consommable…"
               )
placardBalais = Room("placardBalais",
                     "placard à balais",
                     "Dans cette pièce, vous avez à peine la place de vous retourner. Des outils ménagers y ont été jetés et oubliés.. Seaux, balais poussiéreux, toiles d'araignées... tout y est.")


caveAuTresor = Room("caveAuTresor",
                    "cave au trésor",
                    "Jackpot ! Vous venez de trouver une cave regorgeant de trésors, de quoi remplir votre butin généreusement.")

couloirPrincipal = Room("couloirPrincipal",
                        "Couloir",
                        "Lugubre ce couloir, changeons rapidement de pièce...")

cabinePilotage = Room("cabinePilotage",
                      "Cabine de pilotage",
                      "Et voici la salle des commandes. Vous trouvez toujours ces pièces majestueuses et pleindes de charme.")

bureauCommandant = Room("bureauCommandant",
                        "Bureau du Commandant",
                        "C'est bien rangé ici, on dirait que le commandant était un homme méticuleux. Un bureau en chêne occupe en grande partie la pièce")


chambreJaune = Room("chambreJaune",
                    "Chambre Jaune Soleil",
                    "Vous entrez dans une chambre étonnamment lumineuse pour celle d’un bateau englouti depuis des centaines d’années. Elle semble rayonner de l’intérieur : son lit immitant un tournesol ouvert, sa commode élégamment décorée et son armoire imposante vous inspirent. C’est magnifique.")

armoireRayonnante = Room("armoireRayonnate",
                         "Intérieur de l'amoire rayonnante",
                         "Ce faux fond de l’armoire révèle une véritable cave au trésor ! Elle est toute illuminée par un Dieu magnifique."
)
chambreEmploye2 = Room("chambreEmploye2",
                       "Deuxième chambre d'employé du bateau",
                       "Vous pénétrez dans une chambre d’employé de bateau bien miteuse. Un lit à étage arrive à se caser dans un coin, au bas de celui-ci gît un tonneau renversé, et un seau ragoûtant semble avoir contenu des excréments… Eh bah c’était pas le luxe pour tout le monde ici.")

philatelie = Room("philatelie",
                  "chambre d'employé timbré",
                  "Des timbres en suspension dans l'eau, des feuilles se déchirant de dizaines de cahiers ... Cette chambre devait sûrement appartenir à un amateur de philatélie.")

chambreEmploye3 = Room("chambreEmploye3",
                       "Troisième chambre d'employé du bateau",
                       "Visiblement c'était la chambre d'une serveuse. Petit, mais bien aménagé.")

couloirService = Room("couloirService",
                      "Couloir de service des employés du bateau",
                      "Voici un couloir long, fin et peu entretenu.")

reggae = Room ("reggae",
               "chambre reggae",
               "De douces effluves émanent de cette pièce. Quelques notes de basse se font entendre au loin. Que l'esprit rasta soit avec vous !")

disco = Room ("disco",
              "chambre disco",
              "Cette ambiance années 80 vous donne envie de vous trémousser. Ne perdez pas trop de temps sur la piste de danse ;) ")

chambreRose = Room(
    "chambreRose",
    "chambre rose",
    "Cette chambre est très féminine... Mais, je la reconnais! C'est la chambre de Rose dans Titanic !!")

chambreVerte = Room(
    "chambreVerte",
    "chambre verte",
    "Wouh, on dirait une jungle cette chambre! Un bruit de ruisseau résonne au fond, derrière les lianes...")

machine = Room ("machine", "salle des machines", "On entrendrait presque les moteurs tournaient. ")

#création des sorties entre les différentes pièces :
#Room.addDoubleExit(destination, "nom sortie source vers destination", "nom sortie destination vers source")
cuisine.addDoubleExit(placardBalais, "Placard à balais", "Cuisine du bateau")
cuisine.addDoubleExit(salleReception, "Salle de réception", "Cuisine du bateau")
salleReception.addDoubleExit(couloirPrincipal, "Couloir", "Salle de réception")
salleReception.addDoubleExit(bureauCommandant, "Bureau du Commandant", "Salle de réception")
couloirPrincipal.addDoubleExit(reggae, "Chambre ambiance Reggae", "Couloir")
couloirPrincipal.addDoubleExit(disco, "Chambre ambiance Disco", "Couloir")
couloirPrincipal.addDoubleExit(chambreRose, "Chambre Rose", "Couloir")
couloirPrincipal.addDoubleExit(chambreVerte, "Chambre Verte", "Couloir")
chambreJaune.addDoubleExit(couloirPrincipal, "Couloir", "Chambre Jaune Soleil")
chambreEmploye2.addDoubleExit(couloirService, "Couloir de service", "Deuxième chambre d'employé")
couloirService.addDoubleExit(cuisine, "Cuisine du bateau", "Couloir de service")
couloirService.addDoubleExit(philatelie, "Chambre Philatélie", "Couloir de service")
couloirService.addDoubleExit(chambreEmploye3, "Troisième chambre d'employé", "Couloir de service")














#création des items (tout pickables et inspectables) et de leurs actions d'inspection :
#monItem = Item("id", "nom affiché en jeu", "description", Item.monAction souhaitée) (si une seule action lors de l'inspection de l'Item)
#monItem = Item("id", "nom affiché en jeu", "description", Item.multipleActionBuilder(Item.changeInventoryActionBuilder(clope.id, 5), Item.changeTimerActionBuilder(-50)) (si plusieurs actions lors de l'inspection de l'Item)
pieceDor = Item(
    "pieceDor",
    "Pièce d'or",
    "",
    Character.showDescriptionBuilder("Quelle belle pièce d’or bien brillante !")
)

fromageMoisi = Item(
    "fromage",
    "fromage moisi",
    "",
    Character.showDescriptionBuilder("Consommable, consommable… c’est vite dit. On dit d’un fromage que plus il pue, meilleur il est, mais ça ne semble pas vrai pour tous les fromages à en voir celui-ci ! Mais ça pourrait peut-être encore attirer des souris ?")
)

casserole = Item(
    "casserole",
    "casserole salle",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Vous déplacez les casseroles pour voir si elles contiennent quelque chose, et petite armée de rats en est délogée !\nVous entendez alors au loin Ratatouille  : \"eh pas touche fada que tié, c'est le sang de la veine!\" \nIl vous faut quelques secondes pour vous remettre de cette surprise [vous perdez 10 secondes]. Des rats sous l’eau, c’est bien une première. Vous vous sentez décidément de plus en plus à court d’oxygène…"),
        Item.changeTimerActionBuilder(-10)
    )
)

four = Item(
    "four",
    "four de la cuisine",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Vous ouvrez le four et vous trouvez l’intérieur bien profond tout de même. Vous y passez la tête et voyez des petits tas d’objets brillants. Sacre Bleu ! Quel est donc la magie contenue dans ce four ?"),
        Room.addDoubleExitBuilder(cuisine, caveAuTresor, "Cave au trésor cachée", "Cuisine du bateau"),
    )
)

carteDuNavire = Item(
    "carteDuNavire",
    "Carte du navire",
    "",
    Character.showDescriptionBuilder("Ah, vous trouvez une carte représentant l'agencement du navire. Ca sera sûrement utile !")
)

tablier = Item(
    "tablier",
    "tablier de cuisine",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Vous fouillez un tablier au hasard, et vous avez décidément la main chanceuse ! Un petit mot caché s’y trouvait. Vous le fourrez dans votre besace pour le lire plus tard."),
        Item.changeInventoryActionBuilder(carteDuNavire.id, 1)
    )
)

couteau = Item(
    "couteau",
    "couteau de cuisine tranchant",
    "",
    Character.showDescriptionBuilder("En voilà un couteau qu'il tranche bien, Bondiou !")
)

messageTapisserie = Item(
    "messageTapisserie",
    "Message caché derrière la tapisserie",
    "",
    Character.showDescriptionBuilder("Rodolphe, voilà la partie manquante du code. Comme tu le savais, mon voyage s’arrête ici. Le père Fourras m’a donné ce code qu’après avoir répondu aux 100 énigmes mystiques, comme le dit la légende. Cet effort me coûte donc la vie. Je fais cela pour toi mon ami, mon frère. Je veux te savoir heureux, tu le mérite enfin, alors fais-en bon usage. Je sais que tu sauras déchiffrer ce code, grâce à notre langage secret. \n \"Je suis un oiseau noir et blanc, donc les yeux brillent d’envie lorsque les choses scintillent. Alors comme le voleur que je suis, je les pille.\" \n 16.9.5")
)

tapisserie = Item(
    "tapisserie",
    "Immense tapisserie représentant une Mappemonde",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Vous voyez une immense et magnifique tapisserie qui couvre tout le mur arrière de la salle de réception. Elle a dû être magnifique autrefois, car malgré les ravages de l’eau et du temps, elle conserve un peu de sa beauté fanée. Elle représente la carte du monde connu, à l’époque de la construction de ce bateau. Vous vous approchez, et passez votre main sur la tapisserie, fasciné un moment par cette relique d’antan. En passant votre main sur le tissu, vous sentez un papier caché derrière. Vous le saisissez et le mettez dans votre besace."),
        Item.changeInventoryActionBuilder(messageTapisserie.id, 1)
    )
)

argenterie = Item(
    "argenterie",
    "Service d'argenterie précieuse",
    "",
    Character.showDescriptionBuilder("Couteaux, fourchette à plat, fourchette à dessert, cuillère à soupe, cuillère à trou, cuillère à dessert et autres argenteries précieuses composent ce service. Un petit coup de nettoyage léger et ça sera comme neuf pour faire du blé !")
)

tableReception = Item(
    "tableReception",
    "Table de réception",
    "",
    Character.multipleActionBuilder(
        Item.changeInventoryActionBuilder(argenterie.id, 1),
        Character.showDescriptionBuilder("Vous vous approchez des tables de réception, encore dressées et surtout couvertes d’argenterie ! Vos yeux brillent et clignent comme des dollar à cette vue. Ni une, ni deux, vous fourrez l’argenterie dans votre sac. Tant pis si c’est lourd, quand ça paye, c’est que c’est léger !")
    )
)

clefTiroir = Item(
    "clefTiroir",
    "Clef du tiroir du bureau du commandant",
    "",
    Character.showDescriptionBuilder("Cette clef doit permettre d’ouvrir un tiroir contenant des documents précieux !")
)



gouvernail = Item(
    "gouvernail",
    "Imposant gouvernail du navire",
    "",
    Character.showDescriptionBuilder("Un immense gouvernail se isse encore fièrement au centre de la pièce.")
)
ceinture = Item(
    "ceinture",
    "en cours",
    "",
    Character.showDescriptionBuilder("en cours")
)
trappe = Item(
    "trappe",
    "Trappe du haut de la salle des commandes",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Une trappe vous interpelle. Il doit sûrement avoir un moyen de l’ouvrir. "),
        Character.conditionalAnswersBuilder(
            ceinture.id,
            Character.multipleActionBuilder(
                Character.showDescriptionBuilder("Vous utilisez la ceinture que vous avez dans votre inventaire pour la nouer solidement à la petite poignée de la trappe, et tirez un grand coup dessus. Et c’est une pluie d’or qui vous tombe dessus ! Avide, vous ramassez toutes les pièces."),
                Item.changeInventoryActionBuilder(pieceDor.id, 30)
            ),
            Character.showDescriptionBuilder("Ah, mince. Il vous faudrait une sorte de lanière à attacher à la petite poignée de la trappe, afin de pouvoir tirer dessus avec suffisamment de force.")
        )
    )
)


litTournesol = Item(
    "litTournesol",
    "Lit Tournesol",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Le lit au pétales ouvertes vous ouvre les bras. Vous vous y allongez et ne voyez plus le temps passer [vous perdez 40 secondes]."),
        Item.changeTimerActionBuilder(-40)
    )
)

commodeRa = Item(
    "commodeRa",
    "Commode de Râ",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Une petite commode décorée de hiéroglyphes dessinés en or précieux trône près du lit. Soudain, des pièces d’or lévitent de votre inventaire et son avalées aussitôt par le tiroir de la commande. Impossible alors de les récupérer. Quel objet de malheur ! Mais vous n’avez guère plus le temps de vous y attarder, vous poursuivez votre chemin, alors que la commode émet un bruit glouton de déglutition."),
        Item.changeInventoryActionBuilder(pieceDor.id, -1)
    )
)
pantoufles = Item(
    "pantoufles",
    "Pantoufles jaunes",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Qu’il y a-t-il au fond de ces pantoufles de patachon ? Vous y dégotter 10 pièces d’or."),
        Item.changeInventoryActionBuilder(pieceDor.id, 10)
    )
)
armoireChambreJaune = Item(
    "armoireChambreJaune",
    "Armoire rayonnante",
    "",
    Character.multipleActionBuilder(
        chambreJaune.addDoubleExit(armoireRayonnante, "Intérieur de l'armoire rayonnante", "Chambre Jaune Soleil"),
        Character.showDescriptionBuilder("Quelle belle armoire aussi. Elle répète les motifs de la petite commode, mais en plus grand et élaboré. En l’ouvrant et fouillant à l’intérieur, vous appuyez sur une porte qui coulisse doucement. Voilà qui mérite d’être exploré !")
    )
)
brosseCheveux = Item(
    "brosseCheveux",
    "Brosse à cheveux",
    "",
    Character.showDescriptionBuilder("Cette brosse à cheveux porte des motifs très délicats, il vous semble que vous puissiez la casser rien qu’en la touchant. Pas étonnant pour une porcelaine aussi fine, elle doit valoir un petit montant tout de même.")
)
manteauRaffine = Item(
    "manteauRaffine",
    "Manteau raffiné",
    "",
    Character.showDescriptionBuilder("Une robe de chambre est suspendue à côté de l’armoire, sur une patère. Elle n’est pas un objet de luxe en soit, juste confortable, mais ses poches recèlent peut-être des secrets cachés… Eh non :( , rien par ici.")
)
litSuperpose = Item(
    "litSuperpose",
    "Lit superposé miteux",
    "",
    Character.showDescriptionBuilder("Ce n’est qu’un lit superposé, miteux et branlant.")
)
tonneauAir = Item(
    "tonneauAir",
    "Tonneau d'air renversé",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Vous soulevez le tonneau renversé. Il est encore fermé, quelle chance ! Vous ajoutez son contenu d’air dans votre réserve."),
        Item.changeTimerActionBuilder(30)
    )
)
seau = Item(
    "seau",
    "seau ragoûtant",
    "",
    Character.showDescriptionBuilder("Vous vous approchez avec dégoût du seau, et jeter un oeil rapide au-dessus. Effectivement, ce n’est pas du tout ragoûtant ! Vous sentiriez presque la mauvaise odeur malgré votre masque.")
)
bouteilleRhum = Item(
    "bouteilleRhum",
    "Bouteille de pleine de Rhum",
    "",
    Character.showDescriptionBuilder("Une bouteille de rhum encore fermée traîne par terre. Curieux. Vous y voyez une inscription : \”Si vous trouvez cette bouteille de rhum, rendez-là à son propriétaire. Il ressemble à ça :\” Et vous voyez un dessin craquelé d’un homme aux cheveux longs, sûrement portant des dread lock et des perles, avec un chapeau de pirate. C’est pas bête comme idée, tiens. ")
)
infirmiereSexy = Item(
    "infirmiereSexy",
    "Porte-clef d'infirmière sexy",
    "",
    Character.showDescriptionBuilder("Vous trouvez par terre un porte-clef d’infirmière sexy. Vu l’objet, vous n’avez pas été le seul voleur à traîner ici, et le dernier y a laissé ce porte-clef. Drôle d’idée de l’accrocher à sa combinaison de plongée.")
)
compasJackSparrow = Item(
    "compasJackSparrow",
    "Compas mystérieux",
    "",
    Character.showDescriptionBuilder("Un compas gît par terre. Il est niché au sein d’une magnifique boîte, quoique simple, d’un bleu sombre et profond. Il vous semble avoir déjà vu quelque part un compas similaire. Et ce dernier ne portait pas bonheur lorsqu’il était perdu.")
)

couronneEgypte = Item(
    "couronneEgypte",
    "Couronne de Nekhbet",
    "",
    Character.showDescriptionBuilder("Cette couronne est bien l’objet ayant le plus de valeur dans ce navire. Car il s’agit de la couronne blanche de Haute-Égypte. Vous la manipulez avec respect.")
)
boiteAcier = Item(
    "boiteAcier",
    "Boîte en acier rouillée",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Une boîte en acier rouillée traîne au sol. Quelle surprise ! Elle contient une magnifique couronne. Celle de la déesse égyptienne Nekhbet. Vous voilà riche !"),
        Item.changeInventoryActionBuilder(couronneEgypte.id, 1)
    )
)
boiteFer = Item(
    "boiteFer",
    "Boîte en fer rouillée",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Vous ouvrez la boîte en fer rouillée. Et vous bondissez en voyant des cafards de l’enfer en sortir et se répandre dans la pièce. Vous prenez quelques instant pour vous remettre de cette frayeur [vous perdez 30 secondes] "),
        Item.changeTimerActionBuilder(-30)
    )
)
boucleCeinture = Item(
    "boucleCeinture",
    "Boucle de ceinture en or",
    "",
    Character.showDescriptionBuilder("Une boucle de ceinture en or, ça se vend comme du petit pain")
)
drapSoie = Item(
    "drapSoie",
    "Drap de soie",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Vous soulevez des draps de soie, et un \”cling\” sonore se fait entendre. Vous saisissez alors la boucle de ceinture en or pour la mettre dans votre besace."),
        Item.changeInventoryActionBuilder(boucleCeinture.id, 2)
    )
)
lavande = Item(
    "lavande",
    "Brin de lavande fané",
    "",
    Character.showDescriptionBuilder(" Un brin de lavande fané traîne sur le sol. Mais il n’a guère grand intérêt. Peut-être pour l’offrir à votre mère à votre retour ?")
)
collierDor = Item(
    "collierDor",
    "Collier d'or",
    "",
    Character.showDescriptionBuilder("Ce collier fait d’or blanc, doré et rose vaut son pesant d’or.")
)


beauTableau = Item(
    "beauTableau",
    "Beau tableau",
    "",
    Character.showDescriptionBuilder(" Vous y trouvez quand même un beau tableau. Sûrement un souvenir d’un employé de service généreux, pour égayer cet endroit sordide.")
)
tableauLaid = Item(
    "tableauLaid",
    "Tableau laid",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Un tableau bien laid est accroché au mur. Qui a bien pu donc le mettre là. Mais il tinte étonnamment lorsque vous appuyez dessus. Vous y trouvez des pièces d’or cachées derrière ! Ce tableau laid devait servir à détourner l’attention. "),
        Item.changeInventoryActionBuilder(pieceDor.id, 2)
    )
)
balaisDuCouloir = Item(
    "balaisDuCouloir",
    "Balais",
    "",
    Character.showDescriptionBuilder("Un balais traîne encore contre le mur. Rien de bien intéressant à ça.")
)


vaisselier = Item(
    "vaisselier",
    "vaisselier branlant",
    "",
    Character.showDescriptionBuilder("Rien de très intéressant là dedans.")
)
riviere = Item(
    "rivière",
    "rivière de diamants",
    "",
    Character.showDescriptionBuilder("Hihi, ca doit valoir bien cher au marché noir ca ...")
)
lingots = Item(
    "lingots",
    "lingots d'or",
    "",
    Character.showDescriptionBuilder("Vous allez devenir riche, dites donc !")
)
tonneau = Item(
    "tonneau",
    "tonneau remplir d'air",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Alleluia ! Vous allez pouvoir gagner un peu d'énergie"),
        Item.changeTimerActionBuilder(50)
    )
)
montre = Item(
    "montre",
    "montre à gousset",
    "",
    Character.showDescriptionBuilder("Cette montre semble contenir un mécanisme d'horlogerie très complexe")
)
diademe = Item("diademe",
               "diademe de princesse",
               "",
               Character.showDescriptionBuilder("De toute beauté, c'est un véritable diadème !")
)
plastique = Item(
    "plastique",
    "couronne en plastique",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Euuh, pas très utile cette fausse couronne ..."),
        Item.changeInventoryActionBuilder(diademe.id, 1)
    )
)


canape = Item(
    "canape",
    "vieux canape confortable",
    "",
    Character.showDescriptionBuilder("Pas de temps à perdre, on ne se repose pas, paresseux !")
)
bonnet = Item(
    "bonnet",
    "bonnet de Bob Marley",
    "",
    Character.showDescriptionBuilder("Item.showDescriptionAction")
)
lampe = Item(
    "lampe",
    "lampe de chevet",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Vous l'allumez avec l'espoir de trouver quelque chose"),
        Item.changeInventoryActionBuilder(bonnet.id, 1)
    )
)
joint = Item(
    "joint",
    "joint détrempé",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Il faut combattre le mal par le mal, un petit joint vous revigorera"),
        Item.changeTimerActionBuilder(50)
    )
)
bronze = Item(
    "bronze",
    " pièces en bronze",
    "",
    Character.showDescriptionBuilder("No woman, no cry, c'est pas grand chose, mais la vraie richesse de Bob Marley est spirituelle man."))


thon = Item(
    "thon",
    "gros thon",
    "",
    Character.showDescriptionBuilder("Euuuh, ce thon au loin ressemble étrangement à un mégalodon ... Vous n'êtes pas trop tranquille j'ai l'impression")
)


loupe = Item(
    "loupe",
    "loupe",
    "",
    Character.showDescriptionBuilder("Oh cette loupe pourrait vous être utile pour étudier l'écritoire située dans la salle philatélie !")
)
commode = Item(
    "commode",
    "commode poussiéreuse",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Est-ce que vous allez trouver autre chose que du papier là dedans ?") ,
        Item.changeInventoryActionBuilder(loupe.id, 1)
    )
)
sceauNapoleon = Item(
    "sceau",
    "sceau de Napoléon Bonaparte",
    "",
    Character.showDescriptionBuilder("Véridique ! Ce sceau appartenait à notre empereur national. Ne prenez pas trop la grosse tête quand vous signerez vos prochaines lettres")
)
ecritoire = Item(
    "ecritoire",
    "écritoire",
    "",
    Character.conditionalAnswersBuilder(
        loupe.id,
        Character.multipleActionBuilder(
            Character.showDescriptionBuilder("Cet écritoire semble provenir de l'époque impériale ... Vous y trouvez un sceau authentique de Napoléon. Quelle mine d'or ce bateau !"),
            Item.changeInventoryActionBuilder(sceauNapoleon.id, 1)
        ),
        Character.showDescriptionBuilder("Cet écritoire semble provenir de l'époque impériale ... Vous trouverez peut-être quelque chose si vous avez une loupe sur vous.")
    )
)
demimessage = Item(
    "demimessage",
    "Une moitié de message",
    "",
    Character.showDescriptionBuilder("Oh ce message peut vous aider dans votre quête ! : demi ou entier, posé fièrement sur ma portée ou bien tristement allité ... Je suis, je suis ... ?\nRéponse : 20.15.14")
)
album = Item(
    "album",
    "album de timbres",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Ah vous le sentez bien, cet album peut vous aider à vous échapper de cette épave, il suffit de prendre le temps d'étudier chacune des pages ..."),
        Item.changeInventoryActionBuilder(demimessage.id, 1)
    )
)



vinyles = Item(
    "vinyles",
    "vinyles sans rayures",
    "",
    Character.showDescriptionBuilder("L'eau semble avoir bien conservé ces vinyles de qualité. Vous les donnerez à vos parents, en souvenir du bon vieux temps !")
)
vetements = Item(
    "vêtements",
    "vêtements vintages",
    "",
    Character.showDescriptionBuilder("Que vois-je, serait-ce ... non quand même pas ... On dirait ... les costumes des Villages People !!! Y M C A !")
)
diamants = Item(
    "diamants",
    "diamants cachés dans la boule à facettes",
    "",
    Character.showDescriptionBuilder("ces bijoux sont d'une valeur inestimable. Quel faste les années 80, c'est la disco fever sûrement ...")
)
boule = Item(
    "boule",
    "boule à facettes",
    "",
    Character.multipleActionBuilder(
       Character.showDescriptionBuilder("Mais ce n'est pas une banale boule à facettes, elle contient de véritales diamants brillants de mille feux"),
        Item.changeInventoryActionBuilder(diamants.id, 20)
    )
)
broche = Item(
    "broche",
    "broche dorée",
    "",
    Character.showDescriptionBuilder("Cette broche est magnifique ... Et elle prendra peu de place dans votre sacoche. Les cheveux, c'est la base d'un look réussi, elle ira parfaitement avec votre coupe disco")
)

chaudiere = Item(
    "chaudiere",
    "des chaudières suintantes",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("On sent une légère odeur de brûlé dans cette salle ... Ouh, vous commencez à vous brûler, vite éteignez le feu ! Oui, oui, un feu dans l'eau, vous inquiétez pas, c'est les hallucinations ... En attendant, vous en avez perdu du temps !"),
        Item.changeTimerActionBuilder(50)
    )
)
piecesrouillees = Item(
    "piecesrouilles",
    "des pièces rouillées",
    "",
    Character.showDescriptionBuilder("Vous ne finirez pas très riche avec ca ...")
)
tuyaux = Item(
    "tuyaux",
    "tuyauterie âbimée",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Voyons donc si l'on ne peut pas trouver quelque chose là dedans ... Des pièces !"),
        Item.changeInventoryActionBuilder(piecesrouillees.id, 8)
    )
)
turbines = Item(
    "turbines",
    "des turbines",
    "",
    Character.showDescriptionBuilder("Item.showDescriptionAction")
)
pompe = Item(
    "pompe",
    "pompe à oxygène",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Vous gagner un regain d'énergie, par contre, on dirait plutôt de l'hélium, car vous avez une voix étrange maintenant ... ca n'aide pas pour les hallucinations."),
        Item.changeTimerActionBuilder(70)
    )
)




globe = Item(
    "globe",
    "ancien globe terrestre",
    "",
    Character.showDescriptionBuilder("C'est un beau globe sur pied recouvert d'une peinture en vernis noir. Les bordures des pays sont tracées dans une encre dorée... Rien à voir avec les cartes modernes.")
)

machineAnticythere = Item(
    "machineAnticythere",
    "Fameuse machine d'Anticythère",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Vous n'en croyez pas vos yeux! Devant vous, la machine d'Anticythère, considérée comme le premier calculateur analogique antique. Elle semble pointer une direction..."),
        Item.changeTimerActionBuilder(-50)
    )
)

cleTiroir = Item(
    "cleTiroir",
    "clé du tiroir", "",
    Character.showDescriptionBuilder("Une clé tout ce qu'il y a de plus simple")
)
grandTableauDuBureau = Item(
    "grandTableauDuBureau",
    "Grand tableau du Commandant Jackson",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Tiens tiens, on dirait que ce tableau coulisse... Mais, c'est la cabine de pilotage derrière!"),
        bureauCommandant.addDoubleExit(cabinePilotage, "Cabine de pilotage", "Bureau du commandant")
    )
)


uniforme = Item(
    "uniforme",
    "uniforme de servante",
    "",
    Character.showDescriptionBuilder("Une robe simple noire avec un tablier blanc. Tiens, une lettre dans la poche...\n\"Oh belle Violette, douce fleur de printemps, je n'arrive pas à vous sortir de mes pensées... Retrouvons-nous ce soir, dans la salle des machines. Signé Lucio\"")
)
brochePapillon = Item(
    "brochePapillon",
    "broche papillon",
    "",
    Character.showDescriptionBuilder("C\'est une belle broche en forme de papillon irisée. On devrait en tirer un bon prix")
)
vieuxCoffre = Item(
    "plante",
    "plante verte",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("C'est un petit coffre à bijoux en bois. On sent qu'il a voyagé à travers les âges. A l'intérieur... une belle broche en forme de papillon irisée."),
        Item.changeInventoryActionBuilder(brochePapillon.id, 1)
    )
)
jeuTarot = Item(
    "jeuTarot",
    "jeu de Tarot",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("C'est un jeu de Tarot magique.... Il vous fait gagner du temps d'oxygène !"),
        Item.changeTimerActionBuilder(50)
    )
)




dessin = Item(
    "dessin",
    "dessin de Rose",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("C'est un nu de Rose, celui que Jack dessinait avant que le navire ne heurte l\'Iceberg ! Elle est belle, vous passez du temps à la regarder..."),
        Item.changeTimerActionBuilder(-50)
    )
)
bagueFiancailles = Item(
    "bagueFiancailles",
    "bague de fiançailles",
    "",
    Character.showDescriptionBuilder("Une belle bague, avec un vrai diamant... Sans doute un cadeau du prétendant de Rose"))
miroir = Item(
    "miroir",
    "un beau miroir",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Vous vous recoiffez dans le miroir. Tiens, au moment de le reposer, vous apercevez une bague de fiançailles. C'est un vrai diamant !"),
        Item.changeInventoryActionBuilder(bagueFiancailles.id, 1)
    )
)
ceinture = Item(
    "ceinture",
    "une ceinture en cuir",
    "",
    Character.showDescriptionBuilder("Elle n'a rien de spécial, mais ma foi, ça peut toujours servir.")
)
penderie = Item(
    "penderie",
    "penderie en bois sculpté ",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Vous ouvrez la penderie. Une ceinture à l'intérieur. Vous la récupérez."),
        Item.changeInventoryActionBuilder(ceinture.id, 1)
    )
)


photoFamille = Item(
    "photoFamille",
    "Vieille photo de famille",
    "",
    Character.showDescriptionBuilder("On y voit une vielle femme avec un foulard et au sourire édenté, et près d'elle un jeune pirate, tous les deux posants devant une bite d'amarrage. Elle pleure (presque) la jolie dame...")
)
serpillere = Item(
    "serpillere",
    "serpillère",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("C'est une serpillère avec un joli manche en bois. Vous la poussez un peu... Tiens, une photo par terre."),
        Item.changeInventoryActionBuilder(photoFamille.id, 1)
    )
)
seauDeau = Item(
    "seauDeau",
    "Seau rempli d'une eau verdâtre",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Vous vous penchez... Une araignée ! Vous êtes paralysé devant cette hideuse bestiole"),
        Item.changeTimerActionBuilder(-50)
    )
)
balaisBrosse = Item(
    "balaisBrosse",
    "balais brosse usé",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Voici un balais brosse qui a connu de meilleurs jours."),
        Item.changeInventoryActionBuilder(pieceDor.id, 2)
    )
)


pascal = Item(
    "pascal",
    "le caméléon Pascal",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("Mais... c'est Pascal, le caméléon de Raiponce ! Il est tellement mignon, vous ne pouvez pas vous arrêter de le caresser..."),
        Item.changeTimerActionBuilder(-50)
    )
)
plante = Item(
    "plante",
    "plante verte",
    "",
    Character.showDescriptionBuilder("Juste une plante verte... Vous vous approchez et... ah, elle est carnivore !")
)
fiole = Item(
    "fiole",
    "fiole de poison",
    "",
    Character.showDescriptionBuilder("Une fiole en verre avec un liquide violet bouillonant... étrange."))
litLianes = Item(
    "litLianes",
    "lit en lianes",
    "",
    Character.multipleActionBuilder(
        Character.showDescriptionBuilder("C'est un drôle de lit ça ! Vous vous allongez dessus, mais quelque chose se cache dessous: une fiole de poison. Hop, dans l'inventaire."),
        Item.changeInventoryActionBuilder(fiole.id, 1)
    )
)


coeurOcean = Item(
    "coeurOcéan",
    "Collier de Rose : Coeur de l'Océan",
    "",
    Character.showDescriptionBuilder("Ce collier mythique a appartenu à Rose, la survivante du Titanic. Quelle irone de retrouver celà sur le Titpanic ! Quel bijou inestimable… La fortune vous est assurée avec lui en poche. C’est un énorme diamant bleu étincelant par ses reflets brillants, taillé en forme de cœur et incrusté dans un collier de diamants.")
)

#ajout des items pickables dans les différentes pièces :
#Room.addPickable(item.id, occurency)
cuisine.addPickable(couteau.id, 5)
chambreJaune.addPickable(brosseCheveux.id, 1)
chambreJaune.addPickable(manteauRaffine.id, 1)
chambreEmploye2.addPickable(bouteilleRhum.id, 1)
chambreEmploye2.addPickable(infirmiereSexy.id, 1)
chambreEmploye2.addPickable(compasJackSparrow.id, 1)
armoireRayonnante.addPickable(collierDor.id, 3)
caveAuTresor.addPickable(riviere.id, 1)
caveAuTresor.addPickable(pieceDor.id, 5)
caveAuTresor.addPickable(lingots.id, 3)
caveAuTresor.addPickable(montre.id, 1)
reggae.addPickable(bronze.id, 3)
disco.addPickable(vinyles.id, 5)
disco.addPickable(vetements.id, 1)
disco.addPickable(broche.id, 1)
bureauCommandant.addPickable(cleTiroir.id, 1)
chambreRose.addPickable(dessin.id, 1)
chambreRose.addPickable(bagueFiancailles.id, 1)
chambreRose.addPickable(ceinture.id, 1)
chambreEmploye3.addPickable(brochePapillon.id, 2)
placardBalais.addPickable(pieceDor.id, 2)
placardBalais.addPickable(photoFamille.id, 1)

#ajout des items uniquement inspectables (et non pickables), tels que des meubles
#Room.addInspectable(Item.id)
cuisine.addInspectable(fromageMoisi.id)
cuisine.addInspectable(casserole.id)
cuisine.addInspectable(four.id)
cuisine.addInspectable(tablier.id)
salleReception.addInspectable(tapisserie.id)
salleReception.addInspectable(tableReception.id)
cabinePilotage.addInspectable(gouvernail.id)
cabinePilotage.addInspectable(trappe.id)
chambreJaune.addInspectable(litTournesol.id)
chambreJaune.addInspectable(commodeRa.id)
chambreJaune.addInspectable(armoireChambreJaune.id)
chambreEmploye2.addInspectable(litSuperpose.id)
chambreEmploye2.addInspectable(tonneauAir.id)
chambreEmploye2.addInspectable(seau.id)
armoireRayonnante.addInspectable(boiteAcier.id)
armoireRayonnante.addInspectable(boiteFer.id)
armoireRayonnante.addInspectable(drapSoie.id)
armoireRayonnante.addInspectable(lavande.id)
caveAuTresor.addInspectable(vaisselier.id)
caveAuTresor.addInspectable(plastique.id)
reggae.addInspectable(canape.id)
reggae.addInspectable(joint.id)
couloirPrincipal.addInspectable(thon.id)
couloirService.addInspectable(beauTableau.id)
couloirService.addInspectable(tableauLaid.id)
couloirService.addInspectable(balaisDuCouloir.id)
philatelie.addInspectable(commode.id)
philatelie.addInspectable(ecritoire.id)
philatelie.addInspectable(album.id)
disco.addInspectable(boule.id)
machine.addInspectable(chaudiere.id)
machine.addInspectable(tuyaux.id)
machine.addInspectable(turbines.id)
machine.addInspectable(pompe.id)
bureauCommandant.addInspectable(globe.id)
bureauCommandant.addInspectable(machineAnticythere.id)
chambreEmploye3.addInspectable(uniforme.id)
chambreEmploye3.addInspectable(vieuxCoffre.id)
chambreEmploye3.addInspectable(jeuTarot.id)
chambreRose.addInspectable(dessin.id)
chambreRose.addInspectable(miroir.id)
chambreRose.addInspectable(penderie.id)
placardBalais.addInspectable(seau.id)
placardBalais.addInspectable(balaisBrosse.id)
placardBalais.addInspectable(serpillere.id)
chambreVerte.addInspectable(pascal.id)
chambreVerte.addInspectable(plante.id)
chambreVerte.addInspectable(litLianes.id)
chambreVerte.addInspectable(fiole.id)



#ajout d'items à l'inventaire :
#myGame.addItemToInventory(Item.id, 2)
myGame.addItemToInventory(pieceDor.id, 10)








#création des personnages :
#Character = Character("nom", "description affichée du personnage", "dialogue initial du personnage", None)
ratatouille = Character(
    "Ratatouille à l'accent marseillais",
    "Vous voici en parfaite hallucination, voilà que vous parlez à Ratatouille maintenant !",
    "\"Hey, bienvenue dans ma nouvelle cuisine l’ami ! Mes amis et moi mourrions de faim, et nous avons trouvé cette magnifique cuisine que je reprends à mon compte ! Un bout de moisi-fromage peut-être ?\" demande-t-il malicieusement avec un clin d’œil. \"Quoi, non ? Bon ça sera pour plus tard.\" Et il se met alors à chanter une chanson à tue-tête en emportant son fromage pour en faire je ne sais quel plat. \"Et sortez les bouteilles, finis les ennuis. Je dresse la table, de ma nouvelle vie. Je suis heureux à l'idée de ce nouveau destin. Une vie à me cacher, et puis libre enfin\"",
    None
)

corbeau = Character(
    "Maître Corbeau",
    "Vous voyez Maître Corbeau sur son lustre perché",
    "Maître Corbeau, sur un lustre perché, \nTenait en son bec une clef.\nMaître Voleur, par le brillant alléché, \nVoulu ainsi lui parler. \n\"Et bonjour, Monsieur du Voleur. \nQue vous êtes courbé ! que votre sac est gros ! \nSans mentir, si votre butin\nSouhaitait une sortie à ce navire trouver, \nVous me demanderiez cette clef. \nA ces mots, une envie de fromage me vint,\nMoisi dans le navire, je l’aimerais mien.\nAlors seulement peut-être lâcherais-je cette clef\nPour ce fromage à mon bec délicat saisir \"",
    None
)

scar = Character(
    "Scar en Scaphandre",
    "Tout droit sortir de sa savane, Scar se dresse fièrement devant vous. Effet quelque peu limité par la présence d’un scaphandre qu’il utilise pour respirer.",
    "\"Je ne suis pas fou, comme personnages de dessin-animé mal dessiné, à me balader sans avoir de quoi respirer ! Personne ne peut égaler ma grandeur et un jour je serai Roi. Sois donc prêt(e) !\" Son regard carnassier et ses jeux de trône ne vous inspirent guère. Mais il détient peut-être quelque information juteuse. Sur un trésor caché par exemple.",
    None
)

guido = Character(
    "Guido van Rossum",
    "Un homme à lunettes ayant un air savant se tient près du gouvernail.",
    "Ah, tu es donc parvenu jusqu’ici. Il est beau ce navire, n’est-ce pas ? Si tu as correctement réalisé ta quête, tu as dû trouvé le mot de passe pour sortir de ce navire, n’est-ce pas ?\nVoici donc la simple énigme : Qu’ai-je inventé ?\nSi c’est la bonne, la sortie se révèlera.",
    None
)

jackSparrow = Character(
    "Capitaine Jack Sparrow",
    "Jack Sparrow est adossé à un mur vide. Et vous regarde d’un air goguenard.",
    "Hé, gamin ! T'aurais pas un peu de rhum pour moi ? J'ai encore perdu ma bouteille.",
    None
)

dieuRa = Character(
    "Personnification du Dieu Râ",
    "La personnification du Dieu Râ se tient devant un mur de la pièce. Il resplendit tellement que vous tentez de vous protéger de sa lumière en mettant votre bras en visière devant vos yeux. Vous vous prosternez devant ce grand Dieu.",
    "Je sais ce que tu cherches. Ce navire est abandonné depuis bien trop longtemps, et ses richesses doivent rejoindre le monde des hommes vivants. Sachez que la couronne la plus précieuse du monde se trouve dans cette pièce. Voici un indice de taille : elle apprécie l’acier. \nPensez à faire quelqu’offrande à ma commode avant de repartir. Je vous en serai reconnaissant plus tard.",
    None
)

bobMarley = Character(
    "Bob Marley",
    "Vous voyez un jeune homme avec un joint et un bonnet jaune, vert et rouge",
    "\"Hey bro\"",
    None
)


bebeSeanPaul = Character(
    "Bébé Sean Paul",
    "Un jeune garcon se présente à vous, bandana sur la tête, cheveux tressés, grosses chaînes en argent au tour du coup ... Un Bob Marley cheap en quelque sorte.",
    "Eh, eh, tu peux m'aider stp ? \Bob Marley est censé m'enseigner le reggae mais il est soir-disant trop occupé à communiquer avec Haile Selassie, le prophète du rastafarisme ... Il m'aime pas je crois, il se bouche les oreilles quand je chante mon reggaeton. Et toi tu en penses quoi ?",
    None
)


pereFouras = Character(
    "Père Fouras",
    "Oui, c'est bien lui, le vrai Père Fouras de Fort Boyard ! Il fait plus jeune à la TV ... Avant de prendre un selfie avec lui, répondez à son énigme ! Il l'énonce de sa voix douce et chrevrotante.",
    "\"Petite ou grande, On la trouve sur les chemins. D'un philosophe grec comme le dit la légende, A jamais elle a scellé le destin. Qui est-elle ?\"",
    None
)

demons = Character(
    "demons",
    "Un petit groupe de diablotins s'approche, avec leurs petites cornes et leurs fourchettes à la main. Pas de quoi s'effrayer, ils semblent plutôt d'humeur badine. Ce sont les démons de minuit.",
    "\"Hey, salut toi, veux-tu que l'on t'entraîne au bout de la nuit ?\"",
    None
)

dori = Character(
    "dori",
    "Dori, un petit poisson bleu, tout fin et tête en l'air se tient devant vous, la nageoire posée de manière songeuse sur ce qui lui sert de bouche.",
    "\"Oh, tu m'as l'air perdu toi... Moi je me suis déjà échappée du bateau tu sais ? C’est allé vraiment très très vite. Il y avait une bouteille de rhum et une boussole, et Jack Sparrow qui m’a parlé. Il m’a dit plein de trucs mais j’ai pas tout retenu. Et puis je suis passée dans un placard à balais, et là, impossible de sortir, car un pirate voulait absolument voir sa la photo de sa maman pour me laisser passer. Et puis il y a cette drôle de chambre enfumée, avec un monsieur étrange, et puis...\" Déjà lassé par son blabla interminable, vous la coupez.",
    None
)

jackTitanic = Character(
    "jackTitanic",
    "Jack, de Titanic, est assis en boule dans un coin de la chambre, en pleurs.",
    "\"Rose est partie, ma vie n'a plus de sens...\"",
    None)


pirate = Character(
    "Vieux pirate",
    "Un gros pirate surgit de l'ombre. Il bloque la porte et vous menace de sa jambe de bois.",
    "\"Qui va là? Oh, moussaillon, enfin de la compagnie! Dis, j'ai perdu la photo de maman, j'y tiens beaucoup... Tu l'aurais pas vue ?\"",
    None
)

tarzan = Character(
    "Tarzan",
    "Tarzan dans toute sa vigueur, entouré d'une peau de léopard, vous jette un regard de braise.",
    "\"Mon ami! Tu me parais respectueux de la nature, alors je vais te donner un indice : Dans la chambre rose, tu trouveras une ceinture. Elle pourra te rapporter beaucoup, ne passe pas à côté !\"",
    None
)

#création de la ou des speakToAction de chaque personnage :
#Cas d'une action unique :
#Character.speakToAction = Character.conditionalAnswersBuilder(
                    # item.id, [id nécessaire pour avoir la bonne réponse du personnage]
                    #Character.answersMenuBuilder(Character, nomDuMenuDeReponsesDeCePersonnage), [menu des réponses possibles à donner]
                    #Character.showDescriptionBuilder("Dialogue si pas l'item voulu") [si on a pas l'item, autre dialogue]
                    # )
#cas de plusieurs actions exécutées en même temps au moment de parler au personnage :
#Character.speakToAction = Character.multipleActionBuilder(Item.changeInventoryActionBuilder(Item.id, 5), Character.showDescriptionBuilder("dialogue")) [grâce à multipleActionBuilder je peux effectuer plusieurs actions en même temps (il suffit d'en mettre autant que je peux en tant que paramètres]

#Création d'un menu de réponses pour le conditionalAnswersBuilder :
#dorisAnswersMenu = Menu("Vous répondez à Dori :", myGame, myGame.currentMenu)
#dorisAnswersMenu.addOption(Option("Merci Dori", Character.showDescriptionBuilder("De rien, je t'aime.")))
#dorisAnswersMenu.addOption(Option("Vas te faire voir Dori", Character.showDescriptionBuilder("Bah d'accord, je vais à la Hackerhouse de Poupet.")))
#dorisAnswersMenu.addOption(Option("Allez viens Dori, on se fait un python", Character.showDescriptionBuilder("C'est quand tu veux Bouffi !")))
#dorisAnswersMenu.addOption(Option("Fromaaaaaaaaage !!", Character.removeItemBuilder(fromage.id, 1)))

ratatouille.speakToAction = Character.showDescriptionBuilder(ratatouille.dialogue)

corbeau.speakToAction = Character.multipleActionBuilder(
    Character.showDescriptionBuilder(corbeau.dialogue),
    Character.conditionalAnswersBuilder(
        fromageMoisi.id,
        Character.multipleActionBuilder(
            Character.showDescriptionBuilder("« De Grâce ! Qu’est-ce donc que ce mets ? \nIl sera merveilleux pour mon plumage. \nCette clef je te donne, \ncar inutile elle m’est désormais."),
            Item.changeInventoryActionBuilder(clefTiroir.id, 1)
        ),
        Character.showDescriptionBuilder(corbeau.dialogue+"\n\nSans présent de ta part, \nJe ne puis te céder cette clef rare.")
    )
)


answersScarMenu = Menu("Vous répondez à Scar en scaphandre :", myGame, myGame.currentMenu)
answersScarMenu.addOption(
    Option(
        "Pourriez-vous m’aider à trouver un trésor caché, au grand Scar, Roi légitime de tous les lions ? ",
        Character.showDescriptionBuilder("\"Mais bien-sûr mon petit, voilà ton indice : ce corniaud de corbeau est vraiment un nigaud ! Toujours là à caqueter et plaidoyer. Un vieux sénile qu’il est, voilà ! Si j’étais toi je ne l’écouterais même pas. Par contre, moi je sais que j’ai flairé l’odeur d’un trésor dans la chambre qu’à investi ce gueux à bonnet coloré. Puis plus rien, car une fumée infecte se mettait à sortir de sa chambre. Tentes-y donc ta chance mon petit.\"")
    )
)
answersScarMenu.addOption(
    Option(
        "\"Ouais, bah essayez sans le scaphandre déjà, hein. Ca vous rendra peut-être plus effrayant.\" et vous vous en allez en ricanant.",
        Character.showDescriptionBuilder("Scar vous regarde d’un air interloqué et bien dubitatif")
    )
)
answersScarMenu.addOption(
    Option(
        "\"Grand Roi des Hyènes, je suis à court d’air, aidez-moi ! Quelle est donc la sortie de cet enfer ? \"",
        Character.showDescriptionBuilder("\"Roi des Hyènes ?? Court vite avant que je ne t’attrape mécréant ! Je suis le roi légitime des Lions ici !\"")
    )
)

scar.speakToAction = Character.multipleActionBuilder(
    Character.showDescriptionBuilder(scar.dialogue),
    Character.answersMenuBuilder(scar, answersScarMenu)
)

def enterPasswordAction(game):
    password = input("")
    if password.lower() == "python":
        game.clearScreen()
        print("Vous avez réussi à vous échapper avec un bien beau butin. Mes félicitations !")
        exit(0)
    else:
        game.currentAction = "Ce n'est pas la bonne réponse. Retentez votre chance, ou vous mourrez enfermé."


guido.speakToAction = Character.multipleActionBuilder(
    Character.showDescriptionBuilder(guido.dialogue),
    enterPasswordAction
)


jackSparrow.speakToAction = Character.multipleActionBuilder(
    Character.showDescriptionBuilder(jackSparrow.dialogue),
    Character.conditionalAnswersBuilder(
        compasJackSparrow.id,
        Character.multipleActionBuilder(
            Item.changeInventoryActionBuilder(pieceDor.id, -10),
            Character.showDescriptionBuilder("Jack gronde de colère : \”Que fais-tu avec mon précieux compas ?! Lâche-le tout de suite, il n’est pas à toi ! Maintenant ce que je désire le moins au monde s’est libéré. Tu m’as fichu le capitaine Salazar et ses spectres dans le Triangle du Diable aux trousses. Tu comprends dans quelle merde noire tu m’as foutus ? File-moi de la thune, j’en aurai besoin pour m’enfuir.\” Il vous dépouille alors de 10 pièces d’or.")
        ),
        Character.conditionalAnswersBuilder(
            bouteilleRhum.id,
            Character.multipleActionBuilder(
                Character.showDescriptionBuilder("\"Ah, voilà ma bouteille, merci.\" Après avoir bu une rasade, il rajoute : \"Tu sais ? Toi qui est voleur là, je connais une pièce de ce bateau qui pourrait t'intéresser. C'est jaune et luxueux et il y a des tournesol. Caché dedans, il y a le Dieu Râ. Ouais, rien qu'ça hein. Et si tu lui fais une offrande il te donne un trésor. Moi j'lai pas eu, j'avais pas d'offrande. Je suis pas pété de thune, ha ha ha!\" Il achève sa phrase par un grand éclat de rire et un hoquet."),
                Item.changeInventoryActionBuilder(bouteilleRhum.id, -1)
            ),
            Character.showDescriptionBuilder("Passe ton chemin petit, je n'ai rien à te dire. Sans rhum, je parle pas de toute façon.")
        )
    )
)

dieuRa.speakToAction = Character.showDescriptionBuilder(dieuRa.dialogue)


bobMarley.speakToAction = Character.multipleActionBuilder(
    Item.changeTimerActionBuilder(-30),
    Character.showDescriptionBuilder("Comme je suis d'humeur taquine, même si j'en ai pas l'air, parce que je suis shooté H24, je ne te laisse pas partir avant de t'avoir chanté ma nouvelle chanson : one looove, one heaaarth, let's code together and, feeeel like a spy  "))





bebeSeanPaulAnswersMenu = Menu("Vous répondez à Bébé Sean Paul :", myGame, myGame.currentMenu)
bebeSeanPaulAnswersMenu.addOption(
    Option(
        "Oui vive le reggaeton et les mojitos en bord de mer",
        Character.multipleActionBuilder(
            Item.changeTimerActionBuilder(50),
            Character.showDescriptionBuilder("Je t'aime bien toi, tiens un peu d'energie pour améliorer ton déhanché.")
        )
    )
)
bebeSeanPaulAnswersMenu.addOption(
    Option(
        "Personne ne dépassera jamais le maître, retourne à la crèche Sean Paupaul",
        Character.multipleActionBuilder(
            Item.changeTimerActionBuilder(-30),
            Character.showDescriptionBuilder("\"Tu verras, un jour je serai millionnaire, et le monde entier glorifiera ma musique et mon style !!\" Et il éclate d'un grand rire de méchant qui fait peur comme dans les films.")
        )
    )
)
bebeSeanPaul.speakToAction = Character.multipleActionBuilder(
    Character.showDescriptionBuilder(bebeSeanPaul.dialogue),
    Character.answersMenuBuilder(bebeSeanPaul, bebeSeanPaulAnswersMenu)
)





pereFourasAnswersMenu = Menu("Vous répondez à Père Fouras :", myGame, myGame.currentMenu)
pereFourasAnswersMenu.addOption(
    Option(
        "La crotte de chien",
        Character.multipleActionBuilder(
            Item.changeTimerActionBuilder(-30),
            Character.showDescriptionBuilder("Et non, mauvaise réponse ! Une prochaine fois peut-être")
        )
    )
)
pereFourasAnswersMenu.addOption(
    Option(
        "La ciguë",
        Character.multipleActionBuilder(
            Item.changeTimerActionBuilder(+120),
            Character.showDescriptionBuilder("Bonne réponse ! Socrate serait fier de toi, paix à son âme.")
        )
    )
)
pereFourasAnswersMenu.addOption(
    Option(
        "La sagesse",
        Character.multipleActionBuilder(
            Item.changeTimerActionBuilder(-30),
            Character.showDescriptionBuilder("Et non, mauvaise réponse ! Une prochaine fois peut-être")
        )
    )
)
pereFourasAnswersMenu.addOption(
    Option(
        "L'étoile filante",
        Character.multipleActionBuilder(
            Item.changeTimerActionBuilder(-30),
            Character.showDescriptionBuilder("Et non, mauvaise réponse ! Une prochaine fois peut-être")
        )
    )
)

pereFouras.speakToAction = Character.multipleActionBuilder(
    Character.showDescriptionBuilder("Oui, c'est bien lui, le vrai Père Fouras de Fort Boyard ! Il fait plus jeune à la TV ... Avant de prendre un selfie avec lui, répondez à son énigme !\n \"Petite ou grande, On la trouve sur les chemins. D'un philosophe grec comme le dit la légende, A jamais elle a scellé le destin. Qui est-elle ?\""),
    Character.answersMenuBuilder(pereFouras, pereFourasAnswersMenu)
)



demonsAnswersMenu = Menu("Vous répondez aux démons de minuit :", myGame, myGame.currentMenu)
demonsAnswersMenu.addOption(
    Option(
        "oui",
        Character.multipleActionBuilder(
            Item.changeTimerActionBuilder(60),
            Character.showDescriptionBuilder("Alors tiens : un peu d'énergie pour ne pas t'endormir !")
        )
    )
)
demonsAnswersMenu.addOption(
    Option(
        "non",
        Character.multipleActionBuilder(
            Item.changeInventoryActionBuilder(vetements.id, 5),
            Character.showDescriptionBuilder("Que la foudre du disco s'abatte sur toi, on te retire quelque chose de ton inventaire !")
        )
    )
)
demons.speakToAction = Character.multipleActionBuilder(
    Character.showDescriptionBuilder(demons.dialogue),
    Character.answersMenuBuilder(demons, demonsAnswersMenu)
)



dori.speakToAction = Character.multipleActionBuilder(
    Character.showDescriptionBuilder(dori.dialogue),
    Character.conditionalAnswersBuilder(
        carteDuNavire.id,
        Character.showDescriptionBuilder("\"Ah mais je me souviens maintenant ! Pour sortir il faut aller parler au monsieur à lunettes dans la cabine de pilotage. C'est simple, tu passes par le bureau du Commandant. Lui aussi il a une super énigme à te donner.\""),
        Character.showDescriptionBuilder("\"Ah non, je ne me souviens toujours pas de la sortie en fait. J'ai des problèmes de mémoire tu sais ? Surtout à court terme. Peut-être qu'avec une carte des lieux, ça pourrait me revenir cependant.\"")
    )
)





jackTitanic.speakToAction = Character.multipleActionBuilder(
    Character.showDescriptionBuilder(jackTitanic.dialogue),
    Character.conditionalAnswersBuilder(
        dessin.id,
        Character.multipleActionBuilder(
            Item.changeInventoryActionBuilder(dessin.id, -1),
            Item.changeInventoryActionBuilder(coeurOcean.id, 1),
            Character.showDescriptionBuilder("Ma dulcinée! Je peux reposer en paix désormais. Tiens, en remerciement je t’offre le coeur de l’océan, le bijou qu’elle porte sur le dessin. Adieu !")
        ),
        Character.showDescriptionBuilder("Si seulement je pouvais la revoir une dernière fois...")
    )
)


pirate.speakToAction = Character.multipleActionBuilder(
    Character.showDescriptionBuilder(pirate.dialogue),
    Character.conditionalAnswersBuilder(
        photoFamille.id,
        Character.multipleActionBuilder(
            Character.showDescriptionBuilder("\"La photo de ma Maman ! Je l'avais perdue depuis des lustres ! Voilà donc la raison pour laquelle je suis me suis enfermé dans ce placard depuis tout ce temps. Je ne voulais que personne de sorte, de peur qu'on me vole cette photo que j'avais perdue. Merci beaucoup moussaillon !\""),
            Item.changeInventoryActionBuilder(photoFamille.id, -1)
        ),
        Character.showDescriptionBuilder("Sans ma photo, pas de sortie ! Libre à toi de moisir ici comme ces vieux balais.")
    )
)



tarzan.speakToAction = Character.showDescriptionBuilder(tarzan.dialogue)

#ajout du chaque personnage dans une pièce :
#Room.addCharacter(Character)
cuisine.addCharacter(ratatouille)
salleReception.addCharacter(scar)
salleReception.addCharacter(corbeau)
cabinePilotage.addCharacter(guido)
chambreEmploye2.addCharacter(jackSparrow)
reggae.addCharacter(bebeSeanPaul)
reggae.addCharacter(bobMarley)
philatelie.addCharacter(pereFouras)
disco.addCharacter(demons)
machine.addCharacter(dori)
chambreRose.addCharacter(jackTitanic)
placardBalais.addCharacter(pirate)
chambreVerte.addCharacter(tarzan)
