# Documentation
# open() docs
# file_object.close() docs
# file_object.read() docs
# Regular Expressions
# New Terms
# open() - Opens a file in Python. This won't contain the content of the file, it just points to it in memory.
# .read() - Reads the entire contents of the file object it's called on.
# .close() - Closes the file object it's called on. This clears the file out of Python's memory.
# r'string' - A raw string that makes writing regular expressions easier.
# re.match(pattern, text, flags) - Tries to match a pattern against the beginning of the text.
# re.search(pattern, text, flags) - Tries to match a pattern anywhere in the text. Returns the first match.
# A better way to read files
# If you don't know the size of a file, it's better to read it a chunk at a time and close it automatically. The following snippet does that:

# with open("some_file.txt") as open_file:
#     data = open_file.read()
# The with causes the file to automatically close once the action inside of it finishes. And the action inside, the .read(), will finish when there are no more bytes to read from the file.

# Why didn't I cover this in the video? There's more going on here, behind-the-scenes, and I think it's better to know the long way first.