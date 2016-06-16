#i=-1;exec"""L='';j=-1.6;exec'x=y=0;exec"x,y=2*x*y+i,y*y-x*x+j;"*20;L+=" O"[(x*x+y*y)**.5<2];j+=.04;'*80;print L;i+=.1;"""*20
#i=-1;exec"""L='';j=-1.6;exec'x=y=0;exec"x,y=2*x*y+i,y*y-x*x+j;"*20;L+=" O"[x*x+y*y<2];j+=.04;'*60;print L;i+=.1;"""*20
#i=1;exec"""L='';j=-1.6;exec'x=y=0;exec"x,y=2*x*y+i,y*y-x*x+j;"*20;L+=" O"[x*x+y*y<2];j+=.04;'*60;print L;i-=.1;"""*20
#i=1;exec'L="";j=-1.6;exec\'x=y=0;exec"x,y=2*x*y+i,y*y-x*x+j;"*20;L+=" O"[x*x+y*y<2];j+=.04;\'*60;print L;i-=.1;'*20
i=1;exec'L="";j=-1.6;exec\'x=y=0;exec"x,y=2*x*y+i,y*y-x*x+j;"*20;L+=" O"[x*x+y*y<2];j+=.04;\'*60;print L;i-=.1;'*20
