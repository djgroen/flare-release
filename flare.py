from flee import InputGeography
from flare import Ecosystem
import numpy as np
import sys

def AddInitialRefugees(e, d, loc):
    """ Add the initial refugees to a location, using the location name"""
    num_refugees = int(d.get_field(loc.name, 0, FullInterpolation=True))
    for i in range(0, num_refugees):
        e.addAgent(location=loc)

def date_to_sim_days(date):
    return DataTable.subtract_dates(date,"2010-01-01")


if __name__ == "__main__":

    end_time = 100

    if len(sys.argv)>1:
        if (sys.argv[1]).isnumeric():
            end_time = int(sys.argv[1])

    ig = InputGeography.InputGeography()

    ig.ReadLocationsFromCSV("test_input_csv/locations.csv")

    ig.ReadLinksFromCSV("test_input_csv/routes.csv")

    e = Ecosystem.Ecosystem()

    lm = e.StoreInputGeographyInEcosystem(ig)

    #print("Network data loaded")

    file = open("flare-out.csv","w")

    output_header_string = "#Day,"

    for l in e.locations:
        output_header_string += " %s," % (l.name)
    
    output_header_string += "\n"
    file.write(output_header_string)

    for t in range(0,end_time):

        e.evolve()

        output = "%s" % t

        for l in e.locations:
            if l.flare:
                output +=", 1"
            else: 
                output +=", 0"

        output += "\n"
        file.write(output)

    file.close()