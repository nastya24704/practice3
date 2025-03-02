import math
a=int(input())
b=int(input())
c=int(input())
#теорема косинусов a**2=b**2+c**2-2*b*c*cosa
angle_a=math.acos((b**2+c**2-a**2)/(2*b*c))
angle_b=math.acos((a**2+c**2-b**2)/(2*a*c))
angle_c=math.acos((b**2+a**2-c**2)/(2*b*a))
print(math.degrees(angle_a))
print(math.degrees(angle_b))
print(math.degrees(angle_c))
