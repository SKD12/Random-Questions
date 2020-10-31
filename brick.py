case1='|___|'
case2='___|'
case3='|___'
case4='__|'
rows=10
height=6
def wall(rows,height):
    #print((case1*(rows-2) + '\n' + case2*rows + '\n')*height )
    print(((case1+(case2*(rows-1)))+'\n'+(case4+(case2*(rows-1))+'__'+'\n'))*(height//2))
    return

wall(3,4)