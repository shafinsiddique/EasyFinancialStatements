class Compare:
    def __init__(self, c1, c2):
        self.company1 = c1
        self.company2 = c2

    def _greater(self, type, rationame):
        """Return the company with the greater ratio."""

        if self.company1.getallratios()[type][rationame] > \
            self.company2.getallratios()[type][rationame]:
            return self.company1.getprofile['companyName']

        elif self.company2.getallratios()[type][rationame] > \
            self.company1.getallratios()[type][rationame]:
            return self.company2.getallratios['companyName']

        else:
            return 'equal'

    def _less(self, type, rationame):
        if self.company1.getallratios()[type][rationame] < \
                self.company2.getallratios()[type][rationame]:
            return self.company1.getprofile['companyName']

        elif self.company2.getallratios()[type][rationame] < \
                self.company1.getallratios()[type][rationame]:
            return self.company2.getallratios['companyName']

        else:
            return 'equal'


    def compareliquidity(self):
        typer = 'liquidityMeasurementRatios'

        ratios = {'currentRatio':self._greater(typer, 'currentRatio'),
                  'quickRatio': self._greater(typer, 'quickRatio'),
                  'cashRatio': self._greater(typer,'cashRatio'),
                  'daysofSalesOutstanding':
                      self._less(typer,
                                                       'daysofSalesOutstanding'),
                  'daysofInventoryOutstanding':
                      self._less(typer, 'daysofInventoryOutstanding'),
                  'dayofPayablesOutstanding': 'equal',
                  'operatingCycle':self._less(typer, 'operatingCycle'),
                  'cashConversionCycle': self._less(typer, 'cashConversionCycle')}


        return ratios


    def compareprofit(self):
        typer = 'profitabilityIndicatorRatios'

        ratios = {'grossProfitMargin':
                      self._greater(typer, 'grossProfitMargin'),
                  'operatingProfitMargin':
                      self._greater(typer,
                        'operatingProfitMargin'),

                  'pretaxProfitMargin': self._greater(typer, 'pretaxProfitMargin'),
                  'netProfitMargin':
                      self._greater(typer,
                                 'netProfitMargin'),
                  'effectiveTaxRate':
                      self._greater(typer, 'effectiveTaxRate'),
                  'returnOnAssets': self._greater(typer, 'returnOnAssets'),
                  'returnOnEquity': self._greater(typer, 'returnOnEquity'),
                  'returnOnCapitalEmployed':
                      self._greater(typer, 'returnOnCapitalEmployed')}

        return ratios

    def compareall(self):
        all_ratios = {}


        for ratios in self.compareliquidity():
            all_ratios[ratios] = self.compareliquidity()[ratios]

        for ratios in self.compareprofit():
            all_ratios[ratios] = self.compareliquidity()[ratios]

        return all_ratios
