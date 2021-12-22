import random

P = [
    18, 23, 25, 20, 16, 3, 21, 6,
    24, 19, 22, 13, 12, 26, 27, 9,
    4, 1, 31, 10, 2, 29, 15, 8, 
    30, 17, 7, 0, 28, 11, 5, 14
]

# 철수의 블록 암호의 Permutation
def Permutation(a):
    bin_a = ""
    for i in range(0, len(a)):
        bin_a += bin(a[i])[2:].zfill(4)

    new = [0] * 32
    for i in range(0, 32):
        new[P[31-i]] = bin_a[i]
    new.reverse()

    b = "".join(new)
    new = []
    for i in range(0, 8):
        new.append(int(b[4 * i:4 * (i + 1)], 2))
    return new

# 철수의 블록 암호의 Sbox
Sbox = [
    6, 5, 12, 10, 
    1, 14, 7, 9, 
    11, 0, 3, 13, 
    8, 15, 4, 2]

InvSbox = [
    9, 4, 15, 10,
    14, 1, 0, 6, 
    12, 7, 3, 8,
    2, 11, 5, 13
]

# 차분 분포표 생성 16x16
Dtable = []
for i in range(0, len(Sbox)):
    Dtable.append([0 for j in range(0, len(Sbox))])

# 입출력 차분 
for x1 in range(0, len(Sbox)):
    y1 = Sbox[x1];
    for x2 in range(0, len(Sbox)):
        # dx = 입력 차분 값 
        dx = x1 ^ x2            # x1 ^ x2 = dx, 입력 차분 값 
        y2 = Sbox[x2]
        dy = y1 ^ y2            # S(x1) ^ S(x2) = dy, Sbox 차분 값 
        Dtable[dx][dy] += 1     # δ(dx, dy)

# 6라운드 차분 특성 찾기
x1_xor_x2 = [0] * 8
x1_xor_x2[4] = 11
Probability = 1
print("Input 차분 : ", x1_xor_x2)
for i in range(0, 6):
    for j in range(0, 8):
        d1 = x1_xor_x2[j]               # 입력 차분 
        new = Dtable[d1]                # 입력 차분에 대한 차분 특성 확인 
        for h in range(0, len(new)):
            if new[len(new) - 1 - h] == 2:
                d2 = len(new) - 1 - h
            if new[h] == 4:
                d2 = h
                break
        if d1 == 0:                     # 입력 차분이 0이라면 ? => 출력 차분 = 0
            x1_xor_x2[j] = 0
            d2 = 0
        else:
            # print("d1 : ", d1)
            # print("d2 : ", d2)
            x1_xor_x2[j] = d2
            Probability *= (Dtable[d1][d2] / 16)
        print("d1 : ", d1)
        print("d2 : ", d2)
    x1_xor_x2 = Permutation(x1_xor_x2)
    print("Round ", i+1, " 차분 특성: ", x1_xor_x2)

print("6라운드 차분 특성", x1_xor_x2)
print("차분 특성 확률 : ", Probability)


'''
# 6Round 차분 특성을 가지는 평문2개 생성 
dx = 11
f = open("./PlainText.txt", "w")
for i in range(0, 100000):
    x1 = [random.randrange(0, 16), random.randrange(0, 16), random.randrange(0, 16), random.randrange(0, 16), 
          random.randrange(0, 16), random.randrange(0, 16), random.randrange(0, 16), random.randrange(0, 16)]
    
    x2 = [x1[0], x1[1], x1[2], x1[3], x1[4] ^ 11, x1[5], x1[6], x1[7]]
    p1 = ""
    p2 = ""
    for j in range(0, 8):
        p1 += hex(x1[j])[2:]
        p2 += hex(x2[j])[2:]
    p1 += "\n"
    p2 += "\n"
    f.write(p1)
    f.write(p2)
f.close    
'''
'''
# Key 찾기 
# input 차분 : [0, 0, 0, 0, 11, 0, 0, 0]
# 6 Round 차분 : [1, 2, 1, 4, 0, 0, 0, 0]
key_freq = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0}
Round6_Dout = [1, 2, 1, 4, 0, 0, 0, 0]      # 6 Round 차분 특성: [1, 2, 1, 4, 0, 0, 0, 0]
target = 0                      
for i in range(0, 16):
    key = i                              # 첫번째 Key 찾기  
    f = open("./CipherText.txt", "r")
    for l in range(0, 100000):
        c1 = f.readline()
        c2 = f.readline()
        
        c1 = int(c1[target], 16)        # 암호문1의 target 부분만 가져오기 
        c2 = int(c2[target], 16)        # 암호문2의 target 부분만 가져오기
        c1 = InvSbox[c1 ^ key]      # 암호문1, 7라운드 복호화
        c2 = InvSbox[c2 ^ key]      # 암호문2, 7라운드 복호화

        if c1 ^ c2 == Round6_Dout[target]:    # 7라운드 복호화한 암호문 2개의 차분 특성과 
            key_freq[key] += 1                  # 6라운드 차분 특성이 일치하는지 확인한다
    f.close()
    print(i + 1, "번 완료")

print(key_freq)     # 예측 키 빈도수 출력, 가장 높은 빈도수가 키 후보
                    # 빈도수가 같은 것이 있다면, 두개를 키 후보로 생각한다.
'''
