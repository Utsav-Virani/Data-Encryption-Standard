import KeyGen as ky
import numpy as np

IP = {
    0 : 58,
    1 : 50,
    2 : 42,
    3 : 34,
    4 : 26,
    5 : 18,
    6 : 10,
    7 : 2,
    8 : 60,
    9 : 52,
    10 : 44,
    11 : 36,
    12 : 28,
    13 : 20,
    14 : 12,
    15 : 4,
    16 : 62,
    17 : 54,
    18 : 46,
    19 : 38,
    20 : 30,
    21 : 22,
    22 : 14,
    23 : 6,
    24 : 64,
    25 : 56,
    26 : 48,
    27 : 40,
    28 : 32,
    29 : 24,
    30 : 16,
    31 : 8,
    32 : 57,
    33 : 49,
    34 : 41,
    35 : 33,
    36 : 25,
    37 : 17,
    38 : 9,
    39 : 1,
    40 : 59,
    41 : 51,
    42 : 43,
    43 : 35,
    44 : 27,
    45 : 19,
    46 : 11,
    47 : 3,
    48 : 61,
    49 : 43,
    50 : 45,
    51 : 37,
    52 : 29,
    53 : 21,
    54 : 13,
    55 : 5,
    56 : 63,
    57 : 55,
    58 : 47,
    59 : 39,
    60 : 31,
    61 : 23,
    62 : 15,
    63 : 7,
}

E = {
    0 : 32,
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5,
    6 : 4,
    7 : 5,
    8 : 6,
    9 : 7,
    10 : 8,
    11 : 9,
    12 : 8,
    13 : 9,
    14 : 10,
    15 : 11,
    16 : 12,
    17 : 13,
    18 : 12,
    19 : 13,
    20 : 14,
    21 : 15,
    22 : 16,
    23 : 17,
    24 : 16,
    25 : 17,
    26 : 18,
    27 : 19,
    28 : 20,
    29 : 21,
    30 : 20,
    31 : 21,
    32 : 22,
    33 : 23,
    34 : 24,
    35 : 25,
    36 : 24,
    37 : 25,
    38 : 26,
    39 : 27,
    40 : 28,
    41 : 29,
    42 : 28,
    43 : 29,
    44 : 30,
    45 : 31,
    46 : 32,
    47 : 1,
}

# S1 = np.zeros((8,4,16))

S1 = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],  
        [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],  
        [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],  
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],  
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],  
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],  
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]
    ],  
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],  
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],  
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],  
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]
    ],  
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],  
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],  
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],  
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],  
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],  
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],  
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],  
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]
    ],
    [ 
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],  
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],  
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],  
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],  
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],  
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],  
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],  
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],  
    [ 
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],  
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],  
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],  
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
] 


P = {
    0 : 16,
    1 : 7,
    2 : 20,
    3 : 21,
    4 : 29,
    5 : 12,
    6 : 28,
    7 : 17,
    8 : 1,
    9 : 15,
    10 : 23,
    11 : 26,
    12 : 5,
    13 : 18,
    14 : 31,
    15 : 10,
    16 : 2,
    17 : 8,
    18 : 24,
    19 : 14,
    20 : 32,
    21 : 27,
    22 : 3,
    23 : 9,
    24 : 19,
    25 : 13,
    26 : 30,
    27 : 6,
    28 : 22,
    29 : 11,
    30 : 4,
    31 : 25,
}

IIP = [
    40, 8, 48, 16, 56, 24, 64, 32,  
    39, 7, 47, 15, 55, 23, 63, 31,  
    38, 6, 46, 14, 54, 22, 62, 30,  
    37, 5, 45, 13, 53, 21, 61, 29,  
    36, 4, 44, 12, 52, 20, 60, 28,  
    35, 3, 43, 11, 51, 19, 59, 27,  
    34, 2, 42, 10, 50, 18, 58, 26,  
    33, 1, 41, 9, 49, 17, 57, 25
]

# print(S1[0][0][12])

def __plntxtToBinary__(__plnTxt,__txtBinary):
    for i in __plnTxt:
        __txtBinary +=(format(ord(i)-32,'b'))
    if len(__txtBinary) < 64:
        for i in range(len(__txtBinary),64):
            __txtBinary += '0'
    return __txtBinary


if __name__ == "__main__":
    # 2-%9XFKS>  => Plain Text
    _plnTxt = input("Enter the Text :- ")
    ky.__main__()
    __txtBinary = ""
    __txtBinaryFull = __plntxtToBinary__(_plnTxt,__txtBinary)
    # print(__txtBinaryFull)
    # __txtBinaryFull = "0000000100100011010001010110011110001001101010111100110111101111"

    n = len(__txtBinaryFull) // 64
    if len(__txtBinaryFull)%64 == 0:
        n -= 1 
    
    __plnTxt = [[ 0 for i in range(64)] for i in range(n+1)]

    # print(__plnTxt)

    indi = 0
    indj = 0
    for i in __txtBinaryFull:
        if indj == 64:
            indi+=1
            indj =0
        __plnTxt[indi][indj] = i
        indj+=1

    # print(__plnTxt)
    __txtIP = [ 0 for i in range(64)]
    __ciptxtFinal = ""
    for i in __plnTxt:
        for j in range(64):
            # print(j, " => ",IP[j], " => ",i[IP[j]])
            __txtIP[j] = i[IP[j] -1]
            
        
        __plnTxt_L = [0 for k in range(32)]
        __plnTxt_R = [0 for k in range(32)]

        for k in range(32):
            __plnTxt_L[k] = __txtIP[k]

        indx = 0
        for k in range(32,64):
            __plnTxt_R[indx] = __txtIP[k]
            indx +=1

        # print(__plnTxt_L)
        # print(__plnTxt_R)
        for ll in range(16):
            __plnTxt_E = [0 for k in range(48)]
            for k in range(48):
                __plnTxt_E[k] = __plnTxt_R[E[k]-1]
            

            # print(__txt)

            __key = ky._key_all[0]
            # print(__key)
            __txtExOR =[0 for k in range(48)]
            for k in range(48):
                __txtExOR[k] = int(__key[k]) ^ int(__plnTxt_E[k])

            # print(__txtExOR)
            __txtSboxIp = [[0 for l in range(2)] for k in range(8)]
            # print(__txtSboxIp[0])
            indx = 0
            __txtSboxOp = ""
            for k in range(0,43,6):
                row = str(__txtExOR[k])
                row += str( __txtExOR[k+5])
                col = str(__txtExOR[k+1])
                col += str(__txtExOR[k+2])
                col += str(__txtExOR[k+3])
                col += str(__txtExOR[k+4])
                # print(k)
                __txtSboxIp[indx] =[int(row,2),int(col,2)]
                # print(indx , " => " ,int(row,2), " => " ,int(col,2), " => ",S1[indx][int(row,2)])
                # print(indx)
                tmp = format((S1[indx][int(row,2)][int(col,2)]),'b')
                n=0
                if len(tmp) == 3:
                    n=1
                if len(tmp) == 2:
                    n=2
                if len(tmp) == 1:
                    n = 3
                for kk in range(n):
                    __txtSboxOp += '0'
                __txtSboxOp += str(tmp)
                indx += 1

        # print(__txtSboxOp)
        # for kk in __txtSboxIp:
        # print(__txtSboxIp)
        # num = str(__txtExOR[6])
        # num += str(__txtExOR[11])
        # print(int(num,2))

            __txtOp = ""
            for k in range(32):
                __txtOp += str(int(__txtSboxOp[P[k]-1]) ^ int(__plnTxt_L[k]))

            # print(__txtOp)
            __plnTxt_L = __plnTxt_R
            __plnTxt_R = __txtOp

            # print(__plnTxt_L)
            # print(__plnTxt_R)
        __txtPI2 = __plnTxt_L+__plnTxt_R
        # print(__txtPI2)
        __txtPI2Op = ""

        for m in range(64):
            __txtPI2Op += __txtPI2[IIP[m]-1]
        # print(__txtPI2Op)
        
        __ciptxt = ""
        for m in range(0,58,6):
            # num = str(__txtPI2Op[m])
            # num += str(__txtPI2Op[m+1])
            # num += str(__txtPI2Op[m+2])
            # num += str(__txtPI2Op[m+3])
            # num += str(__txtPI2Op[m+4])
            # num += str(__txtPI2Op[m+5])

            # print(num)
            a = (int(__txtPI2Op[m])*(2**5))+(int(__txtPI2Op[m+1])*(2**4))+(int(__txtPI2Op[m+2])*(2**3))+(int(__txtPI2Op[m+3])*(2**2))+(int(__txtPI2Op[m+4])*(2**1))+(int(__txtPI2Op[m+5])*(2**0))+32
            __ciptxt += chr(a)

        __ciptxtFinal += __ciptxt
    print(__ciptxtFinal)
        
            



