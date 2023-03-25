#biggest winner and looser

from stockaccount import StockAccount
from instream import InStream
from outstream import OutStream
import stdarray
#assume all accounts are in one file one after the other in the given format





instream = InStream('accounts.txt')
stockaccounts = []
i = 1
while instream.hasNextLine():
    name = instream.readLine()
    cash = instream.readLine()
    stockCount = instream.readLine()
    stocks = instream.readLine()
    out = OutStream('test_account.txt')
    out.writeln(name)
    out.writeln(cash)
    out.writeln(stockCount)
    out.writeln(stocks)