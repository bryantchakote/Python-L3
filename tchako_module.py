# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 11:26:34 2021

@author: tchak
"""

def f(x):
    """
    Parameters
    ----------
    x : double
        La valeur a elever au carre.

    Returns
    -------
    TYPE
        double.
    """
    
    return x * x

g = lambda x: x * x

def example():
    """
    Returns
    -------
    str
        "Affiche Bon bahhh....

    """
    
    return 'Bon bahh'

def fib(n = 5): # suite de fibonacci jusque n
    a, b = 0, 1
    while b < n:
        print (b)
        a, b = b, a + b

def perm_immut(a, b):
    """
    Parameters
    ----------
    a : TYPE
        DESCRIPTION.
    b : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    a, b = b, a
    print("a = ", a, "\tb = ", b)

def perm_mut(a, b):
    a[0], b[0] = b[0], a[0]
    print("a = ", a, "\tb = ", b)

# pgcd
def pgcd(a, b):
    while b != 0:
        x = a
        a = b
        b = x % a
    return(a)

# n!
def fac(n):
    """
    

    Parameters
    ----------
    n : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if n < 0:
        return ()
    if n == 0:
        return 1
    fac = 1
    for i in range (1,n+1):
        fac *= i
    return fac

# Combinaison
def comb(n, p):
    if (n < 0 or n < p):
        return ()
    return fac(n) // (fac(p) * fac(n-p))

# Arrangement
def arr(n, p):
    if (n < 0 or n < p):
        return ()
    return comb(n, p) * fac(p)

def impair(x):
    return x % 2
