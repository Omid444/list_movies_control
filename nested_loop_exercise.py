from itertools import count

for outerloop in range(4):
    for innerloop in range(4):
        print('*', end='')
    print()

print('='*50)#################################################

for outerloop in range(5):
    for innerloop in range(8):
        print('*', end='')
    print()

print('='*50)#################################################


for outerloop in range(1,8):
    for innerloop in range(outerloop):
        print(innerloop+1, end='')
    print()

print('='*50)#################################################

def choose_cell():
    row = int(input('please enter an number between 1 to 5(including5) to select row: '))
    column = int(input('please enter an number between 1 to 5(including5) to select column: '))
    for outerloop in range(1,6):
        for innerloop in range(1,6):
            if outerloop == row and innerloop == column:
                print('#', end='')
                continue
            print('*', end='')
        print()

#choose_cell()

print('='*50)#################################################

for outerloop in range(0,100,10):
    for innerloop in range(1,11):
        if outerloop < 10:
            print(innerloop + outerloop, end='  ')
        else:
            print(innerloop+outerloop, end=' ')
    print()

print('='*50)#################################################

for outerloop in range(1,11):
    for innerloop in range(outerloop,(10*outerloop)+1,outerloop):
        if innerloop < 10:
            print(innerloop, end='  ')
        else:
            print(innerloop, end=' ')
    print()

print('='*50)#################################################


def choose_cell_3times():
    count = 0
    grid_list = []
    for _ in range(5):
            grid_list.append(['*' for _ in range(5)])
    print(grid_list)
    while count < 3:
        row = int(input('please enter an number between 1 to 5(including5) to select row: '))-1
        column = int(input('please enter an number between 1 to 5(including5) to select column: '))-1
        grid_list[row][column] = '#'
        count += 1
        for outerloop in range(5):
            for innerloop in range(5):
                print(grid_list[outerloop][innerloop], end='')
            print()
choose_cell_3times()