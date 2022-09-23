# ek list create krni h usme kuch bhi dal deta h or fir usme se 6 ya 6 se bdi value print krni h only integer value

a=[int,float,"harry",2,54,2,5,9,9,8,12,5,888,5.96,9.8]
for item in a:
    if str(item).isnumeric() and item>=6:
        print(item)