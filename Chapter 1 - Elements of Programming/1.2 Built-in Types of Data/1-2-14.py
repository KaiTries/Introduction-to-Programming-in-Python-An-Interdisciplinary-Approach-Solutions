#A physics student gets unexpected results when using the code
#force = G * mass1 * mass2 / radius * radius
#to compute values according to the formula F = Gm1m2 / r2. Explain the problem and correct the code.
#Solution: The code divides by r, and then multiplies by r. Instead it should divide by r squared. Use parentheses:
#force = G * mass1 * mass2 / (radius * radius)