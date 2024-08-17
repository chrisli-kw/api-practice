import re


class CheckData:
    @staticmethod
    def isEnglish(name: str):
        '''Check if name contains non-English characters'''
        return ''.join(re.findall('[A-Za-z ]', name)) == name

    @staticmethod
    def isTitle(name: str):
        '''Check if name is capitalized'''
        return name.istitle()

    @staticmethod
    def isPriceLow(price: float):
        '''Check if price <= 2000'''

        if isinstance(price, str):
            price = float(price)
        return price <= 2000

    @staticmethod
    def currency_(currency: str):
        '''Check if currency is TWD/USD'''
        return currency in ['TWD', 'USD']


class ConvertData:
    @staticmethod
    def currency(data: dict):
        '''
        If currency is USD, multiply price by 31 and change 'currency' to TWD
        '''

        if data['currency'] == 'USD':
            data['price'] *= 31
            data['currency'] = 'TWD'
        return data
