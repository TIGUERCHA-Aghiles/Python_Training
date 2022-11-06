print("hello, world")
livre = "Gatsby le Magnifique"
livre
azghal = True
if azghal:
    print("On va a la palge")
else:
    print("On reste a la maison")

race_de_chien = ["aqjoun", "awtoul", "aydi", "amakar", "ahouli"]
for chien in race_de_chien:
    print(chien)

for x in range(5):
    print(x)

for x in range(100):
    print(f"{x} bouteilles de bieres au mur !")

cap_max = 10
cap_act = 2
while cap_act < cap_max :
    cap_act +=1
    print("la capaciter actuelle est à : ",cap_act)

def add(a, b):
    return a + b

print("total = ",add(17, 13))
