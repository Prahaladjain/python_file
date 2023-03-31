str=input("Enter a string\n")
dict={}
for ch in str:
    keys=dict.keys()
    if(ch in keys):
        dict[ch]=dict[ch]+1
    else:
        dict[ch]=1
print("Dictionary is:\n",dict)
