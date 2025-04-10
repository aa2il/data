#! /usr/bin/python3
#############################################################################
#
# Script to get latest cty and scp files
#
#curl -s https://www.country-files.com/cty/download/ | grep -o 'href=".*">' | cut -f 2 -d '"' | cut -f 2 -d '-'
#
#############################################################################

import urllib.request, urllib.error, urllib.parse
import sys
import os

#############################################################################

# Grab latest super check partial file
url='https://supercheckpartial.com/MASTER.SCP'
cmd4='wget --backups=5 '+url
print('cmd4=',cmd4)
os.system(cmd4)
#sys.exit(0)

#############################################################################

# Grab directory listing of all the cty files available
url='https://www.country-files.com/cty/download'
response = urllib.request.urlopen(url)
#print('response=',response)
#print(type(response))
#sys.exit(0)

txt = response.read().decode("utf-8").split('\n')
#print('txt=',txt)
#print(type(txt))

# Sift through the dir listing and find the latest (highest no.)
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

# Download the latest cty zip file
cmd1='wget '+url+'/'+str(nmax)+'/cty-'+str(nmax)+'.zip'
print('cmd1=',cmd1)
os.system(cmd1)

# Pull out cty.plist from the zip file
cmd2='unzip -u cty-'+str(nmax)+'.zip cty.plist'
print('cmd2=',cmd2)
os.system(cmd2)

# Convert cty.plist to cty.bin so that it loads much faster
cmd3='plistutil -i cty.plist -o cty.bin'
print('cmd3=',cmd3)
os.system(cmd3)
