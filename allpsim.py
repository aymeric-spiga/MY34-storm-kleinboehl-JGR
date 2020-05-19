#! /usr/bin/env python

from ppclass import pp

#pp.py diagfi210_240_LT3_precast.nc -v psim -x 999 -t 0 \
# -Z -C seismic -N -20 -M 20 --xp 16 --yp 8 -m 1e-9 \
# -U "$10^9$ kg/s" -F "%.0f" --ymin 1 -T nighttime \
# -T daytime --ylabel "pressure (Pa)" -o psim_day_night \
# -O png -c psim -D 40

lvl = 60 #20
fac = 1.e-9

ps = pp()
ps.nopickle = True
ps.xp = 16
ps.yp = 8
ps.var = ["psim","psim"]
ps.vargoal = ["main","contour"]
ps.c = "psim"
ps.x = 999
ps.t = 0
ps.invert = True
ps.logy = True
ps.colorbar = "seismic"
ps.vmin = -lvl
ps.vmax = +lvl
ps.out = "png"
ps.div = 24
ps.ylabel = "pressure (Pa)"
ps.xlabel = "latitude"
ps.units = r'$10^9$ kg/s'
ps.ymin = 1
ps.fmt = "%.0f"
#ps.clab = True
ps.clev = [\
-60/fac,\
-55/fac,\
-50/fac,\
-45/fac,\
-40/fac,\
-35/fac,\
-30/fac,\
-25/fac,\
-20/fac,\
-15/fac,\
-10/fac,\
-5/fac,\
5/fac,\
10/fac,\
15/fac,\
20/fac,\
25/fac,\
30/fac,\
35/fac,\
40/fac,\
45/fac,\
50/fac,\
55/fac,\
60/fac]

for lt in range(3,27,3):
    print lt
    #lt = 3
    #ps.file = "diagfi210_240_LT"+str(lt)+"_precast.nc"
    ps.file = "psim_Ls210_LT"+str(lt)+".nc"
    ps.filename = "psim_LT"+str(lt)
    ps.title = "local time "+str(lt)
    ps.get()
    ps = fac * ps
    ps.defineplot()
    #ps.p[0].showcb = False
    ps.makeplot()


mmc,xx,yy,zz,tt = pp(file="psim_Ls210_MEAN.nc",useindex="1000",t="0,7",x=999,var="psim").getfd()

lvl = 20
ps.div = 40
lvl = 10
ps.div = 20
ps.filename = "psim_MEAN"
ps.title = "diurnal mean"
ps.vmin = -lvl
ps.vmax = +lvl
ps.clev = [\
-18,\
-17,\
-16,\
-15,\
-14,\
-13,\
-12,\
-11,\
-10,\
-9,\
-8,\
-7,\
-6,\
-5,\
-4,\
-3,\
-2,\
-1,\
+1,\
+2,\
+3,\
+4,\
+5,\
+6,\
+7,\
+8,\
+9,\
+10,\
+11,\
+12,\
+13,\
+14,\
+15,\
+16,\
+17,\
+18\
]
ps.defineplot()

ps.p[0].f = fac * mmc
ps.p[0].c = ps.p[0].f
ps.p[0].x = yy
ps.p[0].y = zz


ps.makeplot()



