# SHA 256 conflict calculator in 24 hours

## Problem Description

Using as many computers as you need, find a collision in 
SHA256 in < 24 hours of wall time. The less resources 
(CPU/RAM/GPU/networking) you use, the better.

## questions

- Do we have to check all 2^ 256 combinations ?
- Do we know the logic behind the SHA calculator or we consider it random ?
- Can we develop some kind of logic there to find how is SHA calculated?
- what is the input this SHA is generated for?
- Can we pregenerate the text?
- can we divide and conquer sha calculator?

## Approach

SHA256 has two possible values for each digit in 256 bits 1/0. 
Thus there are 2^256 possible SHA's that needs to be generated

- day calculations 2 ^ 256
- every hour 2^256 / 24
- every min 2^256 / (24 * 60)
- every sec 2^256 / (24 * 60 * 60) ~ 2^256 / 2^16 ~ 2^240

- text generators capacity assume = 2^20 texts or boolean / second
- SHA calculator capacity assume = 2^10 SHA / second
- duplicate analyzer capacity assume = 2^5 / second
- each queue's capacity assume = 2^5


- No. of text generators needed 2^240 / 2^20 = 2^220
- No. of SHA Calculators needed 2^240 / 2^10 = 2^230
- No. of duplicate analyzers needed 2^240 / 2^5 = 2^235
- no. of queues needed = 2^20 - 2^10 = 2^10 / q capacity = 2^5
- amound of cache needed = 2^10 - 2^5 = 2^5
