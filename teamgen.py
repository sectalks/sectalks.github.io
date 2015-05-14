#SecTalks buggy random team generator
#v0.0
#www.sectalks.org

from random import shuffle

#teams = 2 #number of teams
#names = ['alice','bob','trudy']

def gen(teams,names):
    print '[i] Doing some magic on the names list'
    shuffle(names)
    j=0
    for i in range(len(names)):
        print '[i] Team %i: %s'%(j%teams,names[i-1])
        j+=1

if __name__=='__main__':
    print '\n'
    print 'SecTalks buggy random team generator'
    print '[i] Run this inside Python console'
    print '[i] import teamgen'
    print '[i] teamgen.gen(No. of teams, Array of names)'
    print '[i] e.g. teamgen.gen(2,["alice","bob","trudy"])'
