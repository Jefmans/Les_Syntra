# 1. 
# Write a program that finds the average of a series of numbers entered by the user.
# The program will first ask the user how many numbers there are.
# Note: the average should always be a float. Even if the user only inputs ints.


# 2.
# Write a program that approximates the value of "pi" by summing the terms of this series: 
# 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...
# The program should prompt the user for n, the number of terms to sum of the first n terms of this series.
# Have your program substract the approximation from the value of math.pi to see how accurate it is.


# 3.
# A Fibonaci sequence is a sequence of numbers where each successive number is the sum of the previous two.
# The classic Fibonacci sequence begins: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# Write a program that computes the nth Fibonacci number where n is a clue input by the user. 
# For example, if n = 6, then the result is 8.


# 4.
# You hgave seen that the math library contains a function that computes the square root of numbers. 
# In this excercice, you are to write your own algorithm for computing square roots.
# One way to solve this problem is to use a guess-and-check approach. You first guess what the square root might be and then see how close you guess is.
# You can use this information to make another guess and continue guessing until you have found the square root (or a close approximation to it).
# One particularly good way of making guesses is to use Newton's method.
# Suppose x is the number we want the root of and guess is the current guessed answer. The guess can be imporved by using 
# (guess + x/guess) / 2
# as the next guess.
# Write a program that implements Newton's method. The program should prompt the user for the value to find the square root of (x) and the number of times to improve the guess.
# Starting with a guess value of x/2, your program should loop the specified number of times applying Newton's and report the final value of guess.
# You should also substract your estimate from the value of math.sqrt(x) to show how close it is.


# 5.
# Write a function named right_justify that takes a string named s as a parameter
# and prints the string with enough leading spaces so that the last letter of the string is in column 70
# of the display.
# >>> right_justify('monty')
# monty
# Hint: Use string concatenation and repetition. Also, Python provides a built-in function called len
# that returns the length of a string, so the value of len('monty') is 5.


# 6.
# A function object is a value you can assign to a variable or pass as an argument. For example, do_twice is a function that takes a function object as an argument and calls it twice:
# ```
# def do_twice(f):
#     f()
#     f()
# #Here’s an example that uses do_twice to call a function named print_spam twice.
# def print_spam():
#     print('spam')

# do_twice(print_spam)
# ```
# a) Type this example into a script and test it.
# b) Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument.
# c) Copy the definition of print_twice from earlier in this chapter to your script.
# e) Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.
# f) Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter. There should be only two statements in the body of this function, not four.


# 7.
# a) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated sequence of values:
# print('+', '-')
# By default, print advances to the next line, but you can override that behavior and put a space at the end, like this:

# ```
# print('+', end=' ')
# print('-')
# ```
# The output of these statements is '+ -' on the same line. The output from the next print statement would begin on the next line.

# b) Write a function that draws a similar grid with four rows and four columns.


# 8.
# The time module provides a function, also named time, that returns the current Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. On UNIX systems, the epoch is 1 January 1970.

# >>> import time
# >>> time.time()

# `1437746094.5735958`
# Write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds, plus the number of days since the epoch.


# 9.
# Fermat’s Last Theorem says that there are no positive integers a, b, and c such that
# an + bn = cn
# for any values of n greater than 2.

# a) Write a function named check_fermat that takes four parameters—a, b, c and n—and
# checks to see if Fermat’s theorem holds. If n is greater than 2 and
# an + bn = cn
# the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should
# print, “No, that doesn’t work.”

# b) Write a function that prompts the user to input values for a, b, c and n, converts them to
# integers, and uses check_fermat to check whether they violate Fermat’s theorem.


# 10.
# If you are given three sticks, you may or may not be able to arrange them in a triangle.
# For example, if one of the sticks is 12 inches long and the other two are one inch long, you will not
# be able to get the short sticks to meet in the middle. For any three lengths, there is a simple test to
# see if it is possible to form a triangle:
# If any of the three lengths is greater than the sum of the other two, then you cannot
# form a triangle. Otherwise, you can. (If the sum of two lengths equals the third, they
# form what is called a “degenerate” triangle.)

# a) Write a function named is_triangle that takes three integers as arguments, and that prints
# either “Yes” or “No”, depending on whether you can or cannot form a triangle from sticks
# with the given lengths.
# b) Write a function that prompts the user to input three stick lengths, converts them to integers,
# and uses is_triangle to check whether sticks with the given lengths can form a triangle.


# 11.
# Loterij trekking voor WWF
# Simuleer een loterij trekking voor het WWF. Ons loterij formulier ziet er uit als volgt:
# Afbeeldingen :
# stier vis dolfijn beer
# giraf hond muis orka
# octopus kat slang lama
# olifant pinguin vogel emoe
# koala paard zebra kangoeroe
# We vragen de gebruiker om 5 afbeeldingen te kiezen uit de mogelijke afbeeldingen. We willen als
# output zien, de gekozen afbeeldingen, de winnende afbeeldingen, hoeveel afbeeldingen correct
# gekozen zijn (inclusief de correct gekozen dieren) en het spelformulier met een twist.
# Op het formulier moet het volgende zichtbaar zijn
# - als een afbeelding een winnende en een gekozen afbeelding is vervangen door sterretjes (de hele
# tekst)
# - als een afbeelding een winnende afbeelding is vervangen door streepjes (de hele tekst)
# Voorbeeld output
# Uw gekozen afbeeldingen: giraf, vis, dolfijn, vogel, zebra
# De winnende afbeeldingen zijn: stier, vis, dolfijn, lama, slang
# U heeft de volgende 2 afbeelding(en) correct, namelijk: vis, dolfijn
# Het formulier:
# Afbeeldingen:
# ----- *** ****** beer
# giraf hond muis orka
# octopus kat ----- ----
# olifant pinguin vogel emoe
# koala paard zebra kangoeroe


# 12.
# Maak een programma dat een ongekend aantal getallen vraagt, maak een functie dat de som van al
# deze getallen zal berekenen en teruggeven.

# 13.
# Maak een programma dat het volgende doet: vraag een ongekend aantal nummer van getallen, maak
# een functie dat de max weergeeft, maak een andere functie dat de min weergeeft en maak een functie
# dat de minimale waarde en de maximale waarde van lijst gaat optellen en vermeningvuldigen. Maak een
# 3de functie dat alles zal afdrukken

