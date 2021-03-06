

# Schema
# =======================================
# Planet(attributes)    
# Specie(attributes)
# Environment(p_name PRIMARY KEY, climate)
# Terrain(p_name PRIMARY KEY, terrain)
# Hair_Color(s_name PRIMARY KEY, color)
# Skin_Color(s_name PRIMARY KEY, color)
# Eye_Color(s_name PRIMARY KEY, color)
# =======================================

# MULTIVALUED ATTRIBUTES INCLUDE:
# Planets.csv ==> climate, terrain
# Species.csv ==> skin_colors, hair_colors, eye_colors

# TABLES TO CREATE:
# Planet, Specie, Environment, Color

csv_planets_file_win = "data\\planets.csv"
csv_species_file_win = "data\\species.csv"

csv_planets_file_linux = "./data/planets.csv"     # on linux
csv_species_file_linux = "./data/species.csv"     # on linux



def get_file(filename, os):
    if filename == "planets.csv":
        if os == "linux":
            return csv_planets_file_linux
        else:
            return csv_planets_file_win
    else:
        if os == "linux":
            return csv_species_file_linux
        else:
            return csv_species_file_win


def get_datatypes(file):
    file = file.lower()
    if   file == "planet_csv" : return planet_csv_datatypes
    elif file == "specie_csv" : return specie_csv_datatypes
    elif file == "planet"     : return planet_datatypes 
    elif file == "specie"     : return specie_datatypes
    elif file == "hair_color" : return hair_color_datatypes
    elif file == "eye_color"  : return eye_color_datatypes
    elif file == "skin_color" : return skin_color_datatypes
    elif file == "terrain"    : return terrain_datatypes
    elif file == "environment": return environment_datatypes


def get_column_names(entity):
    if entity == "planet":
        return planet_columns
    elif entity == "specie":
        return specie_columns
    elif entity == "csv_planet":
        return planet_csv_datatypes
    elif entity == "csv_specie":
        return specie_csv_datatypes


planet_csv_datatypes = [["p_name", "varchar(20)", "PRIMARY KEY"], ["rotation_period", "int"], 
                       ["orbital_period", "int"], ["diameter","bigint"], ["climate", "varchar(50)"],
                       ["gravity", "varchar(50)"],     # temporarily change decimal(2,2) to varchar
                       ["terrain", "varchar(50)"], ["surface_water", "int"], ["population", "bigint"]]
# TERRAIN AND GRAVITY --> varchar(50) to make sure space is available

specie_csv_datatypes = [["s_name", "varchar(20)", "PRIMARY KEY"], ["classification", "varchar(15)"],
                        ["designation", "varchar(14)"] ,["average_height", "int"], ["skin_color", "varchar(50)"],
                        ["hair_color", "varchar(50)"], ["eye_color", "varchar(50)"], ["average_lifespan", "int"],
                        ["language", "varchar(18)"], ["homeworld", "varchar(14)"]]


planet_datatypes = [["p_name", "varchar(20)", "NOT NULL", "PRIMARY KEY"], ["rotation_period", "int"], 
                    ["orbital_period", "int"], ["diameter","bigint"], ["gravity", "varchar(20)"],
                    ["surface_water", "int"], ["population", "bigint"]]

specie_datatypes = [["s_name", "varchar(20)", "NOT NULL", "PRIMARY KEY"], ["classification", "varchar(15)"],
                    ["designation", "varchar(14)"] ,["average_height", "int"], 
                    ["average_lifespan", "int"], ["language", "varchar(18)"], ["homeworld", "varchar(14)"]]

environment_datatypes = [["p_name", "varchar(20)"], ["climate", "varchar(20)"]]
terrain_datatypes = [["p_name", "varchar(20)"], ["terrain", "varchar(20)"]]      # FIX
hair_color_datatypes = [["s_name", "varchar(20)"], ["hair_color", "varchar(20)"]]
eye_color_datatypes =  [["s_name", "varchar(20)"], ["eye_color",  "varchar(20)"]]
skin_color_datatypes = [["s_name", "varchar(20)"], ["skin_color", "varchar(20)"]]

# environment_datatypes = [["p_name", "varchar(14)"], ["climate", "varchar(12)"]]
# terrain_datatypes = [["p_name", "varchar(14)"], ["terrain", "varchar(50)"]]      # FIX
# hair_color_datatypes = [["s_name", "varchar(20)"], ["hair_color", "varchar(14)", "PRIMARY KEY"]]
# eye_color_datatypes =  [["s_name", "varchar(20)"], ["eye_color",  "varchar(14)", "PRIMARY KEY"]]
# skin_color_datatypes = [["s_name", "varchar(20)"], ["skin_color", "varchar(14)", "PRIMARY KEY"]]



planet_columns = ["p_name", "rotation_period", "orbital_period", "diameter", "gravity", "surface_water", "population"]
specie_columns = ["s_name", "classification", "designation", "average_height", "average_lifespan", "language", "homeworld"]
