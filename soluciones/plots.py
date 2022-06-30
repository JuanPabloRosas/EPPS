#!/usr/bin/env python
# -*- coding: utf-8 -*-

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


folder = 'C:/Users/pablo/Documents/PISIS/Doctorado/Paper/RepoPaper/EPPS/soluciones/'


def lee_grasp(file):
	return(pd.read_csv(file, names = nombres))

def line_plot(df, name, title, xlabel, ylabel, xdata, ydata):
   sns.set(font="Times New Roman")
   sns.axes_style("white")
   sns.set_style("ticks", {"xtick.major.size": 8, "ytick.major.size": 8})
   ax = sns.lineplot(x=xdata, y=ydata, hue="MODEL", data=df, palette='viridis')
   #ax = sns.lineplot(x=xdata, y=ydata, hue="MODEL", sort=True, hue_order=['m1','m2','m3','m4','m5'], style='MODEL', data=df)
   handles, _ = ax.get_legend_handles_labels()
   ax.legend(handles, ['EPP-PSL','EPP-SL','EPP'], title = "Model:", loc = 'center left', bbox_to_anchor = (1,0.5))
   #ax.legend(handles, ["EPP","EPP-PSL","EPP-SL"], title = "Model:")
   plt.title('', fontsize=16)
   plt.xlabel(xlabel, fontsize=16)
   plt.ylabel(ylabel, fontsize=16)
   plt.xticks(fontsize=14)
   plt.yticks(fontsize=14)
   #plt.ylim(0, 45)
   plt.setp(ax.get_legend().get_texts(), fontsize='14') # for legend text
   plt.setp(ax.get_legend().get_title(), fontsize='16') # for legend title 
   plt.show()
   #plt.savefig(name,dpi=100, bbox_inches = 'tight')
   #plt.close('all')

def box_plot(df, name, title, xlabel, ylabel, xdata, ydata):
   #sns.set(font="Times New Roman")
   #ax = sns.violinplot(x=xdata, y=ydata, hue="MODEL", data=df, palette="mako", inner="quartile", split=True,  bw=.2)
   ax = sns.boxplot(x=xdata, y=ydata, hue="MODEL" ,data=df, palette='mako')
   
   #  FOR SIMILARITY
   #handles, _ = ax.get_legend_handles_labels()
   #ax.legend(handles, ["EPP-PSL", "EPP-SL"], title = "Method:", loc = 'center left', bbox_to_anchor = (1,0.5))
   #plt.title('', fontsize=16)
   #plt.xlabel(xlabel, fontsize=16)
   #plt.ylabel(ylabel, fontsize=16)
   #plt.xticks(fontsize=14)
   #plt.yticks(fontsize=14)
   if(ydata == 'ACTIVITIES'):
      plt.ylim(40, 100)
   else:
      plt.ylim(0, 1200)
   #plt.setp(ax.get_legend().get_texts(), fontsize='14') # for legend text
   #plt.setp(ax.get_legend().get_title(), fontsize='16') # for legend title 
   plt.show()
   #plt.savefig(name,dpi=100, bbox_inches = 'tight')
   #plt.close('all')

#	LEE GRASP
nombres = ['STRESS','INSTANCE','REQUIREMENT','KMIN','IQ','EVALUATE','MODEL','MAKESPAN','RUNTIME','GAP','S1','S2','S3','S4','S5','S6','S7','S8','T1','T2','T3','T4','M1','M2','ACTIVITIES','STRESS_V']
datos = lee_grasp(folder+'acumulado.csv')
datos = datos[(datos.MODEL != 'EPP') & (datos.MODEL != 'EPP-PSL_OutEPP') & (datos.MODEL != 'VNS_EPP-SL')]


#	--------------	MAKESPAN --------------------------------------------
"""
P = ['STRESS','KMIN','REQUIREMENT','IQ']
for p in P: 
   name = 'C:\\Users\\pablo\Documents\\PISIS\\Doctorado\\makespan_'+p.lower()+'_gurobi.png'
   title = 'Makespan'
   ylabel = 'Makespan'
   if p =='IQ':
      xlabel = 'Learning Rate'
   elif p =='KMIN':
      xlabel = 'Minimum Score'
   elif p =='RCL':
      xlabel = p
   else:
      xlabel = p.capitalize()
   xdata = p
   ydata = 'MAKESPAN'
   #line_plot(datos, name, title, xlabel, ylabel, xdata, ydata)
   box_plot(datos, name, title, xlabel, ylabel, xdata, ydata)
"""
name = 'C:/Users/pablo/Documents/PISIS/Doctorado/Paper/RepoPaper/EPPS/plots/plot.png'
box_plot(datos, name, 'Makespan', 'Kmin', 'Makespan', 'KMIN', 'MAKESPAN')

