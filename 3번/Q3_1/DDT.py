import random

# S-box 차분 분포 표를 만들어야 함
# S-box 차분 분포 표를 만들면
# 확률적으로 공격할 수 있다!

Sbox = [
    6, 5, 12, 10, 
    1, 14, 7, 9, 
    11, 0, 3, 13, 
    8, 15, 4, 2]

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

# 차분분포표 출력 
print('    ', end='')
for i in range(0, len(Sbox)):
    print("%3d " %i, end='')
print("\n")
for dx in range(0, len(Sbox)):
    print('%3d ' %dx, end='')
    for dy in range(0, len(Sbox)):
        print('%3d ' %(Dtable[dx][dy]), end='')
    print("\n")

'''
      0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15 

  0  16   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0 

  1   0   0   0   2   0   0   4   2   0   0   0   2   0   0   4   2 

  2   0   0   0   0   0   0   2   2   2   0   2   0   2   4   0   2 

  3   0   0   0   2   0   0   2   0   2   4   2   2   2   0   0   0 

  4   0   0   0   4   0   0   0   4   0   0   0   4   0   0   0   4 

  5   0   2   0   0   4   2   0   0   4   2   0   0   0   2   0   0 

  6   0   2   4   0   2   0   0   0   0   0   0   2   2   2   0   2

  7   0   0   4   0   2   2   0   0   0   2   0   2   2   0   0   2

  8   0   2   0   2   0   2   0   2   0   2   0   2   0   2   0   2

  9   0   2   0   0   0   2   4   0   0   2   0   0   0   2   4   0

 10   0   0   0   0   0   4   2   2   2   0   2   0   2   0   0   2

 11   0   4   0   2   0   0   2   0   2   0   2   2   2   0   0   0

 12   0   0   0   0   4   0   0   0   4   0   4   0   0   0   4   0

 13   0   2   0   0   0   2   0   0   0   2   4   0   0   2   4   0

 14   0   0   4   2   2   2   0   2   0   2   0   0   2   0   0   0

 15   0   2   4   2   2   0   0   2   0   0   0   0   2   2   0   0
'''