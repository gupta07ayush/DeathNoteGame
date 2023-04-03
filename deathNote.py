import time

note=["  -  ", "will", "die", "in", "5", "Seconds."]
print("Death Note Welcomes you.")
print("Here are the rules to use this book.")
time.sleep(1)
print(''' 
      1) The human whose name is written in this note shall die.
      
      2) This note will not take effect unless the writer has 
      the person’s face in their mind when writing his/her name. 
      Therefore, people sharing the same name will not be affected\n''')


name = list(input("Enter the name of person who should die. "))
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
count=(len(name))
upperName=[x.upper() for x in name]

upperName=iter(upperName)

for i in range(count):
    print(next(upperName),end=" ")
    time.sleep(0.5)
    
for i in note:
    print(i,end=" ")
    time.sleep(1)
time.sleep(2)

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

print("Erasing...")


chars= ' '.join(map(str, name))
chars= chars.upper()
loop = range(1, len(chars) + 1)

LINE_UP = '\033[1A' 
LINE_CLEAR = '\x1b[2K'

for idx in reversed(loop):
    time.sleep(0.2)
    print(chars[:idx])
    time.sleep(0.5)
    print(LINE_UP, end=LINE_CLEAR)
    
print("\n\n\n\n\n\n\n\n\n\n\n\n")
print("Erased")


