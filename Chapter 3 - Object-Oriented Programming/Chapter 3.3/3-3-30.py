#data mining
import stdarray
import stdio
from vector import Vector
from sketch import Sketch
from instream import InStream
import random



#-> prepare sketch of end website
#-> Loop: sketch current website -> check if above threshhold -> if not search for link on website -> go to next website
#also print url of website currently on to follow trail

#we set length of gram to 5 and d to 20000 (as in book)

#create a way to get text from websites 

def getHTML(website):
    place = InStream(website)
    text = place.readAll()
    return text

#create a way to find url on the website:
#returns a list of all urls on the website
def findUrls(website):
    place = InStream(website)
    text = place.readAllStrings()
    urls = []
    for i in range(len(text)):
        if 'href="/wiki/Category:' in text[i]:
            x = text[i].find('href="')
            y = text[i][x+7:].find('"')
            urls += ['https://en.wikipedia.org'+ text[i][x+6:x+y+7]]
    return urls



#our looping function

def dataMining(start,end,visited):
    final_html = getHTML(end)
    final = Sketch(final_html,5,20000)
    html = getHTML(start)
    current = Sketch(html,5,20000)
    print(final.similarTo(current))
    if final.similarTo(current) > 0.85: return print('all done', start)
    urls = findUrls(start)
    for i in range(1,len(urls)):
        if urls[i] not in visited:
            print(urls[i])
            visited += [urls[i]]
            dataMining(urls[i],end,visited) 
    return

start = 'https://en.wikipedia.org/wiki/Windward_and_leeward'

end = 'https://en.wikipedia.org/wiki/Asteroid'

visited = [start]

dataMining(start,end,visited)