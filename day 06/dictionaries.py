# dictionaries = { key : value }

customer1 = {
    'name': 'krisha',
    'age':21,
    'email': 'kri@gmail.com',
    'is_verified': True
}
customer1["name"]="Krisha T"
print(customer1["name"])
print(customer1.get("birthdate"))
print(customer1.get("birthdate", "December 27 2004"))

# convert numbers into string (words) 1 - one

phone = input("phone : ")
number = { '1':'one','2':'two','3':'three','4':'four','5':'five',
           '6':'six','7':'seven','8':'eight','9':'nine','0':'zero'}
output=""
for key in number:
    output += number.get(key,"!") + " "
print(output)

