from bs4 import BeautifulSoup
import requests
import pandas
from tkinter import *
from tkinter.ttk import *

def create_csv(heads,data,links):
    df = pandas.DataFrame({"Head": heads, "Data": data, "Link": links})
    df.to_csv('bettgestell.csv', index=False, encoding='utf-8')

def open_tv(heads,data):
    window2 = Tk()
    window2.title('Treeview')
    tree = Treeview(window2)
    tree.grid(row=0, column=0, ipadx=200)
    tree['columns'] = 'Info'
    tree.column('Info', width=100)
    tree.heading('Info', text='Info')

    for i in range(count):
        tree.insert('', i, f'item{i}', text=heads[i], values="".join(data[i]).split())


url = 'https://www.ebay-kleinanzeigen.de/s-chemnitz/bettgestell/k0l3869'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}
response = requests.get(url,headers=headers)
content = response.content
soup = BeautifulSoup(content,features="html.parser")

heads = []
data = []
links = []
count = 0
root = Tk()
root.title('Scraping')

for ad in soup.findAll(name='article',attrs={'class':'aditem'}):
    main = ad.find('a',href=True,attrs={'class':'ellipsis'})
    heads.append(main.text)
    info = "".join(ad.find('div', attrs={'class': 'aditem-details'}).text).split()
    data.append(info)
    link = 'https://www.ebay-kleinanzeigen.de' + main.get('href')
    links.append(link)
    count += 1

label1 = Label(root, text=f'Scraping is done\nFound {count} entries', width=15).grid(row=0,column=0)
gen_csv = Button(root,text='Export CSV',command=lambda: create_csv(heads,data,links)).grid(row=1,column=0)
op_tv = Button(root,text='Open Treeview',command=lambda: open_tv(heads,data)).grid(row=1,column=1)

print(f'Count is : {count}')
mainloop()
