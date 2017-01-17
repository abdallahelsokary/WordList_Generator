print ("""
-----------------------
 _ _ _            __           
\\/\/ord  list  (|_;enerator  
                              
-----------------------
 """)
import random
import time
from optparse import OptionParser
parser = OptionParser("""
usage: script.py -n  lenth of word list numberic value -w  string value for random  -d directory
example : wordlist.py -n 100 -w mynameisas -d c:/Users/abdallah/Desktop/wordlist.txt
""")
parser.add_option("-n","--number",dest="len",type="int",help="put the value of numbers")
parser.add_option("-w","--word",dest="word",type="string",help="put the word for random")
parser.add_option("-d","--dir",dest="dir",type="string",help="put the directory of wordlist")
(options, args) = parser.parse_args()
random1 = 1
if options.len == None or options.word == None or options.dir == None:
    print (parser.usage)
    exit(0)
else:
    srand = str(options.word)
    a =int(random1)
    a2 =int(options.len)
print ("plz wait for wordlist ....")
time.sleep(5)
file = open(options.dir,"+w")
file.close()
while a < a2:
    a = a + 1
    g = random.randrange(a,a+100)
    file = open(options.dir,"a")
    r = random.randrange(1,10)
    n = ''.join(map(lambda unused: random.choice(srand),range(r)))
    file.write(str(g)+n+"\n")

    if True:
        file.close()
        file = open(options.dir,"r")
        c = file.read()
        print (c)
file.close()
if True:
    print ("done the wordlist hase been created "+str(options.dir))


