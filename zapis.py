# uzivatel neco napise a to se ulozi do promene

fly = input("kolik litas(ano,ne,mozna)")
# pretipovani ze stringu na str

fly = str(fly)
# pokud se promena neco rovna tak se podle toho neco vypise
if fly == "ano":
    print("dobrej litak")
elif fly == "ne"or"mozna": # elif je dalsi podminka akorat v retezci
    print("nelitavej ptak ses ")
else:             # else je za predpokladu ze zadna z techto podminek se nesplni
    print("tak ty mas dost")
# print nam vypise to co je v zavorce
