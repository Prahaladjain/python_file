list1=["Harry","Larry","Carry","Marie"]
for item in list1:
    print(item)

list1=(["Harry",1],["Larry",2],["Carry",5],["Marie",52])
for item in list1:
    print(item)
for item ,lollypop in list1:
    print(item,"and lolly is",lollypop)

dict1=dict(list1)
print(dict1)

for item ,lollypop in dict1.items():
    print(item,"and lolly is",lollypop)