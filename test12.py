#!python3
def needl (tr):
    filename = "task02.csv"
    file = open(filename,"r")
    data = file.read()
    lineData = data.split("\n")
    newList = []
    for line in lineData:
        tempList = line.split(",")
        strings_with_substring = [string for string in strings if substring in string]
    print(newList)
    x= newList
    s=len(newList)
    if s==1:
        lineData.index(needl)
    else:
        print(f"there are {s} stoks with the symbole {tr}")
if __name__ == "__main__":
    tr=input("enter a stock simbole=>")
    needl (tr)