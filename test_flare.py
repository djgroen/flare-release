from flee import InputGeography
from flare import Ecosystem
import numpy as np
import sys

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

    output_header_string = "Day"
    for l in e.locations:
        output_header_string += ",%s" % (l.name)

    print(output_header_string)

    for t in range(0,end_time):

        e.evolve()

        output = "%s" % t

        for l in e.locations:
            if l.flare:
                output +=",1"
            else: 
                output +=",0"

        print(output)
