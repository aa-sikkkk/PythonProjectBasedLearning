# Program to find the Discount
def CalDis(price,per):
    discount = (price) * (per/100)
    PriceAfterDisc = price - discount
    return PriceAfterDisc

price = float(input("Enter the Price of the Commodity: "))
per = float(input("Enter the Percent of discount of the Commodity: "))
print(f"The Price after discount is {CalDis(price,per)} ")



#Including Value error

# def CalDis(price,per):
#     discount = (price) * (per/100)
#     PriceAfterDisc = price - discount
#     return PriceAfterDisc

# try:
#     price = float(input("Enter the Price of the Commodity: "))
       
#     if price < 0:
#         raise ValueError("Please input price more than zero")
    
#     per = float(input("Enter the Percent of discount of the Commodity: "))
#     if per < 0:
#         raise ValueError("Please input percentage more than zero")

#     discountedPrice = CalDis(price,per)
#     print(f"The Price after Discount is {discountedPrice:.2f}")
# except ValueError as e:
#     raise ValueError(f"Error: Invalid Input {e} ")

