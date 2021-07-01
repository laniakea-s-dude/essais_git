dico_km = {}

veh1 = "vehicule n°1"
veh2 = "vehicule n°2"
veh3 = "vehicule n°3"

dico_km[veh1] = int(input("Entrez les km du véhicule n°1 :\n"))

dico_km[veh2] = int(input("Entrez les km du véhicule n°2 :\n"))

dico_km[veh3] = int(input("Entrez les km du véhicule n°3 :\n"))


print(dico_km)

for ve, k in dico_km.items():
    print("Le", ve, "est à", k, "km")
