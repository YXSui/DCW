import DCW.core.load as ld
from DCW.core.load import *
loaddata('train.csv',labellist=['SalePrice'],IDlist=['Id'])

#ld.data
#ld.df_train
#ld.quantitative
#ld.qualitative
#ld.targetdf_list
print 'initial shape',ld.df_train.shape


##############################################
#EDA
##############################################

###univariable
import DCW.core.EDA.univariable as uv
#uv.Countplot('RoofStyle')
#uv.Describe('SalePrice')
#uv.Distplot('SalePrice')
#uv.Skewness()
#uv.Kurtosis()

##############################################

###multivariable
import DCW.core.EDA.multivariable as mv
#mv.Scatterplot(xlabel='GrLivArea',ylabel='SalePrice')
#mv.Jointplot(xlabel='GrLivArea',ylabel='SalePrice')
#mv.Pairplot('GrLivArea','SalePrice',columns=['SalePrice','GrLivArea','BsmtFinSF1'],diag_kind='kde')
#mv.Correlation('GrLivArea','SalePrice',show_cm=False,zoom=1)

#mv.Barplot(xlabel='MSZoning',ylabel='SalePrice',hue='Fence')
#mv.Boxplot(xlabel='MSZoning',ylabel='SalePrice',hue='Street')
#mv.Violinplot(xlabel='MSZoning',ylabel='SalePrice',hue='Street')
#mv.Pointplot(xlabel='MSZoning',ylabel='SalePrice',hue='Street')
#mv.Stripplot(xlabel='MSZoning',ylabel='SalePrice',hue='Street')
#mv.Swarmplot(xlabel='MSZoning',ylabel='SalePrice',hue='Street')
#mv.Factorplot(xlabel='MSZoning',ylabel='SalePrice',hue='Street',col='RoofStyle',kind='box')

################################################



#################################################
#Missing Process
#################################################

import DCW.core.missing as ms
#ms.Missing_Table()
#ms.Missing_Plot()
ms.Missing_Process(drop_threshold=0.90,filllist=[],fillnum='mean',fillcat='Missing')
############################################################
#loaddata('train.csv',labellist=['SalePrice'],IDlist=['Id'])
############################################################
print 'after missing process the shape is ',ld.df_train.shape


#################################################
#Single Process
#################################################

import DCW.core.single as sg
sg.single_process(drop_threshold=0.99,single_ratio=0.95,collect=True,show_plot=True,show_table=False,drop=True)
sg.duplicate_process()

print 'after single process the shape is ',ld.df_train.shape


#################################################
#Outlier Process
#################################################

import DCW.core.outlier as ot
#ot.Outlier_collect(feature='GrLivArea',label='SalePrice')
#ot.Outlier_Plot(feature='GrLivArea',label='SalePrice')
ot.Outlier_Drop(feature='all',label='SalePrice',method='dropall')

print 'after outlier process the shape is ',ld.df_train.shape
ld.df_train.to_csv('afterprocess.csv',index=False)
