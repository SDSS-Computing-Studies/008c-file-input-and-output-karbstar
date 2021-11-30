#!python3
'''
Read the data from the file task02.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"

Example:
Enter stock symbol: AA
There are 21 stocks with that symbol
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches
'''

def needl (tr):
    filename = "task02.csv"
    file = open(filename,"r")
    data = file.read()
    lineData = data.split("\n")
    newList = []
    for line in lineData:
        df=False
        tempList = line.split(",")
        check=tempList[0]
        if tr in check:
            df =True
        if df== True:
            newList.append(tempList)
            print(newList)
    print(newList)
    x= newList
    s=len(newList)
    if s==1:
        print(newList)
    else:
        print(f"there are {s} stoks with the symbole {tr}")
if __name__ == "__main__":
    tr=input("enter a stock simbole=>")
    needl (tr)    
