i=-1
while i<1:
    L=''
    j=-1.6
    exec'x=y=0;exec"x,y=2*x*y+i,y*y-x*x+j;"*20;L+=" O"[(x*x+y*y)**.5<2];j+=.04;'*80
    print L
    i+=.1
