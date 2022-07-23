import mechanicalsoup

browser = mechanicalsoup.Browser(
    session=None, soup_config={'features': 'lxml'})
url = "https://www.trendyol.com/en/koton/dress-pink-bodycon-p-691089?boutiqueId=609641&merchantId=968"

site = browser.get(url)
page = site.soup

price1 = page.find_all("div")
x=0
for i in price1:
    i1 = str(i)
    if "product_original_price" in i1:
        data1=price1[x]
        break
    x=x+1

y=0
for i in data1.contents:
    i1 = str(i)
    if "product_original_price" in i1:
        data2=data1.contents[y]
        break
    y=y+1
pr=str(data2.text)
m=pr.split(sep=',')
for i in m:
    if "product_original_price" in i:
        pop=i
        pass
pr2=pop.split(sep=':')
finpr = float(pr2[1])
print(finpr)
