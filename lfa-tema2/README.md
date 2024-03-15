# NFA/DFA word generator

This is a python script that generates a list of words of given lenght that are accepted by a Deterministic Finite Automaton (DFA) or a Non-Deterministic Finite Automaton (NFA).


# Input format

```
q0 1 q0
q0 0 q1
q1 1 q0
q1 1 q0
q1 0 q2
q2 2 q3
q1 q3
6
```
where the last row dictates the lenght of the words and the second to last contains the final states of the automaton

# Output format

The script outputs words that would be accepted by the automaton.

```
abccca abbbbc
```

