def hideLast(cardNumber):
    # Convert the CardNumber to String for manipulation
    cardNumberStr = str(cardNumber)
    # Get the last four digit of the card number
    last_four_digit = cardNumber[-4:] 
     # Create the masked string with asterisks for all but the last four characters
    masked =  'X' * (len(cardNumberStr) -4) + last_four_digit
    print(masked)
    return masked
print(hideLast("44444400044000")) # Output XXXXXXXXXX4000
