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
x=input("enter a stock symbol=>")
def needl (needle):
    filename = "task01.txt"
    file = open(filename,"r")
    data = file.read()
    lineData = data.split("\n")
    x= lineData.index(needle)
    return x 