#include <stdio.h>
#include "./aes.h"
#include <intrin.h>

__int64 cpucycles() 
{
    return __rdtsc();
}

void AES128_E(uint8 (*input_Plain)[4], uint8 (*RoundKey)[4][4])
{
    AddRoundKey(input_Plain, RoundKey[0]);
    for (uint8 i = 1; i < Round; i++){
        SubBytes(input_Plain);
        ShiftRows(input_Plain);
        MixColumns(input_Plain);
        AddRoundKey(input_Plain, RoundKey[i]);
    }
    SubBytes(input_Plain);
    ShiftRows(input_Plain);
    AddRoundKey(input_Plain, RoundKey[10]);
}

int main()
{   
    uint8 input_Plain[4][4];
    uint8 Plaintext[16] = {0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff};
    block2state(Plaintext, input_Plain);

    uint8 RoundKey[11][4][4];
    uint8 key[16] = {0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f};
    KeyExpansion(key, RoundKey);

    AES128_E(input_Plain, RoundKey);

    uint8 Cipher[16];
    state2block(input_Plain, Cipher);
    printf("Cipher : ");
    for (uint8 i = 0; i < 16; i++){
        printf("%x ", Cipher[i]);
    }
}



