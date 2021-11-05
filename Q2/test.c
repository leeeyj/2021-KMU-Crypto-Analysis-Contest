#include <stdio.h>
#include "./aes.h"

int main()
{   
    uint8 Cipher[16];

    uint8 input_Plain[4][4];
    uint8 Plaintext[16] = {0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff};
    block2state(Plaintext, input_Plain);

    uint8 RoundKey[11][4][4];
    uint8 key[16] = {0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f};
    KeyExpansion(key, RoundKey);

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
    
    state2block(input_Plain, Cipher);
    printf("Cipher : ");
    for (uint8 i = 0; i < 16; i++){
        printf("%d ", Cipher[i]);
    }

    
    //  <Testing Key Scheme>   
    /*
    for (int k = 0; k < 11; k++){
        printf("key sch %d : ", k);
        for (int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                printf("%d ", RoundKey[k][j][i]);
            }
        }
        printf("\n");
    }
    */
    /*
    ShiftRows(input_Plain);
        printf("ShiftRows %d : ", i);
        for (uint8 i = 0; i < 4; i++){
            for (uint8 j = 0; j < 4; j++){
                printf("%d ", input_Plain[j][i]);
            }
        }
        printf("\n");
    */
}



