#web scraper that gives me current temperature 
#search input is the zip code
import sys
from instream import InStream
import stdio

#string we want for meto website
#<span class=\"meteo-c-temp-10\">10°<\/span>

postalcode = sys.argv[1]

# Return the raw HTML from the website 
def _readHTML(postalcode):
    WEBSITE = 'https://meteo.search.ch/'
    page = InStream(WEBSITE+postalcode)
    html = page.readAll()
    return html

#-----------------------------------------------------------------------

def currentWeather(postalcode):
    html  = _readHTML(postalcode)
    weather = html.find('<span class=\"meteo-c-temp')
    end   = html.find('span', weather+5)
    weatherNum = html.rfind('>',weather,end)
    currentTemp = html[weatherNum+1:end-2]
    stdio.writef('The current weather at Postalcode %4s,CH is %3s. \n',postalcode,currentTemp)

def Weathertomorrow(postalcode):    
        html  = _readHTML(postalcode)
        weather = html.find('<p>Morgen<\/p>')
        weather = html.find('"meteo-limit-height',weather)
        start = html.find('">',weather)
        end   = html.find('.<', start)
        currentTemp = html[start+2:end+1]
        stdio.writef('The Weather prognosis for tomorrow is:\n%-50s',currentTemp)    

currentWeather(postalcode)
Weathertomorrow(postalcode)