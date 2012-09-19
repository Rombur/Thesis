#! /usr/bin/env python
#----------------------------------------------------------------------------#
# Python code
# Author: Bruno Turcksin
# Date: 2012-09-19 10:14:18.504436
#----------------------------------------------------------------------------#

import numpy as np
import pylab

dof = np.array([3144.,6132.,15396.,25524.,51780.])

ls_ref_1 = 11.9539148892
ls_ref_2 = 0.54158890028
ls_ref_3 = 0.835561029899
ls_ref_4 = 19.1910062885
ls_zone_1 = np.array([np.abs(11.918326621-ls_ref_1),
  np.abs(11.9409681044-ls_ref_1),np.abs(11.9473948898-ls_ref_1),
  np.abs(11.9510654617-ls_ref_1),np.abs(11.9520856169-ls_ref_1)])
ls_zone_2 = np.array([np.abs(0.547362661934-ls_ref_2),
  np.abs(0.544469649011-ls_ref_2),np.abs(0.542994460593-ls_ref_2),
  np.abs(0.542402860473-ls_ref_2),np.abs(0.542019101323-ls_ref_2)])
ls_zone_3 = np.array([np.abs(0.85225654363-ls_ref_3),
  np.abs(0.84190046208-ls_ref_3),np.abs(0.838540296013-ls_ref_3),
  np.abs(0.836624441455-ls_ref_3),np.abs(0.8363250071-ls_ref_3)])
ls_zone_4 = np.array([np.abs(19.1351956005-ls_ref_4),
  np.abs(19.1608814707-ls_ref_4),np.abs(19.1784951165-ls_ref_4),
  np.abs(19.1848483758-ls_ref_4),np.abs(19.187796122-ls_ref_4)])

glc_ref_1 = 11.9540542452
glc_ref_2 = 0.541539678016
glc_ref_3 = 0.835530238282
glc_ref_4 = 19.1912088357
glc_zone_1 = np.array([np.abs(11.9185872-glc_ref_1),
  np.abs(11.9411503344-glc_ref_1),np.abs(11.9475592157-glc_ref_1),
  np.abs(11.951210227-glc_ref_1),np.abs(11.9522271094-glc_ref_1)])
glc_zone_2 = np.array([np.abs(0.54728719918-glc_ref_2),
  np.abs(0.544410111789-glc_ref_2),np.abs(0.542940589399-glc_ref_2),
  np.abs(0.542352706613-glc_ref_2),np.abs(0.54196973376-glc_ref_2)])
glc_zone_3 = np.array([np.abs(0.852173299226-glc_ref_3),
  np.abs(0.841848752441-glc_ref_3),np.abs(0.838497127668-glc_ref_3),
  np.abs(0.836591284639-glc_ref_3),np.abs(0.836292721138-glc_ref_3)])
glc_zone_4 = np.array([np.abs(19.1355791976-glc_ref_4),
  np.abs(19.1611742042-glc_ref_4),np.abs(19.1787388738-glc_ref_4),
  np.abs(19.18505985-glc_ref_4),np.abs(19.1880017418-glc_ref_4)])

fig = pylab.figure(num=1)
ax = fig.add_subplot(111)
ax.loglog(dof,ls_zone_1,'s-',dof,ls_zone_2,'s-',dof,ls_zone_3,'s-',dof,ls_zone_4,'s-',[3000,60000],[0.07,0.0035])
ax.set_xlabel('log(# of unknowns)')
ax.set_ylabel('log(error)')
ax.legend(('Zone 1','Zone 2','Zone 3','Zone 4','Linear'),loc='upper left')
ax.grid(True)

fig2 = pylab.figure(num=2)
ax2 = fig2.add_subplot(111)
ax2.loglog(dof,glc_zone_1,'s-',dof,glc_zone_2,'s-',dof,glc_zone_3,'s-',dof,glc_zone_4,'s-',[3000,60000],[0.07,0.0035])
ax2.set_xlabel('log(# of unknowns)')
ax2.set_ylabel('log(error)')
ax2.legend(('Zone 1','Zone 2','Zone 3','Zone 4','Linear'),loc='upper left')
ax2.grid(True)

pylab.show()
