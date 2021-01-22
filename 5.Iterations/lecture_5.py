# While loops, enumerate, zip

# generator - zip function
'''
Using the Python zip() Function for Parallel Iteration
>>> numbers = [1, 2, 3]
>>> letters = ['a', 'b', 'c']
>>> zipped = zip(numbers, letters)
>>> zipped  # Holds an iterator object
<zip object at 0x7fa4831153c8>
>>> type(zipped)
<class 'zip'>
>>> list(zipped)
[(1, 'a'), (2, 'b'), (3, 'c')]

 Notice how the Python zip() function returns an iterator. To retrieve the final list object, you need to use list() to consume the iterator.

 If you’re working with sequences like lists, tuples, or strings, then your iterables are guaranteed to be evaluated from left to right. This means that the resulting list of tuples will take the form [(numbers[0], letters[0]), (numbers[1], letters[1]),..., (numbers[n], letters[n])]. However, for other types of iterables (like sets), you might see some weird results:

    >>> s1 = {2, 3, 1}
    >>> s2 = {'b', 'a', 'c'}
    >>> list(zip(s1, s2))
    [(1, 'a'), (2, 'c'), (3, 'b')]
'''

l1 = ['.py', '.js', '.rb', '.java', '.c']
l2 = ['python', 'javascript', 'ruby', 'java', 'c']

tupled_list = zip(l2,l1) 
print(tupled_list)  # print out <zip object at 0x10e0e4548>

#To print out the zip object located in memory, convert it to list
tupled_list = list(tupled_list)
print(tupled_list)
#[('python', '.py'), ('javascript', '.js'), ('ruby', '.rb'), ('java', '.java'), ('c', '.c')]
