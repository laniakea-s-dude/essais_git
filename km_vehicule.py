dico_km = {}

veh1 = "vehicule_1"
veh2 = "vehicule_2"
veh3 = "vehicule_3"

dico_km[veh1] = int(input("Entrez les km du véhicule_1 :\n"))

dico_km[veh2] = int(input("Entrez les km du véhicule_2 :\n"))

dico_km[veh3] = int(input("Entrez les km du véhicule_3 :\n"))


print(dico_km)

for ve, k in dico_km.items():
    print(ve, "est à", k, "km")
