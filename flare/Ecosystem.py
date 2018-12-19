
class Ruleset:
    def __init__(self):
        self.default_chance = 0.0
        self.adjacency_chance = [0.0,0.05,0.1,0.15,0.2]

    def doesFlareStartHere(adjacent_flares):
        flare_chance = self.default_chance
        if adjacent_flares > len(self.adjacency_chance):
            flare_chance += self.adjacency_chance[-1]
        else:
            flare_chance += self.adjacency_chance[adjacent_flares]

        

class Location:
    def __init__(self, name, pop, country):
        self.pop = 0
        self.name = name
        self.country = country
        self.links = []

        self.flare = False

    def evolve(self, r):
        """
        r = Ruleset.
        """
        if self.flare:
            pass
        else:
            adjacent_flares = 0
            for l in self.links:
                if l.endpoint.flare:
                    adjacent_flares += 1
            self.flare = r.doesFlareStartHere(adjacent_flares)

class Link:
    def __init__(self, endpoint, distance)
        self.endpoint = endpoint
        self.distance = float(distance)

class Ecosystem:

    def __init__(self):
        self.locations = []
        self.locationNames = []
        self.time = 0
        self.closures = []

    def addLocation(self, name, pop=0, country=""):
        l = Location(name, pop, country)
        self.locations.append(l)
        self.locationNames.append(name)

    def linkUp(self, endpoint1, endpoint2, distance=1.0):
    """ Creates a link between two endpoint locations
    """
        endpoint1_index = -1
        endpoint2_index = -1
        for i in range(0, len(self.locationNames)):
            if(self.locationNames[i] == endpoint1):
                endpoint1_index = i
            if(self.locationNames[i] == endpoint2):
                endpoint2_index = i

        if endpoint1_index < 0:
            print("Diagnostic: Ecosystem.locationNames: ", self.locationNames)
            print("Error: link created to non-existent source: ", endpoint1, " with dest ", endpoint2)
            sys.exit()
        if endpoint2_index < 0:
            print("Diagnostic: Ecosystem.locationNames: ", self.locationNames)
            print("Error: link created to non-existent destination: ", endpoint2, " with source ", endpoint1)
            sys.exit()

        self.locations[endpoint1_index].links.append( Link(self.locations[endpoint2_index], distance) )
        self.locations[endpoint2_index].links.append( Link(self.locations[endpoint1_index], distance) )


    def StoreInputGeographyInEcosystem(self, ig):
        """
        Store the geographic information in this class in a flare simulation,
        overwriting existing entries.
        """
        lm = {}

        for l in ig.locations:
            if len(l[1]) < 1:  # if population field is empty, just set it to 0.
                l[1] = "0"
            if len(l[7]) < 1:  # if population field is empty, just set it to 0.
                l[7] = "unknown"

            movechance = l[4]

            lm[l[0]] = self.addLocation(
                l[0], movechance=movechance, pop=int(l[1]), country=l[7])

        for l in ig.links:
            if (len(l) > 3):
                if int(l[3]) == 1:
                    self.linkUp(l[0], l[1], int(l[2]))
                if int(l[3]) == 2:
                    self.linkUp(l[1], l[0], int(l[2]))
                else:
                    self.linkUp(l[0], l[1], int(l[2]))
            else:
                self.linkUp(l[0], l[1], int(l[2]))

        for l in self.closures:
            self.closures.append([l[0], l[1], l[2], int(l[3]), int(l[4])])

        return lm

