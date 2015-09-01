remove-crap.py
==============

```
usage: remove-crap.py [-h] -p PATTERNS_FILE INPUT_FILE

Prints lines NOT matching any patterns defined in the patterns file

positional arguments:
  INPUT_FILE            File to process

optional arguments:
  -h, --help            show this help message and exit
  -p PATTERNS_FILE, --patterns PATTERNS_FILE
                        File containing patterns to filter (one per line)
```

Example:
---------

Content of patterns.txt:
```
ANNOYING
^\s*$
```

Content of log.txt:
```
Start
All lines containing ANNOYING is not printed

The previous line is not printed since the regex ^\s*$ removes empty lines
The end
```

Result after running ```python remove-crap.py -p patterns.txt log.txt```:
```
Start
The previous line is not printed since the regex ^\s*$ removes empty lines
The end
```

Tip:
----
To save the result to a new file, simply redirect the output using the ```>``` operator:
```
python remove-crap.py -p patterns.txt log.txt > result.txt
```
