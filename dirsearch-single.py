#By TeamsSix
#Blog teamssix.com
import sys,requests
requests.packages.urllib3.disable_warnings()

try:
	path = sys.argv[1]
	dir_path = sys.argv[2]
except:
	print('python3 disearch_single.py url_filepath dir_path')
	sys.exit()

f = open(path,'r')
f_read = f.readlines()
f.close()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}
for i in f_read:
	i = i.replace('\n','')
	url = i+dir_path
	try:
		r = requests.get(url,headers=headers,verify=False)
		r_text = len(r.text)
	except KeyboardInterrupt:
		sys.exit()
	except:
		print('[-] Connetion Failed {}'.format(url))
	if r.status_code == 200:
		print('\033[1;34;40m[+] 200 {} Vulnerability Found !!! {}\033[0m'.format(r_text,url))
	else:
		print('[-] {} {} {}'.format(r.status_code,r_text,url))
