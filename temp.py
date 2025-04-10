def create_a_grid(marked_list):
    for i in range(1, 6):
        for j in range(1, 6):
            if (i, j) in marked_list:
                print("#", end=" ")
                continue
            print("*", end=" ")
        print()

def get_user_input():
    get_row = int(input("Enter a row: "))
    get_column = int(input("Enter a column: "))
    return get_row, get_column


def main():
    marked_list = []
    for i in range(3):
        marked_row, marked_column = get_user_input()
        marked_list.append((marked_row, marked_column))
        create_a_grid(marked_list)

if __name__ == "__main__":
    main()