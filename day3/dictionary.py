phones = {
    "Foo": "123",
    "Bar": "456"
}
print(phones)
print(phones.keys())

for name in phones.keys():
    print(f"{name}: {phones[name]}")

print()
for key, value in phones.items():
    print(f"{key}: {value}")
# this works but it is better to give the variables meaningful names like "name" and "number"

print()
for name, number in phones.items():
    print(f"{name}: {number}")

