import Item
class Data:

    def __init__(self):
        
        self.cpus=Item.init_cpus()
        self.gpus=Item.init_gpus()
        self.cpu_prices=Item.cpu_prices()
        self.gpus_prices=Item.gpu_prices()

    def handel_msg(self,msg):
        x = msg.split("\n")
        cpu=x[1][4:]
        gpu=x[2][4:]
        ram=x[3][4:]
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
        for i in range(len(x)-5):
            print(x[i+5])
            discs.append(x[i+5][4:])
            if(x[i+5][:3]=="ssd"):
                sum=sum+self.get_ssd_value(x[i+5][4:])
                new_sum=new_sum+self.get_new_ssd_value(x[i+5][4:])
            else:
                sum=sum+self.get_hdd_value(x[i+5][4:])
                new_sum=new_sum+self.get_new_hdd_value(x[i+5][4:])
            
        print("***")
        
        return(str(sum)+":"+str(new_sum))
        pass
    
    def get_cpu_value(self,cpu):
        #print(cpu)
        return 0
        pass
    def get_gpu_value(self,gpu):
        #print(gpu)
        return 0
        pass
    def get_ssd_value(self,ssd):
        a=int(ssd[:-2])
        num=(a/500)*80
        return num
        pass
    def get_hdd_value(self,hdd):
        a=int(hdd[:-2])
        num=(a/500)*20
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
        num=(a/1000)*75
        return num
        return 1
        pass    