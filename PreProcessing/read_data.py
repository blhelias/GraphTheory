"""
TODO: Find a way to create the graph dynamically and save it in txt file.
This script aims at writing a .txt file to build a graph
The .txt file will looks like:

station_1_id sation_2_id weight (distance between 2 stations (meter))
...
...
...
station_n-1_id station_n_id weight

"""
from zipfile import ZipFile

with ZipFile('../data/RATP_GTFS_RER_A.zip') as myzip:
    print(myzip.namelist())