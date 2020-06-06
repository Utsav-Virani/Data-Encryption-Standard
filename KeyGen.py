
import numpy as np

_pc_1 = {
    1: 57,
    2: 49,
    3: 41,
    4: 33,
    5: 25,
    6: 17,
    7: 9,
    8: 1,
    9: 58,
    10: 50,
    11: 42,
    12: 34,
    13: 26,
    14: 18,
    15: 10,
    16: 2,
    17: 59,
    18: 51,
    19: 43,
    20: 35,
    21: 27,
    22: 19,
    23: 11,
    24: 3,
    25: 60,
    26: 52,
    27: 44,
    28: 36,
    29: 63,
    30: 55,
    31: 47,
    32: 39,
    33: 31,
    34: 23,
    35: 15,
    36: 7,
    37: 62,
    38: 54,
    39: 46,
    40: 38,
    41: 30,
    42: 22,
    43: 14,
    44: 6,
    45: 61,
    46: 53,
    47: 45,
    48: 37,
    49: 29,
    50: 21,
    51: 13,
    52: 5,
    53: 28,
    54: 20,
    55: 12,
    56: 4,
}
_pc_2 = {
    0: 14,
    1: 17,
    2: 11,
    3: 24,
    4: 1,
    5: 5,
    6: 3,
    7: 28,
    8: 15,
    9: 6,
    10: 21,
    11: 10,
    12: 23,
    13: 19,
    14: 12,
    15: 4,
    16: 26,
    17: 8,
    18: 16,
    19: 7,
    20: 27,
    21: 20,
    22: 13,
    23: 2,
    24: 41,
    25: 52,
    26: 31,
    27: 37,
    28: 47,
    29: 55,
    30: 30,
    31: 40,
    32: 51,
    33: 45,
    34: 33,
    35: 48,
    36: 44,
    37: 49,
    38: 39,
    39: 56,
    40: 34,
    41: 53,
    42: 46,
    43: 42,
    44: 50,
    45: 36,
    46: 29,
    47: 32,
}


_key_all = [0 for i in range(16)]



def __convert_to_binary__(_key,_key_full_binary):
    for i in _key:
        # print(i)
        # print(ord(i)-32)
        _key_full_binary +=(format(ord(i)-32,'b'))
    if len(_key_full_binary) < 64:
        for i in range(len(_key_full_binary),64):
            _key_full_binary += '0'

    _keybinary = ""
    for i in range(0,64):
        _keybinary += _key_full_binary[i]
    return _keybinary




def __keyConvertion56__(_key_binary):

    _key56 = [0 for i in range(56)]
    for i in range(0, 56):
        _key56[i] = _key_binary[(_pc_1[i + 1]) - 1]

    return _key56



def __main__():
    _key = input("Enter the Key : ")
    _key_binary_full = ""
    _key_binary = __convert_to_binary__(_key,_key_binary_full)
    # _key_binary = "0001001100110100010101110111100110011011101111001101111111110001"
    # print(_key_binary)
    __key56 = __keyConvertion56__(_key_binary)
    _key28_L = [0 for i in range(28)]
    _key28_R = [0 for i in range(28)]

    for i in range(28):
        _key28_L[i] = __key56[i]

    ind = 0
    for i in range(28, 56):
        _key28_R[ind] = __key56[i]
        ind += 1

    for i in range(1,17):
        j= -2
        if i == 1 or i == 2 or i == 9 or i == 16:
            j= -1
        _key28_L_shift = np.roll(_key28_L, j)
        _key28_R_shift = np.roll(_key28_R, j)


        # print(_key28_R_shift)


        _key56_After_shift = list()
        for k in _key28_L_shift:
            _key56_After_shift.append(k)

        for k in _key28_R_shift:
            _key56_After_shift.append(k)

        _key_1 = ""
        for k in range(48):
            # print(i," => ",_pc_2[i]," => ",_key56_After_shift[_pc_2[i]])
            key = _key56_After_shift[_pc_2[k] - 1]
            _key_1 += key

        # print(i)
        _key_all[i-1] = _key_1
        _key28_L = _key28_L_shift
        _key28_R = _key28_R_shift

    print(_key_all)
    # indx = 0
    # for i in _key_all[0]:
    #     print(indx ," => ",i)
    #     indx +=1






# if __name__ == "__main__":
#     __main__()
