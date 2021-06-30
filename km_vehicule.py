dico_km = {}

veh1 = "vehicule 1"
veh2 = "vehicule 2"
veh3 = "vehicule 3"

dico_km[veh1] = int(input("Entrez les km du véhicule 1 :\n"))

dico_km[veh2] = int(input("Entrez les km du véhicule 2 :\n"))

dico_km[veh3] = int(input("Entrez les km du véhicule 3 :\n"))


print(dico_km)

for ve, k in dico_km.items():
    print(ve, "est à", k, "km")
