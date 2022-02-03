from bs4 import BeautifulSoup
f = open("./data.txt", "r")
data = f.read()
soup = BeautifulSoup(data, "html.parser")
prices = []
raw = soup.find_all("div", class_="item-price")

for i in raw:
    prices.append(float(i.string.rstrip("\n")[3:].replace(',','')))

print("total price:", sum(prices))
print("total orders: ",len(prices))
print("price per order: ", sum(prices)/len(prices))