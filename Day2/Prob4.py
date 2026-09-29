# Display Fibonacci series up to 10 terms.

N = 10

print(f"Fibonacci series up to {N} terms:")         # => print("Fibonacci series up to", N, "terms:")

term1 = 0
term2 = 1

if N >= 1:
    print(term1, end=", ")
if N >= 2:
    print(term2, end="")


for i in range(2, N):
    next_term = term1 + term2
    print(f", {next_term}", end="")

    term1 = term2
    term2 = next_term

print("\n--- End of Series ---")


# The f stands for "Formatted string literal," but most people simply call them f-strings.
# F-strings provide a concise, readable, and highly efficient way to embed Python expressions 
# (like variables or calculations) directly inside a string literal.