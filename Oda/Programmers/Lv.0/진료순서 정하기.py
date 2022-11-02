emergency = [1,2,3,4,5,6,7]
emer = sorted(emergency, reverse=True)

print(emer)

dict = {}

for key, value in enumerate(emer):
    dict[key+1] = value

print(dict)

result=[]
for key, value in dict.items():
        for i in range(len(emergency)):
            if emergency[i] == value:
                result.insert(i, key)
print(result)

