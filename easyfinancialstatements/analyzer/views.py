from django.shortcuts import render, redirect
from . import CompanyRatio
from .forms import CompanyForm
from .compare import Compare


def _getcontext(c1, c2):
    """Return the dictionary that contains all the informaiton,"""
    comp = Compare(c1, c2)

    v1 = False
    v2 = False

    if float(c1.getprofile()['Changes']) > 0:
        v1 = True

    if float(c2.getprofile()['Changes']) > 0:
        v2 = True
    context = {
                'Company1': {
                    'company_name': c1.getprofile()['companyName'],
                    'profitability_ratios': c1.getallratios()
                    ['profitabilityIndicatorRatios'],
                    'liquidity_ratios' : c1.getallratios()
                    ['liquidityMeasurementRatios'],
                    'debt_ratios': c1.getallratios()['debtRatios'],
                    'operating_performance':
                        c1.getallratios()['operatingPerformanceRatios'],
                    'cashflow_indicator':c1.getallratios()
                    ['cashFlowIndicatorRatios'],
                    'investment_valuation':
                        c1.getallratios()['investmentValuationRatios'],
                    'price': c1.getprofile()['Price'],
                    'description': c1.getprofile()['description'],
                    'picture': c1.getprofile()['image'],
                    'profile': c1.getprofile(),
                    'changes': v1
                },
                'Company2': {
                    'company_name': c2.getprofile()['companyName'],
                    'profitability_ratios': c2.getallratios()
                    ['profitabilityIndicatorRatios'],
                    'liquidity_ratios' : c2.getallratios()
                    ['liquidityMeasurementRatios'],
                    'debt_ratios': c2.getallratios()['debtRatios'],
                    'operating_performance':
                        c2.getallratios()['operatingPerformanceRatios'],
                    'cashflow_indicator':c2.getallratios()
                    ['cashFlowIndicatorRatios'],
                    'investment_valuation':
                        c2.getallratios()['investmentValuationRatios'],
                'price': c2.getprofile()['Price'],
                'description': c2.getprofile()['description'],
                'picture': c2.getprofile()['image'],
                'profile': c2.getprofile(),
                'changes': v2},

    'winner': comp.compareall()}


    return context


def home(requests):
    """views for the home page of the site."""

    if requests.method == "POST":
        return compare(requests)

    else:
        form = CompanyForm()
        return render(requests, 'analyzer/home.html', context={"form": form})


def compare(requests):
    """views for the comparison page of the site."""


    if requests.method == "POST":
        form = CompanyForm(requests.POST)

        if form.is_valid():
            company1 = form.cleaned_data['company_1']
            company2 = form.cleaned_data['company_2']

            c1 = CompanyRatio.CompanyInformation(company1)
            c2 = CompanyRatio.CompanyInformation(company2)

            return render(requests, 'analyzer/compare.html',
                          _getcontext(c1, c2))

    else:

        return home(requests)
