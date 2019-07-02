def bepaal_hittegolven(file_name):
    dag = 0
    aantal = 0
    hitegolven = []
    with open(file_name) as file:
        temps = []
        for line in file.readlines():
            temps += line.split()
        boven_25 = 0
        boven_30 = 0
        for temp in temps:
            dag += 1
            if int(temp) >= 30:
                boven_30 += 1
            if int(temp) >= 25:
                boven_25 += 1
            else:
                if boven_25 >= 5 and boven_30 >= 3:
                    aantal += 1
                    hitegolven.append((dag - boven_25, dag - 1))
                boven_30, boven_25 = 0, 0

    return aantal, hitegolven