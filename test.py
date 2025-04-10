# count = 1
# for i in ['A', 'B']:
#     for j in range(3):
#         print(f'{i}{j+1}', end=' ')
#
#     print()


def draw_row():
    for j in range(3):
        print(f'{i}{j+1}', end=' ')
        i = i +2
    print()
i = 10
draw_row()
#for i in ['A', 'B']:
    #draw_row()