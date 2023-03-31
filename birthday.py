str=input("Enter Date Of Birth:\n")
list=str.split("/")
bday=".".join(list)
dict={"Birthday":bday}
if "Birthday" in dict:
    print(dict["Birthday"])

