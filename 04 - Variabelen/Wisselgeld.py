geld = int(input('geld: '))
muntstukken = 0

muntstukken += geld // 100
rest = geld % 100
muntstukken += rest // 50
rest = rest % 50
muntstukken += rest // 20
rest = rest % 20
muntstukken += rest // 10
rest = rest % 10
muntstukken += rest // 5
rest = rest % 5
muntstukken += rest // 2
rest = rest % 2
muntstukken += rest // 1
rest = rest % 1

print(geld,'cent kan je omwisselen in',muntstukken,'muntstukken')