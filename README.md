# Sobieszewo
Simple interpreter

## Usage
```
python interpreter.py code.sobieszewo
```

You can write a simple Fibonacci sequence program.
```
SET X
ADD 0
SET Y
ADD 1
IFF A
SET X
MOR 50
NPRT Y
NPRT X
ELS A
SET Y
ADD X
SET X
ADD Y
NPRT Y
NPRT X
GOT 4
SEE A
```

You can also run sobieszewo in editor and interactive mode.

Editor mode:
```
python interpreter.py -e
```
Interactive mode:
```
python interpreter.py -i
```