import csv





def read_row(csv_file):
    reader = open(csv_file, 'r')
    for row in reader:
        print(row)



def read_multivalued_attribute(path):
    with open(path, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row_split = row['climate'].split(",")
            if len(row_split) > 1:
                print(row['climate'])




read_multivalued_attribute("./data/planets.csv")
