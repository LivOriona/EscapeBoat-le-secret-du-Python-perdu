class Exit:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __repr__(self):
        return "Exit("+self.source.name+"=>"+self.destination.name+")"
