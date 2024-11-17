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

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Optional, Union, NamedTuple

import apininjas.abc
from .enums import CommodityType, InflationIndicatorType, InflationCountry
from . import utils

if TYPE_CHECKING:
    from .http import HTTPClient
    from .types.finance import (
        Stock as StockPayload,
        Commodity as CommodityPayload,
        Gold as GoldPayload,
        Crypto as CryptoPayload,
        IBANValidation as IBANValidationPayload,
        Inflation as InflationPayload,
    )


# fmt: off
__all__ = (
    "Stock",
    "Crypto",
    "Commodity",
    "Currency",
    "IBANValidation",
    "Inflation",
)
# fmt: on


class Stock(apininjas.abc.FinancialInstrument):
    """Represents a stock from the Stock Price API.

    .. container:: operations

        .. describe:: str(x)

            Returns the stock's name.

        .. describe:: x == y

            Checks if two stocks are equal.

        .. describe:: x != y

            Checks if two stocks are not equal.

        .. describe:: x < y

            Checks if a stock's price is less than another.

        .. describe:: x > y

            Checks if a stock's price is greater than another.

        .. describe:: x <= y

            Checks if a stock's price is less or equal than another.

        .. describe:: x >= y

            Checks if a stock's price is greater or equal than another.

    Attributes
    -----------
    ticker: :class:`str`
        The stock's ticker symbol.
    name: :class:`str`
        The stock's name.
    exchange: Optional[:class:`str`]
        The stock exchange the stock is traded on. ``None`` if it's not an exchange for stocks.
    price: :class:`float`
        The current price of the stock, last updated at :attr:`.updated_at`.
    """

    __slots__ = ("_http", "ticker", "name", "price", "exchange", "_updated")

    def __init__(self, *, http: HTTPClient, data: StockPayload):
        self._http = http
        self.ticker: str = data["ticker"]
        self.name: str = data["name"]
        self.exchange: Optional[str] = None

        exchange = data["exchange"]
        if exchange not in ["COMMODITY", "CRYPTO"]:
            self.exchange = exchange

        self._update(data=data)

    def __repr__(self) -> str:
        attrs = [
            ("ticker", self.ticker),
            ("name", self.name),
            ("exchange", self.exchange),
        ]
        joined = " ".join([f"{a}={v!r}" for a, v in attrs])
        return f"<Stock {joined}>"

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other: Stock) -> bool:
        return self.ticker == other.ticker

    def __ne__(self, other: Stock) -> bool:
        return not self.__eq__(other)

    def _update(self, *, data: StockPayload) -> None:
        self.price: float = data["price"]
        self._updated = data["updated"]

    @utils.copy_doc(apininjas.abc.FinancialInstrument.update)
    async def update(self) -> float:
        data = await self._http.get_stock(ticker=self.ticker)
        self._update(data=data)

        return self.price


class Commodity(apininjas.abc.FinancialInstrument):
    """Represents a commodity future from the Commodity Price API or the Gold Price API.

    .. container:: operations

        .. describe:: str(x)

            Returns the name of the commodity future.

        .. describe:: x == y

            Checks if two commodity futures are equal.

        .. describe:: x != y

            Checks if two commodity futures are not equal.

        .. describe:: x < y

            Checks if the price of a commodity future is less than the one of another.

        .. describe:: x > y

            Checks if the price of a commodity future is greater than the one of another.

        .. describe:: x <= y

            Checks if the price of a commodity future is less or equal than the one of another.

        .. describe:: x >= y

            Checks if the price of a commodity future is greater or equal than the one of another.

    Attributes
    -----------
    name: :class:`str`
        The name of the commodity future.
    exchange: :class:`str`
        The exchange the commodity future is traded on.
    price: :class:`float`
        The current price of the commodity future, last updated at :attr:`.updated_at`.
    type: :class:`CommodityType`
        The type of the commodity future.
    """

    __slots__ = ("_http", "name", "price", "exchange", "type", "_updated")

    def __init__(self, *, http: HTTPClient, type: CommodityType, data: Union[GoldPayload, CommodityPayload]):
        self._http = http
        self.type: CommodityType = type

        self.name: str
        self.exchange: str
        if type == CommodityType.gold:
            self.name = "Gold Futures"
            self.exchange = "CME"
        else:
            self.name: str = data["name"]  # type: ignore # can't be gold payload here
            self.exchange: str = data["exchange"]  # type: ignore # can't be gold payload here

        self._update(data=data)

    def __repr__(self) -> str:
        attrs = [
            ("name", self.name),
            ("exchange", self.exchange),
            ("type", self.type),
        ]
        joined = " ".join([f"{a}={v!r}" for a, v in attrs])
        return f"<Commodity {joined}>"

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other: Commodity) -> bool:
        return self.type == other.type

    def __ne__(self, other: Commodity) -> bool:
        return not self.__eq__(other)

    def _update(self, *, data: Union[GoldPayload, CommodityPayload]) -> None:
        self.price: float = data["price"]
        self._updated = data["updated"]

    @utils.copy_doc(apininjas.abc.FinancialInstrument.update)
    async def update(self) -> float:
        data = await self._http.get_commodity(name=self.type.value)
        self._update(data=data)

        return self.price


class Crypto(apininjas.abc.FinancialInstrument):
    """Represents a cryptocurrency from the Crypto Price API.

    .. container:: operations

        .. describe:: str(x)

            Returns the cryptocurrency's symbol.

        .. describe:: x == y

            Checks if two cryptocurrencies are equal.

        .. describe:: x != y

            Checks if two cryptocurrencies are not equal.

        .. describe:: x < y

            Checks if a cryptocurrency's price is less than another.

        .. describe:: x > y

            Checks if a cryptocurrency's price is greater than another.

        .. describe:: x <= y

            Checks if a cryptocurrency's price is less or equal than another.

        .. describe:: x >= y

            Checks if a cryptocurrency's price is greater or equal than another.

    Attributes
    -----------
    symbol: :class:`str`
        The cryptocurrency's symbol.
    price: :class:`float`
        The current price of the cryptocurrency, last updated at :attr:`.updated_at`.
    """

    __slots__ = ("_http", "symbol", "price", "_updated")

    def __init__(self, *, http: HTTPClient, data: CryptoPayload):
        self._http = http
        self.symbol: str = data["symbol"]
        self._update(data=data)

    def __repr__(self) -> str:
        return f"<Crypto symbol={self.symbol}>"

    def __str__(self) -> str:
        return self.symbol

    def __eq__(self, other: Crypto) -> bool:
        return self.symbol == other.symbol

    def __ne__(self, other: Crypto) -> bool:
        return not self.__eq__(other)

    def _update(self, *, data: CryptoPayload) -> None:
        self.price: float = float(data["price"])
        self._updated = data["timestamp"]

    @utils.copy_doc(apininjas.abc.FinancialInstrument.update)
    async def update(self) -> float:
        data = await self._http.get_crypto(symbol=self.symbol)
        self._update(data=data)

        return self.price


class Currency:
    """Represents a currency from the Exchange Rate API or Currency Conversion API.

    .. container:: operations

        .. describe:: str(x)

            Returns the currency's name.

        .. describe:: x == y

            Checks if two currencies are equal.

        .. describe:: x != y

            Checks if two currencies are not equal.

    Attributes
    -----------
    name: :class:`str`
        The name of the currency.
    exchange_rate: :class:`float`
        The exchange rate relative to the :attr:`reference` currency.
    reference: :class: `str`
        The name of the reference currency.
    """

    __slots__ = ("_http", "name", "reference", "exchange_rate")

    def __init__(self, *, http: HTTPClient, name: str, exchange_rate: float, reference: str):
        self._http: HTTPClient = http
        self.name: str = name
        self.reference: str = reference
        self._update(exchange_rate=exchange_rate)

    def __repr__(self) -> str:
        attrs = [
            ("name", self.name),
            ("reference", self.reference),
        ]
        joined = " ".join([f"{a}={v!r}" for a, v in attrs])
        return f"<Currency {joined}>"

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other: Currency) -> bool:
        return self.name == other.name and self.reference == other.reference

    def __ne__(self, other: Currency) -> bool:
        return not self.__eq__(other)

    def _update(self, *, exchange_rate: float) -> None:
        self.exchange_rate: float = exchange_rate

    def is_stronger(self) -> bool:
        """:class:`bool`: Whether the currency is stronger (more valuable) than its :attr:`reference`."""
        return self.exchange_rate < 1

    async def update(self) -> float:
        """|coro|

        Updates :attr:`exchange_rate` of the current object and returns the new exchange rate.

        .. note::

            This makes an API call.

        Raises
        -------
        HTTPException
            Retrieving the exchange rate failed.

        Returns
        --------
        :class:`float`
            The newly updated exchange rate.
        """
        pair = f"{self.reference}_{self.name}"
        data = await self._http.get_exchange_rate(pair=pair)
        self._update(exchange_rate=data["exchange_rate"])

        return self.exchange_rate


class CurrencyWithAmount(NamedTuple):
    currency: Currency
    amount: float


class CurrencyConversion(NamedTuple):
    old: CurrencyWithAmount
    new: CurrencyWithAmount


class IBANValidation:
    """Represents an International Bank Account Number (IBAN) validation from the IBAN API.

    .. container:: operations

        .. describe:: str(x)

            Returns the IBAN.

        .. describe:: x == y

            Checks if two IBANs are equal.

        .. describe:: x != y

            Checks if two IBANs are not equal.

    Attributes
    -----------
    iban: :class:`str`
        The IBAN.
    bank_name: :class:`str`
        The bank's name, which the IBAN belongs to.
    account_number: :class:`str`
        The account number from the IBAN.
    bank_code: :class:`str`
        The bank code from the IBAN.
    country_code: :class:`str`
        The country code from the IBAN.
    checksum: :class:`str`
        The checksum from the IBAN.
    bban: :class:`str`
        The Basic Bank Account Number (BBAN) from the IBAN.
    valid: :class:`bool`
        Whether the IBAN is valid or not.

        .. note::

            This only includes the IBAN checksum validation.
    """

    __slots__ = (
        "iban",
        "bank_name",
        "account_number",
        "bank_code",
        "country_code",
        "checksum",
        "bban",
        "valid",
    )

    def __init__(self, *, data: IBANValidationPayload):
        self.iban: str = data["iban"]
        self.bank_name: str = data["bank_name"]
        self.account_number: str = data["account_number"]
        self.bank_code: str = data["bank_code"]
        self.country_code: str = data["country"]
        self.checksum: str = data["checksum"]
        self.bban: str = data["bban"]
        self.valid: bool = data["valid"]

    def __repr__(self) -> str:
        attrs = [
            ("iban", self.iban),
            ("bank_name", self.bank_name),
            ("valid", self.valid),
        ]
        joined = " ".join([f"{a}={v!r}" for a, v in attrs])
        return f"<IBANValidation {joined}>"

    def __str__(self) -> str:
        return self.iban

    def __eq__(self, other: IBANValidation) -> bool:
        return self.iban == other.iban

    def __ne__(self, other: IBANValidation) -> bool:
        return not self.__eq__(other)

    def is_valid(self) -> bool:
        """:class:`bool`: Checks whether the IBAN is valid or not.

        .. note::

            This only includes the IBAN checksum validation.
        """
        return self.valid


class Inflation:
    """Represents the inflation of a country from the Inflation API.

    .. container:: operations

        .. describe:: x == y

            Checks if two inflations are equal.

        .. describe:: x != y

            Checks if two inflations are not equal.

    Attributes
    -----------
    country: :class:`str`
        The country to which the inflation belongs.
    type: :class:`InflationIndicatorType`
        The type of inflation indicator.
    monthly_rate: :class:`float`
        The inflation rate on a monthly basis, in percent.
    yearly_rate: :class:`float`
        The inflation rate on a yearly basis, in percent.
    """

    __slots__ = ("country", "type", "monthly_rate", "yearly_rate", "_period")

    def __init__(self, *, data: InflationPayload):
        self.country: InflationCountry = InflationCountry(data["country"])
        self.type: InflationIndicatorType = InflationIndicatorType(data["type"])
        self.monthly_rate: float = data["monthly_rate_pct"]
        self.yearly_rate: float = data["yearly_rate_pct"]
        self._period: str = data["period"]

    def __repr__(self) -> str:
        attrs = [
            ("country", self.country),
            ("type", self.type),
        ]
        joined = " ".join([f"{a}={v!r}" for a, v in attrs])
        return f"<Inflation {joined}>"

    def __eq__(self, other: Inflation) -> bool:
        return self.country == other.country and self.type == other.type and self.period == other.period

    def __ne__(self, other: Inflation) -> bool:
        return not self.__eq__(other)

    @property
    def period(self) -> datetime.datetime:
        """:class:`datetime.datetime`: The time period for the inflation data."""
        return datetime.datetime.strptime(self._period, "%b %Y")

    def is_monthly_increased(self) -> bool:
        """:class:`bool`: Whether the monthly inflation rate increased."""
        return self.monthly_rate > 0

    def is_yearly_increased(self) -> bool:
        """:class:`bool`: Whether the yearly inflation rate increased."""
        return self.yearly_rate > 0
