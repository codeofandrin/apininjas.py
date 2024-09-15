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


Utility Functions
------------------

.. autofunction:: apininjas.utils.from_timestamp


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

.. autoclass:: Stock
    :inherited-members:
    :members:

Commodity
~~~~~~~~~~

.. attributetable:: Commodity

.. autoclass:: Commodity
    :inherited-members:
    :members:

Crypto
~~~~~~~

.. attributetable:: Crypto

.. autoclass:: Crypto
    :inherited-members:
    :members:

Currency
~~~~~~~~~

.. attributetable:: Currency

.. autoclass:: Currency
    :members:

.. class:: CurrencyWithAmount

    A namedtuple which represents a currency with an amount.

    .. attribute:: currency

        The currency.

        :type: :class:`Currency`

    .. attribute:: amount

        The amount.

        :type: :class:`float`


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
