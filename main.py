import csv
import requests
from bs4 import BeautifulSoup


url = "https://bank.uz/uz/credits?PAGEN_1=19"


response = requests.get(url)


if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")


    loans = soup.find_all("div", class_="table-card-offers-bottom")
    


    with open("loans.csv", "w", newline="") as file:
        writer = csv.writer(file)


        writer.writerow(["Category", "Bank", "protsent ", "Lifetime", "Amount"])


        for loan in loans:
            category = loan.find("ul", class_="tabs-top")
            bank = loan.find("div", class_="table-card-offers-block1-text").text
            protsent = loan.find("div", class_="table-card-offers-block2").text
            Lifetime = loan.find("div", class_="table-card-offers-block3").text
            amount = loan.find("div", class_="table-card-offers-block4").text

            writer.writerow([category, bank, protsent, Lifetime, amount])
else:
   
    print("Failed to retrieve loan information. Error code:", response.status_code)