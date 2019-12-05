class PresentValueCalculator():
    futureValue = None
    annualInterestRate = None
    numberOfYears = None

    def __init__(self, futureValue, annualInterestRate, numberOfYears):
        self.futureValue = futureValue
        self.annualInterestRate = annualInterestRate
        self.numberOfYears = numberOfYears

    def calculate(self):
        print('>>\tPresent Value:\t\t\t', self.futureValue /
              ((1 + self.annualInterestRate)**self.numberOfYears))


futureValue = int(input('>>\tEnter the future value:\t\t'))
annualInterestRate = float(input('>>\tEnter the interest rate:\t'))
numberOfYears = int(input('>>\tEnter the number of years:\t'))

presentValueClc = PresentValueCalculator(
    futureValue, annualInterestRate, numberOfYears)
presentValueClc.calculate()
