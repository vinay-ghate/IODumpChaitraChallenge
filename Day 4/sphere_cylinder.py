# Program to find volume of sphere and cylinder.💻🚀
x = int(input("Enter \n1 for Sphere\n2 for sylinder\n"))
rad = int(input("Enter radius : "))
if x==1:vol = (4/3)*(22/7)*rad**3;print(f"Volume is {vol}")
elif x==2:height = int(input("Enter Height : "));vol = (22/7)*height*rad**2;print(f'Volume is {vol}')