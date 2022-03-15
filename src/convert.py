import geopandas as gpd
import os

shapes_dir = "/mnt/c/Users/Julie/git/portfolio/data/shapes/"
json_dir = "/mnt/c/Users/Julie/git/portfolio/data/geojson/"

os.makedirs(json_dir, exist_ok=True)
shapefiles=os.listdir(shapes_dir)

for file in shapefiles:
    print(f"Converting {file}") 
    zipfile = f"zip:////{shapes_dir}{file}"
    df = gpd.read_file(zipfile)
    json_filename = file.replace(".zip", ".json")
    outfile = open(f"{json_dir}{json_filename}", "w")
    outfile.write(df.to_json())
    outfile.close()

# Need to figure out a way to shrink these files
# one idea is to reduce the precision of the decimal lat/lon values
# consider:
#  1 degree of lattitude = 10^7/90 = 111,111 meters
#  1 in the 6th decimal place (.000001) is :
#       111,000/10^6 = 0.1111 meters 
#       0.1111 meters * 39.37 in/meter = ~4.37 inches
#
#  1 degree of logitude at 38 degrees north lattitude (Uentral US)
#       is ~87843 meters
#       87843/10^6 = 0.087843 meters = ~3.5 inches
#
#  Many coordinates in the geojson look like this:
#   [-77.05827099999999, 38.901948999999995]
#  we could truncate to 6 decimal places without losing much accuracy
#  and potentially reduce the data size significantly...
#    [-77.058270, 38.901948]
