# Exemple directement récupéré de stackoverflow et adapté pour fonctionner sur tous les OS. Sinon quelques lignes sur windows auraient suffit:

# import msvcrt


# while True:
#     if not msvcrt.kbhit():
#     	continue
#     print("Key pressed: %s" % msvcrt.getch())
#     print("Now next input...")

class Getch:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        if(msvcrt.kbhit()):
            return msvcrt.getch()
        return None


arrow_keys_mapping = {
	b'H': 'z',
	b'K': 'q',
	b'P': 's',
	b'M': 'd'
}

def waitForKey():
    inkey = Getch()

    k=inkey()

    if k is None:
        return None
    # cas spécial touches non ascii sur windows
    if k == b'\xe0' or k == b'\000':
        return arrow_keys_mapping[inkey()]
    if k == b'\x08':
        return "return"
    if k == b'\x1b':
        return "escape"

    if k != '':
        return k.decode('ascii')


    return None