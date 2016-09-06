# email-raker

Collect e-mail addresses from any type of (potentially
unstructured) text files and output them as a single-column
on stdout. A text file containing e-mails to be excluded can
also be provided. UTF-8 encoding is assumed, but all text is
projected down to ASCII before searching for e-mail
addresses.

This is a small Python utility and supposed to be run form
the command line. Tested on Mac OS X, Python 2.7.


## Usage

```
usage: email-raker.py [-h] [--exclude-addr EXCLUDE_ADDR]
                      inputfiles [inputfiles ...]

Collect emails from unstructured files.

positional arguments:
  inputfiles

optional arguments:
  -h, --help            show this help message and exit
  --exclude-addr EXCLUDE_ADDR, -e EXCLUDE_ADDR
                        Name of file containing e-mail addresses to be
                        excluded.

```

Any number of input files can be provided (or piped) to the function. A file containing _blacklisted_ e-mails can optionally be considered as well (that file, too, does not have to be structured).


## Example

For demonstration, three example files are provided with the code. They are captures from the public address registry of three departments at the ETH Zurich. Example use:

```
email-raker.py phys.txt erdw.txt > 1col-emaillist.csv
```