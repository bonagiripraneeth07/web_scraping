import  requests
from bs4 import BeautifulSoup
import  pandas as pd
product_name=[]
product_discription =[]
product_rating=[]
product_prize=[]

try:
    for i in range(2,8):
        source = requests.get("https://www.flipkart.com/search?q=mobiles+under+15000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_16_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_16_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles+under+15000%7CMobiles&requestId=40df05ca-d86e-4868-a3a0-455b98232800&as-backfill=on&page="+str(i))
        source.raise_for_status()
        soup = BeautifulSoup(source.content,'html.parser')
        box = soup.find('div',class_='DOjaWF gdgoEp')
        product = box.find_all('div',class_='KzDlHZ')
        for item in product :
            name= item.text
            product_name.append(name)
        #print(product_name)

        rating = box.find_all("div",class_='XQDdHH')
        for r in rating:
            rate = r.text.strip( ' ')
            product_rating.append(rate)
        #print  (product_rating)

        discription = box.find_all('div',class_='_6NESgJ')
        for d in discription:
            disc = d.text
            product_discription.append(disc)
        #print(product_discription)

        price = box.find_all("div",class_='Nx9bqj _4b5DiR')
        for p in price:
            pr = p.text
            product_prize.append(pr)
        #print(product_prize)
    df = pd.DataFrame({"Product name ":product_name,"Discription ":product_discription,"Rating":product_rating,"Price":product_prize})
    #print(df)
    df.to_csv("flipkart_mobiles under 15k.csv")
    print("done")





except Exception as e :
    print(e)
