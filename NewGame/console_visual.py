def buildPrintBloc(description, lengthMax):
    newList = description.split('\n')
    bloc = []
    for string in newList:
        nbOfline = len(string) // lengthMax
        restLine = len(string) % lengthMax

        for i in range(nbOfline):
            substring = string[(i * lengthMax):(i + 1) * lengthMax]
            bloc.append(substring)
        lastString = string[(nbOfline * lengthMax):]

        nbOfSpace = lengthMax - restLine
        spaceString = " " * nbOfSpace

        printedString = lastString + spaceString
        bloc.append(printedString)

    return bloc

def printBloc(bloc):
    for line in bloc:
        print(line)


def addBorderToBloc(bloc, angleHautGauche="╒", angleHautDroite="╕", angleBasGauche="╘", angleBasDroite="╛", hautBas="═", gaucheDroite="│"):
    blocWithBorder = []
    firstLine = angleHautGauche+(len(bloc[0]))*hautBas+angleHautDroite
    blocWithBorder.append(firstLine)

    for line in bloc:
        centerLine = gaucheDroite+line+gaucheDroite
        blocWithBorder.append(centerLine)

    lastLine = angleBasGauche+(len(bloc[0]))*hautBas+angleBasDroite
    blocWithBorder.append(lastLine)

    return blocWithBorder

    #sousChaine1 =   string[:lengthMax]
    #sousChaine2 = string[lengthMax:(lengthMax*...)]
    #affichage = []
    #affichage.append(sousChaine1)
    #affichage.append(sousChaine2)

    #lastString = string[lengthMax*...:lengthMax]

#description = "Vous êtes dans un saloon qui n'a pas vu la lumière du jour\n depuis des lustres ! Oui, comme celui tout éclaté qui devait éclairer cette pièce autrefois. La dernière fête qui s'est déroulée ici a dû faire salle comble : les bouteilles jonchent pêle-même de grandes tables. Une immense tapisserie habiextdcfykvghlbuijmnbihvgucfyxdtwrserxdcfjkvghljblle le mur du fond.Vous êtes dans un saloon qui n'a pas vu la lumière du jour depuis des lustres ! Oui, comme celui tout éclaté qui devait éclairer cette pièce autrefois. La dernière fête qui s'est déroulée ici a dû faire salle comble :\n les bouteilles jonchent pêle-même de grandes tables. Une immense tapisserie habiextdcfykvghlbuijmnbihvgucfyxdtwrserxdcfjkvghljblle le mur du fond.Vous êtes dans un saloon qui n'a pas vu la lumière du jour depuis des lustres ! Oui, comme celui tout éclaté qui devait éclairer cette pièce autrefois. La dernière fête qui s'est déroulée ici a dû faire salle comble : les bouteilles jonchent pêle-même de grandes tables. Une immense tapisserie habiextdcfykvghlbuijmnbihvgucfyxdtwrserxdcfjkvghljblle le mur du fond."
#myNewString = buildPrintBloc(description, 100)
#myNewString = addBorderToBloc(myNewString, "╒", "╕", "╘", "╛", "═", "│")
#printBloc(myNewString)