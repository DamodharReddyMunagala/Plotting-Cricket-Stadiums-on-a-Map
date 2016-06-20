# Plotting-Cricket-Stadiums-on-a-Map
#I have scrapped the cricket schedule from a website, I created a .csv file of cricket matches, got the locations of the stadiums with the geocoder module and plotted them on a Map
##importing requests to download html data
import requests
from bs4 import BeautifulSoup
r = requests.get('http://sports.ndtv.com/cricket/schedules-fixtures')
r.raise_for_status()
cricket_matches = open('CricketSchedule.html', 'wb')
for chunk in r.iter_content(100000):
    cricket_matches.write(chunk)
cricket_matches.close()

##importing BeautifulSoup to parse the html data
from bs4 import BeautifulSoup
soup = BeautifulSoup(open('C:\Users\damod_75cg7mp\Desktop/CricketSchedule.html'), 'lxml')
right_table = soup.find('table', {'class' : "crick-result-tbl"} )
A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []
K = []
for item in right_table.findAll('tr', {'class' : 'vevent'}):
    cells = item.findAll('td')
    A.append(cells[0].find(text = True))
    B.append(cells[0].find('span', {'class' : "smallfont"}).text)
    C.append(cells[1].strong.find(text = True))
    D.append(cells[1].find('span', {'class' : "smallfont"}).text)
    E.append(cells[2].find(text = True))
    F.append(cells[3].find(text = True))

#import geocoder to get latitudes and longitudes of a place
import geocoder
for i in range(len(E)):
    g = geocoder.google(str(E[i]))
    G.append(g.lat)
    H.append(g.lng)

#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(A,columns=['Teams'])
df['Type of Match'] = B
df['Date'] = C
df['Time'] = D
df['Venues'] = E
df['Series'] = F
df['Latitiude'] = G
df['Longitude'] = H
##print df
##Creating a csv file
df.to_csv('CricketMatchesScheduleWithLatLng.csv',index=True,header=True)
