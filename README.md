# Overview
This program is a graphic user interface which allows the user to grab data on desired stocks and store that data in a wanted number of .csv files. The advantage of these files is that after aquired, they can be opened in a system such as Microsoft Excel or Google Spreadsheets. This program is useful for aquiring data of a variety of stocks for a trader.

##### WHEN SETTING UP, MUST CHANGE THE PATH OF FILE CREATION IN LINE 31 OF StockProgram.py TO DESIRED FOLDER, WHILE STILL RETAINING THE +"\\output"+str(x+1)+".csv" AT END OF PATH.
##### The format of output is {"assetType","assetMainType","cusip","assetSubType","symbol","description","bidPrice":28.74,"bidSize":1300,"bidId":"P","askPrice,"askSize","askId","lastPrice","lastSize","lastId","openPrice","highPrice","lowPrice","bidTick","closePrice","netChange","totalVolume","quoteTimeInLong","tradeTimeInLong","mark","exchange","exchangeName","marginable","shortable","volatility","digits","52WkHigh","52WkLow","nAV","peRatio","divAmount","divYield","divDate","securityStatus","regularMarketLastPrice","regularMarketLastSize","regularMarketNetChange","regularMarketTradeTimeInLong","netPercentChangeInDouble","markChangeInDouble","markPercentChangeInDouble","regularMarketPercentChangeInDouble","delayed","dateAndTime"}.

##### OUTPUT WILL INCLUDE "assetSubType" ONLY IF AT LEAST ONE OF ENTERED STOCKS HAVE IT AS A VALID ATTRIBUTE

##### An example of the values of these labels can be found at https://api.tdameritrade.com/v1/marketdata/quotes?apikey=JITOXNVGAC9TICFWUG4VTPS3ZIRQEDE4&symbol=T

## Files
### software.py
This is the file that is actually run, and will result in a GUI opening on the screen. The symbols of the desired stocks should be entered, each separated by commas with or without spaces (Ex. "T, GOOG, MSFT"), in the corresponding entry box. The other box is for the number of output files desired, which will all contain information on every stock entered on subsequent lines.
### StockProgram.py
This contains the function that accesses the API, obtaining the stock data. It then creates files that contains that data. *WHEN SETTING UP, MUST CHANGE THE PATH OF FILE CREATION IN LINE 31 TO DESIRED FOLDER, WHILE STILL RETAINING THE +"\\output"+str(x+1)+".csv" AT END OF PATH*.
### ExampleOutput.csv
This is an example of an outputted file with input of stock symbols "GOOG, T, UMC", and the creation of a single output file.
