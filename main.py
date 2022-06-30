#In this programme you can add as many items with their corresponding prices as you want
items = ["yoghurt", "curd", "cheese", "butter", "gold"]
prices = [120, 200, 750, 800, 6217240.16]
exc = ["ALL", "EUR", "USD"]
cur_symbols = ["L","€","$"]
print("LOOK UP FOR THE ITEMS' PRICES\n" + str(items), "\n\n\nCurrencies available: ALL; EUR; USD")
cur = input("\nEnter the currency: ").upper()
#If currency input is not valid or available
while True:
  if cur not in exc:
    print("Unavailable currency entered")
    cur = input("\nEnter the currency: ").upper()
  else:
    break
###for i in range(len(items)):
search = input("\nPress Enter to show the table of prices\nSearch the item: ").lower()
#Converting to EUR & USD
conv1 = []
conv2 = []
if cur == exc[1]:
  for i in range(len(prices)):
    done = prices[i] * 0.0083#EUR
    conv1.append(done)
elif cur == exc[2]:
  for i in range(len(prices)):
    done1 = prices[i] * 0.0094#USD
    conv2.append(done1)
prices_list = [prices, conv1, conv2]
#Show prices
def show_prices():
  print("\n")
  for i, c in enumerate(cur_symbols):
    if cur == exc[i]:
      for j in range(len(items)):
        print(items[j].capitalize(), "costs", str(round(prices_list[i][j], 2 )) + c, "per kilogram")
#Show price
def show_price():
  for i, c in enumerate(cur_symbols):
    if cur == exc[cur_symbols.index(c)]:
      print(str(round(prices_list[i][items.index(search)], 2 )) + c,"per kilogram")
#If item is not on the list

while True:
  if search == "":
    show_prices()
    break
  elif search not in items:
    print("Item is missing!")
    search = input("Search the item: ").lower()
  else:
    show_price()
    break