lijst = ["audi","mercedes","lamborghini","bmw","nissan"]
for merk in lijst:
    print(merk)

print()

tuple = ("opel","renault","ferrari","ford","kia")
for merk in tuple:
    print(merk)

print()

dict = {
    "merk"      : "audi",
    "model"     : "RS 6",
    "bouwjaar"  : "2022"
}
for auto in dict.keys():
    print(auto)

print(dir(dict))