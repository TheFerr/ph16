from cat import Cat
cat1 = Cat('Baron',2,'m')
cat2 = Cat('Sam',2,'m')

cats = [cat1, cat2]

for cati in cats:
    print(cati.name, cati.age, cati.gender)