#
#
## Tom
#
## Library for Final Project
#   Meteorite dataset


# imports
import pandas as pd
from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6373.0

def calc_distance(lat1, long1, lat2, long2):

    # convert to radians
    lat1, long1, lat2, long2 = radians(lat1), radians(long1), radians(lat2), radians(long2)
    dlong = long2 - long1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlong / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Distance is in km!
    distance = R * c

    return distance
    

# Create function for generating dataset
def download_data():

    # This function simply calls the API and pulls our dataset 

    df = pd.read_csv('https://query.data.world/s/plssyzzuum3lzrpxcvzooxkloh4xbv')

    return df

def get_data():
    
    # This function will take a raw df for our data pull, and return a clean frame
    df = download_data()

    #make sure only complete rows are retained
    df.dropna(inplace=True)

    # datetime formatting
    df['year'] =  pd.to_datetime(df['year'], infer_datetime_format=True, errors='coerce')

    #make sure only complete rows are retained
    df.dropna(inplace=True)
    df['year'] = df.year.dt.year.astype(int)

    # make sure year is in the past
    df = df[df.year <= 2019]

    # print date range for dataset
    YearList = list(df.year.sort_values(ascending=False))
    #print("Date Range: ", str(YearList[0]) + "-" + str(YearList[-1]))

    return df

def generate_records(df):

    # This function takes a df as input, and outpits a list of dicts
    records = df.to_dict(orient='records')
    NameList = list(df.name.sort_values(ascending=True))

    return records, NameList


def new_record(mydict):

    # This function takes a dictionary as input and turns it into a new meteorite entry
    m = mydict
    new_entry = Meteorite(m['name'], m['recclass'], m['mass (g)'], m['year'], m['reclat'], m['reclong'])
    return new_entry

def userLocation():

    # This function is to request the user's location
    user_lat = float(input("Please enter your latitude: "))
    user_long = float(input("Please enter your longitude: "))

    return user_lat, user_long

def valueEstimate(meteorite):

    # This function takes a meteorite object input and prints an estimated value range
    L = 300 # low-ball estimate for $/g
    H = 1000 # high-ball estimate for $/g

    M = float(meteorite.getMass())

    LE = round(L*M,2)
    HE = round(H*M,2)
    print("\nThe estimated value is between:")
    print("$"+str(LE)+" & "+"$"+str(HE))
    
        
class Location():
    locCount = 0

    # Constructor
    def __init__(self, name, lat, long):
        self.name = name
        self.lat = lat
        self.long = long
        Location.locCount += 1

    # getters
    def getCount(self):
        return Location.locCount

    def getName(self):
        return self.name

    def getLat(self):
        return self.lat

    def getLong(self):
        return self.long

    def getDistance(self, lat1, long1):
        lat2 = self.getLat()
        long2 = self.getLong()
        distance = calc_distance(lat1, long1, lat2, long2)
        return distance
    
    # Str
    def __str__(self):
        aString = "LocationObj:" + self.name + str(self.lat) + str(self.long)
        return aString

    # deconstructor
    def __del__(self):
        print("A location has been destroyed: ",self.name)
        Location.locCount -=1

class Meteorite(Location):

    mCount = 0

    # Constructor
    def __init__(self, name, metClass, mass_g, year, lat, long):
        Location.__init__(self, name, lat, long)
        self.metClass = metClass
        self.mass_g = mass_g
        self.year = year
        Meteorite.mCount +=1

    # getters
    def getCount(self):
        return Meteorite.mCount

    def getClass(self):
        return self.metClass
    
    def getMass(self):
        return self.mass_g
    
    def getYear(self):
        return self.year

    # Str
    def __str__(self):
        aString = "MeteoriteObj: "+self.name+ \
                  ", \n"+"Weight (g):"+" "+str(self.mass_g)+ \
                  ", \nDiscovery Year: "+str(self.year)+ \
                  ", \nClass: "+str(self.metClass)
                  
        return aString

    # deconstructor
    def __del__(self):
        print("A Meteorite has been destroyed: ",self.name)
        Meteorite.mCount -=1

    
