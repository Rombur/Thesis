#! /usr/bin/env python
#----------------------------------------------------------------------------#
# Python code
# Author: Bruno Turcksin
# Date: 2012-01-19 14:55:38.631510
#----------------------------------------------------------------------------#

import numpy as np
from mayavi import mlab

def Create_figures() :
  """Open mayavi and create the figures."""

  N = 100
  space = np.linspace(0,1,N)

  x = np.zeros([N])
  y = np.zeros([N])
  z = np.zeros([N,N])

  x = space.copy()
  y = space.copy()
      
  for i in xrange(0,N) :
    for j in xrange(0,N) :
      z[i,j] = (1.-x[i])*(1.-y[j])
  bld1 = mlab.surf(x,y,z,name='Basis function BLD 1')
  bld1.scene.z_plus_view()
  bld1.scene.parallel_projection = True
  Vtk_light(bld1)
  mlab.savefig('bld_1.png')
  mlab.clf()

  z = np.zeros([N,N])
  for i in xrange(0,N) :
    for j in xrange(0,N) :
      z[i,j] = x[i]*(1.-y[j])
  bld2 = mlab.surf(x,y,z,name='Basis function BLD 2')
  bld2.scene.z_plus_view()
  bld2.scene.parallel_projection = True
  Vtk_light(bld2)
  mlab.savefig('bld_2.png')
  mlab.clf()

  z = np.zeros([N,N])
  for i in xrange(0,N) :
    for j in xrange(0,N) :
      z[i,j] = x[i]*y[j]
  bld3 = mlab.surf(x,y,z,name='Basis function BLD 3')
  bld3.scene.z_plus_view()
  bld3.scene.parallel_projection = True
  Vtk_light(bld3)
  mlab.savefig('bld_3.png')
  mlab.clf()

  z = np.zeros([N,N])
  for i in xrange(0,N) :
    for j in xrange(0,N) :
      z[i,j] = (1.-x[i])*y[j]
  bld4 = mlab.surf(x,y,z,name='Basis function BLD 4')
  bld4.scene.z_plus_view()
  bld4.scene.parallel_projection = True
  Vtk_light(bld4)
  mlab.savefig('bld_4.png')
  mlab.clf()

  z = np.zeros([N,N])
  for i in xrange(0,N) :
    for j in xrange(0,N) :
      if y[j]+x[i]<=1. :
        z[i,j] = 1.-x[i]-y[j]
      z[i,j] += Hat_function(x[i],y[j])
  pwld1 = mlab.surf(x,y,z,name='Basis function PWLD 1')
  pwld1.scene.z_plus_view()
  pwld1.scene.parallel_projection = True
  Vtk_light(pwld1)
  mlab.savefig('pwld_1.png')
  mlab.clf()

  z = np.zeros([N,N])
  for i in xrange(0,N) :
    for j in xrange(0,N) :
      if y[j]-x[i]<=0. :
        z[i,j] = x[i]-y[j]
      z[i,j] += Hat_function(x[i],y[j])
  pwld2 = mlab.surf(x,y,z,name='Basis function PWLD 2')
  pwld2.scene.z_plus_view()
  pwld2.scene.parallel_projection = True
  Vtk_light(pwld2)
  mlab.savefig('pwld_2.png')
  mlab.clf()

  z = np.zeros([N,N])
  for i in xrange(0,N) :
    for j in xrange(0,N) :
      if y[j]+x[i]>=1. :
        z[i,j] = x[i]+y[j]-1.
      z[i,j] += Hat_function(x[i],y[j])
  pwld3 = mlab.surf(x,y,z,name='Basis function PWLD 3')
  pwld3.scene.z_plus_view()
  pwld3.scene.parallel_projection = True
  Vtk_light(pwld3)
  mlab.savefig('pwld_3.png')
  mlab.clf()

  z = np.zeros([N,N])
  for i in xrange(0,N) :
    for j in xrange(0,N) :
      if y[j]-x[i]>=0. :
        z[i,j] = y[j]-x[i]
      z[i,j] += Hat_function(x[i],y[j])
  pwld4 = mlab.surf(x,y,z,name='Basis function PWLD 4')
  pwld4.scene.z_plus_view()
  pwld4.scene.parallel_projection = True
  Vtk_light(pwld4)
  mlab.savefig('pwld_4.png')
  mlab.clf()

#----------------------------------------------------------------------------#

def Hat_function(x,y) :
  """Build the hat function."""

  if x+y<=1.:
    if y-x<=0. :
      z = 0.25*2.*y
    else :
      z = 0.25*2.*x
  else :
    if y-x<=0. :
      z = 0.25*(1.-2.*(x-0.5))
    else :
      z = 0.25*(1.-2.*(y-0.5))

  return z

#----------------------------------------------------------------------------#

def Vtk_light(scene) :
  """Use only 1 light coming from the top."""

  camera_light1 = scene.scene.light_manager.lights[0]
  camera_light1.elevation = 0.
  camera_light1.azimuth = 0.
  camera_light2 = scene.scene.light_manager.lights[1]
  camera_light2.active = False
  camera_light3 = scene.scene.light_manager.lights[2]
  camera_light3.active = False

  scene.scene.light_manager.light_mode = 'vtk'
