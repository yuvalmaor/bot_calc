from posixpath import split
import requests
import csv


def get_linear_value(a,b,c):
    pass
def cpu_prices():
    prices={}
    prices["i9-12900KF"]=[41163,2500]

    prices["i7-12700KF"]=[34110,1800]

    prices["i5-12600KF"]=[27186,1200]

    prices["i3-12300"]=[14955,650]
    prices["Pentium Gold G7400"]=[6896,350]

    return prices
    pass

def gpu_prices():
    prices={}
    prices["3060"]=[16958,1700]
    prices["3060ti"]=[20206,1900]
    prices["3070"]=[22093,2000]

    prices["3070ti"]=[23367,2000]
    prices["3080"]=[24853,3100]
    prices["3080ti"]=[26887,4500]
    prices["3090ti"]=[29094,7000]
    return prices
    pass
#get cpu data


def init_cpus():
    dict={}
    with open('CPUv4.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                try:
                    print(f'\t'+str([row[0],row[2],row[9],row[11]]))
                    line_count += 1
                    dict[row[0]]=[row[2],row[9],row[11]]

                except:
                    print(row)
                    pass
        print(f'Processed {line_count} lines.')
    print("len="+str(len(dict)))
    return dict

def init_gpus():
    dict={}
    with open('GPUv7.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                try:
                    print(f'\t'+str([row[0],row[1],row[7],row[8]]))
                    line_count += 1
                    dict[row[0]]=[row[1],row[7],row[8]]

                except:
                    print(row)
                    pass
        print(f'Processed {line_count} lines.')
    print("len="+str(len(dict)))
    return dict






def get_score():
    return 1000

def get_gpu_mark(arg):
    argv=arg.split(" ")
    s=""
    for i in argv:
        s=s+i+"+"
    #AMD+Ryzen+3+3100
    s=s[:-1]
    x = requests.get('https://www.videocardbenchmark.net/video_lookup.php?gpu=GeForce+GTX+1070')

    #print(x.text)
    html=x.text
    #start=html.find("Average G3D Mark")
    #html=html[start:]
    print(html)
    end=html.find("Single Thread Rating")
    html=html[:end]
    start=html.find("color")
    html=html[start:]
    start=html.find(">")
    end=html.find("<")
    html=html[start+1:end]
    #print(html[:end])

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
