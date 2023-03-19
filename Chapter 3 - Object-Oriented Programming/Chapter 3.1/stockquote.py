#-----------------------------------------------------------------------
# stockquote.py
#-----------------------------------------------------------------------

import sys
import stdio
from instream import InStream

#-----------------------------------------------------------------------

# Return the raw HTML from the website http://finance.yahoo.com

def _readHTML(stockSymbol):
    WEBSITE = 'https://www.marketwatch.com/investing/stock/'
    page = InStream(WEBSITE+stockSymbol)
    html = page.readAll()
    return html

#-----------------------------------------------------------------------

# Extract the current stock price of the stock whose symbol is 
# stockSymbol from the HTML and return it.
#<meta name="price" content="$101.62" />
def priceOf(stockSymbol):
    html  = _readHTML(stockSymbol)
    trade = html.find('<meta name="price"', 0)
    beg   = html.find('t="', trade)
    end   = html.find('" />', beg)
    price = html[beg+4:end]
    return float(price)

#-----------------------------------------------------------------------

# Accept string stockSymbol as a command-line argument. Write to
# standard output the current stock price for stockSymbol, as reported
# by the website http://finance.yahoo.com/.

def main():
    stockSymbol = 'amc'
    price = priceOf(stockSymbol)
    stdio.writef('%.2f\n', price)

if __name__ == '__main__':
    main()
