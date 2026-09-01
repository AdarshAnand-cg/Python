a="I Love Java"
b="Python"
print(a.replace("Java",b))

#Strip
c="  Hello World     "
print(c.strip())
Info="Strip() method removes the whitespacing around the string. Whitespacing means space before string and after the string characters."
Info="There is lstrip() and rstrip() method also. lstrip() removes the whitespacing from the left side of the string and rstrip() removes the whitespacing from the right side of the string."

#Complete Path
v=r"C:\Users\Dell\Desktop\Python Class-08\Demo.py"
print(v)
print(v.split("\\")[-1])
w="C:\news\table\new.txt"
print(w)
info2="In the above example, we have used the split() method to split the string into a list of substrings based on the backslash character. The [-1] index is used to access the last element of the list, which is the file name 'Demo.py'."
info3="without the 'r' prefix, the backslashes in the string are treated as escape characters, which can lead to unexpected results. For example, '\n' is interpreted as a newline character, and '\t' is interpreted as a tab character. By using the 'r' prefix, we tell Python to treat the string as a raw string, which means that backslashes are treated as literal characters and not escape characters. This is important when working with file paths on Windows, where backslashes are commonly used as directory separators."

words = ["Python", "is", "easy"]
result = " ".join(words)
print(result)

INFO="The join() method is used to join the elements of a list into a single string, with a specified separator between each element. In this case, we are using a space character as the separator, so the resulting string will have spaces between each word in the list."
