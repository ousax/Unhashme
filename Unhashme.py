#run using Python 2 
from hashlib import md5,sha1,sha224,sha256,sha384,sha512
from sys import exit
from os.path import exists
from time import time
import argparse
global _Instragram, _Github
_Instagram, _Github = "https://instagram.com/0xc10xc81", "https://github.com/ousax"
class Unhashme:
    def __init__(self, Text, wd):
        self.Text = Text
        self.wd = wd
    def Start(self):
        g, r, o = "\033[32m", "\033[31m", "\033[33m"
        global Text,wd,t0,t1
        di_len = [32,40,56,64,96,128]
        while not exists(wd):
        	print(r+"{} doesn't exist!".format(wd)+g)
        	wd = raw_input("Wordlist: ")
        with open(wd, "r") as f:
            fread = f.readlines()
            if len(fread) == 0:
                exit(r+"Empty wordlist"+g)
            else:
                print(o+"{} password(s) loaded".format(len(fread)))
                if len(Text) not in di_len:
                    exit(r+"Not available!")
                else:
                    i, t0 = 0, time()
                    if len(Text) == di_len[0]:#md5
                        print(o+"md5")
                        try:
                            for x in range(len(fread)):
                                pwd = fread[x].replace("\n", "")
                                Match = md5(b'{}'.format(pwd)).hexdigest()
                                if Match == Text:
                                    t1 = time()
                                    t = str(t1-t0)[:5]
                                    print(g+"Found : {} in line [{}] after [{}](s)".format(pwd, i ,t))
                                    break
                                else:
                                    print(r+"[{}] Wrong password".format(pwd))
                                i += 1
                        except:
                            pass
                        f.close()
                    if len(Text) == di_len[1]:#sh1
                        print(o+"sha1")  
                        t0 = time() 
                        try:
                            for x in range(len(fread)):
                                pwd = fread[x].replace("\n", "")
                                Match = sha1(b'{}'.format(pwd)).hexdigest()
                                if Match == Text:
                                    t1 = time()
                                    t = str(t1-t0)[:5]
                                    print(g+"Found : {} in line [{}] after [{}](s)".format(pwd, i ,t))
                                    break
                                else:
                                    print(r+"[{}] Wrong password".format(pwd))
                                i += 1
                        except:
                            pass
                        f.close()
                    if len(Text) == di_len[2]:#sh224
                        try:
                            t0 = time()
                            for x in range(len(fread)):
                                pwd = fread[x].replace("\n", "")
                                Match = sha224(b'{}'.format(pwd)).hexdigest()
                                if Match == Text:
                                    t1 = time()
                                    t = str(t1-t0)[:5]
                                    print(g+"Found : {} in line [{}] after [{}](s)".format(pwd, i ,t))
                                    break
                                else:
                                    print(r+"[{}] Wrong password".format(pwd))
                        	i += 1
                        except:
                            pass
                        f.close()
                    if len(Text) == di_len[3]:#sha256
                        try:
                            t0 = time()
                            for x in range(len(fread)):
                                pwd = fread[x].replace("\n", "")
                                Match = sha256(b'{}'.format(pwd)).hexdigest()
                                if Match == Text:
                                    t1 = time()
                                    t = str(t1-t0)[:5]
                                    print(g+"Found : {} in line [{}] after [{}](s)".format(pwd, i ,t))
                                    break
                                else:
                                    print(r+"[{}] Wrong password".format(pwd))
                       		i += 1
                        except:
                            pass
                        f.close()
                    if len(Text) == di_len[4]:#sha384
                        try:
                            t0 = time()
                            for x in range(len(fread)):
                                pwd = fread[x].replace("\n", "")
                                Match = sha384(b'{}'.format(pwd)).hexdigest()
                                if Match == Text:
                                    t1 = time()
                                    t = str(t1-t0)[:5]
                                    print(g+"Found : {} in line [{}] after [{}](s)".format(pwd, i ,t))
                                    break
                                else:
                                    print(r+"[{}] Wrong password".format(pwd))
                        	i += 1
                        except:
                            pass
                        f.close()
                    if len(Text) == di_len[5]:#sha512
                        try:
                            t0 = time()
                            for x in range(len(fread)):
                                pwd = fread[x].replace("\n", "")
                                Match = sha512(b'{}'.format(pwd)).hexdigest()
                                if Match == Text:
                                    t1 = time()
                                    t = str(t1-t0)[:5]
                                    print(g+"Found : {} in line [{}] after [{}](s)".format(pwd, i ,t))
                                    break
                                else:
                                    print(r+"[{}] Wrong password".format(pwd))
                        	i += 1
                        except:
                            pass
                        f.close()
def SL():
    o = "\033[33m"
    r = "\033[31m"
    g = "\033[32m"
    infos = """
                {2}[Instagram]{3}[{0}]
                {2}[Github]{3}[{1}]{2}
            unhash.py is a simple script to brute force some algorithms such as md5, sha1 and sha512
            coded by 0xc10x81
            {4}Only for educational purpose{3}
    """.format(_Instagram, _Github,o,g,r)
    print(infos)
parser = argparse.ArgumentParser(description=SL())
parser.add_argument("-txt", type=str, help="The hashed text [copy and past]")
parser.add_argument("-wd", type=str, help="The path to the wordlist")
args = parser.parse_args()
Text = args.txt
wd = args.wd
unhash = Unhashme(Text, wd)
unhash.Start()
