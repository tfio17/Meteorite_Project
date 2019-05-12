#
#
## Tom
#
## Final Project
#   Meteorite dataset application


# Project requirements

# 1) Demo (slide deck)
# 2) Code itself

# Code Reqs:

'''
1) A custom library - contains classes, functions, constants
2) Iteration, some decision making
3) import from your library and some standard libraries
4) list of third party libraries used
5) must do some kind of file i/o - at least read something in
    and produce an output file
6) Use of a data structure
7) Use of object orientation, specifically inheritance
8) Data File with at least 10,000 items
'''

# Do I meet?

'''
1) Meteorite_Lib - Location & Meteorite Classes (M is sublcass of L)
                    - Contains other functions for generating/cleaning data
                    - contains constant for Radius of Earth in km
2) iterates through list of records to generate objects
    - iterates through to calculate distance and find minimum
    - makes a decision by finding the minumum distance and returning
3) done, import Meteorite_Lib & from pandas/math in 
4) pandas, math
5) reads input from weburl, returns obj details (could return as json)
6) Create a queue of meteorite records
7) use inheritance and OO where Meteorite entries are inheriting from Location
    which also gets used for the user's location
8) Cleaned file containes >38,000 meteorite entries!

'''

from Meteorite_Lib import *


# First run get_data to pull file from online API and clean it up
df = get_data()
# Then we generate records and a list of names
records, NameList = generate_records(df)

# Populate our new database

met_list = []
for i in records:
    meteorite_i = new_record(i)
    met_list.append(meteorite_i)

# Request User Location
'''
A couple examples to try:

New Brunswick, NJ (Rutgers University) is lat = 40.4862, long = -74.4518
Skillman, NJ (Bloomberg Office) is lat = 40.4201, long = -74.7147
Paris, France is lat = 48.8566, long = 2.3522
London, ,England is lat = 51.5074, long = 0.1278
'''

user_lat, user_long = userLocation()
myLoc = Location("userLoc", user_lat, user_long)

dist_list = []
for i in range(len(met_list)):
    dist_i = met_list[i].getDistance(myLoc.getLat(),myLoc.getLong())
    dist_list.append(dist_i)

x = dist_list.index(min(dist_list))
name = met_list[x].getName()

#print("Meteorites in Database: ", met_list[0].getCount())
print("Nearest impact to your location: ", name)
print("Impacted ", round(min(dist_list),2), "km from your location.")
print("Details: \n")
print(met_list[x])

valueEstimate(met_list[x])
