b = float(input("breed: "))
l = float(input("lengte: "))
oppervlakte_veld = (b * l)*(10**(-4))


c = float(input("c: "))
graan = c * oppervlakte_veld


r = float(input("straal: "))
h = float(input("hoogte: "))
pi = 3.1415926535897931
silo_inhoud = r * r * pi * h


aantal_silos = graan // silo_inhoud


rest = graan % silo_inhoud


hoogte_silo = rest / (r * r * pi)

if rest == 0:
    print(int(aantal_silos))
    print(h)
else:
    print(int(aantal_silos)+1)
    print(hoogte_silo)