Hash Function
-------------
| Algorithm  | Variant  | Output size  (bits) | Internal state  size (bits) | Block size  (bits) | Rounds |
|------------|----------|---------------------|-----------------------------|--------------------|--------|
|     MD5    |          |         128         |         128 (4 × 32)        |         512        |   64   |
|            |          |                     |                             |                    |        |
|    SHA-0   |          |         160         |         160 (5 × 32)        |         512        |   80   |
|            |          |                     |                             |                    |        |
|    SHA-1   |          |         160         |         160 (5 × 32)        |         512        |   80   |
|            |          |                     |                             |                    |        |
|    SHA-2   |  SHA-224 |         224         |         256 (8 × 32)        |         512        |   64   |
|            |  SHA-256 |         256         |         256 (8 × 32)        |         512        |   64   |
|            |  SHA-384 |         384         |         512 (8 × 64)        |        1024        |   80   |
|            |  SHA-512 |         512         |         512 (8 × 64)        |        1024        |   80   |
|            |          |                     |                             |                    |        |
|    SHA-3   | SHA3-224 |         224         |      1600 (5 × 5 × 64)      |        1152        |   24   |
|            | SHA3-256 |         256         |      1600 (5 × 5 × 64)      |        1088        |   24   |
|            | SHA3-384 |         384         |      1600 (5 × 5 × 64)      |         832        |   24   |
|            | SHA3-512 |         512         |      1600 (5 × 5 × 64)      |         576        |   24   |


* Plain text -> Hash Algorithm -> Digest aka Message Digest aka Hash 
* MD5: not secure 
* SHA characteristics:
  + Deterministic: same input always produces same output
  + fast: 
  + irreversible: input can not be generated from the output
  + Utilize "Avalanche Effect": slightly different inputs will product entirely different output
  + Collision-resistant: no two inputs results in same output
    - Google in 2017 produced two PDFs that had same SHA1. It was mostly similar data just different background colors. 
      it took them lot of time and about 110K worth of compute resources to find that collision. 
  + same algorithm always produces same size string irrespective of the input
    - 'a' -> sha256 -> 256 bit long string
    - 'abc12345' -> sha256 -> 256 bit long string


* Usage:
  + verifying files and message integrity
  + File and data identification (Git)
    - git uses sha as file names internally so it's easier to compare if there is a diff
  + password verification 
  + message cryptography


SHA1 Functioning: 
* text -> 
  1. ascii codes -> 
  2. binary codes -> 
  3. pad zeros to make 8 bits long -> 
  4. combine -> 
  5. pad binary message with zeroes until its length is 512 mod 448 (so it's always 40 characters long) 
  6. take the length of array in step 3 and convert it to binary - > pad 0's to make 64 characters
  7. append step 6 output to step 5 output 
  8. you get 512 bit long binary string, for bigger strings we have multiple chunks each of 512 bits.
  9. break each 512 bit chunk into 32 -bit words
  10. using bitwise operations extend each chunk to 80 words (80-32 are the made up words)
  11. initialize five constants  a, b, c, d, e with some initial binary values 
      - a = 01010101 01010101 01010101 01010101
      - b = 01010101 01010101 01010101 11110000
      - c = 01010101 01010101 01010101 01000011
      - d = 01010101 01010101 01010101 11010101
      - e = 01010101 01010101 01010101 01100111

  12. for each chunk and then word do bitwise operation with these five variables.
      - eg: for each chunk: for word in chunk.80words: a xor word, b xor word ....

  13. at the end take hexadecimal values of these five vars
  14. combine to produce hash

* 'A Test' -> [A, T,e,s,t] -> [65, 32, 84, 101, 115, 116] -> binary of each padded with zeros -> 5*8 -> 48 bit long string -> pad 0's 



- Pre-image resistance
- Second pre-image resistance
- Unbreakable without using a brute force approach
- one-way




## Collision 
-------------
* Lets say we have a hash function that takes a phone number, add the three parts to give the hash
  + Then the following two phone numbers generate the same hash
    - (408)123-4567 -> 408+123+4567 -> 5098
    - (408)131-4559 -> 408+131+4559 -> 5098





