# Flare
Flare is a simple propagation code. It is used to model the gradual geographical spread of certain events. These could include certain food conditions, knowledge, diseases, opinions or violent events.

## Installation

Flare is installed simply by copying it to your favorite directory, or by using `git clone`.

## Testing
Simply type `python3 test_flare.py`. This will run Flare with a default ruleset and the following input files:
* `test_input_csv/locations.csv` for location data.
* `test_input_csv/links.csv` for link data.

Note that Flare does not support reading in `closures.csv` files, while Flee does.

### Output

Flare will produce CSV output in the terminal. 
* Column 1 will indicate number of days elapsed.
* Other columns indicate the conflict state for each of the locations in Flare. (location names are in row 0)
  * state will be 1 if labelled as an affected area, or 0 if not.
