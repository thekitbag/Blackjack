import urllib2
import re
from bs4 import BeautifulSoup
response = urllib2.urlopen('http://www.paddypower.com/football/football-matches/premier-league?ev_oc_grp_ids=21481')
html = response.read() 
soup = BeautifulSoup(html, "html5lib")
findtitles = soup.find_all("h2")
findodds =  soup.find_all("span", { "class" : 'odd'  })



for odd in findodds:
	print odd.text


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