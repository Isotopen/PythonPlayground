# lists [,]
# dictionaries {:}
# strings "" or ''
# tuple (,) or tuple([1, 2, 3])

# One of the most common ways you'll see sets being used is to make some other iterable unique.
# For example, say you have a list of page numbers where terms appear in a book.
# Since some pages could contain multiple terms, you're likely to get repeats. In that case, you'll see people doing code like this:
# pages = list(set(pages))

# sets are mutable

set([1, 3, 5])
# creates the set {1, 3, 5}
{1, 3, 5}
# also creates the set {1, 3, 5}
type(set())

low_primes = {1, 3, 5, 7, 11, 13}
low_primes.add(17) # adds single items
low_primes.update({19, 23}, {2, 29}) # adds multiple items
