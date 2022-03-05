

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



planet_csv_datatypes = [["name", "varchar(20)", "PRIMARY KEY"], ["rotation_period", "int"], 
                       ["orbital_period", "int"], ["diameter","bigint"], ["climate", "varchar(40)"],
                       ["gravity", "varchar(40)"],     # temporarily change decimal(2,2) to varchar
                       ["terrain", "varchar(30)"], ["surface_water", "int"], ["population", "bigint"]]


specie_csv_datatypes = [["s_name", "varchar(15)", "PRIMARY KEY"], ["classification", "varchar(15)"],
                        ["designation", "varchar(14)"] ,["average_height", "int"], ["skin_colors", "varchar(14)"],
                        ["hair_colors", "varchar(12)"], ["eye_colors", "varchar(10)"], ["average_lifespan", "int"],
                        ["language", "varchar(18)"], ["homeworld", "varchar(14)"]]


planet_datatypes = [["p_name", "varchar(20)", "NOT NULL", "PRIMARY KEY"], ["rotation_period", "int"], 
                    ["orbital_period", "int"], ["diameter","bigint"], ["gravity", "varchar(20)"],
                    ["surface_water", "int"], ["population", "bigint"]]

specie_datatypes = [["s_name", "varchar(15)", "NOT NULL", "PRIMARY KEY"], ["classification", "varchar(15)"],
                    ["designation", "varchar(14)"] ,["average_height", "int"], 
                    ["average_lifespan", "int"], ["language", "varchar(18)"], ["homeworld", "varchar(14)"]]

environment_datatypes = [["p_name", "varchar(14)", "NOT NULL", "PRIMARY KEY"], ["terrain", "varchar(12)"]]
terrain_datatypes = [["p_name", "varchar(14)", "NOT NULL", "PRIMARY KEY"], ["terrain", "varchar(12)"]]      # FIX
hair_color_datatypes = [["s_name", "varchar(20)"], ["hair_color", "varchar(14)", "PRIMARY KEY"]]
eye_color_datatypes =  [["s_name", "varchar(20)"], ["eye_color",  "varchar(14)", "PRIMARY KEY"]]
skin_color_datatypes = [["s_name", "varchar(20)"], ["skin_color", "varchar(14)", "PRIMARY KEY"]]





