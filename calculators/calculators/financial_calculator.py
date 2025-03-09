
# Use a relative import to import BasicCalculator from basic_calculator in the same directory
from .basic_calculator import BasicCalculator

class FinancialCalculator(BasicCalculator):
    def monthly_interest(self, annual_interest_rate):
        return self.divide(annual_interest_rate, 12)

    def months_from_years(self, years):
        return self.multiply(years, 12)