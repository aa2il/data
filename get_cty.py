#! /usr/bin/python3

# Script to get latest cty files

#curl -s https://www.country-files.com/cty/download/ | grep -o 'href=".*">' | cut -f 2 -d '"' | cut -f 2 -d '-'

import urllib.request, urllib.error, urllib.parse
import sys
import os

url='https://www.country-files.com/cty/download'
response = urllib.request.urlopen(url)
#print('response=',response)
#print(type(response))
#sys.exit(0)

txt = response.read().decode("utf-8").split('\n')
#print('txt=',txt)
#print(type(txt))

nmax=0
for line in txt:
    #print('line=',line)
    idx1=line.find('href=')
    #print('idx1=',idx1)
    if idx1>0:
        idx2=idx1+line[idx1:].find('>')+1
        idx3=idx2+line[idx2:].find('<')
        fname = line[idx2:idx3]
        #print(idx2,idx3,'\t-',fname,'-')
        if fname[-1]=='/':
            num = int(fname[0:-1])
            print(fname[0:-1],num)
            if num>nmax:
                nmax=num
print('\nnmax=',nmax)

cmd1='wget '+url+'/'+str(nmax)+'/cty-'+str(nmax)+'.zip'
print('cmd1=',cmd1)
os.system(cmd1)

#cmd2='unzip -u cty-'+str(nmax)+'.zip'
cmd2='unzip -u cty-'+str(nmax)+'.zip cty.plist'
print('cmd2=',cmd2)
os.system(cmd2)

cmd3='plistutil -i cty.plist -o cty.bin'
print('cmd3=',cmd3)
os.system(cmd3)

