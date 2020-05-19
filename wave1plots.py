#! /usr/bin/env python

#pp.py -v dustq -v PV -i u -j v  -t 1 -t 1.5 --ymax 0 -W 150


from ppclass import pp
import numpy as np

tablt = [1,1.25,1.5,1.75]


rq = pp()
rq.nopickle = True
rq.out = "png"
rq.xp = 20
rq.yp = 8
rq.file = "PVnew_diagfi210_240_cut.nc"
rq.var = ["dustq","u","v"]
rq.vargoal = ["main","vector","vector"]
rq.wscale = 150.
rq.vmin = -9
rq.vmax = -4

rq.ymax = 0
rq.svx = 2
rq.svy = 2

rq.div = 20
rq.colorbar = "Oranges"
rq.fmt = "%.1f"
rq.units = "log$_{10}$ $q$"
for ttt in tablt:
    rq.t = ttt
    lt = 24.*(ttt - np.floor(ttt))
    rq.filename = "dust%02d"%(lt)
    rq.get()
    rq.defineplot()
    rq.p[0].f = np.log10(rq.p[0].f)
    #rq.p[0].title = "UTC %02d"%(lt)
    rq.makeplot()


rq = pp()
rq.nopickle = True
rq.out = "png"
rq.xp = 20
rq.yp = 8
rq.file = "PVnew_diagfi210_240_cut.nc"
#rq.var = ["PV","u","v"]
#rq.vargoal = ["main","vector","vector"]

rq.var = ["PV","dustq"]
rq.vargoal = ["main","contour"]

rq.proj = "spstere"
rq.blat = -40

rq.wscale = 150.
rq.vmin = -2.4
rq.vmax = +0.0
rq.div = 24
rq.colorbar = "terrain"#"cool"#"plasma_r"#"viridis"
rq.fmt = "%.1f"
rq.units = '$10^{-4}$ m$^2$ s$^{-1}$ K kg$^{-1}$'
for ttt in tablt:
    rq.t = ttt
    lt = 24.*(ttt - np.floor(ttt))
    rq.filename = "PV%02d"%(lt)
    rq.get()
    rq.defineplot()
    rq.p[0].f = rq.p[0].f * 1e2
    #rq.p[0].title = "UTC %02d"%(lt)
    rq.p[0].c = np.log10(rq.p[0].c)
    rq.p[0].clev = [-9.,-8.5,-8,-7.5,-7,-6.5,-6,-5.5,-5,-4.5,-4,-3.5,-3]
    rq.p[0].clab = True
    rq.makeplot()





