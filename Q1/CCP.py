def Right_rotation(M, K):
    for i in range(0, K):
        M = M[-1] + M[:-1]     
    M = "0b" + M
    return M


def Left_rotation(C, K):
    for i in range(0, K):
        C = C[1:] + C[0]
    return C

def CCP_Enc(M, K):
    # Key Value 만큼 Right Rotation
    output = ""
    for i in range(0, len(M)):
        output += bin(ord(M[i]))[2:].zfill(8)
        # print(output)
    output = Right_rotation(output, K)
    return output


def CCP_Dec(C, K):
    # Key Value 만큼 Left Shift
    output = ""
    C = C[2:]
    C = Left_rotation(C, K)
    for i in range(0, int(len(C) / 8)):
        # print(C[8 * i : 8 * (i + 1)])
        output += chr(int(C[8 * i : 8 * (i + 1)], 2))
    
    return output


def main():
    M = "orld!HelloW"                   # 평문					
    K = 0x39                            # 암호화 키
    C = CCP_Enc(M, K)                   # 암호문 생성
    print("Encrypt output : " + C)      # 암호문 출력
    D = CCP_Dec(C, K)                   # 복호화
    print("Decrypt output : " + D)      # 복호화 출력 


if __name__ == "__main__":
    print("test")
    main()

