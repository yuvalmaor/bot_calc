from posixpath import split
import requests
def get_score():
    return 1000

def get_cpu_mark(arg):
    argv=arg.split(" ")
    s=""
    for i in argv:
        s=s+i+"+"
    #AMD+Ryzen+3+3100
    s=s[:-1]
    x = requests.get('https://www.cpubenchmark.net/cpu.php?cpu='+s)

    #print(x.text)
    html=x.text
    start=html.find("Average CPU Mark")
    html=html[start:]
    end=html.find("Single Thread Rating")
    html=html[:end]
    start=html.find("color")
    html=html[start:]
    start=html.find(">")
    end=html.find("<")
    html=html[start+1:end]
    print(html[:end])

def get_item():
    x = requests.get('https://www.cpubenchmark.net/cpu.php?cpu=AMD+Ryzen+3+3100')

    #print(x.text)
    html=x.text
    html.find("Average CPU Mark")
    print(html.find("Average CPU Mark"))
