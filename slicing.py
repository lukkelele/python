

colors = ['blue', 'green', 'red', 'orange', 'black', 'gray']

print(f"Colors ==> {colors}")

print(f"Slicing [10:] ==> {colors[10:]}")
print(f"Slicing [4:] ==> {colors[4:]}")
print(f"Slicing [10:2] ==> {colors[10:2]}")
print(f"Slicing [5:2] ==> {colors[5:2]}")
print(f"Slicing [5:2:-1] ==> {colors[5:2:-1]}")

# Joining strings
s1 = 'Lukas Gunnarsson'
s2 = 'byyn'
s3 = 'röd mazda'


s4 = s1.join(s3)
print(f"s1.join(s3) --> {s4}")
s4 = s2.join(s2)
print(f"s2.join(s3) --> {s4}")
s1 = "K"
print(f"s1 == K --> {s1.join(s2)}")
print(f"s1 , s2.join(s1) with s1 == K --> {s1.join(s2)}")
print(f"s1 == K , s1.join(colors) ==> {s1.join(colors)}")


# join words with slicing
colors = ['           blue', '    green   ', 'red', 'orange', 'black', 'gray']
print(f"' ' joins colors with slice -----> {' '.join(colors[1:])}")
colors = ['           blue', '    green   ', 'red', 'orange', 'black', 'gray      ']
print(f"' 'joins colors with slice AND strip ==> {' '.join(colors[:]).strip(' ')}")
colors = ['           blue', '    green   ', 'red', 'orange', 'black', 'gray      ']
print(f"' 'joins colors with slice AND strip ==> {' '.join(colors[:]).strip(' ')}")
