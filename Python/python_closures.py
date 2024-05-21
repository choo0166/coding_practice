"""
How can we fix the anonymous functions to behave as we'd expect?

functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())


In Python (and most OOP languages), environments are mutable, 
we can assign a new value to an existing variable and that 
mutates the environment it is part of. Any functions defined in 
that environment are evaluated in that environment, so they will 
see the new value of any variable.

As Python closures are late-binding, the argument i in the function
body is not bound to the value in the loop and loops do not create
new scope/environment, so the value of i still exists and takes the
last value at the end of the loop in the global environment.

When the function closures are called in the 2nd loop, the function
body is evaluated and the value of i is looked up in the global
environment.

Note that this does not conflict with the fact that Python is still
a lexically scoped language. Consider:

x = 1
def add(y):
    return x + y

x = 2
y = 3

def call_add(y):
    x = 3 
    return add(y)

call_add(x+y)

When call_add is evaluated, the arguments are evaluted in the global
environment, with x = 2 and y = 3 since value of x is reassigned. 
In the body, the value of x in the function environment is not used
when add is called, instead where it is defined in the global environment
i.e. 2.

To fix the scoping issue with closures, we can explicitly bind the value
to the function argument.
"""

functions = []
for i in range(10):
    functions.append(lambda i=i: i)

for f in functions:
    print(f())


