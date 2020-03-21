
# Permutations

Ordering Matters. There are basically two types of permutation:

## Repetition is Allowed

such as a lock code. It could be "333".

When a thing has n different types ... we have n choices each time!

choosing r of something that has n different types, the permutations are:

n × n × ... (r times) = n^r times

## No Repetition

for example the first three people in a running race. You can't be first and second.

```math
P(n, r) = n! / (n − r)!
```

eg:

- number of purmutations to arrange 3 of 16 pool balls:

   16 ! / (16 - 3)! = 16 x 15 x 14 = 3,360

- How many ways can first and second place be awarded to 10 people?

   10 ! / (10 - 2)! = 10 x 9 = 90

# Combinations

Ordering does not matter.

## Combinations without Repetition

This is how lotteries work. The numbers are drawn one at a time, and if we have the lucky numbers (no matter what order) we win!

```math
C(n ,r) = n! / (r! (n − r)!)
```

## Combinations with Repetition

there are five flavors of icecream: banana, chocolate, lemon, strawberry and vanilla. We can have three scoops. How many variations will there be?

{b, c, l, s, v}

example selections: {c, c, c}, {b, l, v}, {b, v, v}...

[b, c, l, s, v]

at each index we can either pick or move forward. And we can only pick three.

- {c, c, c} : [ > 1 1 1 > > > ]
- {b, l, v} : [ 1 > > 1 > > 1 ]
- {b, v, v} : [ 1 > > > > 1 1 ]

Basically we can chose 3 one's and 4 arrows out of 7 places:

```math
C(n ,r) = (n + r - 1)! / (r! (n − 1)!)
```
