def div(divisor, divident):
    quotient = divisor / divident
    return quotient

divisor = int(input("Enter a divisor: "))
while True:
    divident = int(input("Enter a divident: "))
    if divident != 0: break

print(div(divisor, divident))