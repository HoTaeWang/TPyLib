# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def traversal_func():
    fruit = 'banana'
    index = 0
    while index < len(fruit):
        letter = fruit[index]
        print(letter)
        index = index + 1

def anti_traversal_func():
    fruit = 'banana'
    index = len(fruit)
    while index > 0:
        letter = fruit[index-1]
        print(letter)
        index = index -1

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(traversal_func())
    print(anti_traversal_func())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
