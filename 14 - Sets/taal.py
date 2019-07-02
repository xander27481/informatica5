def behoort_tot_taal(woord, letters):
    # spatie verwijderen
    gesplitst = []
    gesplitst += ''.join(woord.split())
    #rest
    return set(gesplitst).issubset(letters)


def is_onleesbaar(woord, letters):
    # spatie verwijderen
    gesplitst = []
    gesplitst += ''.join(woord.split())
    # rest
    return set(gesplitst).isdisjoint(letters)


def perfect_woord(woord, letters):
    # spatie verwijderen
    gesplitst = []
    gesplitst += ''.join(woord.split())
    # rest
    return set(gesplitst).issuperset(letters)


print(behoort_tot_taal('do well',{'o', 'd', 'e', 'l', 'w', 'r', 'h'}))
print(behoort_tot_taal('ambigu',{'o', 'd', 'e', 'l', 'w', 'r', 'h'}))
print(is_onleesbaar('do well',{'o', 'd', 'e', 'l', 'w', 'r', 'h'}))
print(is_onleesbaar('ambigu',{'o', 'd', 'e', 'l', 'w', 'r', 'h'}))
print(perfect_woord('do well',{'o', 'd', 'e', 'l', 'w',}))
print(perfect_woord('ambigu',{'o', 'd', 'e', 'l', 'w', 'r', 'h'}))