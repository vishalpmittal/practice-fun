# Finite state machine, FSM, Finite Automata

## Terms

- Finite: Limited Number
- State: state of something at that moment(solid/liquid/gas, hot/cold,
    walk/eat/talk/sleep, On/off)
- Symbols: a,b,c,0,1,2,3, etc.
- Alphabet: collection of symbols
- String: sequence of symbols
- Language: Set of Strings
  - Regular Languages: A language is said to be a Regular Language if and only if some FSM recongnizes it.
  - Non-Regular Languages: not recognized by any FSM. Requires Memory:
- Cardinality: number of elements in a set

## Operations

- Union - A U B = {x | x ε A or x ε B}
- Concatenation - A ο B = {xy | x ε A and y ε B}
- Star - A* = { x1 x2 x3 .... xk | k >=0 and each xi ε A}
- Examples:

    ```python
    A = {pq, r}, B = {t, uv}
    A U B = {pq, r, t, uv}
    A ο B = {pqt, pquv, rt, ruv}
    A* = {ε, pq, r, pqr, rpq, pqpq, rr, pqpqpq, rrr, ......}
    ```

## Properties

- simplest model of computation
- has very limited memory

## Types

- with output
  - Moore Machine
  - Mealy Machine

- without output
  - DFA (Deterministic Finite Automata)

    ```bash
    (Q, Σ, qο, F, δ)
    Q: set of all states
    Σ: inputs
    qο: start/initial state
    F: Set of final states
    δ : transition function that maps from Q x Σ -> Q
    ```

    - eg: set of all strings of length<=3 that contains {0,1} and starts with 0

       {0, 00, 01, 001, 010, 011}

    - code eg: leetcode.P0xx.P065_ValidNumber.py

  - NFA (Non-Deterministic Finite Automata)
    - Characterstics:
      - Given current state, there could be multiple next states
      - the next state may be chosen at random
      - all the next state may be chosen in parallel
    - eg: set of all strings that end with 0

  - E-NFA (epsellon Non-Deterministic Finite Automata)
