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
  
bld_dof = np.array([3136.,6400.,14400.,25600.,50176.])

bld_ls_zone_1 = np.array([np.abs(11.9020839282-ls_ref_1),
  np.abs(11.9295860381-ls_ref_1),np.abs(11.9442764001-ls_ref_1),
  np.abs(11.9491133437-ls_ref_1),np.abs(11.9518831301-ls_ref_1)])
bld_ls_zone_2 = np.array([np.abs(0.553699159282-ls_ref_2),
  np.abs(0.547286164022-ls_ref_2),np.abs(0.543862916701-ls_ref_2),
  np.abs(0.542728993852-ls_ref_2),np.abs(0.54207476615-ls_ref_2)])
bld_ls_zone_3 = np.array([np.abs(0.860803663537-ls_ref_3),
  np.abs(0.847340025272-ls_ref_3),np.abs(0.840187506983-ls_ref_3),
  np.abs(0.837852346013-ls_ref_3),np.abs(0.836525673494-ls_ref_3)])
bld_ls_zone_4 = np.array([np.abs(19.0817209606-ls_ref_4),
  np.abs(19.140982451-ls_ref_4),np.abs(19.171619975-ls_ref_4),
  np.abs(19.1814641939-ls_ref_4),np.abs(19.1870123946-ls_ref_4)])

bld_glc_zone_1 = np.array([np.abs(11.9023773431-glc_ref_1),
  np.abs(11.9298080094-glc_ref_1),np.abs(11.9444478841-glc_ref_1),
  np.abs(11.9492656206-glc_ref_1),np.abs(11.9520251548-glc_ref_1)])
bld_glc_zone_2 = np.array([np.abs(0.553610986043-glc_ref_2),
  np.abs(0.547216373242-glc_ref_2),np.abs(0.543806020831-glc_ref_2),
  np.abs(0.54267690842-glc_ref_2),np.abs(0.54202514266-glc_ref_2)])
bld_glc_zone_3 = np.array([np.abs(0.860709568176-glc_ref_3),
  np.abs(0.847274597823-glc_ref_3),np.abs(0.840142347796-glc_ref_3),
  np.abs(0.837815151926-glc_ref_3),np.abs(0.836493044091-glc_ref_3)])
bld_glc_zone_4 = np.array([np.abs(19.0821894179-glc_ref_4),
  np.abs(19.1413269727-glc_ref_4),np.abs(19.1718786758-glc_ref_4),
  np.abs(19.181690221-glc_ref_4),np.abs(19.1872205875-glc_ref_4)])  
  

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

fig3 = pylab.figure(num=3)
ax3 = fig3.add_subplot(111)
ax3.loglog(bld_dof,bld_ls_zone_1,'s-',bld_dof,bld_ls_zone_2,'s-',bld_dof,bld_ls_zone_3,'s-',bld_dof,bld_ls_zone_4,'s-',[3000,60000],[0.07,0.0035])
ax3.set_xlabel('log(# of unknowns)')
ax3.set_ylabel('log(error)')
ax3.legend(('Zone 1','Zone 2','Zone 3','Zone 4','Linear'),loc='upper left')
ax3.grid(True)

fig4 = pylab.figure(num=4)
ax4 = fig4.add_subplot(111)
ax4.loglog(dof,glc_zone_1,'s-',dof,glc_zone_2,'s-',dof,glc_zone_3,'s-',dof,glc_zone_4,'s-',[3000,60000],[0.07,0.0035])
ax4.set_xlabel('log(# of unknowns)')
ax4.set_ylabel('log(error)')
ax4.legend(('Zone 1','Zone 2','Zone 3','Zone 4','Linear'),loc='upper left')
ax4.grid(True)

pylab.show()
