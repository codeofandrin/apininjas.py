"""
MIT License

Copyright (c) 2024-present Puncher1

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

from typing import TYPE_CHECKING

import finjas.abc
from . import utils

if TYPE_CHECKING:
    from .http import HTTPClient
    from .types.instrument import Crypto as CryptoPayload


# fmt: off
__all__ = (
    "Crypto",
)
# fmt: on


class Crypto(finjas.abc.FinancialInstrument):
    """Represents a cryptocurrency from the Crypto Price API.

    .. container:: operations

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

    def __eq__(self, other: Crypto) -> bool:
        return self.symbol == other.symbol

    def __ne__(self, other: Crypto) -> bool:
        return not self.__eq__(other)

    def _update(self, *, data: CryptoPayload) -> None:
        self.price: float = float(data["price"])
        self._updated = data["timestamp"]

    @utils.copy_doc(finjas.abc.FinancialInstrument.update)
    async def update(self) -> float:
        data = await self._http.get_crypto(symbol=self.symbol)
        self._update(data=data)

        return self.price
