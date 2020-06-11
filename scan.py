import socket
import re
from threading import Thread
from time import time


#IP和端口文件名在此修改
ip_filename="iplist.txt"
iplist=[]
port_filename="portlist.txt"
portlist=[]

#读取IP地址并存放在数组中
for i in open(ip_filename):
	#正则筛选符合标准的IP地址
	ip_pattern=re.match(r'((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)',i)
	if ip_pattern:
		#替换文件中的换行符
		ip_value=i.replace('\n','')
		iplist.append(ip_value)


#读取port地址并存放在数组中
for i in open(port_filename):
	#替换文件中的换行符
	port_value=i.replace('\n','')
	port_pattern=re.match(r'((\d{1,5})-(\d{1,5}))',port_value)
	if port_pattern:
		port_value=port_value.split('-')
		for j in range(int(port_value[0]),int(port_value[1])+1):
			portlist.append(j)
	else:
		portlist.append(port_value)


#线程模块--scoket
def download(ip,port):
	try :
		s=socket.socket(2,1)
		res=s.connect_ex((ip,port))
		if res==0:
			print ('{}:{}:open'.format(ip, port))
		s.close()
	except Exception as e:
		print (str(e.message))


#线程模块--nmap
# def download(ip,port):


#扫描模块
def scan():
	#扫描开始计时
	start=time()
	for ip in iplist:
		print('当前扫描地址为%s' %ip)
		for port in portlist:
			#转换port Type为整型
			port=int(port)
			scan1=Thread(target=download,args=(ip,port))
			scan1.start()
			scan1.join()
	#扫描结束计时
	end=time()
	print('扫描结束，共耗时%.2f' %(end-start))


scan()
