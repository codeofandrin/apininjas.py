.. currentmodule:: apininjas

:tocdepth: 3

API Reference
==============

This section provides a detailed overview of the API of apininjas.py.


Clients
-------

Client
~~~~~~~

.. attributetable:: Client

.. autoclass:: Client
    :members:


Utilities
------------------

.. autofunction:: apininjas.utils.from_timestamp

.. data:: MISSING
    :module: apininjas.utils

    A type-safe sentinel used within the library to indicate a missing value, distinct from ``None``.


Enumerations
-------------
All enumerations inherit from :class:`enum.Enum`.

CommodityType
~~~~~~~~~~~~~~

.. class:: CommodityType

    Specifies the type of a commodity future.

    .. attribute:: gold

        Gold Futures.

    .. attribute:: soybean_oil

        Soybean Oil Futures.

    .. attribute:: wheat

        Wheat Futures.

    .. attribute:: platinum

        Platinum Futures.

    .. attribute:: micro_silver

        Micro Silver Futures.

    .. attribute:: lean_hogs

        Lean Hogs Futures.

    .. attribute:: corn

        Corn Futures.

    .. attribute:: oat

        Oat Futures.

    .. attribute:: aluminum

        Aluminum Futures.

    .. attribute:: soybean_meal

        Soybean Meal Futures.

    .. attribute:: silver

        Silver Futures.

    .. attribute:: soybean

        Soybean Futures.

    .. attribute:: lumber

        Lumber Futures.

    .. attribute:: live_cattle

        Live Cattle Futures.

    .. attribute:: sugar

        Sugar Futures.

    .. attribute:: natural_gas

        Natural Gas Futures.

    .. attribute:: crude_oil

        Crude Oil Futures.

    .. attribute:: orange_juice

        Orange Juice Futures.

    .. attribute:: coffee

        Coffee Futures.

    .. attribute:: cotton

        Cotton Futures.

    .. attribute:: copper

        Copper Futures.

    .. attribute:: micro_gold

        Micro Gold Futures.

    .. attribute:: feeder_cattle

        Feeder Cattle Futures.

    .. attribute:: rough_rice

        Rough Rice Futures.

    .. attribute:: palladium

        Palladium Futures.

    .. attribute:: cocoa

        Cocoa Futures.

    .. attribute:: brent_crude_oil

        Brent Crude Oil Futures.

    .. attribute:: gasoline_rbob

        Gasoline RBOB Futures.

    .. attribute:: heating_oil

        Heating Oil Futures.

    .. attribute:: class_3_milk

        Class III Milk Futures.

InflationIndicatorType
~~~~~~~~~~~~~~~~~~~~~~~

.. class:: InflationIndicatorType

    Specifies the type of inflation indicator.

    .. attribute:: cpi

        The Consumer Price Index.

    .. attribute:: hicp

        The Harmonized Index of Consumer Prices.

InflationCountry
~~~~~~~~~~~~~~~~~~~~~~~

.. class:: InflationCountry

    Specifies the inflation country.

    .. attribute:: austria

        Austria.

    .. attribute:: belgium

        Belgium.

    .. attribute:: brazil

        Brazil.

    .. attribute:: canada

        Canada.

    .. attribute:: chile

        Chile.

    .. attribute:: china

        China.

    .. attribute:: czech_republic

        Czech Republic.

    .. attribute:: czechia

        Alias of :attr:`czech_republic`.

    .. attribute:: denmark

        Denmark.

    .. attribute:: estonia

        Estonia.

    .. attribute:: finland

        Finland.

    .. attribute:: france

        France.

    .. attribute:: germany

        Germany.

    .. attribute:: greece

        Greece.

    .. attribute:: hungary

        Hungary.

    .. attribute:: iceland

        Iceland.

    .. attribute:: india

        India.

    .. attribute:: indonesia

        Indonesia.

    .. attribute:: ireland

        Ireland.

    .. attribute:: israel

        Israel.

    .. attribute:: italy

        Italy.

    .. attribute:: japan

        Japan.

    .. attribute:: mexico

        Mexico.

    .. attribute:: norway

        Norway.

    .. attribute:: poland

        Poland.

    .. attribute:: portugal

        Portugal.

    .. attribute:: russia

        Russia.

    .. attribute:: slovakia

        Slovakia.

    .. attribute:: slovenia

        Slovenia.

    .. attribute:: south_korea

        South Korea.

    .. attribute:: south_africa

        South Africa.

    .. attribute:: spain

        Spain.

    .. attribute:: sweden

        Sweden.

    .. attribute:: switzerland

        Switzerland.

    .. attribute:: netherlands

        The Netherlands.

    .. attribute:: turkiye

        Türkiye.

    .. attribute:: united_kingdom

        United Kingdom.

    .. attribute:: uk

        Alias of :attr:`united_kingdom`.

    .. attribute:: united_states

        United States.

    .. attribute:: usa

        Alias of :attr:`united_states`.


Abstract Base Classes
----------------------

FinancialInstrument
~~~~~~~~~~~~~~~~~~~~

.. attributetable:: apininjas.abc.FinancialInstrument

.. autoclass:: apininjas.abc.FinancialInstrument
    :members:


Models
-------

Stock
~~~~~~

.. attributetable:: Stock

.. autoclass:: Stock()
    :inherited-members:
    :members:

Commodity
~~~~~~~~~~

.. attributetable:: Commodity

.. autoclass:: Commodity()
    :inherited-members:
    :members:

Crypto
~~~~~~~

.. attributetable:: Crypto

.. autoclass:: Crypto()
    :inherited-members:
    :members:

Currency
~~~~~~~~~

.. attributetable:: Currency

.. autoclass:: Currency()
    :members:

.. class:: CurrencyWithAmount

    A namedtuple which represents a currency with an amount.

    .. attribute:: currency

        The currency.

        :type: :class:`Currency`

    .. attribute:: amount

        The amount.

        :type: :class:`float`

IBANValidation
~~~~~~~~~~~~~~~

.. attributetable:: IBANValidation

.. autoclass:: IBANValidation()
    :members:

Inflation
~~~~~~~~~~~~~~~

.. attributetable:: Inflation

.. autoclass:: Inflation()
    :members:


Exceptions
-----------

.. autoexception:: APINinjasBaseException

.. autoexception:: ClientException

.. autoexception:: HTTPException
    :members:

.. autoexception:: NotFound

.. autoexception:: MethodNotAllowed

.. autoexception:: APINinjasServerError

.. autoexception:: StockNotFound

Exception Hierarchy
~~~~~~~~~~~~~~~~~~~~

.. exception_hierarchy::

    - :exc:`APINinjasBaseException`
        - :exc:`ClientException`
            - :exc:`StockNotFound`
        - :exc:`HTTPException`
            - :exc:`NotFound`
            - :exc:`MethodNotAllowed`
            - :exc:`APINinjasServerError`
