from matplotlib.pyplot import *

T = {'id':['a','a','b','b'],'start':[1,5,1,4], 'end':[2,10,3,10]}

def partition(*data):
    p = {}
    for key, *values in zip(*data):
        if key in p:
            p[key].append(values)
        else:
            p[key] = [values]
    return list(p.keys()), list(p.values())
    
    
    
def plotTimeLines(ids, start, end):
    idset, segments = partition(ids, start, end)
    y = { idset[i]:i for i in range(len(idset))}
    
    for id, segment in zip(idset, segments):
        for s, t in segment:       
            l, = plot([s,t],[y[id],y[id]])
            setp(l, color='black', label=str(id))

    legend()
