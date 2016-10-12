import jsondict

object1 = {'A':"23", 'z':0.0, 'a':123, 'b':456}
object2 = {'A':"23", 'z':object1, 'a':123, 'b':456}

print(jsondict.json_serial(object1))
print(jsondict.json_pretty(object1))

# object3 is a copy separate to object1
object3 = object1.copy()
object3['A'] = "24"
print(jsondict.json_serial(object1))
print(jsondict.json_serial(object3))

object4 = {}
jsondict.json_serial(object4)

record1 = jsondict.record()
record2 = jsondict.record(data=object1)
print(record1.equals(record2))

string = "Hello"
print("the hash of '" + string + "': " + jsondict.string_hash(bytes(string, 'utf-8')) + "\n")
