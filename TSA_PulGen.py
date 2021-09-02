import math
import numpy as np

import csv

toffset = 0.000001
vdd = 1.2
period = 0.000001
transition_time = 0.0000000001
# write WL
f = open('wl_source.txt', 'w')
f.write('simulator lang=spectre\n')
for cnt_name in range(96):

    f.write('vwl_%s (WL\\<%s\\> VSS) vsource type=pwl wave=[  \\\n'%(cnt_name, cnt_name))
    f.write('%s %s \\\n' % ('{0:.12f}'.format(0), '{0:.12f}'.format(float(0) * vdd)))
    f.write('%s %s \\\n' % ('{0:.12f}'.format(toffset), '{0:.12f}'.format(float(0) * vdd)))

    f.write('%s %s  \\\n' % ('{0:.12f}'.format(period * (cnt_name + 1) + toffset),'{0:.12f}'.format(0 * vdd)))
    f.write('%s %s  \\\n' % ('{0:.12f}'.format(period * (cnt_name + 1) + transition_time + toffset),'{0:.12f}'.format(1 * vdd)))

    f.write('%s %s  \\\n' % ('{0:.12f}'.format(period * (cnt_name + 2) + toffset),'{0:.12f}'.format(1 * vdd)))
    f.write('%s %s] \n\n' % ('{0:.12f}'.format(period * (cnt_name + 2) + transition_time + toffset),'{0:.12f}'.format(0 * vdd)))

f.close()
