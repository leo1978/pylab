def plotTimeLines(ids, start, end):
    y = { ids[i]:i for i in range(len(ids))}
    
    for id, s, t in zip(ids, start, end):       
        plot([s,t],[y[id],y[id]],'black')
        
