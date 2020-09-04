import numpy as np

chars = []
states = []


def state_changer(char, state):
    char_num = ord(char) - 97
    return int(arr[state, char_num, 0])


def accepted(my_string0):
    length = len(my_string0)

    state = start

    for i in range(length):
        if my_string0[i] in chars:
            state = state_changer(my_string0[i], state)
        else:
            return 0
    if state == end:
        return 1
    else:
        return 0


def read_file():
    f = open("DFA_Input_1.txt", "r")

    my_chars = f.readline().split()
    for i in range(len(my_chars)):
        chars.append(my_chars[i])

    my_states = f.readline().split()
    for i in range(len(my_states)):
        states.append(my_states[i])

    start_s = int(f.readline()[-2])
    end_s = int(f.readline()[-2])

    arr_0 = np.zeros((100, 100, 100))

    for i in range(len(chars) * len(states)):
        str0 = f.readline()
        arr_0[int(str0[1]), ord(str0[3]) - 97, 0] = int(str0[6])

    return arr_0, start_s, end_s


if __name__ == "__main__":
    my_string = input('enter your string: ')
    arr, start, end = read_file()
    if accepted(my_string):
        print('accepted')
    else:
        print('not accepted')
