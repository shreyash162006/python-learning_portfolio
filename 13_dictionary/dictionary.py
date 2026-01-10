# doctionary - collection of { key : value } pairs
#              ordered and changeable , No duplicates

capitals = {"USA" : "Washington " ,
            "INDIA" : "New Delhi" ,
            "China" : "Beijing" ,
            "Russia"  : "Moscow" }

print(capitals)
# dictionary methods 


# 1. dict.get(key) - gives the value associated with the key
print(capitals.get("INDIA"))
print(capitals.get("JAPAN"))  # returns none as japan is not defined

# 2. dict.update({key : value}) - adds a new key value pair to the dict also we can change the value of an existing key
capitals.update({ "Germany" : "Berlin" })
print(capitals)

capitals.update( {"USA" : "London"} )
print(capitals)
# dict.pop(key) - removes the key value pair from the dict

capitals.pop("China")
print(capitals)
# dict.popitem() - removes the latest key value pair from the dictionary

capitals.popitem()
print(capitals)
# dict.clear()- clears the dictionary 

# dict.keys() - returns all the keys of the dict
keys = capitals.keys()
print(keys)

for key in capitals.keys():
    print(key)
# dict.values() - returns the values in the dict
values = capitals.values()
print(values)

for value in capitals.values():
    print(value)
# dict.items() - returns the key value pairs 
for key,value in capitals.items():
    print(f" {key} : {value}")