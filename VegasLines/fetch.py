import urllib2
import re
from bs4 import BeautifulSoup
response = urllib2.urlopen('http://www.paddypower.com/football/football-matches/premier-league?ev_oc_grp_ids=21481')
html = response.read()
soup = BeautifulSoup(html, "html5lib")
links = soup.find_all("a")
divs = soup.find_all("div")
titles = soup.find_all("h2")
mydiv = soup.find_all("div", { "id" : "mod-goalscorermarkets-1068" })
headers = soup.find_all("div", { "class" : "market-list-header" })
odds = soup.find_all("div", { "class" : "runner-markets-container " })
myheader = "market-name ui-924_71516247"
myprice = "ui-runner-price ui-924_71516247-5851483 ui-fraction-price"
headers1 = []
prices1 = []
theprices = []
theheaders = []

for item in mydiv:
	headers1.append(item.text)

for item in headers1:
	item = re.sub(r'[\t\r\n]', '', item)

print headers1





"""
for item in soup.find_all("span", { "class" : headers }):  
		for item in soup.find_all("span"):
			print item.text

for item in soup.find_all("span", { "class" : myprice }):  
		print item.text

f = open("div.txt", "w")
for item in headers:
	f.write(str(headers))
	f.write("")
f.close()

yui_3_5_0_1_1481117081423_12796
yui_3_5_0_1_1481117081423_12798

market-container 

<div class="market-list-header" id="yui_3_5_0_1_1481117081423_12768">
<span class="market-name ui-924_71516247" id="yui_3_5_0_1_1481117081423_12799">
0.5
<br><span class="unit" id="yui_3_5_0_1_1481117081423_12798">Goals</span>
</span>
<span class="market-name ui-924_71516248">
1.5
<br><span class="unit">Goals</span>
</span>
<span class="market-name ui-924_71516249">
2.5
<br><span class="unit">Goals</span>
</span>
<span class="market-name ui-924_71516250">
3.5
<br><span class="unit">Goals</span>
</span>
<span class="market-name ui-924_71516251">
4.5
<br><span class="unit">Goals</span>
</span>
<span class="market-name ui-924_71516252">
5.5
<br><span class="unit">Goals</span>
</span>
<span class="market-name ui-924_71516253" id="yui_3_5_0_1_1481117081423_12767">
6.5
<br><span class="unit" id="yui_3_5_0_1_1481117081423_12766">Goals</span>
</span>
<span class="market-name ui-924_71516254" id="yui_3_5_0_1_1481117081423_12944">
7.5
<br><span class="unit">Goals</span>
</span>
<span class="market-name ui-924_71516255">
8.5
<br><span class="unit">Goals</span>
</span>
</div>







f = open("div.txt", "w")
f.write(str(overpoint5))
f.close()


underpoint5 = = soup.find_all("div", { "class" : "ui-runner-price ui-924_71516247-5851482 ui-fraction-price" })


headers = response.info()
f = open("raw.txt", "w")
f.write("I am writing to this file")
f.close()
"""