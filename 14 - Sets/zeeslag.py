def boot_overlappend(boot, raster):
    return not boot.isdisjoint(raster)


def boot_toevoegen(boot, raster):
    if not boot_overlappend(boot, raster):
        raster.update(boot)
    return raster


def vuur(vak, raster):
    output = False
    if vak in raster:
        output = True
        raster.discard(vak)
    return output, raster


print(boot_overlappend({'B4', 'A4', 'C4'},{'C4', 'D4', 'E4', 'A2', 'I8', 'F8', 'H8', 'A3', 'G8'}))
print(boot_overlappend({'F4', 'F5', 'F6', 'F3'},{'C4', 'D4', 'E4', 'A2', 'I8', 'F8', 'H8', 'A3', 'G8'}))
print(boot_toevoegen({'B4', 'A4', 'C4'},{'C4', 'D4', 'E4', 'A2', 'I8', 'F8', 'H8', 'A3', 'G8'}))
print(boot_toevoegen({'F4', 'F5', 'F6', 'F3'},{'C4', 'D4', 'E4', 'A2', 'I8', 'F8', 'H8', 'A3', 'G8'}))
print(vuur('I7',{'E4', 'H8', 'I8', 'A2', 'G8', 'D4', 'C4', 'F8'}))
print(vuur('F8',{'E4', 'H8', 'I8', 'A2', 'G8', 'D4', 'C4', 'F8'}))