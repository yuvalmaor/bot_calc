import Item
class Data:

    def __init__(self):
        
        self.cpus=Item.init_cpus()
        self.gpus=Item.init_gpus()
        self.cpu_prices=Item.cpu_prices()
        self.gpus_prices=Item.gpu_prices()

    def handel_msg(self,msg):
        x = msg.split("\n")
        cpu=x[0][4:]
        gpu=x[1][4:]
        ram=x[2][4:]
        ram=ram.split(" ")
        memory=ram[0]
        ddr=ram[1]
        sum=0
        new_sum=0
        discs=[]
        print(x)
        print("***")
        print(cpu)
        print(gpu)
        print(memory)
        print(ddr)
        log=""
        v_cpu=self.get_cpu_value(cpu)
        sum=sum+v_cpu[0]
        log=log+"cpu+mobo:"+str(v_cpu[0])+"\n"

        v_gpu=self.get_gpu_value(gpu)
        sum=sum+v_gpu[0]

        log=log+"gpu:"+str(v_gpu[0])+"\n"
        sum=sum+self.get_ram_value((memory,ddr)) 
        log=log+"ram:"+str(self.get_ram_value((memory,ddr)))+"\n"
        for i in range(len(x)-3):
            print(x[i+3])
            discs.append(x[i+3][4:])
            if(x[i+3][:3]=="ssd"):
                sum=sum+self.get_ssd_value(x[i+3][4:])
                log=log+"drive"+str(i)+":"+str(self.get_ssd_value(x[i+3][4:]))+"\n"
                new_sum=new_sum+self.get_new_ssd_value(x[i+3][4:])
            else:
                sum=sum+self.get_hdd_value(x[i+3][4:])
                log=log+"drive"+str(i)+":"+str(self.get_hdd_value(x[i+3][4:]))+"\n"
                new_sum=new_sum+self.get_new_hdd_value(x[i+3][4:])

         
        print("***")
        
        #return(str(sum)+":"+str(new_sum))
        #return("pc value beta=>"+str(sum)+"\n\nbeta log (not visable in alpha)\n"+log)
        return("מחיר מומלץ:"+str(int(sum))+" שח \n\n\n"+str(v_cpu[1])+"\n"+str(v_gpu[1]))
        pass

    def handel_msg_t(self,msg):
        x = msg.split("\n")
        cpu=x[0][4:]
        gpu=x[1][4:]
        ram=x[2][4:]
        ram=ram.split(" ")
        memory=ram[0]
        ddr=ram[1]
        sum=0
        new_sum=0
        discs=[]
        print(x)
        print("***")
        print(cpu)
        print(gpu)
        print(memory)
        print(ddr)
        log=""
        v_cpu=self.get_cpu_value(cpu)
        sum=sum+v_cpu[0]
        log=log+"cpu+mobo:"+str(v_cpu[0])+"\n"

        v_gpu=self.get_gpu_value(gpu)
        sum=sum+v_gpu[0]

        log=log+"gpu:"+str(v_gpu[0])+"\n"

        sum=sum+self.get_ram_value((memory,ddr)) 
        log=log+"ram:"+str(self.get_ram_value((memory,ddr)))+"\n"
        for i in range(len(x)-4):
            print(x[i+4])
            discs.append(x[i+4][4:])
            if(x[i+4][:3]=="ssd"):
                sum=sum+self.get_ssd_value(x[i+4][4:])
                log=log+"drive"+str(i)+":"+str(self.get_ssd_value(x[i+4][4:]))+"\n"
                new_sum=new_sum+self.get_new_ssd_value(x[i+4][4:])
            else:
                sum=sum+self.get_hdd_value(x[i+4][4:])
                log=log+"drive"+str(i)+":"+str(self.get_hdd_value(x[i+4][4:]))+"\n"
                new_sum=new_sum+self.get_new_hdd_value(x[i+4][4:])

         
        print("***")
        
        #return(str(sum)+":"+str(new_sum))
        return("pc value beta=>"+str(sum)+"\n\nbeta log (not visable in alpha)\n"+log)
        #return("pc value is:"+str(sum))

    def get_ram_value(self,ram):
        print("my ram:"+str(ram))
        num=int(ram[0][:-2])
        ddr=ram[1]
        price=0
        print("num:"+str(num))
        if(ddr=='ddr3'):
            price=(num/8)*50
        if(ddr=='ddr4'):
            price=(num/8)*100
        if(ddr=='ddr5'):
            price=(num/8)*200
        return price
        pass
    def get_cpu_value(self,cpu):

        print("my cpu:"+str(cpu))
        print(cpu.split(" "))
        n_cpu=""
        cpus=[]
        print(cpu.split(" ")[-1])
        print(cpu.split(" ")[-1] in self.cpus.keys())
        #print(self.cpus.keys())
        if(cpu not in self.cpus.keys()):
            for i in  self.cpus.keys():
                if(cpu  in i):
                    print("heydad:"+i)
                    n_cpu=i
                    cpus.append(i)

            print(cpus)
            cpu=n_cpu
            for i in cpus:
                if(len(i)<len(cpu)):
                    cpu=i
                
                    
        d_cpu=self.cpus[cpu]
        print("cpu data\n"+str( d_cpu))
        d=Item.cpu_prices()
        gpu_p=int( d_cpu[0])#power
        gpu_y=int( d_cpu[1])#year
        better_gpu=None
        worse_gpu=None
        for key in d.keys():
            if(d[key][0]<=gpu_p and worse_gpu==None):
                worse_gpu=d[key]
                
            elif(worse_gpu!=None and d[key][0]<=gpu_p and d[key][0]>worse_gpu[0]):
                worse_gpu=d[key]

            if(d[key][0]>=gpu_p and better_gpu==None):
                better_gpu=d[key]
                
            elif(better_gpu!=None and d[key][0]>=gpu_p and d[key][0]<better_gpu[0]):
                better_gpu=d[key]
        if(better_gpu==None and worse_gpu!=None):
            price=(gpu_p/worse_gpu[0])*worse_gpu[1]
            
            
        if(better_gpu!=None and worse_gpu==None):
            price=(gpu_p/better_gpu[0])*better_gpu[1]
            
        if(better_gpu!=None and worse_gpu!=None):
            price=(worse_gpu[1]+better_gpu[1])/2
            pass
        age=2022-gpu_y
        if(age>=2):
            for i in range(age-1):
                price=price*0.9
        if("Laptop" in d_cpu[2]):
            price=price*2
        return price,cpu

    def get_gpu_value(self,gpu):
        if gpu =="":
            return 0,""
        gpus=[]
        n_gpu=""
        print("my gpu:"+str(gpu))
        if(gpu not in self.gpus.keys()):
            for i in  self.gpus.keys():
                if(gpu in i):
                    print("heydad:"+i)
                    n_gpu=i
                    gpus.append(i)
                
                    
            print(gpus)
            gpu=n_gpu
            for i in gpus:
                if(len(i)<len(gpu)):
                    gpu=i

        d_gpu=self.gpus[gpu]
        print("gpu data\n"+str(d_gpu))
        gpu_p=int( d_gpu[0])#power
        gpu_y=int( d_gpu[1])#year
        better_gpu=None
        worse_gpu=None
        price=0
        d=Item.gpu_prices()
        for key in d.keys():
            if(d[key][0]<=gpu_p and worse_gpu==None):
                worse_gpu=d[key]
                
            elif(worse_gpu!=None and d[key][0]<=gpu_p and d[key][0]>worse_gpu[0]):
                worse_gpu=d[key]

            if(d[key][0]>=gpu_p and better_gpu==None):
                better_gpu=d[key]
                
            elif(better_gpu!=None and d[key][0]>=gpu_p and d[key][0]<better_gpu[0]):
                better_gpu=d[key]
        if(better_gpu==None and worse_gpu!=None):
            price=(gpu_p/worse_gpu[0])*worse_gpu[1]
            
            
        if(better_gpu!=None and worse_gpu==None):
            price=(gpu_p/better_gpu[0])*better_gpu[1]
            
        if(better_gpu!=None and worse_gpu!=None):
            price=(worse_gpu[1]+better_gpu[1])/2
            pass
        age=2022-gpu_y
        if(age>=2):
            for i in range(age-1):
                price=price*0.9
        return price,gpu
        
    def get_ssd_value(self,ssd):
        print(ssd.split(" "))
        my_ssd=ssd.split(" ")
        ssd=my_ssd[0]
        if("gen4" in my_ssd):
            pass
        a=int(ssd[:-2])
        num=(a/500)*150
        return num
        pass

    def get_hdd_value(self,hdd):
        a=int(hdd[:-2])
        num=(a/500)*30
        return num
        pass

    def get_new_cpu_value(self,cpu):
        print(cpu)
        return 0
        pass
    def get_new_gpu_value(self,gpu):

        #print(gpu)
        return 1
        pass
    def get_new_ssd_value(self,ssd):
        a=int(ssd[:-2])
        num=(a/500)*200
        return num
        pass
    def get_new_hdd_value(self,hdd):
        a=int(hdd[:-2])
        num=(a/500)*45
        return num
        pass    