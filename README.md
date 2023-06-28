# Advanced Python And Python Automation

</h1></h2>

### String Literals
*typing quotation in quotaions*: 
<br>One benefit of using double quotes is that the string can have a single quote character in it.<br>
``` print("That is Alice's cat")```

*Escape characters*:
<br> An escape character lets you use characters that are otherwise impossible to put into a string. An escape character consists of a backslash (\) followed by the character you want to add to the string. (Despite consisting of two characters, it is commonly referred to as a singular escape character.) For example, the escape character for a single quote is \'. You can use this inside a string that begins and ends with single quotes.<br>
```>>> spam = 'Say hi to Bob\'s mother.'```
<br>Python knows that since the single quote in Bob\'s has a backslash, it is not a single quote meant to end the string value. The escape characters \' and \" let you put single quotes and double quotes inside your strings, respectively.<br>

*Escape Character* ---*Prints*<br>
\'-------------------------Single quote<br>
\"-------------------------Double quote<br>
\t-------------------------Tab<br>
\n-------------------------Newline (line break)<br>
\\\\-----------------------Backslash<br>

### Raw Strings
You can place an r before the beginning quotation mark of a string to make
it a raw string. A raw string completely ignores all escape characters and
prints any backslash that appears in the string. For example, type the fol-
lowing into the interactive shell:<br>
```>>> print(r'That is Carol\'s cat.')``` <br>
```That is Carol\'s cat.``` <br>
Because this is a raw string, Python considers the backslash as part of
the string and not as the start of an escape character. Raw strings are help
ful if you are typing string values that contain many backslashes. <br>

### Useful String Methods
*upper()*<br>
```Returns a new string where all the letters in the original string have been converted to uppercase```<br>
*lower()*<br>
```Returns a new string where all the letters in the original string have been converted to lowercase```<br>
*isupper()*<br>
*islower()*<br>
```Returns a boolean value where the string is upper or lower respectively```<br>

