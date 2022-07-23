from operator import contains
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

opts = Options()
opts.headless
#opts.set_headless()
#assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
browser.get('https://www.trendyol.com/en/koton/dress-pink-bodycon-p-691089?boutiqueId=609641&merchantId=968')
results = browser.find_elements(By.TAG_NAME, 'div')
for i in range(len(results)):
    if "(VAT Included)" in results[i].text:
        price = results[i].text
        break

priceList=price.split()
for i in range(len(priceList)):
    if "(VAT" in priceList[i]:
        price = priceList[(i-2)]
        break
x=price.replace(',', '.')
priceFinal=float(x)
print(priceFinal)

browser.close()
quit()
