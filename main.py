# -*- coding: utf-8 -*-

### 2021-2-3  李运辰

import requests
import json
import matplotlib
import matplotlib as mpl
mpl.use('Agg')
import numpy as np
from matplotlib import pyplot as plt
matplotlib.rc('font', family='SimHei', weight='bold')
###获取数据
def get_data():

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'cookie':'cna=QsEFGOdo0BICARsnWHe+63/1; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; t=effdb32648fc8553a0d1a87926b80343; mt=ci%3D-1_0; xlly_s=1; _m_h5_tk=1227b52d20f9a7627b1319f8086d0fc7_1612352927433; _m_h5_tk_enc=cf938c3f97b5aae66bfc7406933622df; tfstk=cIQ1Be9yCAD6fIqq71NE7NrLaJYfZfuBt2vF1GyuAoZ7vL11iZgyFoYv1vgp2B1..; l=eBIj49hqOGMgJKgFBOfwourza77OSIRAguPzaNbMiOCPO7fp58vVW6MarCY9C3GVh62kR3yMI8QgBeYBqI2jPGKhaGUhCOMmn; isg=BGxsut-SICWv_wu3EOqa27UrPUqeJRDPNElnC8ateJe60Qzb7jXgX2Jn8Znp2Ugn',
        'referer':'https://temai.taobao.com/',
    }
    ###请求url
    url="https://h5api.m.taobao.com/h5/mtop.alimama.union.xt.en.api.entry/1.0/?jsv=2.5.1&appKey=12574478&t=1612344646955&sign=9650d7c2752bc40a2bde0b90b44d58d4&api=mtop.alimama.union.xt.en.api.entry&v=1.0&AntiCreep=true&type=jsonp&dataType=jsonp&callback=mtopjsonp2&data=%7B%22pNum%22%3A0%2C%22pSize%22%3A%2288%22%2C%22floorId%22%3A%2223919%22%2C%22spm%22%3A%22a2e1u.13363363.35064267%22%2C%22app_pvid%22%3A%22201_11.186.139.24_4399690_1612344646453%22%2C%22ctm%22%3A%22spm-url%3A%3Bpage_url%3Ahttps%253A%252F%252Ftemai.taobao.com%252F%22%7D"
    ###requests+请求头headers
    r = requests.get(url, headers=headers)
    r.encoding = 'utf8'
    s = (r.content)
    ###乱码问题
    s = s.decode('utf8')
    s= s.replace("mtopjsonp1(","").replace(")","")
    print(s)
    with open("data.txt",'a+') as f:
        f.write(s)

###分析1：销量分析
def analysis1(indexlist):
    #商品名称
    itemNames = []
    #销量
    datas = []
    for j in indexlist:
        ###商品名称
        itemName = resultList[new_countdict[j][0]]['itemName']
        print("商品名称=" + str(itemName).replace(" ",""))
        itemNames.append(str(itemName)[0:10].replace(" ",""))
        ###月销量
        monthSellCount = resultList[new_countdict[j][0]]['monthSellCount']
        print("月销量" + str(monthSellCount))
        datas.append(int(monthSellCount))

    itemNames.reverse()
    datas.reverse()

    # 绘图。
    fig, ax = plt.subplots()
    b = ax.barh(range(len(itemNames)), datas, color='#6699CC')

    # 为横向水平的柱图右侧添加数据标签。
    for rect in b:
        w = rect.get_width()
        ax.text(w, rect.get_y() + rect.get_height() / 2, '%d' %
                int(w), ha='left', va='center')

    # 设置Y轴纵坐标上的刻度线标签。
    ax.set_yticks(range(len(itemNames)))
    ax.set_yticklabels(itemNames)
    plt.title('淘宝商品热卖月销量', loc='center', fontsize='20',
              fontweight='bold', color='red')

    plt.show()

###分析2：优惠券领取分析
def analysis2(indexlist):
    # 商品名称
    itemNames = []
    # 优惠券总量
    datas1 = []
    # 优惠券领取量
    datas2 = []
    for i in range(0,len(indexlist)):
        j = indexlist[i]
        ###商品名称
        itemName = resultList[new_countdict[j][0]]['itemName']
        print("商品名称=" + str(itemName).replace(" ", ""))
        itemNames.append(str(i+1)+str(itemName)[1:4].replace(" ", ""))
        ###优惠劵总数
        couponTotalCount = resultList[new_countdict[j][0]]['couponTotalCount']
        print("优惠劵总数=" + str(couponTotalCount))
        datas1.append(int(couponTotalCount))
        ###优惠劵领取数
        couponSendCount = resultList[new_countdict[j][0]]['couponSendCount']
        print("优惠劵领取数=" + str(couponSendCount))
        datas2.append(int(couponSendCount))
    N = len(datas1)
    S = datas1
    C = datas2
    d = []
    for i in range(0, len(S)):
        sum = S[i] + C[i]
        d.append(sum)

    ind = np.arange(N)  # the x locations for the groups
    width = 0.35  # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, S, width, color='#d62728')  # , yerr=menStd)
    p2 = plt.bar(ind, C, width, bottom=S)  # , yerr=womenStd)
    plt.ylabel('数量')
    plt.title('优惠券领取分析')
    itemNames
    plt.xticks(ind, itemNames)
    plt.legend((p1[0], p2[0]), ('优惠券总量', '优惠券领取数'))

    plt.show()

###分析3：优惠券金额分析
def analysis3(indexlist):
    # 商品名称
    itemNames = []
    # 优惠券金额
    datas = []

    for i in range(0,len(indexlist)):
        j = indexlist[i]
        ###商品名称
        itemName = resultList[new_countdict[j][0]]['itemName']
        print("商品名称=" + str(itemName).replace(" ", ""))
        itemNames.append(str(i+1)+str(itemName)[0:6].replace(" ", ""))
        ###优惠劵金额
        couponAmount = resultList[new_countdict[j][0]]['couponAmount']
        print("优惠劵金额=" + str(couponAmount))
        datas.append(int(couponAmount))

    x = range(len(itemNames))
    plt.plot(x, datas, marker='o', mec='r', mfc='w', label=u'优惠金额')
    plt.legend()  # 让图例生效
    plt.xticks(x, itemNames, rotation=45)
    plt.margins(0)
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"商品名称")  # X轴标签
    plt.ylabel("金额")  # Y轴标签
    plt.title("优惠券金额分析")  # 标题

    plt.show()

###分析4：商品原价和限价对比分析
def analysis4(indexlist):
    # 商品名称
    itemNames = []
    # 原价
    datas1 = []
    # 限价
    datas2 = []

    for i in range(0,len(indexlist)):
        j = indexlist[i]
        ###商品名称
        itemName = resultList[new_countdict[j][0]]['itemName']
        print("商品名称=" + str(itemName).replace(" ", ""))
        itemNames.append(str(i+1)+str(itemName)[1:4].replace(" ", ""))
        ###原价
        promotionPrice = resultList[new_countdict[j][0]]['promotionPrice']
        print("原价=" + str(promotionPrice))
        datas1.append(float(promotionPrice))
        ###限价
        priceAfterCoupon = resultList[new_countdict[j][0]]['priceAfterCoupon']
        print("价格=" + str(priceAfterCoupon))
        datas2.append(float(priceAfterCoupon))

    font_size = 10  # 字体大小
    fig_size = (8, 6)  # 图表大小

    names = (u'限价', u'原价')
    data = (datas2,datas1)

    # 更新字体大小
    mpl.rcParams['font.size'] = font_size
    # 更新图表大小
    mpl.rcParams['figure.figsize'] = fig_size
    # 设置柱形图宽度
    bar_width = 0.35

    index = np.arange(len(data[0]))
    # 绘制「小明」的成绩
    rects1 = plt.bar(index, data[0], bar_width, color='#0072BC', label=names[0])
    # 绘制「小红」的成绩
    rects2 = plt.bar(index + bar_width, data[1], bar_width, color='#ED1C24', label=names[1])
    # X轴标题
    plt.xticks(index + bar_width, itemNames)
    # Y轴范围
    plt.ylim(ymax=100, ymin=0)
    # 图表标题
    plt.title(u'商品原价和限价对比分析')
    # 图例显示在图表下方
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.03), fancybox=True, ncol=5)

    # 添加数据标签
    def add_labels(rects):
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2, height, height, ha='center', va='bottom')
            # 柱形图边缘用白色填充，纯粹为了美观
            rect.set_edgecolor('white')

    add_labels(rects1)
    add_labels(rects2)

    # 图表输出到本地
    plt.savefig('4.png')

if __name__ == '__main__':
    ###获取数据
    #get_data()
    ###加载数据
    with open("data.txt", 'r') as f:
        s = f.readline()
    s = s.replace("mtopjsonp2(", "").replace(")", "")
    ###转为json格式
    s = json.loads(s)
    resultList = s['data']['recommend']['resultList']

    ###字段放入集合
    countdict = {}

    for j in range(0, len(resultList)):
        i = resultList[j]
        ###月销量
        monthSellCount = i['monthSellCount']
        # 初始化
        countdict[j] = int(monthSellCount)

    # 按键(key)排序:
    new_countdict = sorted(countdict.items(), key=lambda kv: (kv[1], kv[0]))

    ###倒序取值（目的是从销量大到小的方式取值）
    index_resultList = []
    for j in range(len(resultList) - 1, len(resultList) - 11, -1):
        index_resultList.append(j)
    ###分析1：销量分析
    #analysis1(index_resultList)
    ###分析2：优惠券领取分析
    #analysis2(index_resultList)
    ###分析3：优惠券金额分析
    #analysis3(index_resultList)
    ###分析4：商品原价和限价对比分析
    analysis4(index_resultList)



'''
    ###商品名称
    itemName = i['itemName']
    print("商品名称="+str(itemName))
    ###月销量
    monthSellCount = i['monthSellCount']
    print("月销量"+str(monthSellCount))
    ###价格
    priceAfterCoupon = i['priceAfterCoupon']
    print("价格"+str(priceAfterCoupon))
    ###原价
    promotionPrice = i['promotionPrice']
    print("原价="+str(promotionPrice))
    ###优惠金额
    couponAmount = i['couponAmount']
    print("优惠金额="+str(couponAmount))
    ###店铺名称
    shopTitle = i['shopTitle']
    print("店铺名称="+str(shopTitle))
    ###优惠劵总数
    couponTotalCount = i['couponTotalCount']
    print("优惠劵总数="+str(couponTotalCount))
    ###优惠劵领取数
    couponSendCount = i['couponSendCount']
    print("优惠劵领取数="+str(couponSendCount))
    print("-------------------------")
'''

