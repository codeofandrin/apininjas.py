.. currentmodule:: apinjas

Quickstart
===========

This page gives you a brief introduction to the library.
If you don't have the library installed yet, check :doc:`install` first.


Minimal example
----------------

Let's make our first API interaction. For this example we want to get a stock from the
`Stock Price API <https://api-ninjas.com/api/stockprice>`_.

First, create a file called ``main.py`` and add following code (explanation below):

.. code-block:: python3

    import asyncio
    from apininjas import Client

    async def main():
        async with Client("your_api_key") as client:
            stock = await client.fetch_stock("AAPL")
            print(f"{stock.name} is trading at ${stock.price}")

    if __name__ == "__main__":
        asyncio.run(main())

It's a really basic example, but let's have a look what happens here:

1. First lines imports :py:mod:`asyncio` and the :class:`.Client` to interact with the API.
2. Inside the ``main`` function we create our :class:`.Client` with our API key as a context manager.
3. After that, we retrieve the :class:`.Stock` with ticker ``AAPL`` via the :meth:`~.Client.fetch_stock` method.
4. We then print out the :attr:`~.Stock.name` and :attr:`~.Stock.price` of the stock.
5. Finally we execute our ``main`` coroutine with :py:func:`asyncio.run`.

|

Now let's run the script.

On Linux/MacOS, use

.. code-block:: shell

    python3 main.py

On Windows, use

.. code-block:: shell

    py -3 main.py

This should output something like this ::

    Apple Inc. is trading at $220.11
