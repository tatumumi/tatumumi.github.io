#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 07:44:12 2023

@author: tatumumiamaka
"""

import numpy as np
import matplotlib.pyplot as plt

#.............................................................................#

def vecFRK4x(fx, fv, t, xold, vold, dt, params):
  k1x = dt*fx(t, xold, vold, params)
  k1v = dt*fv(t, xold, vold, params)

  k2x = dt*fx(t+dt/2.0, (xold+0.5*k1x), (vold+0.5*k1v), params)
  k2v = dt*fv(t+dt/2.0, (xold+0.5*k1x), (vold+0.5*k1v), params)

  k3x = dt*fx(t+dt/2.0, (xold+0.5*k2x), (vold+0.5*k2v), params)
  k3v = dt*fv(t+dt/2.0, (xold+0.5*k2x), (vold+0.5*k2v), params)

  k4x = dt*fx(t+dt, (xold+k3x), (vold+k3v), params)
  k4v = dt*fv(t+dt, (xold+k3x), (vold+k3v), params)
  
  return (k1x+ 2.0*k2x+ 2.0*k3x + k4x)/6.0

def vecFRK4v(fx, fv, t, xold, vold, dt, params):
  k1x = dt*fx(t, xold, vold, params)
  k1v = dt*fv(t, xold, vold, params)

  k2x = dt*fx(t+dt/2.0, (xold+0.5*k1x), (vold+0.5*k1v), params)
  k2v = dt*fv(t+dt/2.0, (xold+0.5*k1x), (vold+0.5*k1v), params)

  k3x = dt*fx(t+dt/2.0, (xold+0.5*k2x), (vold+0.5*k2v), params)
  k3v = dt*fv(t+dt/2.0, (xold+0.5*k2x), (vold+0.5*k2v), params)

  k4x = dt*fx(t+dt, (xold+k3x), (vold+k3v), params)
  k4v = dt*fv(t+dt, (xold+k3x), (vold+k3v), params)
  
  return (k1v+ 2.0*k2v+ 2.0*k3v + k4v)/6.0

#earth
def f_vE(t, r, v, params):
  G = params[0]
  Mass_earth = params[1]
  Mass_sun = params[2]
  Mass_mars = params[3]
  Mass_jupiter = params[4]
  Mass_saturn = params[5]
  Mass_venus = params[6]
  Mass_mercury = params[7]
  Mass_uranus = params[8]
  Mass_neptune = params[9]
  rtEold = np.array(params[11])
  rtSold = np.array(params[12])
  rtMold = np.array(params[13])
  rtJold = np.array(params[14])
  rtSaold = np.array(params[15])
  rtVold = np.array(params[16])
  rtMcold = np.array(params[17])
  rtUold = np.array(params[18])
  rtNold = np.array(params[19])
  
  DrS = r - rtSold
  RS = np.linalg.norm(DrS)
  
  DrM= r - rtMold
  RM = np.linalg.norm(DrM)
  
  DrJ = r - rtJold
  RJ = np.linalg.norm(DrJ)
  
  DrV = r - rtVold
  RV = np.linalg.norm(DrV)
  
  DrSa = r - rtSaold
  RSa = np.linalg.norm(DrSa)
  
  DrMc = r - rtMcold
  RMc = np.linalg.norm(DrMc)
  
  DrU = r - rtUold
  RU = np.linalg.norm(DrU)
  
  DrN = r - rtNold
  RN = np.linalg.norm(DrN)
  

  FgS = -(G*Mass_earth*Mass_sun / RS**3) * DrS
  FgM = -(G*Mass_earth*Mass_mars / RM**3) * DrM
  FgJ = -(G*Mass_jupiter*Mass_earth/ RJ**3) * DrJ
  FgV = -(G*Mass_earth*Mass_venus / RV**3) * DrV
  FgSa = -(G*Mass_earth*Mass_saturn / RSa**3) * DrSa
  FgMc = -(G*Mass_earth*Mass_mercury / RMc**3) * DrMc
  FgU = -(G*Mass_earth*Mass_uranus / RU**3) * DrU
  FgN = -(G*Mass_earth*Mass_neptune / RN**3) * DrN
  
  
  return (FgM+FgJ+FgV+FgS+FgSa+FgMc+FgU+FgN) / Mass_earth

#sun
def f_vS(t, r, v, params):
  G = params[0]
  Mass_earth = params[1]
  Mass_sun = params[2]
  Mass_mars = params[3]
  Mass_jupiter = params[4]
  Mass_saturn = params[5]
  Mass_venus = params[6]
  Mass_mercury = params[7]
  Mass_uranus = params[8]
  Mass_neptune = params[9]
  rtEold = np.array(params[11])
  rtSold = np.array(params[12])
  rtMold = np.array(params[13])
  rtJold = np.array(params[14])
  rtSaold = np.array(params[15])
  rtVold = np.array(params[16])
  rtMcold = np.array(params[17])
  rtUold = np.array(params[18])
  rtNold = np.array(params[19])
  
  DrE = r - rtEold
  RE = np.linalg.norm(DrE)
  
  DrM = r - rtMold
  RM = np.linalg.norm(DrM)
  
  DrJ = r - rtJold
  RJ = np.linalg.norm(DrJ)
  
  DrV = r - rtVold
  RV = np.linalg.norm(DrV)
  
  DrSa = r - rtSaold
  RSa = np.linalg.norm(DrSa)
  
  DrMc = r - rtMcold
  RMc = np.linalg.norm(DrMc)
  
  DrU = r - rtUold
  RU = np.linalg.norm(DrU)
  
  DrN = r - rtNold
  RN = np.linalg.norm(DrN)
  

  FgE = -(G*Mass_earth*Mass_sun / RE**3) * DrE
  FgM = -(G*Mass_sun*Mass_mars / RM**3) * DrM
  FgJ = -(G*Mass_jupiter*Mass_sun/ RJ**3) * DrJ
  FgV = -(G*Mass_sun*Mass_venus / RV**3) * DrV
  FgSa = -(G*Mass_sun*Mass_saturn / RSa**3) * DrSa
  FgMc = -(G*Mass_sun*Mass_mercury / RMc**3) * DrMc
  FgU = -(G*Mass_sun*Mass_uranus / RU**3) * DrU
  FgN = -(G*Mass_sun*Mass_neptune / RN**3) * DrN
  
  
  return (FgE+FgJ+FgV+FgM+FgSa+FgMc+FgU+FgN) / Mass_sun

#mars
def f_vM(t, r, v, params):
  G = params[0]
  Mass_earth = params[1]
  Mass_sun = params[2]
  Mass_mars = params[3]
  Mass_jupiter = params[4]
  Mass_saturn = params[5]
  Mass_venus = params[6]
  Mass_mercury = params[7]
  Mass_uranus = params[8]
  Mass_neptune = params[9]
  rtEold = np.array(params[11])
  rtSold = np.array(params[12])
  rtMold = np.array(params[13])
  rtJold = np.array(params[14])
  rtSaold = np.array(params[15])
  rtVold = np.array(params[16])
  rtMcold = np.array(params[17])
  rtUold = np.array(params[18])
  rtNold = np.array(params[19])

  DrS = r - rtSold
  RS = np.linalg.norm(DrS)
  
  DrE = r - rtEold
  RE = np.linalg.norm(DrE)
  
  DrJ = r - rtJold
  RJ = np.linalg.norm(DrJ)
  
  DrV = r - rtVold
  RV = np.linalg.norm(DrV)
  
  DrSa = r - rtSaold
  RSa = np.linalg.norm(DrSa)
  
  DrMc = r - rtMcold
  RMc = np.linalg.norm(DrMc)
  
  DrU = r - rtUold
  RU = np.linalg.norm(DrU)
  
  DrN = r - rtNold
  RN = np.linalg.norm(DrN)
  

  FgE = -(G*Mass_earth*Mass_mars / RE**3) * DrE
  FgS = -(G*Mass_mars*Mass_sun / RS**3) * DrS
  FgJ = -(G*Mass_jupiter*Mass_mars / RJ**3) * DrJ
  FgV = -(G*Mass_mars*Mass_venus / RV**3) * DrV
  FgSa = -(G*Mass_mars*Mass_saturn / RSa**3) * DrSa
  FgMc = -(G*Mass_mars*Mass_mercury / RMc**3) * DrMc
  FgU = -(G*Mass_mars*Mass_uranus / RU**3) * DrU
  FgN = -(G*Mass_mars*Mass_neptune / RN**3) * DrN
  
  
  return (FgS+FgJ+FgV+FgE+FgSa+FgMc+FgU+FgN) / Mass_mars

#jupiter
def f_vJ(t, r, v, params):
  G = params[0]
  Mass_earth = params[1]
  Mass_sun = params[2]
  Mass_mars = params[3]
  Mass_jupiter = params[4]
  Mass_saturn = params[5]
  Mass_venus = params[6]
  Mass_mercury = params[7]
  Mass_uranus = params[8]
  Mass_neptune = params[9]
  rtEold = np.array(params[11])
  rtSold = np.array(params[12])
  rtMold = np.array(params[13])
  rtJold = np.array(params[14])
  rtSaold = np.array(params[15])
  rtVold = np.array(params[16])
  rtMcold = np.array(params[17])
  rtUold = np.array(params[18])
  rtNold = np.array(params[19])

  DrS = r - rtSold
  RS = np.linalg.norm(DrS)
  
  DrE = r - rtEold
  RE = np.linalg.norm(DrE)
  
  DrM = r - rtMold
  RM = np.linalg.norm(DrM)
  
  DrV = r - rtVold
  RV = np.linalg.norm(DrV)
  
  DrSa = r - rtSaold
  RSa = np.linalg.norm(DrSa)
  
  DrMc = r - rtMcold
  RMc = np.linalg.norm(DrMc)
  
  DrU = r - rtUold
  RU = np.linalg.norm(DrU)
  
  DrN = r - rtNold
  RN = np.linalg.norm(DrN)
  

  FgE = -(G*Mass_earth*Mass_jupiter / RE**3) * DrE
  FgS = -(G*Mass_jupiter*Mass_sun / RS**3) * DrS
  FgM = -(G*Mass_jupiter*Mass_mars / RM**3) * DrM
  FgV = -(G*Mass_jupiter*Mass_venus / RV**3) * DrV
  FgSa = -(G*Mass_jupiter*Mass_saturn / RSa**3) * DrSa
  FgMc = -(G*Mass_jupiter*Mass_mercury / RMc**3) * DrMc
  FgU = -(G*Mass_jupiter*Mass_uranus / RU**3) * DrU
  FgN = -(G*Mass_jupiter*Mass_neptune / RN**3) * DrN
  
  
  return (FgS+FgM+FgV+FgE+FgSa+FgMc+FgU+FgN) / Mass_jupiter

  
#venus
def f_vV(t, r, v, params):
  G = params[0]
  Mass_earth = params[1]
  Mass_sun = params[2]
  Mass_mars = params[3]
  Mass_jupiter = params[4]
  Mass_saturn = params[5]
  Mass_venus = params[6]
  Mass_mercury = params[7]
  Mass_uranus = params[8]
  Mass_neptune = params[9]
  rtEold = np.array(params[11])
  rtSold = np.array(params[12])
  rtMold = np.array(params[13])
  rtJold = np.array(params[14])
  rtSaold = np.array(params[15])
  rtVold = np.array(params[16])
  rtMcold = np.array(params[17])
  rtUold = np.array(params[18])
  rtNold = np.array(params[19])

  DrS = r - rtSold
  RS = np.linalg.norm(DrS)
  
  DrE = r - rtEold
  RE = np.linalg.norm(DrE)
  
  DrM = r - rtMold
  RM = np.linalg.norm(DrM)
  
  DrJ = r - rtJold
  RJ = np.linalg.norm(DrJ)
  
  DrSa = r - rtSaold
  RSa = np.linalg.norm(DrSa)
  
  DrMc = r - rtMcold
  RMc = np.linalg.norm(DrMc)
  
  DrU = r - rtUold
  RU = np.linalg.norm(DrU)
  
  DrN = r - rtNold
  RN = np.linalg.norm(DrN)
  

  FgE = -(G*Mass_earth*Mass_venus / RE**3) * DrE
  FgS = -(G*Mass_venus*Mass_sun / RS**3) * DrS
  FgM = -(G*Mass_venus*Mass_mars / RM**3) * DrM
  FgJ = -(G*Mass_venus*Mass_jupiter / RJ**3) * DrJ
  FgSa = -(G*Mass_venus*Mass_saturn / RSa**3) * DrSa
  FgMc = -(G*Mass_venus*Mass_mercury / RMc**3) * DrMc
  FgU = -(G*Mass_venus*Mass_uranus / RU**3) * DrU
  FgN = -(G*Mass_venus*Mass_neptune / RN**3) * DrN
  
  
  return (FgS+FgM+FgJ+FgE+FgSa+FgMc+FgU+FgN) / Mass_venus

#saturn
def f_vSa(t, r, v, params):
  G = params[0]
  Mass_earth = params[1]
  Mass_sun = params[2]
  Mass_mars = params[3]
  Mass_jupiter = params[4]
  Mass_saturn = params[5]
  Mass_venus = params[6]
  Mass_mercury = params[7]
  Mass_uranus = params[8]
  Mass_neptune = params[9]
  rtEold = np.array(params[11])
  rtSold = np.array(params[12])
  rtMold = np.array(params[13])
  rtJold = np.array(params[14])
  rtSaold = np.array(params[15])
  rtVold = np.array(params[16])
  rtMcold = np.array(params[17])
  rtUold = np.array(params[18])
  rtNold = np.array(params[19])

  DrS = r - rtSold
  RS = np.linalg.norm(DrS)
  
  DrE = r - rtEold
  RE = np.linalg.norm(DrE)
  
  DrM = r - rtMold
  RM = np.linalg.norm(DrM)
  
  DrJ = r - rtJold
  RJ = np.linalg.norm(DrJ)
  
  DrV = r - rtVold
  RV = np.linalg.norm(DrV)
  
  DrMc = r - rtMcold
  RMc = np.linalg.norm(DrMc)
  
  DrU = r - rtUold
  RU = np.linalg.norm(DrU)
  
  DrN = r - rtNold
  RN = np.linalg.norm(DrN)
  

  FgE = -(G*Mass_earth*Mass_saturn / RE**3) * DrE
  FgS = -(G*Mass_saturn*Mass_sun / RS**3) * DrS
  FgM = -(G*Mass_saturn*Mass_mars / RM**3) * DrM
  FgJ = -(G*Mass_saturn*Mass_jupiter / RJ**3) * DrJ
  FgV = -(G*Mass_saturn*Mass_venus / RV**3) * DrV
  FgMc = -(G*Mass_saturn*Mass_mercury / RMc**3) * DrMc
  FgU = -(G*Mass_saturn*Mass_uranus / RU**3) * DrU
  FgN = -(G*Mass_saturn*Mass_neptune / RN**3) * DrN
  
  return (FgS+FgM+FgJ+FgE+FgV+FgMc+FgU+FgN) / Mass_saturn


#mercury
def f_vMc(t, r, v, params):
  G = params[0]
  Mass_earth = params[1]
  Mass_sun = params[2]
  Mass_mars = params[3]
  Mass_jupiter = params[4]
  Mass_saturn = params[5]
  Mass_venus = params[6]
  Mass_mercury = params[7]
  Mass_uranus = params[8]
  Mass_neptune = params[9]
  rtEold = np.array(params[11])
  rtSold = np.array(params[12])
  rtMold = np.array(params[13])
  rtJold = np.array(params[14])
  rtSaold = np.array(params[15])
  rtVold = np.array(params[16])
  rtMcold = np.array(params[17])
  rtUold = np.array(params[18])
  rtNold = np.array(params[19])

  DrS = r - rtSold
  RS = np.linalg.norm(DrS)
  
  DrE = r - rtEold
  RE = np.linalg.norm(DrE)
  
  DrM = r - rtMold
  RM = np.linalg.norm(DrM)
  
  DrJ = r - rtJold
  RJ = np.linalg.norm(DrJ)
  
  DrV = r - rtVold
  RV = np.linalg.norm(DrV)
  
  DrSa = r - rtSaold
  RSa = np.linalg.norm(DrSa)
  
  DrU = r - rtUold
  RU = np.linalg.norm(DrU)
  
  DrN = r - rtNold
  RN = np.linalg.norm(DrN)
  

  FgE = -(G*Mass_earth*Mass_mercury / RE**3) * DrE
  FgS = -(G*Mass_mercury*Mass_sun / RS**3) * DrS
  FgM = -(G*Mass_mercury*Mass_mars / RM**3) * DrM
  FgJ = -(G*Mass_mercury*Mass_jupiter / RJ**3) * DrJ
  FgV = -(G*Mass_mercury*Mass_venus / RV**3) * DrV
  FgSa = -(G*Mass_saturn*Mass_mercury / RSa*3) * DrSa
  FgU = -(G*Mass_mercury*Mass_uranus / RU**3) * DrU
  FgN = -(G*Mass_mercury*Mass_neptune / RN**3) * DrN
  
  return (FgS+FgM+FgJ+FgE+FgV+FgSa+FgU+FgN) / Mass_mercury

#uranus
def f_vU(t, r, v, params):
  G = params[0]
  Mass_earth = params[1]
  Mass_sun = params[2]
  Mass_mars = params[3]
  Mass_jupiter = params[4]
  Mass_saturn = params[5]
  Mass_venus = params[6]
  Mass_mercury = params[7]
  Mass_uranus = params[8]
  Mass_neptune = params[9]
  rtEold = np.array(params[11])
  rtSold = np.array(params[12])
  rtMold = np.array(params[13])
  rtJold = np.array(params[14])
  rtSaold = np.array(params[15])
  rtVold = np.array(params[16])
  rtMcold = np.array(params[17])
  rtUold = np.array(params[18])
  rtNold = np.array(params[19])

  DrS = r - rtSold
  RS = np.linalg.norm(DrS)
  
  DrE = r - rtEold
  RE = np.linalg.norm(DrE)
  
  DrM = r - rtMold
  RM = np.linalg.norm(DrM)
  
  DrJ = r - rtJold
  RJ = np.linalg.norm(DrJ)
  
  DrV = r - rtVold
  RV = np.linalg.norm(DrV)
  
  DrSa = r - rtSaold
  RSa = np.linalg.norm(DrSa)
  
  DrMc = r - rtMcold
  RMc = np.linalg.norm(DrMc)
  
  DrN = r - rtNold
  RN = np.linalg.norm(DrN)
  

  FgE = -(G*Mass_earth*Mass_uranus / RE**3) * DrE
  FgS = -(G*Mass_uranus*Mass_sun / RS**3) * DrS
  FgM = -(G*Mass_uranus*Mass_mars / RM**3) * DrM
  FgJ = -(G*Mass_uranus*Mass_jupiter / RJ**3) * DrJ
  FgV = -(G*Mass_uranus*Mass_venus / RV**3) * DrV
  FgSa = -(G*Mass_uranus*Mass_saturn / RSa*3) * DrSa
  FgMc = -(G*Mass_uranus*Mass_mercury / RMc**3) * DrMc
  FgN = -(G*Mass_uranus*Mass_neptune / RN**3) * DrN
  
  return (FgS+FgM+FgJ+FgE+FgV+FgSa+FgMc+FgN) / Mass_uranus


#neptune
def f_vN(t, r, v, params):
  G = params[0]
  Mass_earth = params[1]
  Mass_sun = params[2]
  Mass_mars = params[3]
  Mass_jupiter = params[4]
  Mass_saturn = params[5]
  Mass_venus = params[6]
  Mass_mercury = params[7]
  Mass_uranus = params[8]
  Mass_neptune = params[9]
  rtEold = np.array(params[11])
  rtSold = np.array(params[12])
  rtMold = np.array(params[13])
  rtJold = np.array(params[14])
  rtSaold = np.array(params[15])
  rtVold = np.array(params[16])
  rtMcold = np.array(params[17])
  rtUold = np.array(params[18])
  rtNold = np.array(params[19])

  DrS = r - rtSold
  RS = np.linalg.norm(DrS)
  
  DrE = r - rtEold
  RE = np.linalg.norm(DrE)
  
  DrM = r - rtMold
  RM = np.linalg.norm(DrM)
  
  DrJ = r - rtJold
  RJ = np.linalg.norm(DrJ)
  
  DrV = r - rtVold
  RV = np.linalg.norm(DrV)
  
  DrSa = r - rtSaold
  RSa = np.linalg.norm(DrSa)
  
  DrMc = r - rtMcold
  RMc = np.linalg.norm(DrMc)
  
  DrU = r - rtUold
  RU = np.linalg.norm(DrU)
  

  FgE = -(G*Mass_earth*Mass_neptune / RE**3) * DrE
  FgS = -(G*Mass_neptune*Mass_sun / RS**3) * DrS
  FgM = -(G*Mass_neptune*Mass_mars / RM**3) * DrM
  FgJ = -(G*Mass_neptune*Mass_jupiter / RJ**3) * DrJ
  FgV = -(G*Mass_neptune*Mass_venus / RV**3) * DrV
  FgSa = -(G*Mass_neptune*Mass_saturn / RSa*3) * DrSa
  FgMc = -(G*Mass_neptune*Mass_mercury / RMc**3) * DrMc
  FgU = -(G*Mass_uranus*Mass_neptune / RU**3) * DrU
  
  return (FgS+FgM+FgJ+FgE+FgV+FgSa+FgMc+FgU) / Mass_neptune

def f_vShip(t, r, v, params):
  G = params[0]
  Mass_earth = params[1]
  Mass_sun = params[2]
  Mass_mars = params[3]
  Mass_jupiter = params[4]
  Mass_saturn = params[5]
  Mass_venus = params[6]
  Mass_mercury = params[7]
  Mass_uranus = params[8]
  Mass_neptune = params[9]
  Mass_ship = params[10]
  rtEold = np.array(params[11])
  rtSold = np.array(params[12])
  rtMold = np.array(params[13])
  rtJold = np.array(params[14])
  rtSaold = np.array(params[15])
  rtVold = np.array(params[16])
  rtMcold = np.array(params[17])
  rtUold = np.array(params[18])
  rtNold = np.array(params[19])
  rtShip_old = np.array(params[20])
  
  DrE = r - rtEold
  RE = np.linalg.norm(DrE)
  
  DrS = r - rtSold
  RS = np.linalg.norm(DrS)
  
  DrM= r - rtMold
  RM = np.linalg.norm(DrM)
  
  DrJ = r - rtJold
  RJ = np.linalg.norm(DrJ)
  
  DrV = r - rtVold
  RV = np.linalg.norm(DrV)
  
  DrSa = r - rtSaold
  RSa = np.linalg.norm(DrSa)
  
  DrMc = r - rtMcold
  RMc = np.linalg.norm(DrMc)
  
  DrU = r - rtUold
  RU = np.linalg.norm(DrU)
  
  DrN = r - rtNold
  RN = np.linalg.norm(DrN)
  
  FgE = -(G*Mass_ship*Mass_earth / RE**3) * DrE
  FgS = -(G*Mass_ship*Mass_sun / RS**3) * DrS
  FgM = -(G*Mass_ship*Mass_mars / RM**3) * DrM
  FgJ = -(G*Mass_jupiter*Mass_ship/ RJ**3) * DrJ
  FgV = -(G*Mass_ship*Mass_venus / RV**3) * DrV
  FgSa = -(G*Mass_ship*Mass_saturn / RSa**3) * DrSa
  FgMc = -(G*Mass_ship*Mass_mercury / RMc**3) * DrMc
  FgU = -(G*Mass_ship*Mass_uranus / RU**3) * DrU
  FgN = -(G*Mass_ship*Mass_neptune / RN**3) * DrN
  
  return (FgM+FgJ+FgV+FgS+FgSa+FgMc+FgU+FgN+FgE) / Mass_ship

def f_rE(t, r, v, params):
  return np.array(v)

def f_rS(t, r, v, params):
  return np.array(v)

def f_rM(t, r, v, params):
    return np.array(v)

def f_rJ(t, r, v, params):
    return np.array(v)

def f_rSA(t, r, v, params):
    return np.array(v)

def f_rV(t, r, v, params):
    return np.array(v)

def f_rMc(t, r, v, params):
    return np.array(v)

def f_rU(t, r, v, params):
    return np.array(v)

def f_rN(t, r, v, params):
    return np.array(v)

def f_rShip(t, r, v, params):
    return np.array(v)

#.............................................................................#


G = 6.6730e-11
Radius_earth = 6.3710e6
Mass_earth = 5.9736e24
Mass_sun = 1.988544e30
Mass_mars = 6.39e23
Mass_jupiter = 1.89813e27
Mass_saturn = 5.683e26
Mass_venus = 4.867e24
Mass_mercury = 3.302e23
Mass_uranus = 8.681e25
Mass_neptune = 1.024e26
Mass_ship = 1315417.873
Radius_sun = 695700e3
Dist_EarthSun = 1.5e11
Earth_orbit = 365
Ttot = 2.8e7
dt = 1000

#data extracted from JPL Horizons
rtEold = [1.132685657004147e11,9.415666424813995e10,2.214607619884610e07]
vtEold = [-1.951626160987056e04,2.280284099719450e04,-5.364041214654947e-01]

rtSold = [-9.202670706759800e08,-6.984640546752170e08,2.786275545373460e07]
vtSold = [1.185251361218829e01,-7.542606423242878e00,-1.825825600783471e-01]

rtMold = [4.016110659921604e10,2.266129642464140e11,3.783651590928748e09]
vtMold = [-2.291588107808676e04,6.360701843611478e03,6.955886618299711e02]

rtJold = [2.234280624557506e11,7.227392966628635e11,-7.996650816235423e09]
vtJold = [-1.263198864129004e04,4.482214838116185e03,2.640360595458855e02]

rtSaold = [1.407227785178647e12,-3.136670243385941e11,-5.057477915342526e10]
vtSaold = [1.565563967513693e03,9.408668931121090e03,-2.261731533704276e02]

rtVold = [7.682651155846827e10,-7.680283431670529e10,-5.503393228809241e09]
vtVold = [2.428430241876983e04,2.488814910172179e04,-1.058813653013743e03]

rtMcold = [1.500436504784467e10,-6.644604689052798e10,-6.805752411158472e09]
vtMcold = [3.758786020280949e04,1.394601812832913e03,-2.306432294572655e03]

rtUold = [1.689423967464181e12,2.388395767818121e12,-1.301627994791734e10]
vtUold = [-5.609423915743850e03,3.615158302710255e03,8.608346500404851e01]
          
rtNold = [4.468610232621434e12,-1.239430217299966e11,-1.004314903177636e11]
vtNold = [1.146484271038958e02, 5.465714736600558e03,-1.147873639051187e02]

theta0 = np.deg2rad(29)
Orb_Park = 200e3 + 6.3710e6
Orb = np.array([Orb_Park*np.sin(theta0), Orb_Park*np.cos(theta0),0.0])
rtShip_old = rtEold + Orb

correction = 4.7e3 
addition = np.array([(correction)*np.cos(theta0),(correction)*np.sin(theta0),0.0])
vtShip_old = vtEold + addition
print(vtShip_old)

T = np.arange(0, Ttot, dt)

N = int(Ttot / 5000)+1


REoft = np.zeros((N, 3)) 
VEoft = np.zeros((N, 3)) 
AEoft = np.zeros((N, 3)) 

RSoft = np.zeros((N, 3)) 
VSoft = np.zeros((N, 3)) 
ASoft = np.zeros((N, 3))

RMoft = np.zeros((N, 3)) 
VMoft = np.zeros((N, 3)) 
AMoft = np.zeros((N, 3)) 
    
RJoft = np.zeros((N, 3)) 
VJoft = np.zeros((N, 3)) 
AJoft = np.zeros((N, 3)) 

RSaoft = np.zeros((N, 3)) 
VSaoft = np.zeros((N, 3)) 
ASaoft = np.zeros((N, 3)) 

RVoft = np.zeros((N, 3)) 
VVoft = np.zeros((N, 3)) 
AVoft = np.zeros((N, 3)) 

RMcoft = np.zeros((N, 3)) 
VMcoft = np.zeros((N, 3)) 
AMcoft = np.zeros((N, 3)) 

RUoft = np.zeros((N, 3)) 
VUoft = np.zeros((N, 3)) 
AUoft = np.zeros((N, 3)) 

RNoft = np.zeros((N, 3)) 
VNoft = np.zeros((N, 3)) 
ANoft = np.zeros((N, 3)) 

RShipoft = np.zeros((N, 3))
VShipoft = np.zeros((N, 3))
AShipoft = np.zeros((N, 3))

T0 = np.zeros(N)


params = [G, Mass_earth, Mass_sun, Mass_mars, Mass_jupiter, Mass_saturn, Mass_venus, Mass_mercury, Mass_uranus, Mass_neptune, Mass_ship,
          rtEold, rtSold, rtMold, rtJold,rtSaold, rtVold, rtMcold, rtUold, rtNold, rtShip_old]

for i, t in enumerate(T):
    rtS = rtSold + vecFRK4x(f_rS, f_vS, t, rtSold, vtSold, dt, params)
    vtS = vtSold + vecFRK4v(f_rS, f_vS, t, rtSold, vtSold, dt, params)
    atS = (vtS - vtSold)/dt   
    
    rtE = rtEold + vecFRK4x(f_rE, f_vE, t, rtEold, vtEold, dt, params)
    vtE = vtEold + vecFRK4v(f_rE, f_vE, t, rtEold, vtEold, dt, params)
    atE = (vtE - vtEold)/dt   
    
    rtM = rtMold + vecFRK4x(f_rM, f_vM, t, rtMold, vtMold, dt, params)
    vtM = vtMold + vecFRK4v(f_rM, f_vM, t, rtMold, vtMold, dt, params)
    atM = (vtM - vtMold)/dt 
    
    rtJ = rtJold + vecFRK4x(f_rJ, f_vJ, t, rtJold, vtJold, dt, params)
    vtJ = vtJold + vecFRK4v(f_rJ, f_vJ, t, rtJold, vtJold, dt, params)
    atJ = (vtJ - vtJold)/dt 
    
    rtSa = rtSaold + vecFRK4x(f_rSA, f_vSa, t, rtSaold, vtSaold, dt, params)
    vtSa = vtSaold + vecFRK4v(f_rSA, f_vSa, t, rtSaold, vtSaold, dt, params)
    atSa = (vtSa - vtSaold)/dt 
    
    rtV = rtVold + vecFRK4x(f_rV, f_vV, t, rtVold, vtVold, dt, params)
    vtV = vtVold + vecFRK4v(f_rV, f_vV, t, rtVold, vtVold, dt, params)
    atV = (vtV - vtVold)/dt 
    
    rtMc = rtMcold + vecFRK4x(f_rMc, f_vMc, t, rtMcold, vtMcold, dt, params)
    vtMc = vtMcold + vecFRK4v(f_rMc, f_vMc, t, rtMcold, vtMcold, dt, params)
    atMc = (vtMc - vtMcold)/dt 
    
    rtU = rtUold + vecFRK4x(f_rU, f_vU, t, rtUold, vtUold, dt, params)
    vtU = vtVold + vecFRK4v(f_rU, f_vU, t, rtUold, vtUold, dt, params)
    atU = (vtU - vtUold)/dt 
    
    rtN = rtNold + vecFRK4x(f_rN, f_vN, t, rtNold, vtNold, dt, params)
    vtN = vtNold + vecFRK4v(f_rN, f_vN, t, rtNold, vtNold, dt, params)
    atN = (vtN - vtNold)/dt 
    
    rtShip = rtShip_old + vecFRK4x(f_rShip, f_vShip, t, rtShip_old, vtShip_old, dt, params)
    vtShip = vtShip_old + vecFRK4v(f_rShip, f_vShip, t, rtShip_old, vtShip_old, dt, params)
    atShip = (vtShip - vtShip_old)/dt 
    
    if rtShip[0] == rtM[0]:
        print("hit")
     

    rtEold = rtE
    vtEold = vtE
    
    rtSold = rtS
    vtSold = vtS
    
    rtMold = rtM
    vtMold = vtM
    
    rtJold = rtJ
    vtJold = vtJ
    
    rtSaold = rtSa
    vtSaold = vtSa
    
    rtVold = rtV
    vtVold = vtV
    
    rtMcold = rtMc
    vtMcold = vtMc
    #print(rtEold)
    
    rtUold = rtU
    vtUold = vtU
    
    rtNold = rtN
    vtNold = vtN
    
    rtShip_old = rtShip
    vtShip_old = vtShip
    
    
    params = [G, Mass_earth, Mass_sun, Mass_mars, Mass_jupiter, Mass_saturn, Mass_venus, Mass_mercury, Mass_uranus, Mass_neptune, Mass_ship,
              rtEold, rtSold, rtMold, rtJold,rtSaold, rtVold, rtMcold, rtUold, rtNold, rtShip_old]

    if (t % (5000)) < dt:

      # calculate the index that we are storing into
      j = int(np.floor(t // 5000))

      # save our values into our arrays
      REoft[j, :] = rtE
      VEoft[j, :] = vtE
      AEoft[j, :] = atE
      
      RSoft[j, :] = rtS
      VSoft[j, :] = vtS
      ASoft[j, :] = atS
      
      RMoft[j, :] = rtM
      VMoft[j, :] = vtM
      AMoft[j, :] = atM
      
      RJoft[j, :] = rtJ
      VJoft[j, :] = vtJ
      AJoft[j, :] = atJ
      
      RSaoft[j, :] = rtSa
      VSaoft[j, :] = vtSa
      ASaoft[j, :] = atSa
      
      RVoft[j, :] = rtV
      VVoft[j, :] = vtV
      AVoft[j, :] = atV
      
      RMcoft[j, :] = rtMc
      VMcoft[j, :] = vtMc
      AMcoft[j, :] = atMc
      
      RUoft[j, :] = rtU
      VUoft[j, :] = vtU
      AUoft[j, :] = atU
      
      RNoft[j, :] = rtN
      VNoft[j, :] = vtN
      ANoft[j, :] = atN
      
      RShipoft[j, :] = rtShip
      VShipoft[j, :] = vtShip
      AShipoft[j, :] = atShip
      
      T0[j] = t
      
REoft = REoft[0:len(REoft)-1,:]
RSoft = RSoft[0:len(RSoft)-1,:]   
RMoft = RMoft[0:len(RMoft)-1,:]  
RJoft = RJoft[0:len(RJoft)-1,:]  
RSaoft = RSaoft[0:len(RSaoft)-1,:]  
RVoft = RVoft[0:len(RVoft)-1,:]
RMcoft = RMcoft[0:len(RMcoft)-1,:]
RUoft = RUoft[0:len(RUoft)-1,:]
RNoft = RNoft[0:len(RNoft)-1,:]
RShipoft = RShipoft[0:len(RShipoft)-1,:]

      
plt.figure(figsize=(10,10),dpi=300) 
plt.axis('equal')
plt.title("Trajectory of Starship to Mars in 2D",fontsize=20)
plt.plot(RSoft[:,0], RSoft[:,1], '--*', linewidth=2,label='Sun Orbit')
plt.plot(REoft[:,0], REoft[:,1], '--o', linewidth=2,label='Earth Orbit')
plt.plot(RMoft[:,0], RMoft[:,1], '--o', linewidth=2,label='Mars Orbit')
plt.plot(RShipoft[:,0], RShipoft[:,1], '--o', linewidth=2,label='Ship Orbit')
#plt.plot(RJoft[:,0], RJoft[:,1], '--o', linewidth=2,label='Jupiter Orbit')
#plt.plot(RSaoft[:,0], RSaoft[:,1], '--o', linewidth=2,label='Saturn Orbit')
#plt.plot(RVoft[:,0], RVoft[:,1], '--o', linewidth=2,label='Venus Orbit')
#plt.plot(RMcoft[:,0], RMcoft[:,1], '--o', linewidth=2,label='Mercury Orbit')
#plt.plot(RUoft[:,0], RUoft[:,1], '--o', linewidth=2,label='Uranus Orbit')
#plt.plot(RNoft[:,0], RNoft[:,1], '--o', linewidth=2,label='Neptune Orbit')
plt.xlabel('X Position [m]',fontsize=15)
plt.xlim(-.5e12,.5e12)
plt.ylim(-.5e12,.5e12)
plt.xlabel('X Position [m]',fontsize=15)
plt.ylabel('Y Position [m]',fontsize=15)
plt.tick_params(labelsize=14)
plt.legend(fontsize=10)
plt.savefig("Ship2D.png")
plt.show()

plt.figure(figsize=(10,10),dpi=300) 
ax = plt.axes(projection='3d')
#ax.set_axis('equal')
ax.plot3D(RSoft[:,0], RSoft[:,1],RSoft[:,2], '-*',linewidth=2,label='Sun Orbit')
ax.set_title("Trajectory of Starship to Mars in 3D",fontsize=20)
ax.plot3D(REoft[:,0], REoft[:,1],REoft[:,2], '-o', linewidth=2,label='Earth Orbit')
ax.plot3D(RMoft[:,0], RMoft[:,1],RMoft[:,2], '-o',linewidth=2,label='Mars Orbit')
ax.plot3D(RShipoft[:,0], RShipoft[:,1],RShipoft[:,2], '-o',linewidth=2,label='Starship')
#ax.plot3D(RJoft[:,0], RJoft[:,1],RJoft[:,2], '-o',linewidth=2,label='Jupiter Orbit')
#ax.plot3D(RSaoft[:,0], RSaoft[:,1],RSaoft[:,2], '-o',linewidth=2,label='Saturn Orbit')
#ax.plot3D(RVoft[:,0], RVoft[:,1],RVoft[:,2], '-o',linewidth=2,label='Venus Orbit')
#ax.plot3D(RMcoft[:,0], RMcoft[:,1],RMcoft[:,2], '-o',linewidth=2,label='Mercury Orbit')
#ax.plot3D(RUoft[:,0], RUoft[:,1],RUoft[:,2], '-o',linewidth=2,label='Uranus Orbit')
#ax.plot3D(RNoft[:,0], RNoft[:,1],RNoft[:,2], '-o',linewidth=2,label='Neptune Orbit')
ax.set_xlabel('X Position [m]',fontsize=15)
ax.set_ylabel('Y Position [m]',fontsize=15)
ax.set_zlabel('z Position [m]', fontsize=15)
#ax.set_tick_params(labelsize=14)
plt.legend(fontsize=10)
plt.savefig("Ship3D.png")
plt.show()

      






