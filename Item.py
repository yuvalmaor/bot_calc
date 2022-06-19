from posixpath import split
import requests
import csv



def cpu_prices():
    return 0
    pass

def gpu_prices():
    return 0
    pass
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
