class Compare:
    def __init__(self, c1, c2):
        self.company1 = c1
        self.company2 = c2

    def _greater(self, type, rationame):
        """Return the company with the greater ratio."""

        try:
            if self.company1.getallratios()[type][rationame] > \
            self.company2.getallratios()[type][rationame]:
                return self.company1.getprofile()['companyName']

            elif self.company2.getallratios()[type][rationame] > \
                self.company1.getallratios()[type][rationame]:
                return self.company2.getprofile()['companyName']

            else:
                return 'equal'
        except:
            return 'equal'

    def _less(self, type, rationame):
        try:
            if self.company1.getallratios()[type][rationame] < \
                    self.company2.getallratios()[type][rationame]:
                return self.company1.getprofile()['companyName']

            elif self.company2.getallratios()[type][rationame] < \
                    self.company1.getallratios()[type][rationame]:
                return self.company2.getprofile()['companyName']

            else:
                return 'equal'

        except:
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


    def comparedebt(self):
        typer = "debtRatios"

        ratios = {'debtRatio':
                      self._less(typer, 'debtRatio'),
                  'debtEquityRatio':
                      self._less(typer,
                                    'debtEquityRatio'),

                  'longtermDebtToCapitalization':
                      self._less(typer,
                                                                'longtermDebtToCapitalization'),
                  'totalDebtToCapitalization':
                      self._less(typer,
                                    'totalDebtToCapitalization'),
                  'interestCoverageRatio':
                      self._greater(typer, 'interestCoverageRatio'),
                  'cashFlowToDebtRatio': self._greater(typer, 'cashFlowToDebtRatio'),
                  'companyEquityMultiplier':
                      self._less(typer, 'companyEquityMultiplier')}

        return ratios

    def comparecashflow(self):
        typer = "cashFlowIndicatorRatios"

        ratios = {'operatingCashFlowSalesRatio':
                      self._less(typer, 'operatingCashFlowSalesRatio'),
                  'freeCashFlowOperatingCashFlowRatio':
                      self._less(typer,
                                 'freeCashFlowOperatingCashFlowRatio'),

                  'cashFlowCoverageRatios':
                      self._less(typer,
                                 'cashFlowCoverageRatios'),
                  'shortTermCoverageRatios':
                      self._less(typer,
                                 'shortTermCoverageRatios'),
                  'capitalExpenditureCoverageRatios':
                      self._greater(typer, 'capitalExpenditureCoverageRatios')}
        return ratios

    def compareinvestment(self):
        typer = "investmentValuationRatios"

        ratios = {'priceBookValueRatio':
                      self._less(typer, 'priceBookValueRatio'),
                  'priceCashFlowRatio':
                      self._less(typer,
                                 'priceCashFlowRatio'),

                  'priceEarningsRatio':
                      self._less(typer,
                                 'priceEarningsRatio'),
                  'priceEarningsToGrowthRatio':
                      self._less(typer,
                                 'priceEarningsToGrowthRatio'),
                  'dividendYield':
                      self._greater(typer, 'dividendYield'),
                  'enterpriseValueMultiple':
                      self._less(typer,
                                 'enterpriseValueMultiple'),
                  'priceFairValue':
                      self._less(typer,
                                 'priceFairValue'),
                  'priceSalesRatio':
                  self._less(typer, 'priceSalesRatio')}
        return ratios

    def compareoperating(self):
        typer = "operatingPerformanceRatios"

        ratios = {'fixedAssetTurnover':
                      self._greater(typer, 'fixedAssetTurnover'),
                  'assetTurnover':
                      self._greater(typer,
                                 'assetTurnover')}
        return ratios

    def winner_section(self, d):
        comp1 = 0
        comp2 = 0

        for ratios in d:
            if d[ratios] == \
                self.company1.getprofile()['companyName']:
                comp1 += 1

            elif d[ratios] == self.company2.getprofile()['companyName']:
                comp2 += 1

            else:
                comp1 +=1
                comp2 += 1

        if comp1 > comp2:
            return self.company1.getprofile()['companyName']

        elif comp2 > comp1:
            return self.company2.getprofile()['companyName']

        else:
            return 'tie'


    def compareall(self):
        all_ratios = {}


        for ratios in self.compareliquidity():
            all_ratios[ratios] = self.compareliquidity()[ratios]

        for ratios in self.compareprofit():
            all_ratios[ratios] = self.compareprofit()[ratios]


        for ratios in self.comparedebt():
            all_ratios[ratios] = self.comparedebt()[ratios]

        for ratios in self.comparecashflow():
            all_ratios[ratios] = self.comparecashflow()[ratios]

        for ratios in self.compareinvestment():
            all_ratios[ratios] = self.compareinvestment()[ratios]


        for ratios in self.compareoperating():
            all_ratios[ratios] = self.compareoperating()[ratios]

        all_ratios['winner_profit'] = \
            self.winner_section(self.compareprofit())
        all_ratios['winner_debt'] = \
            self.winner_section(self.comparedebt())

        all_ratios['winner_cash'] = \
            self.winner_section(self.comparecashflow())

        all_ratios['winner_liquidity'] = \
            self.winner_section(self.compareliquidity())

        all_ratios['winner_investment'] = \
            self.winner_section(self.compareinvestment())

        all_ratios['winner_operating'] = \
            self.winner_section(self.compareoperating())

        return all_ratios




if __name__ == "__main__":
    pass