from datamanager import handle_refugee_data
from datamanager import DataTable #DataTable.subtract_dates()
from flee import InputGeography
import numpy as np
import outputanalysis.analysis as a
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

    ig.ReadLocationsFromCSV("test_data/test_input_csv/locations.csv")

    ig.ReadLinksFromCSV("test_data/test_input_csv/routes.csv")

    e,lm = ig.StoreInputGeographyInEcosystem(e)

    #print("Network data loaded")

    output_header_string = "Day,"

    for t in range(0,end_time):

        e.evolve()

        for i in camp_locations:
            errors += [a.rel_error(lm[i].numAgents, loc_data[j])]
            abs_errors += [a.abs_error(lm[i].numAgents, loc_data[j])]

            j += 1

        output = "%s" % t

        print(output)
