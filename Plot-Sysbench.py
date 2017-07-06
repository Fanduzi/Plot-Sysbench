import charts
import subprocess
import os
class MyCharts:
    def __init__(self,file_list,qpsortps,title,interval=None):
        self.file_list=file_list
        self.qpsortps=qpsortps
        self.interval=interval
        self.title=title
        self.options = {
        'title':{'text':self.title},
        'xAxis':{
            'labels':{
                'step':1
            },
        },
        'yAxis':{
            'title':{'text':self.qpsortps},
        },
        'chart': {
                'type': 'line',
                'zoomType': 'x',
                'panning': 'true',
                'panKey': 'shift'
            },
        }

    def getOne(self,file):
        with open(file,'r') as data:
            dicList=[]
            for line in data:
                dic=eval(line.strip())
                if self.interval:
                    if int(dic['time'][:-1])%self.interval == 0:
                        dicList.append(dic)
                else:
                    dicList.append(dic)

        timeList,qpsortpsList=[],[]
        for i in dicList:
            timeList.append(int(i['time'][:-1]))
            if self.qpsortps == 'qps':
                qpsortpsList.append(float(i['qps']))
            else:
                qpsortpsList.append(float(i['tps']))

        qpsortpsData=list(zip(timeList,qpsortpsList))
        temp = file[file.rindex('/')+1:file.rindex('.')]
        return {'data':qpsortpsData,'name':temp}


    def getMulti(self):
        s1List = []
        for file in self.file_list:
            s1List.append(self.getOne(file))

        return s1List

def etl(file_list):
    for file in file_list:
        file_txt='/Users/TiM/sysbench_file/'+file+'.txt'
        file_out='/Users/TiM/sysbench_file/'+file+'.out'
        if not os.path.exists(file_out):
            cmd='''grep "^\[" %s \
            |awk -F'(' '{print $1}'|sed -e "s/\[\ /\{'time':'/g" -e \
            "s/\ \]//g" -e "s/:\ /':'/g" -e "s/\ /','/g" -e "s/,'$/\}/g" \
            > %s''' % (file_txt,file_out)
            subprocess.call(cmd,shell=True)

etl(['oltp_point_select','oltp_read_only','oltp_read_write'])

file_list = [
            '/Users/TiM/sysbench_file/oltp_read_write.out',
            '/Users/TiM/sysbench_file/oltp_point_select.out',
            '/Users/TiM/sysbench_file/oltp_read_only.out'
            ]
char_1=MyCharts(file_list,'qps','16G 4core Benchmark')
res=char_1.getMulti()

charts.plot(res,options=char_1.options,show='inline',)

