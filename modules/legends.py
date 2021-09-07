# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 11:12:39 2021

@author: dviqu
"""

import matplotlib as mpl
import settings.detector as setdet
import settings.screen as setscr
import params.constants as cts


def add_legend_padcolor(fig):
    """
    Function to plot legend of colors of pads
    """
    ax1 = fig.add_subplot(5,20,17)
    cmap = mpl.cm.rainbow
    norm = mpl.colors.Normalize(vmin=0, vmax=20*setscr.tstcol)

    cb1 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap,norm=norm,orientation='vertical')
    cb1.set_label('Delay (ns)')
    return


def add_legend_trackcolor(fig):
    """
    Function to plot legend of colors of pads
    """
    ax1 = fig.add_subplot(5,20,20)
    cmap = mpl.cm.inferno
    norm = mpl.colors.Normalize(vmin=(1-setdet.tol_lo)*cts.c, vmax=(1+setdet.tol_up)*cts.c)

    cb1 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap,norm=norm,orientation='vertical')
    cb1.set_label('Velocity (mm/ns)')
    return