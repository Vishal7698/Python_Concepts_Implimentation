from builtins import print

listExample=["python",3.9,"java",11,"c",'c++']
print(listExample)
print(listExample[0])
print(listExample[2])
print(listExample[-1])
print(listExample[1:])
print(listExample[:3])
print(listExample[1:4])

#we can create list of list by combine them
listExample2=["ruby","perl"]
combine=[listExample,listExample2]
print(combine)

#their are multiple methods to manupulate list
listExample.append("react")
print(listExample)

listExample.insert(1,"javascript")
print(listExample)

listExample.remove("javascript")
print(listExample)

listExample.pop()
print(listExample)

listExample.pop(2)
print(listExample)

del listExample[1:]
print(listExample)

listExample.extend(["typescript","go"])
print(listExample)

listExample.sort()
print(listExample)