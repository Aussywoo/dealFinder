# A central class with functions to add search results to a list

mainList = []

# Adds a search result to the total list
def addItem(itemName:str, location:str, price:float, date:str, imageURL:str, origin:str):
    mainList.append([itemName, location, date, price, imageURL, origin])

# Returns the list of all search results
def getList() -> list:
    return mainList

# Returns a list of all search results sorted from lowest to highest
def getSortedList() -> list:
    return []

# Returns all search results from a specific store
def getStore(origin:str) -> list:
    specifiedList = []
    for item in mainList:
        if item[5] == origin:
            specifiedList.append(item)
    return specifiedList