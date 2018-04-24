# Plot-Sysbench

prepare
```
sysbench /tmp/sysbench-master/src/lua/oltp_read_write.lua  --mysql-user=root --mysql-password=mysql --mysql-port=3306 \
--mysql-socket=/data/mysql55/mysql.sock  --mysql-host=localhost \
--mysql-db=sysbenchtest  --tables=10 --table-size=5000000  --threads=30 \
--events=5000000 --report-interval=5 prepare

##--table-size=五百万,一个表五百万 10个表 五千万
##--threads=30 开30个线程并发prepare

Initializing worker threads...

Creating table 'sbtest6'...
Creating table 'sbtest4'...
Creating table 'sbtest5'...
Creating table 'sbtest10'...
Creating table 'sbtest8'...
Creating table 'sbtest3'...
Creating table 'sbtest9'...
Creating table 'sbtest1'...
Creating table 'sbtest2'...
Creating table 'sbtest7'...
Inserting 5000000 records into 'sbtest4'
Inserting 5000000 records into 'sbtest5'
Inserting 5000000 records into 'sbtest6'
Inserting 5000000 records into 'sbtest8'
Inserting 5000000 records into 'sbtest3'
Inserting 5000000 records into 'sbtest9'
Inserting 5000000 records into 'sbtest10'
Inserting 5000000 records into 'sbtest7'
Inserting 5000000 records into 'sbtest1'
Inserting 5000000 records into 'sbtest2'
Creating a secondary index on 'sbtest6'...
Creating a secondary index on 'sbtest9'...
Creating a secondary index on 'sbtest4'...
Creating a secondary index on 'sbtest8'...
Creating a secondary index on 'sbtest3'...
Creating a secondary index on 'sbtest7'...
Creating a secondary index on 'sbtest2'...
Creating a secondary index on 'sbtest1'...
Creating a secondary index on 'sbtest5'...
Creating a secondary index on 'sbtest10'...
```
sysbenchtest库大小
```
[root@uz6535 mysql55]# du -sh sysbenchtest/
12G     sysbenchtest/
```

run
```
sysbench \
/tmp/sysbench-master/src/lua/oltp_read_write.lua \
--mysql-user=root  --mysql-password=mysql --mysql-port=3306 \
--mysql-socket=/data/mysql55/mysql.sock  --mysql-host=localhost \
--mysql-db=sysbenchtest  --tables=10 --table-size=5000000 \
--threads=30 --report-interval=5 --time=300 run > binlog_off.txt
```
输出的原始结果
```
[ 5s ] thds: 30 tps: 73.76 qps: 1538.67 (r/w/o: 1084.35/300.82/153.51) lat (ms,95%): 733.00 err/s: 0.00 reconn/s: 0.00
[ 10s ] thds: 30 tps: 75.80 qps: 1519.27 (r/w/o: 1062.85/304.81/151.61) lat (ms,95%): 590.56 err/s: 0.00 reconn/s: 0.00
[ 15s ] thds: 30 tps: 58.39 qps: 1183.57 (r/w/o: 831.24/235.55/116.78) lat (ms,95%): 926.33 err/s: 0.00 reconn/s: 0.00
[ 20s ] thds: 30 tps: 48.21 qps: 961.19 (r/w/o: 672.13/192.64/96.42) lat (ms,95%): 1129.24 err/s: 0.00 reconn/s: 0.00
[ 25s ] thds: 30 tps: 43.57 qps: 863.96 (r/w/o: 606.66/170.15/87.14) lat (ms,95%): 1109.09 err/s: 0.00 reconn/s: 0.00
[ 30s ] thds: 30 tps: 21.70 qps: 418.24 (r/w/o: 291.07/83.77/43.41) lat (ms,95%): 2585.31 err/s: 0.00 reconn/s: 0.00
[ 35s ] thds: 30 tps: 19.99 qps: 420.45 (r/w/o: 299.09/81.37/39.99) lat (ms,95%): 3267.19 err/s: 0.00 reconn/s: 0.00
[ 40s ] thds: 30 tps: 26.41 qps: 511.99 (r/w/o: 352.53/106.64/52.82) lat (ms,95%): 2198.52 err/s: 0.00 reconn/s: 0.00
[ 45s ] thds: 30 tps: 30.20 qps: 608.26 (r/w/o: 427.04/120.81/60.41) lat (ms,95%): 2279.14 err/s: 0.00 reconn/s: 0.00
[ 50s ] thds: 30 tps: 20.58 qps: 438.48 (r/w/o: 308.03/89.29/41.15) lat (ms,95%): 1973.38 err/s: 0.00 reconn/s: 0.00
[ 55s ] thds: 30 tps: 26.03 qps: 486.74 (r/w/o: 338.97/95.71/52.06) lat (ms,95%): 2279.14 err/s: 0.00 reconn/s: 0.00
[ 60s ] thds: 30 tps: 46.98 qps: 955.28 (r/w/o: 670.77/190.54/93.97) lat (ms,95%): 1170.65 err/s: 0.00 reconn/s: 0.00
[ 65s ] thds: 30 tps: 40.62 qps: 803.33 (r/w/o: 562.03/160.06/81.23) lat (ms,95%): 1533.66 err/s: 0.00 reconn/s: 0.00
[ 70s ] thds: 30 tps: 40.49 qps: 814.29 (r/w/o: 569.19/164.13/80.97) lat (ms,95%): 1903.57 err/s: 0.00 reconn/s: 0.00
[ 75s ] thds: 30 tps: 38.90 qps: 779.99 (r/w/o: 550.83/151.36/77.80) lat (ms,95%): 1589.90 err/s: 0.00 reconn/s: 0.00
[ 80s ] thds: 30 tps: 30.30 qps: 617.64 (r/w/o: 428.84/128.19/60.61) lat (ms,95%): 2009.23 err/s: 0.00 reconn/s: 0.00
[ 85s ] thds: 30 tps: 21.46 qps: 418.45 (r/w/o: 292.27/83.25/42.93) lat (ms,95%): 2449.36 err/s: 0.00 reconn/s: 0.00
[ 90s ] thds: 30 tps: 37.61 qps: 755.12 (r/w/o: 527.08/152.82/75.21) lat (ms,95%): 1771.29 err/s: 0.00 reconn/s: 0.00
[ 95s ] thds: 30 tps: 32.54 qps: 651.63 (r/w/o: 457.56/128.98/65.08) lat (ms,95%): 1869.60 err/s: 0.00 reconn/s: 0.00
[ 100s ] thds: 30 tps: 42.28 qps: 826.39 (r/w/o: 577.77/164.27/84.36) lat (ms,95%): 1453.01 err/s: 0.00 reconn/s: 0.00
[ 105s ] thds: 30 tps: 30.84 qps: 653.14 (r/w/o: 460.72/130.55/61.87) lat (ms,95%): 2198.52 err/s: 0.00 reconn/s: 0.00
[ 110s ] thds: 30 tps: 49.66 qps: 975.39 (r/w/o: 684.23/191.85/99.31) lat (ms,95%): 1149.76 err/s: 0.00 reconn/s: 0.00
[ 115s ] thds: 30 tps: 39.18 qps: 779.72 (r/w/o: 540.44/160.93/78.35) lat (ms,95%): 1376.60 err/s: 0.00 reconn/s: 0.00
[ 120s ] thds: 30 tps: 19.13 qps: 370.96 (r/w/o: 258.79/74.11/38.05) lat (ms,95%): 3095.38 err/s: 0.00 reconn/s: 0.00
[ 125s ] thds: 30 tps: 21.44 qps: 460.58 (r/w/o: 325.15/92.36/43.07) lat (ms,95%): 3267.19 err/s: 0.00 reconn/s: 0.00
[ 130s ] thds: 30 tps: 29.84 qps: 581.09 (r/w/o: 404.44/116.97/59.68) lat (ms,95%): 3040.14 err/s: 0.00 reconn/s: 0.00
[ 135s ] thds: 30 tps: 23.97 qps: 467.19 (r/w/o: 328.38/90.86/47.95) lat (ms,95%): 3326.55 err/s: 0.00 reconn/s: 0.00
[ 140s ] thds: 30 tps: 25.41 qps: 516.94 (r/w/o: 363.70/102.43/50.81) lat (ms,95%): 2449.36 err/s: 0.00 reconn/s: 0.00
[ 145s ] thds: 30 tps: 26.00 qps: 518.58 (r/w/o: 363.19/103.40/52.00) lat (ms,95%): 2778.39 err/s: 0.00 reconn/s: 0.00
[ 150s ] thds: 30 tps: 22.56 qps: 447.75 (r/w/o: 314.40/88.25/45.11) lat (ms,95%): 2539.17 err/s: 0.00 reconn/s: 0.00
[ 155s ] thds: 30 tps: 23.66 qps: 485.03 (r/w/o: 333.80/103.92/47.31) lat (ms,95%): 2405.65 err/s: 0.00 reconn/s: 0.00
[ 160s ] thds: 30 tps: 22.00 qps: 427.88 (r/w/o: 305.20/78.68/44.00) lat (ms,95%): 2932.60 err/s: 0.00 reconn/s: 0.00
[ 165s ] thds: 30 tps: 25.84 qps: 521.81 (r/w/o: 362.14/108.00/51.68) lat (ms,95%): 2632.28 err/s: 0.00 reconn/s: 0.00
[ 170s ] thds: 30 tps: 40.39 qps: 818.20 (r/w/o: 575.66/161.76/80.78) lat (ms,95%): 2082.91 err/s: 0.00 reconn/s: 0.00
[ 175s ] thds: 30 tps: 35.98 qps: 697.47 (r/w/o: 485.77/139.73/71.97) lat (ms,95%): 2045.74 err/s: 0.00 reconn/s: 0.00
[ 180s ] thds: 30 tps: 18.50 qps: 391.91 (r/w/o: 277.32/77.59/37.00) lat (ms,95%): 2680.11 err/s: 0.00 reconn/s: 0.00
[ 185s ] thds: 30 tps: 26.36 qps: 520.54 (r/w/o: 363.80/104.03/52.72) lat (ms,95%): 1973.38 err/s: 0.00 reconn/s: 0.00
[ 190s ] thds: 30 tps: 32.40 qps: 641.60 (r/w/o: 447.40/129.40/64.80) lat (ms,95%): 1903.57 err/s: 0.00 reconn/s: 0.00
[ 195s ] thds: 30 tps: 32.60 qps: 668.65 (r/w/o: 465.04/138.41/65.21) lat (ms,95%): 2405.65 err/s: 0.00 reconn/s: 0.00
[ 200s ] thds: 30 tps: 23.99 qps: 469.08 (r/w/o: 328.12/92.98/47.99) lat (ms,95%): 2985.89 err/s: 0.00 reconn/s: 0.00
[ 205s ] thds: 30 tps: 35.41 qps: 715.31 (r/w/o: 506.48/138.02/70.81) lat (ms,95%): 1903.57 err/s: 0.00 reconn/s: 0.00
[ 210s ] thds: 30 tps: 28.97 qps: 571.75 (r/w/o: 396.95/116.87/57.93) lat (ms,95%): 1836.24 err/s: 0.00 reconn/s: 0.00
[ 215s ] thds: 30 tps: 27.81 qps: 538.34 (r/w/o: 374.30/108.43/55.61) lat (ms,95%): 2539.17 err/s: 0.00 reconn/s: 0.00
[ 220s ] thds: 30 tps: 41.66 qps: 855.75 (r/w/o: 605.81/166.62/83.31) lat (ms,95%): 1213.57 err/s: 0.00 reconn/s: 0.00
[ 225s ] thds: 30 tps: 43.58 qps: 844.54 (r/w/o: 584.88/172.51/87.15) lat (ms,95%): 2120.76 err/s: 0.00 reconn/s: 0.00
[ 230s ] thds: 30 tps: 29.80 qps: 613.46 (r/w/o: 433.04/120.81/59.61) lat (ms,95%): 1533.66 err/s: 0.00 reconn/s: 0.00
[ 235s ] thds: 30 tps: 35.47 qps: 716.43 (r/w/o: 503.19/142.29/70.95) lat (ms,95%): 2198.52 err/s: 0.00 reconn/s: 0.00
[ 240s ] thds: 30 tps: 35.54 qps: 702.84 (r/w/o: 487.17/144.58/71.09) lat (ms,95%): 1506.29 err/s: 0.00 reconn/s: 0.00
[ 245s ] thds: 30 tps: 28.79 qps: 581.14 (r/w/o: 410.41/113.15/57.57) lat (ms,95%): 1938.16 err/s: 0.00 reconn/s: 0.00
[ 250s ] thds: 30 tps: 19.20 qps: 393.79 (r/w/o: 272.59/82.80/38.40) lat (ms,95%): 3151.62 err/s: 0.00 reconn/s: 0.00
[ 255s ] thds: 30 tps: 31.60 qps: 608.62 (r/w/o: 427.62/117.80/63.20) lat (ms,95%): 2493.86 err/s: 0.00 reconn/s: 0.00
[ 260s ] thds: 30 tps: 29.00 qps: 588.06 (r/w/o: 411.64/118.41/58.01) lat (ms,95%): 2159.29 err/s: 0.00 reconn/s: 0.00
[ 265s ] thds: 30 tps: 34.99 qps: 705.06 (r/w/o: 494.30/140.77/69.99) lat (ms,95%): 1836.24 err/s: 0.00 reconn/s: 0.00
[ 270s ] thds: 30 tps: 16.41 qps: 333.18 (r/w/o: 229.72/70.64/32.82) lat (ms,95%): 2778.39 err/s: 0.00 reconn/s: 0.00
[ 275s ] thds: 30 tps: 32.99 qps: 670.70 (r/w/o: 472.39/132.34/65.97) lat (ms,95%): 3040.14 err/s: 0.00 reconn/s: 0.00
[ 280s ] thds: 30 tps: 38.99 qps: 755.84 (r/w/o: 527.09/150.77/77.98) lat (ms,95%): 1771.29 err/s: 0.00 reconn/s: 0.00
[ 285s ] thds: 30 tps: 36.41 qps: 720.35 (r/w/o: 503.91/143.63/72.82) lat (ms,95%): 1561.52 err/s: 0.00 reconn/s: 0.00
[ 290s ] thds: 30 tps: 35.80 qps: 740.01 (r/w/o: 523.00/145.40/71.60) lat (ms,95%): 1678.14 err/s: 0.00 reconn/s: 0.00
[ 295s ] thds: 30 tps: 32.94 qps: 662.28 (r/w/o: 466.61/129.78/65.89) lat (ms,95%): 1973.38 err/s: 0.00 reconn/s: 0.00
[ 300s ] thds: 30 tps: 32.27 qps: 639.95 (r/w/o: 439.33/136.09/64.54) lat (ms,95%): 1869.60 err/s: 0.00 reconn/s: 0.00
SQL statistics:
    queries performed:
        read:                            139958
        write:                           39988
        other:                           19994
        total:                           199940
    transactions:                        9997   (33.18 per sec.)
    queries:                             199940 (663.60 per sec.)
    ignored errors:                      0      (0.00 per sec.)
    reconnects:                          0      (0.00 per sec.)

General statistics:
    total time:                          301.2969s
    total number of events:              9997

Latency (ms):
         min:                                 13.53
         avg:                                901.57
         max:                               5107.53
         95th percentile:                   2238.47
         sum:                            9012972.28

Threads fairness:
    events (avg/stddev):           333.2333/6.55
    execution time (avg/stddev):   300.4324/0.32

```
shell处理一下,文件名 最好为测试的条件  比如binlog_off binlog_on   thread_30 thread90
```
grep "^\[" binlog_off.txt |awk -F'(' '{print $1}'|sed -e "s/\[\ /\{'time':'/g" -e "s/\ \]//g" -e "s/:\ /':'/g" -e "s/\ /','/g" -e "s/,'$/\}/g"

{'time':'5s','thds':'30','tps':'14.95','qps':'391.01'}
{'time':'10s','thds':'30','tps':'27.33','qps':'549.58'}
{'time':'15s','thds':'30','tps':'29.01','qps':'585.07'}
{'time':'20s','thds':'30','tps':'27.51','qps':'528.04'}
{'time':'25s','thds':'30','tps':'24.80','qps':'503.08'}
{'time':'30s','thds':'30','tps':'34.22','qps':'688.40'}
```
处理成字典的样子,然后用python的 eval函数就能转换成字典了.我这里只取了输出结果的tps qps thds部分数据

###出图用charts库,我用的jupyter notebook直接执行的

测试机跑完文件那下来,统一命名测试机跑出来的结果为.txt,处理完的为.out
```
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
```
![image](https://raw.githubusercontent.com/Fanduzi/Plot-Sysbench/master/image/Snip20170706_70.png)
