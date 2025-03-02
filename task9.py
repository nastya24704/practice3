ATT=int(input())
COMP=int(input())
YDS=int(input())
TD=int(input())
INT=int(input())
# (comp/att-0,3)/0,2
# (yds/att-3)/4
# td/att/0,05
# (0,095-int/att)/0,04
#summ*100/6
first=(COMP/ATT-0.3)/0.2
second=(YDS/ATT-3)/4
third=(TD/ATT/0.05)
fourth=(0.095-INT/ATT)/0.04
passer_rating=(first+second+third+fourth)*100/6
print(passer_rating)
