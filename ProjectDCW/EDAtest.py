import DCW.core.load as ld
from DCW.core.load import *
loaddata('train.csv',labellist=['SalePrice'],IDlist=['Id'])

##############################################
#EDA
##############################################

###univariable
import DCW.core.EDA.univariable as uv
uv.Countplot('RoofStyle')
uv.Describe('SalePrice')
uv.Distplot('SalePrice')
uv.Skewness()
uv.Kurtosis()

##############################################

###multivariable
import DCW.core.EDA.multivariable as mv
mv.Scatterplot(xlabel='GrLivArea',ylabel='SalePrice')
mv.Jointplot(xlabel='GrLivArea',ylabel='SalePrice')
mv.Pairplot('GrLivArea','SalePrice',columns=['SalePrice','GrLivArea','BsmtFinSF1'],diag_kind='kde')
mv.Correlation('GrLivArea','SalePrice',show_cm=False,zoom=1)

mv.Barplot(xlabel='MSZoning',ylabel='SalePrice',hue='Fence')
mv.Boxplot(xlabel='MSZoning',ylabel='SalePrice',hue='Street')
mv.Violinplot(xlabel='MSZoning',ylabel='SalePrice',hue='Street')
mv.Pointplot(xlabel='MSZoning',ylabel='SalePrice',hue='Street')
mv.Stripplot(xlabel='MSZoning',ylabel='SalePrice',hue='Street')
mv.Swarmplot(xlabel='MSZoning',ylabel='SalePrice',hue='Street')
mv.Factorplot(xlabel='MSZoning',ylabel='SalePrice',hue='Street',col='RoofStyle',kind='box')

################################################