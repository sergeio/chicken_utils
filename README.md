Chicken Utils
=============

A collection of utils for the [Chicken Chicken Chicken programming
language](http://torso.me/chicken).

chicken_to_code.py
------------------

Turns Chicken machine code into a chicken assembly:

```bash
$ cat cat.chn | ./chicken_to_code.py
1
load
```

code_to_chicken.py
------------------

Turns chicken assembly into Chicken machine code.

```bash
$ echo "10\n10\nmultiply\nchars" | ./code_to_chicken.py
chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken
chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken
chicken chicken chicken chicken
chicken chicken chicken chicken chicken chicken chicken chicken chicken
```

chicken_run
-----------

Uses [mcwhittemore's unobfuscated chicken
VM](https://github.com/mcwhittemore/chicken) to run your chicken machine code.

```bash
$ echo "10\n10\nmultiply\nchars" | ./code_to_chicken.py | ./chicken_run
d
```

encode.py
---------

Translates STDIN into Chicken machine language that prints out text from STDIN.
Compresses the Chicken code by about 50% as compared to a naive implementation.

echo 'hi!'
```bash
$ echo 'hi!' | ./encode.py
chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken
chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken
chicken chicken chicken chicken
chicken chicken chicken chicken chicken chicken chicken chicken chicken
chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken
chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken
chicken chicken chicken chicken
chicken chicken chicken chicken chicken chicken chicken chicken chicken
chicken chicken
chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken
chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken
chicken chicken chicken chicken
chicken chicken chicken chicken chicken chicken chicken chicken chicken
chicken chicken
```

```bash
$ echo 'hi!' | ./encode.py | ./chicken_run
hi!
```
