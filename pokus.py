def hello_world():
    print("Hello world")

def five_stars(cislo,limit):

    if cislo > limit:
        print(f"Číslo je větší než {limit}")

    while cislo < limit:
        print("*")
        cislo+=1

def in_range(number,minimum,maximum):
    if number > minimum and number<maximum:
        print(f"Number {number} is in range ({minimum}-{maximum})")
    else:
        print(f"Number {number} is out of range ({minimum}-{maximum})")
    pass

def max_number(a,b,c):
    if a>b and a>c:
        return a
    if b>a and b>c:
        return b
    if c>a and c>b:
        return c

         
#in_range(2,3,20)

num = max_number(2,8,4)
print(num) 