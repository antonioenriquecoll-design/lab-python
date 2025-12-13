#!/usr/bin/env python
# coding: utf-8

# ### Reduction operation: the sum of the numbers in the range [0, a)

# In[1]:


import time

def reduc_operation(a):
    """Compute the sum of the numbers in the range [0, a)."""
    x = 0
    for i in range(a):
        x += i
    return x

# Secuencial

value = 1000000

initialTime = time.time()
suma = reduc_operation(value)
finalTime = time.time()

print("Time taken by reduction operation:", (finalTime - initialTime), "seconds")

# Utilizando las operaciones mágicas de ipython
get_ipython().run_line_magic('timeit', '-r 2 reduc_operation(value)')

print(f"\n \t Computing the sum of numbers in the range [0, value): {suma}\n")

