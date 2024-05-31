# Make your version

If you want write a python script that can be invoked as

```bash
python project/assignments/YOURNAME.py test-files/test.fa
```

and prints the translated version.

There are minimal checks, where  your script is executed both with *test.fa* and *test.fa.gz*
 
1.    **Command Success**: Checks if the command executed without errors (return code is 0).
2.    **Lines Starting with '>'**:  Verifies that the output contains exactly 3 lines starting with the character '>'.
3.    **Non-Empty Lines**: Ensures there are exactly 6 non-empty lines in the output.
4.    **Line Matching 'QIDTP'**:  Checks that there is exactly 1 line in the output containing the string "QIDTP".