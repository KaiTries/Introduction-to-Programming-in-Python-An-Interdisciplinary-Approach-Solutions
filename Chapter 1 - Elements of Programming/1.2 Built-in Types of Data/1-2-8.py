#Suppose that a is 3.14159. What do each of these statements write? Explain each outcome.
#stdio.writeln(a)
#stdio.writeln(a + 1.0)
#stdio.writeln(8 // int(a))
#stdio.writeln(8.0 / a)
#stdio.writeln(int(8.0 / a))

# Output:
#3.14159
#4.14159
#2
#2.546479089470325
#2
#outcome depends on the type of a and the type of the expression. If a is an int, then the expression is an int. If a is a float, then the expression is a float.