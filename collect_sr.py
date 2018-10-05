# -*- coding: utf-8 -*-
import urllib2, string, re, time
from pprint import pprint
_version_ = 0.1
_python_version_ = 2.7

def str2arr(inp_string):
    #printable = set(string.printable)
    #inp_string = filter(lambda x: x in printable, inp_string)
    inp_string = inp_string.split('\n')

    return [i.strip(' ').replace('#','-') for i in inp_string if i != '']

def get_SR(rawhtml):
    matchObj = re.search(r'u-align-center h5">(\d{3,4})<',rawhtml)
    if matchObj == None: 
        return "SR not found"
    else:
        return int(matchObj.group(1))


def get_stats(btags):
    SR_dict = {}

    for btag in btags:
        if btag not in SR_dict: SR_dict[btag] = []
        #print "Collecting data of %s"%btag
        url = 'https://playoverwatch.com/en-us/career/pc/' + btag
        rawhtml = urllib2.urlopen(url).read()
        SR_dict[btag].append( get_SR(rawhtml) )
        time.sleep(0.6)

    return SR_dict

def print_summary_stats(SR_dict):
    def avg(lst):
        lst = [i[0] for i in lst]
        l = [i for i in lst if type(i) == int and i != 0]
        return sum(l)/len(l)

    avg_SR = avg(SR_dict.values())
    top_6_avg_SR = avg(sorted([i if type(i[0]) == int else [0] for i in list(SR_dict.values())], reverse=True)[:6])

    print "Avg SR: ",avg_SR
    print "Top 6 SR: ",top_6_avg_SR


def main():
    teams = {'Lawrence': '''NotEaster#1812   

LukeKapone#1544   

Oatman#11864   

TheHappyHeel#1420   

DaleCooper#12233   

spacesloth#1831   

Sokratos#11247   

YourMama#1151   

Zygoptera#1254''',
'Boulder': '''drygrasses#1364   

MinecraftKid#11503   

Atomicsp00n#11471   

Alchemist#12408   

tsarfish#1853   

Javelin#1705   

Tuna#12725   

Ŝystem#1991''',
'tartans':'''Alan7996#1296
 OneEyedKing#11402             
 Allen#13708             
 Simpathey#2158             
 Hand#11969           
 Meeow#1317            
 hamaHA#11282'''}
    for key in teams.keys():
        print '\n===== %s ====='%key
        SR_dict = get_stats( str2arr(teams[key]) )
        pprint(SR_dict)
        print_summary_stats(SR_dict)


main()


    