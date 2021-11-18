
Sbox = [
    6, 5, 12, 10, 
    1, 14, 7, 9, 
    11, 0, 3, 13, 
    8, 15, 4, 2]

P = [
    18, 23, 25, 20, 16, 3, 21, 6,
    24, 19, 22, 13, 12, 26, 27, 9,
    4, 1, 31, 10, 2, 29, 15, 8, 
    30, 17, 7, 0, 28, 11, 5, 14
]

def Permutation(a):
    bin_a = ""
    for i in range(0, len(a)):
        bin_a += bin(a[i])[2:].zfill(4)

    new = [0] * 32
    for i in range(0, 32):
        new[P[31-i]] = bin_a[i]
    new.reverse()

    b = "".join(new)
    # print(b)
    new = []
    for i in range(0, 8):
        # print(int(b[4 * i:4 * (i + 1)], 2))
        new.append(int(b[4 * i:4 * (i + 1)], 2))
    return new

Plain_text = [0x2, 0xa, 0xb, 0xa, 0xe, 0x8, 0xd, 0xb]
Cipher_text = [0xd, 0x2, 0xa, 0xc, 0x5, 0x5, 0x0, 0x4]

Key = [0x4, 0x3, 0x1, 0x2, 0x4, 0x3, 0x8, 0x6]

for i in range(0, len(Plain_text)):
    Plain_text[i] = Plain_text[i] ^ Key[i]

for i in range(0, 6):
    for j in range(0, len(Plain_text)):
        Plain_text[j] = Sbox[Plain_text[j]]
    Plain_text = Permutation(Plain_text)
    for j in range(0, len(Plain_text)):
        Plain_text[j] = Plain_text[j] ^ Key[j]

for j in range(0, len(Plain_text)):
    Plain_text[j] = Sbox[Plain_text[j]]
    Plain_text[j] = Plain_text[j] ^ Key[j]

print(Plain_text)

# Key = [4, 3, 1, 2, 4, 3, 8, 6]
'''
# Key 복구 하기 
print("Finding Key : ")
for a in range(0, 16):
    for b in range(0, 16):
        for c in range(0, 16):
            for d in range(0, 16):
                Plain_text = [0x2, 0xa, 0xb, 0xa, 0x5, 0x8, 0xd, 0xb]
                Key[4] = a
                Key[5] = b
                Key[6] = c
                Key[7] = d
                for i in range(0, len(Plain_text)):
                    Plain_text[i] = Plain_text[i] ^ Key[i]

                for i in range(0, 6):
                    for j in range(0, len(Plain_text)):
                        Plain_text[j] = Sbox[Plain_text[j]]
                    Plain_text = Permutation(Plain_text)
                    for j in range(0, len(Plain_text)):
                        Plain_text[j] = Plain_text[j] ^ Key[j]

                for j in range(0, len(Plain_text)):
                    Plain_text[j] = Sbox[Plain_text[j]]
                    Plain_text[j] = Plain_text[j] ^ Key[j]

                # print(Plain_text)
                if Plain_text == Cipher_text:
                    print("Key : ", Key)
'''