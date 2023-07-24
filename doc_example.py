class example():
    '''
    Example doc string for class
    '''
    def __init__(self):
        # it is empty
        pass

    def factorial(self,x:int) -> int:
        '''
        factorial(x): returns the product of all of the integers from 1 to x inclusive
        '''
        self.x = x
        result = 1
        for i in range(2, self.x + 1):
            result += i
        return result

'''
when documenting code you want to be able to give
other users of the code an understanding of what
functions and class do in the code and the type
will result from the code or if specific input type is needed.
'''
#type casting is forcing a specific type to be inputted and a setting a specific type for outcome, this is sometimes known as type hints.

'''
A cool thing about python documentation is that the
doc strings and type hints in the functions can be called upon
by users using the python help in the terminal
'''

'''
python has a inbuilt function known as pydoc
allowing you to print out the information from the files,
the document name and the doc strings that would be included
as well as the file path

    python -m pydoc -w -doc_example
    wrote doc_example.html

this will write a html file that will include all
the documentation in the pydoc

You can implement this into a CI pipeline to update and
recreate a new html file for the documentation
'''