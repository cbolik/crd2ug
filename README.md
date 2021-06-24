# crd2ug
A small Python3 script to convert text files with embedded chord symbols as was used by [ChordPro](https://en.wikipedia.org/wiki/ChordPro) to the multi-line format used by [Ultimate Guitar](https://www.ultimate-guitar.com/).

For example, this:

```
[D]I walk like you [Asus4]guide [G]me, my [D]eyes
Are shut like I'm [Asus4]blind [G]
```

will be converted to this:

```
D               Asus4 G      D
I walk like you guide me, my eyes
                  Asus4 G
Are shut like I'm blind 
```


To use, specify the file to convert as a command line argument, 
e.g. `python crd2ug.py myfile.crd`.
Or pipe it in, e.g. `cat myfile.crd | python crd2ug.py`.

In either case the processed lines are printed to stdout, so you will want 
to redirect it into a file.


