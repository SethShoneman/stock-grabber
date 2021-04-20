import requests
import json
from datetime import datetime

def stockFunc(num,stocks):
    for x in range(int(num)):
        #gets data from API
        url = "https://api.tdameritrade.com/v1/marketdata/quotes?apikey=JITOXNVGAC9TICFWUG4VTPS3ZIRQEDE4&symbol="+stocks
        querystring = {"region":"US","lang":"en"}
        response = requests.request("GET", url, params=querystring)

        #puts data into a usable form
        data=json.loads(response.text)

        #records all stocks requested to loop through
        stockList = []
        for stock in data:
            stockList.append(stock)

        values = []

        # check for if an offset exists
        offsetError = False
        for symbol in stockList:
            elementNum = 1
            for val in data[symbol].keys():
                if(elementNum == 4 and val == "symbol"):
                    offsetError = True
                elementNum += 1

        # initially populates value two dimensional array with titles for easier csv reading
        stockTitles = []
        elementNum = 1
        for val in data[stockList[0]].keys():
            if(offsetError and elementNum == 4 and val == "symbol"):
                stockTitles.append("assetSubType")
            stockTitles.append(val)
            elementNum += 1
        values.append(stockTitles)


        # gets all stock values contained together, separated by stock, into a list
        for symbol in stockList:
            stockValues = []
            for val in data[symbol].values():
                stockValues.append(val)
            values.append(stockValues)

        #changes name of file
        name = 'C:\\Users\\sidda\\Documents\\ameritrade\\outputFiles'+"\\output"+str(x+1)+".csv"
        print(name)

        #writes final values to a csv file, initially creating a title row for easier use
        with open(name, 'w') as f:
            for title in values[0]:
                f.write("\"" + str(title) + "\",")
            f.write("\"dateAndTime\"")
            f.write("\n")
            for row in values[1:]:
                elementNum2 = 1
                for val in row:
                    # N/A if doesnt have assetSubtype to correct for offset
                    if(val == "" or val == " "):
                        f.write("\"N/A\",")
                    elif(offsetError == True and len(row) == 48 and elementNum2 == 4):
                        f.write("\"N/A\",")
                        f.write("\"" + str(val) + "\",")
                    # N/A if there is not an available value
                    else:
                        f.write("\""+str(val)+"\",")
                    elementNum2 += 1
                f.write("\""+str(datetime.now())+"\"")
                f.write("\n")
