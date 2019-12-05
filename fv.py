class FutureValueCalculator():
    presentValue = None
    annualInterestRate = None
    numberOfYears = None

    def __init__(self, presentValue, annualInterestRate, numberOfYears):
        self.presentValue = presentValue
        self.annualInterestRate = annualInterestRate
        self.numberOfYears = numberOfYears

    def calculate(self):
        print('>>\tFuture Value:\t\t\t', self.presentValue *
              (1 + self.annualInterestRate)**self.numberOfYears)


presentValue = int(input('>>\tEnter the present value:\t'))
annualInterestRate = float(input('>>\tEnter the interest rate:\t'))
numberOfYears = int(input('>>\tEnter the number of years:\t'))

futureValueClc = FutureValueCalculator(
    presentValue, annualInterestRate, numberOfYears)
futureValueClc.calculate()
