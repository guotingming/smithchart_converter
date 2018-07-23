import numpy as np
import matplotlib.pyplot as plt
c_g='g'
colours={'blue':'b', 'green':'g', 'red':'r', 'cyan':'c', 'magenta':'m', 'yellow':'y', 'black':'k'}
def gamma(z):
    """
    :param z: 归一化阻抗(复数)
    :return: 反射系数(复数)
    """
    return 1.0*(z-1)/(z+1)


def g2z(g):
    """
    :param g: 反射系数(复数)
    :return: 归一化阻抗(复数)
    """
    return 1.0*(1+g)/(1-g)
def displaysmithchart(smith_xs,smith_ys, smith_colours):
    # 构建一个-1到+1的均匀数列x：
    # 为防止下一步出现无穷大，此处用0.9999代替1
    x = np.arange(-0.9999, 0.9999, 0.005)

    # 由上一步的均匀数列生成一个非均匀的（从0开始近密远疏）数列t0，一会用来表示归一化阻抗的实部或虚部
    # 其远端的数值很大，在圆图中肉眼可分辨的范围内可视为无穷
    t0 = g2z(x)

    # 选取几个离散的数值与用来表示归一化阻抗的虚部或实部，与t0配合，由此搭建史密斯圆图的背景骨架
    t1 = [0,0.1, 0.2,0.3, 0.5,0.8, 1.0,1,5, 2.0,2.5,3.0,3.5,4.0,4.5, 5.0]

    sc = []
    for n1 in t1:
        sub_sc0 = []
        sub_sc1 = []
        sub_sc2 = []
        sub_sc3 = []
        for n0 in t0:
            sub_sc0.append(gamma(complex(n1, n0)))
            sub_sc1.append(gamma(complex(n1, -n0)))
            sub_sc2.append(gamma(complex(n0, n1)))
            sub_sc3.append(gamma(complex(n0, -n1)))
        sc.append(sub_sc0)  # 一条等电阻圆弧(上)
        sc.append(sub_sc1)  # 一条等电阻圆弧(下)
        sc.append(sub_sc2)  # 一条等电抗圆弧(上)
        sc.append(sub_sc3)  # 一条等电抗圆弧(下)
    # 此时sc为包含若干条圆弧的二维列表，每一个子列表都是一段圆弧，
    # 子列表的每一个元素都是一个复数，将其实部和虚部提取出来画散点图即可

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    for sub_sc in sc:
        x0 = []
        y0 = []
        for c in sub_sc:
            if abs(c) > 2:
                print(c)
                continue
            x0.append(c.real)
            y0.append(c.imag)
        # 基于归一化阻抗生成的图里没有无穷点，可能导致无穷点缺一个像素，因此需要补一个点：
        x0.append(1)
        y0.append(0)
        linestyle = '0.5'  # 灰度
        ax.plot(x0, y0, linestyle, lw=0.5)
    i=0
    for smith_x in smith_xs:
        plt.plot(smith_x, smith_ys[i], '.',ms=12,mfc=colours[smith_colours[i]])
        i=i+1
    #plt.plot(smith_x, smith_y, '.',ms=10,mfc=c_g)
    #print(x0)
    fig.savefig('sc_%s.png'%linestyle)
    plt.show()
    #plt.figure(1) 
    #time.sleep(3)

a=[-0.3, 0.2, 0.5]
b=[0.7, 0.5, 0.2]
c=['blue','blue','blue']
#displaysmithchart(a,b, c)

#print(colours['blue'])
