"""
import time
initial=time.time()
k=0
while(k<45):
    print("This is harry bhai")
    k+=1
print("While loop run in",time.time()-initial,"second")

initial2=time.time()
for i in range(45):
    print("This is a prahalad bahi")
print("for loop run in",time.time()-initial2,"second")
"""


"""
import time
localtime=time.asctime(time.localtime(time.time()))
print(localtime)
"""

import time
k=0
while(k<45):
    print("This is prahalad bhai")
    time.sleep(2)