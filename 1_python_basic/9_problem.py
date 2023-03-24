n = int(input("Enter : "))
if n%2 != 0:
    print("Weird")
elif n%2 == 0 and range(2, 6+1):
    print("Not Weird")
elif n%2 == 0 and range(6, 20+1):
    print("Weird")
elif n%2 == 0 and n >= 20:
    print("Not Weird")