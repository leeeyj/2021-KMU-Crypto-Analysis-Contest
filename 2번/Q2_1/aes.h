#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef unsigned char uint8;

#define Round 10
#define BlockSize 16
#define KeySize 16

/* -----------------------------------------------------------------------------------------------------------------------------------------------*/
/*                                                             <Basic Functions>                                                                  */

uint8 xtime(uint8 a);           // xtime : Multiplication on GF(2^8)  
uint8 m02(uint8 a);             // m02 : Multiply by 0x02 in MixColumns 
uint8 m03(uint8 a);             // m03 : Multiply by 0x03 in MixColumns => 0x03 * x = 0x02 * x xor 0x01 * x 

void Rot(uint8* t);             // Rot : Rotation 1-word(=4bytes)
void Sub(uint8* t);             // Sub : {Sbox(x0), Sbox(x1), Sbox(x2), Sbox(x3)} => Sbox 1-word

/* -----------------------------------------------------------------------------------------------------------------------------------------------*/


/* -----------------------------------------------------------------------------------------------------------------------------------------------*/
/*                                                         <Array processing Fuctions>                                                            */

void block2state(uint8* block, uint8 (*in_state)[4]);       // Block to State : 16bytes Block change to 2D Array[4][4]
void state2block(uint8 (*state)[4], uint8* block);          // State to Block : 2D Array[4][4] change to 16bytes Block

/* -----------------------------------------------------------------------------------------------------------------------------------------------*/

/* -----------------------------------------------------------------------------------------------------------------------------------------------*/
/*                                                         <AES-128 Algorithm Fuctions>                                                            */

void AddRoundKey(uint8 (*P)[4], uint8 (*key)[4]);           // AddRoundKey : Key adding functions
void SubBytes(uint8 (*P)[4]);                               // Sbox : Non-linear byte substitution
void ShiftRows(uint8 (*P)[4]);                              // ShiftRows : Rotate shift operation 
void MixColumns(uint8 (*P)[4]);                             // MixColumns : Column by Column operation
void KeyExpansion(uint8 *key, uint8 (*rk)[4][4]);           // KeyExpansion : Generate round key 

/* -----------------------------------------------------------------------------------------------------------------------------------------------*/
