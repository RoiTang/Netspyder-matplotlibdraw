import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
#从database文件中导入获取数据库中的数据函数
from database import select_population, select_finance

#人口绘图模块
def population_draw():

    year = []          #年份
    total_amount = []  #总人口
    male_amount = []   #男性人口
    female_amount = [] #女性人口
    ma_scale = []      #男性人口占比
    fema_scale = []    #女性人口占比

    #调用select_population()函数获取以上6个列表值
    select_population(year, total_amount, male_amount, female_amount, ma_scale, fema_scale)

    #正常显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']

    # -------------------------------------------------
    # 开启第一个视图，用来显示年末总人口随年份变化条形图
    # -------------------------------------------------
    fig1 = plt.figure('fig1')
    #设置标题
    plt.title('年末总人口-年份')
    #绘制年末总人口随年份变化条形图
    plt.bar(np.arange(20), total_amount, width=0.8, label=u'年末总人口', color='r')
    #设置y轴取值范围、标注
    plt.ylim(125000, 140000)
    plt.ylabel('年份')
    #设置x轴标注、刻度、倾斜60°
    plt.xlabel('年末总人口数')
    plt.xticks(np.arange(20), year)
    plt.xticks(rotation=60)
    #设置图例
    plt.legend(loc='upper left')
    #添加网格
    plt.grid(b=True,axis='y',linestyle='--')
    #-------------------------------------------
    #开启第二个视图，用来显示男女性人口占比折线图
    #-------------------------------------------
    fig2 = plt.figure('fig2')
    #y轴显示百分数
    fmt = '%.2f%%'
    ytickscale = mtick.FormatStrFormatter(fmt)
    plt.gca().yaxis.set_major_formatter(ytickscale)
    #设置折线图标题
    plt.title('男女性人口占比的变化')
    #绘图
    p1, = plt.plot(np.arange(20), ma_scale, color = 'red')#男性人口占比图
    p2, = plt.plot(np.arange(20), fema_scale, color = 'blue')#女性人口占比图
    #设置x轴标注、刻度、倾斜60°
    plt.xlabel('年份')
    plt.xticks(np.arange(20), year)
    plt.xticks(rotation=60)
    #设置y轴标注
    plt.ylabel('占总人口比例')
    #添加图例
    plt.legend([p1, p2], ['男性人口占比', '女性人口占比'], loc='upper right')
    #添加网格
    plt.grid(b=True, linestyle='--')
    plt.show()

#财政绘图模块
def finance_draw():
    year = []           #年份
    income_amount = []  #财政收入
    outcome_amount = [] #财政支出
    inspeed = []        #财政收入增长速度
    outspeed = []       #财政支出增长速度

    #正常显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']

    select_finance(year,income_amount,outcome_amount,inspeed,outspeed)
    # ---------------------------------------------------
    # 开启第一个视图，用来显示财政收入财政支出随年份变化图
    # ---------------------------------------------------
    fig1 = plt.figure('fig1')
    #绘图
    plt.bar(np.arange(19), height=income_amount, width=0.35, alpha=0.8, color='r', label=u'财政收入')#财政收入随年份变化条形图
    plt.bar(np.arange(19)+0.35, height=outcome_amount, width=0.35, alpha=0.8, color='b', label=u'财政支出')#财政支出随年份变化条形图
    # ----------------------------------
    # 设置x轴参数(标注、刻度值并旋转60°)
    # ----------------------------------
    plt.xlabel('年份')
    plt.xticks(np.arange(19), year)
    plt.xticks(rotation=60)
    # 设置y轴标注
    plt.ylabel('亿元')
    # 设置条形图标题
    plt.title('财政收入支出随年份变化条形图')
    #显示网格
    plt.grid(b=True, axis='y', linestyle='--')
    #添加图例
    plt.legend()
    #-----------------------------------------------
    #开启第二个视图，显示财政收入、支出增长速度折线图
    #-----------------------------------------------
    fig2 = plt.figure('fig2')
    #绘图
    p1, = plt.plot(np.arange(19), inspeed, color='red')  # 财政收入增长速度折线图
    p2, = plt.plot(np.arange(19), outspeed, color='blue')  # 财政支出增长速度折线图
    #-----------------------------------
    #添加x轴标注,x轴刻度值,x轴字体旋转60°
    #-----------------------------------
    plt.xlabel('年份')
    plt.xticks(np.arange(19),year)
    plt.xticks(rotation=60)
    # -------------
    # 设置y轴参数
    # -------------
    #y轴显示小数点后一位百分数
    fmt = '%.1f%%'
    ytickscale = mtick.FormatStrFormatter(fmt)
    plt.gca().yaxis.set_major_formatter(ytickscale)
    #添加y轴标注
    plt.ylabel('增长速度%')
    #添加折线图标题
    plt.title('财政收入支出增长速度折线图')
    #添加图例
    plt.legend([p1, p2], ['财政收入增长速度', '财政支出增长速度'], loc='upper right')
    #显示网格
    plt.grid(b=True, linestyle='--')
    plt.show()