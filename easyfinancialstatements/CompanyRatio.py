import requests
CURRENT_DATE = "2018-09"
class CompanyInformation:
    def __init__(self, ticker):
        self.ticker = ticker
        self.ratios = requests.get("https://financialmodelingprep.com/"
                                   "api/financial-ratios/" + ticker +
                                   "?datatype=json").json()
        self.profile = requests.get("https://financialmodelingprep.com/api/company/" \
                       "profile/" + ticker + "?datatype=json").json()

        self.dates = [*self.ratios['financialRatios']]
    def getprofile(self) -> dict:
        """Return a dictionary of the company's profile."""
        return self.profile[self.ticker]

    def getallratios(self) -> None:
        """Return a dictionary of all the financial ratios."""
        _cleandictionary(self.ratios['financialRatios'][self.dates[-2]])

        return self.ratios['financialRatios'][self.dates[-2]]

    def getratio(self, ratiotype) -> dict:
        """Return ratios of only the given type."""
        return self.ratios['financialRatios'][self.dates[-2]][ratiotype]

def _cleandictionary(d: dict) -> None:
    """Make sure all the values in the dictionary are rounded to 2 decimal points.
    """
    for ratiotypes in d:
        for ratios in d[ratiotypes]:
            try:
                d[ratiotypes][ratios] = round(d[ratiotypes][ratios], 2)
            except:
                pass

c = CompanyInformation("GOOG")
print(c.ratios['financialRatios'])
# print(c.getratio('liquidityMeasurementRatios'))
print(c.getratio("liquidityMeasurementRatios"))