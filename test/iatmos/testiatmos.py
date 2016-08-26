#dasp, the Durham Adaptive optics Simulation Platform.
#Copyright (C) 2004-2016 Alastair Basden and Durham University.

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as
#published by the Free Software Foundation, either version 3 of the
#License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.

#You should have received a copy of the GNU Affero General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Tests the new iscrn module.  
Note - this may not be kept up to date with the module."""

import science.iscrn
import science.iatmos
import base.readConfig
import util.Ctrl
ctrl=util.Ctrl.Ctrl(globals=globals())
iscrn01=science.iscrn.iscrn(None,ctrl.config,idstr="L0-1")
iscrn2=science.iscrn.iscrn(None,ctrl.config,idstr="L2")
iatm=science.iatmos.iatmos({"L0-1":iscrn01,"L2":iscrn2},ctrl.config,idstr="a")

execOrder=[iscrn01,iscrn2,iatm]
ctrl.mainloop(execOrder)

