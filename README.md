# AI-Elearning-2

Source code for EL02 - The Dining Philosophers Problem.

## Problem Model

- Variables: `P1, P2, ..., Pn`
- Domain: `{Thinking, Eating}`
- Constraint: two adjacent philosophers cannot both be `Eating`
- Circular table: `Pn` is adjacent to `P1`

## Run

```powershell
python src/main.py
```

Run with another number of philosophers:

```powershell
python src/main.py --philosophers 7
```

Show constraint trace:

```powershell
python src/main.py --trace
```

## Test

```powershell
python -m unittest discover -s test
```

## Expected n = 5 Result

One valid complete assignment:

```text
P1 = Eating
P2 = Thinking
P3 = Eating
P4 = Thinking
P5 = Thinking
```

This is valid because no two adjacent philosophers are both `Eating`.
