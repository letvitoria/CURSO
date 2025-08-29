for i in range(10):
    print(i)

string = "Hello World!"
for i in range(0, len(string), 2):
    print(str(i) + "th letter is "+ string[i])

#while
count = 0 
while (count < 10):
    print(count)
    count += 1

while True:
    user = input("Enter something to be repeated: ")
    if user =="end":
        print("Terminate the program!!")
        break
    print(user)
   