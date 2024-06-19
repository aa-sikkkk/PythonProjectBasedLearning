def Check(string):
    # Convert The Input String to Lowercase.
    LowerString = string.lower()
    # Count the number of x in the string
    countX = LowerString.count("x")
    # Count the number of 0 in the string
    countO = LowerString.count("o")
    #Return True if both are equal else False
    return countX == countO
print(Check("XOXO")) # Returns True as X AND O are Equal.
print(Check("XOX")) # Returns False as X AND O are Not Equal.
print(Check("XOXOXO")) # Returns True as X AND O are Equal.
