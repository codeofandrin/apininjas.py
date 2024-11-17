"""
MIT License

Copyright (c) 2024-present codeofandrin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from typing import TypedDict, List, Literal


class Gold(TypedDict):
    price: float
    updated: int


class Stock(TypedDict):
    ticker: str
    name: str
    exchange: str
    price: float
    updated: int


class Commodity(TypedDict):
    name: str
    exchange: str
    price: float
    updated: int


class Crypto(TypedDict):
    symbol: str
    price: str
    timestamp: int


class CryptoSymbols(TypedDict):
    symbols: List[str]


class CurrencyConversion(TypedDict):
    old_amount: float
    old_currency: str
    new_amount: float
    new_currency: str


class ExchangeRate(TypedDict):
    currency_pair: str
    exchange_rate: float


class IBANValidation(TypedDict):
    iban: str
    bank_name: str
    account_number: str
    bank_code: str
    country: str
    checksum: str
    valid: bool
    bban: str


class Inflation(TypedDict):
    country: str
    type: Literal["CPI", "HICP"]
    period: str
    monthly_rate_pct: float
    yearly_rate_pct: float
