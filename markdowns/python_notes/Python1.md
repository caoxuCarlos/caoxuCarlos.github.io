## Preface

这段时间学习的思路基本上是这样子的, 先学李笑来的<自学是门手艺>, 然后开始学习 Numpy, 接着在试着处理  tablular data 的时候学习pandas, 接着为了搞懂<概率论与数理统计>上的知识, 学了符号运算, 接触 SciPy. 为了搞懂 SciPy 又去学习了 Matplotlib 里的 figure 和 axes, 还有一些绘图的操作. 

我的学习笔记大概就分这几个部分, 并且结合几个例子来说明.

为了减少输入法转换带来的注意力耗散, 下文用使用英文书写. 

[TOC]

## NumPy

Here is a very good tutotial:point_down::

 [Python Numpy Tutorial by Justin Johnson](http://cs231n.github.io/python-numpy-tutorial/#numpy)

Numpy is the **core library**  for scientific computing in Python. And I think it features **elementwise** caclulation. (*It will be easy to understand if you learnt Matlab before.*)

```Python
import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
print(x) # [[1,2]
		 #  [3,4]]
print(y)# [[5,6]
		#  [7,8]]
print(x,y) #[[5,12]
		   # [21,32]]
```



To use numpy, we must know **array** well, which is a ndarray [object](https://github.com/selfteaching/the-craft-of-selfteaching/blob/master/markdown/Part.3.B.1.classes-1.md)(*I remember ndarray as n-demensions-array*). 

**A numpy array is a container of values**, all of the **same** data type, and is **indexed by a tuple** of nonnegative integers. 

To understand array, we need to understand two concepts about array : **shape & rank**, and [this blog](https://flat2010.github.io/2017/05/31/Numpy数组解惑/) explains it pretty well. 

OK, then how to **create** a array? [Here](https://docs.scipy.org/doc/numpy/user/basics.creation.html).

And **array indexing**? [Here](http://cs231n.github.io/python-numpy-tutorial/#numpy-array-indexing) and [here](https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html).

Besides, **array math** [Here](http://cs231n.github.io/python-numpy-tutorial/#numpy-math) and [here](https://docs.scipy.org/doc/numpy/reference/routines.math.html).

To be honest, I know it's a little bit confusing, I spent a whole day (if not 2) to figure these concepts out. Personally I **don't** think we need to know every methods and functions specifically to start doing something, we can start as soon as we can ,  just **learning by doing**. (There is [google](www.google.com) anyway.)

Here is an example, I used it to analysis math socres in 2017 mock exam of my senior high school. (You can download the csv file [here](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/csv/math-score.zip).)

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 把 CSV 文件中数学成绩读入成为列表
a=[]
with open("F:\data-for-analysis\math-score.csv",'r') as f:
    for line in f.readlines():
        a=a+[float(line.strip())]
print(a)

# 计算平均值
score=np.array(a)
# print(score.shape) 
# 注意, shape的后面没有() 
mean=np.mean(a)
print(f'The mean of maths socre is {round(mean,2)}')

# 计算方差和标准差
variance=np.var(a,ddof=1)#var（）函数默认计算总体方差。要计算样本的方差，必须将ddof参数设置为值1 
StandardDeviation=variance**0.5
print(f'The variance of scores is {round(variance,3)}')
print(f'The standard deviation is {round(StandardDeviation,3)}')

# 计算峰度和偏度
skewness=stats.skew(a)
kurtosis=stats.kurtosis(a)
print(f'The skewness of score is {round(skewness,3)}')
print(f'The Kurtosis of score is {round(kurtosis,3)}')

# 计算各区间人数并且画出频率分布直方图 
np.histogram(a,bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150])
histogram_of_score=plt.hist(a,bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150])
plt.show()
```

You see, there are not only numpy methods but also some interesting and useful methods from other libraries. I know there are many forward refereces in this example, it maybe a little bit difficult for you to understand if you are a newborn in python just like me, and I did google a lot when I wrote this program. So take it easy, find a job you want to be done, and **let google help you finish it.**

The following example is related to generate random numbers in numpy: 

```python
# random nmubers in numpy
import numpy as np
import matplotlib.pyplot as plt # basic steps to data analysisi
# random values in a given shape
# ramd(d0,d1,d2....)
a=np.random.rand(2,3)
print(a)

#return a sample from the #standard normal distribution#
b=np.random.randn(100,100)
print(b)
 
# I think the most important thing
# is to know what it can do and 
# lean how to use it qucikly.

c=np.random.randint(10,100,size=(2,4))
print(c)

# If I want to generate some exam grades of a whole class
a=np.random.randint(30,101,size=(56,))
compute_hist_a=np.histogram(a,bins=[30,40,50,60,70,80,90])
print(compute_hist_a)
histogram_of_a=plt.hist(a,10)		# draw the histogram of a
plt.show()
```



## Pandas

> Pandas is an open-source Python Library providing high-performance **data manipulation and analysis tool using its powerful data structures**. 
>
> Using Pandas, we can accomplish five typical steps inthe processing and analysis of data, regardless of the origin of data — **load, prepare, manipulate, model, and analyze**.

To make it easy to understand, not strict, it's like excel. 

For this part, I strongly recommend [tutorialspoint](https://www.tutorialspoint.com/python_pandas/python_pandas_introduction_to_data_structures.htm), this website explain things really nicely, though it seems this website uses Python 2.X instead of Python 3.X.

```python
# Basically, we just need to add a "()" after "print" when we try to run some python2.x code from tutorialspoint.
import numpy as np
a=np.arange(10)
# If you want to print a, use this:
print(a) # This is what in python 3.x
#instead of 
print a # This is what in python 2.x
```

I suggest you start from [this one](https://www.tutorialspoint.com/python_pandas/python_pandas_introduction_to_data_structures.htm) to understand data structures in pandas.

Next, to read [Seires](https://www.tutorialspoint.com/python_pandas/python_pandas_series.htm), [DataFrame](https://www.tutorialspoint.com/python_pandas/python_pandas_dataframe.htm) (which is really like excel data)and you will know whether you want to read [Panel](https://www.tutorialspoint.com/python_pandas/python_pandas_panel.htm) after reading the first three.

For DataFrame indexing, I have this example:(download csv file [here](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/csv/subjects.zip))

```python
# 这个程序一开始就是为了分析高三一模成绩中各个学科成绩之间的相关性
import pandas as pd
data=pd.read_csv("F:\data-for-analysis\subjects.csv")
del data['理综'] # 选择列,删除掉理综
cn=data.corr() #相关系数矩阵
cc=data.cov() #协方差矩阵

for i in range(6):
    cn.iloc[i,i]=0 ##取i号行, i号列, 如果是iloc[i]是取
                   ##i号行的意思, 如果是i[2:4]就是从第3行取到第5行

print(cn)
cn.max()
a=cn[cn.生物>0.49].index.tolist() #获取符合要求的index 
print(a)

## 用标题索引

cn['物理'] # 取这一列
data.物理 #等于data['物理']
cn.loc['理数'] # 取这一行

cn.loc['理数']['物理'] #这两个都可以把
cn.loc['物理']['理数'] #给取出来

## 用数字来索引

data[2:4] #取这几行
data.iloc[2:4] #=data[2,4]

data.iloc[2,4] #取2号行, 4号列

data.iloc[2] # 取2号行
data.loc[2] #取2号行

data.iloc[,2] # 这是错的, 不能取2号列
data.iloc[0:,2] # 这样是取2号列
```

Yesterday I read an artical about "the law of diminishing marginal returns", the writer give a picture like this.

![](https://github.com/caoxuCarlos/caoxuCarlos.github.io/raw/master/images-for-notes/marginal.jpg)

So I spent sometime to redo this on python:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 创建前两列, 后面一列一列往上拼
# 在这里, 我就先创建 Series, 再拼起来
number_of_people=pd.Series(np.arange(11))
columns_1=[0,6,16,24,30,34,36,36,32,27,21]
## Check the length of the list
## Don't use "size" !
## len(columns_1) 
total_production=pd.Series(columns_1)
##如果需要创建 DataFrame, 使用 Dictionary 还是在所难免的
Dictionary_for_prototype={'People_on_Board':number_of_people, \
    'Total_Production':total_production}
data=pd.DataFrame(Dictionary_for_prototype)
## print(data)


# 创建并且拼接"边际产量"
columns_2=[0]
##这里要注意, 转化成 list 的时候要直接加[], 而不要用list()
for i in range(10):
    columns_2=columns_2+[(columns_1[i+1]-columns_1[i])]
## print(columns_2)
data['marginal_production']=pd.Series(columns_2)

# 创建平均产量
data['average_production']=data['Total_Production']/data['People_on_Board']
data.iloc[0,3]=0
print(data)

# 创建团体总产量, 并拼接
all_people_production=np.arange(4000,3959,-4) \
    +np.array(columns_1)
print(all_people_production)
data['all_people_production']=pd.Series(all_people_production)
print(data)

#创建团体边际产量并且拼接
mapp=[0]
for_mapp=list(all_people_production)
for i in range(10):
    mapp=mapp+[(for_mapp[i+1]-for_mapp[i])]
margin_all_people_production=mapp
data['margin_all_people_production']=pd.Series(np.array(margin_all_people_production))
print(data)

#画工人数量和捕鱼数的图
from scipy.interpolate import make_interp_spline, BSpline
x=np.array(data.People_on_Board)
y=np.array(data.Total_Production)
spl=make_interp_spline(x,y,k=3) #模拟x->y的对应关系, 创建Bspine对象
xnew=np.linspace(x.min(),x.max(),500)
smooth_y=spl(xnew) #用新的数组, 按照原来x和y的对应关系, 模拟出新x和新y的关系
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.plot(xnew,smooth_y)
plt.xlabel('工人数量')
plt.ylabel('捕鱼数')
plt.show()

#画边际生产率和平均生产率的图
x1=np.array(data.People_on_Board)
y1=np.array(data.marginal_production)
y2=np.array(data.average_production)
y3=np.array([4,4,4,4,4,4,4,4,4,4,4])
spl_1=make_interp_spline(x1,y1,k=3)
spl_2=make_interp_spline(x1,y2,k=3)
x1_smooth=np.linspace(x1.min(),x1.max(),500)
y1_smooth=spl_1(x1_smooth)
y2_smooth=spl_2(x1_smooth)
y3_fake_smooth=x1_smooth*0+4
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.plot(x1_smooth,y1_smooth)
plt.plot(x1_smooth,y2_smooth)
plt.plot(x1_smooth,y3_fake_smooth)
plt.ylim((-6,15))
plt.xlim(0,9)
plt.xlabel('工人数量')
plt.ylabel('捕鱼数')
plt.show()
```

To make it look nicer, I used B-Spline to fit the curves.But, if you run it, you will find the curves fitted by B-spline is not very proper, as the highest point of the average production doesn't cross the margin production. 

## Integrate

When I saw pdf(probability density function), I want to  integrate it to caculate the probablity, so I wrote this: 

```python
from sympy import * # 直接把这个库里要用到的有关复函变量的函数全部都取出来

from sympy.abc import x,a,y  #要在这里把需要的符号先引用出来

integrate(sin(x)/x,(x,-float("inf"),float("inf"))) 
#是函数+*()的形式,
# 函数就是函数, 但是()里面要写积分的对象, 开始值和终止值

xx=symbols('xx') ## 另外一种声明符号变量的方法
# a, b, c = symbols('a,b,c')
integrate(sin(xx)/xx,(xx,-float("inf"),float("inf"))) 
```

## Matplotlib

I first learn this from numpy:joy:.

This one is easy to used, but when it comes to `subplots`, here are two concepts that we need to figure out ---- **figure** and **axes**.

I saw [this amazing answer](https://stackoverflow.com/questions/37970424/what-is-the-difference-between-drawing-plots-using-plot-axes-or-figure-in-matpl/56629063?stw=2#56629063) on stack overflow offered by [gboffi](https://stackoverflow.com/users/2749397/gboffi):

> Matplotlib is strongly object oriented and its principal objects are the **figure** and the **axes** (I find the name `axes` a bit misleading, but probably it's just me).
>
> You can think of the **figure** as a *canvas*, of which you typically specify the dimensions and possibly e.g., the background color etc etc. You use the canvas, the **figure**, essentially in two ways, placing other objects on it (mostly **axes**, but also text labels etc) and saving its contents with `savefig`.

And gbiffi give some examples after this paragraph, to read it, click "this amazing answer" above :point_up: ​.  

Once you had these two basic ideas about `subplots`, you may try to understand this:

(I basiclly copy these from [matplotlib.org](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots.html), and you can find more on this site.)

```python
import numpy as np
import matplotlib.pyplot as plt
# First create some toy data:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# Creates just a figure and only one subplot
fig,ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple plot')

# Creates two subplots and unpacks the output array immediately
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)

# Creates four polar axes, and accesses them through the returned array
fig, axes = plt.subplots(2, 2, subplot_kw=dict(polar=True))
axes[0, 0].plot(x, y)
axes[1, 1].scatter(x, y)

# Share a X axis with each column of subplots
plt.subplots(2, 2, sharex='col')

# Share a Y axis with each row of subplots
plt.subplots(2, 2, sharey='row')

# Share both X and Y axes with all subplots
plt.subplots(2, 2, sharex='all', sharey='all')

# Note that this is the same as
plt.subplots(2, 2, sharex=True, sharey=True)

# Creates figure number 10 with a single subplot
# and clears it if it already exists.
fig, ax=plt.subplots(num=10, clear=True)
```

## Scipy.stats

> This module contains a large number of probability distributions as well as a growing library of statistical functions.

As this one it really large and just like a checklist, so I simply put the "[checklist](https://docs.scipy.org/doc/scipy/reference/stats.html#continuous-distributions)" here.

Actually, the reason why I wanted to know what exactly do figure an axes are, is to understand the following program:

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
fig,ax=plt.subplots(1,1)

#Caculate few first moments
mean,var,skew,kurt=norm.stats(moments='mvsk')

#Display the probability density function (pdf):
x=np.linspace(norm.ppf(0.01),norm.ppf(0.09),100)
ax.plot(x,norm.pdf(x),'r-',lw=2,alpha=0.6,label='norm pdf')

# Freeze the distribution and display the frozen pdf:
# 为啥叫frozen呢? 这个例子不好看出来, 可是
# 面对rv1 = stats.gamma(a, loc, scale)这个分布的时候
# 就很清楚了, 原来的norm, 是一种分布, 而rv_frozen
# 是已经确定了一些参数的 norm(或者其他分布)
rv=norm()
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# Check accuracy of cdf and ppf:
vals = norm.ppf([0.001, 0.5, 0.999])
np.allclose([0.001, 0.5, 0.999], norm.cdf(vals))
# norm.cdf()括号里面这个点左边的累计概率
# 和norm.ppf()正好相反,ppf是给出百分数, 求出点来

# Generate random numbers:
r = norm.rvs(size=1000)

# And compare the histogram
ax.hist(r, normed=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()
```

And here is another example:

```python
import scipy.stats as st
generated=st.norm.rvs(size=900)
##rvs是生成符合这个分布的一个ndarray

# generated.shape
# generated.ndim
# generated.dtype
Mean, std = st.norm.fit(generated)
print(f'Mean is {Mean}\n Std is {std}')

skew=st.skewtest(generated)
kurt=st.kurtosistest(generated)
print(skew)
print(kurt)
st.normaltest(generated)

#获取区间中95%的数值
st.scoreatpercentile(generated, 95)
#通过某一个数值获取百分比
st.percentileofscore(generated, 1)

import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
# pdf的用法, 在这个例子中表达的是
# 一个变量,它的值分布在-5到5之间,
# 它在不同区间的取值概率的大小
# 生成*随机变量*对于*区间*的概率密度函数 
x=np.linspace(-5,+5,500)
y=st.norm.pdf(x,0,1)
plt.plot(x,y)
plt.show()
```