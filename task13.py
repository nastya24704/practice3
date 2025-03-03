lines=int(input())
columns=int(input())
number=int(input())
#page*columns*lines= number
page=number//columns//lines+1
#55=(x-1)25
column=(number-(page-1)*lines*columns)//lines+1
#55=25+25+5=>
#55=lines*(column-1)+line
line=((number-(page-1)*lines*columns)-lines*(column-1))
print('страница', page, 'столбец', column, 'строка',line)
