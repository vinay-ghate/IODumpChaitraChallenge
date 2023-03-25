#Program to find the area of a triangle, rectangle, and square.💻🚀

x = ['Triangle','Rectangle','Square']

print(" Which area you want to calculate?")
for i in range(len(x)):
    print("%d"%(i+1),x[i])
y = int(input())

def tringle_a(base,height):
    return base*height*(1/2)
def square_a(side):
    return side**2
def rectangle_a(height,width):
    return height*width
def take_len(S):
    print(f"Enter length of {S} = ")
    tmp = int(input())
    return tmp
def print_ans(y,temp):
    print(f"The Area of {x[y-1]} is {temp}")
if y==1:
    base = take_len("Base")
    height = take_len("Height")
    print_ans(y,tringle_a(base, height))
elif y==2:
    height = take_len("Height")
    width = take_len("Width")
    print_ans(y,rectangle_a(height, width))
elif y==3:
    side = take_len("Side")
    print_ans(y,square_a(side))

# Which area you want to calculate?
# 1 Triangle
# 2 Rectangle
# 3 Square
# 2
# Enter length of Height = 
# 4
# Enter length of Width = 
# 3
# The Area of Rectangle is 12