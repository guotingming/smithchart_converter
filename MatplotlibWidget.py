import sys
import random
import matplotlib
import numpy as np
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QWidget
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
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

class MyMplCanvas(FigureCanvas):
    """FigureCanvas的最终的父类其实是QWidget。"""

    def __init__(self, parent=None, width=5, height=4, dpi=100):

        # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        self.fig = Figure(figsize=(width, height), dpi=dpi)  # 新建一个figure
        self.axes = self.fig.add_subplot(111)  # 建立一个子图，如果要建立复合图，可以在这里修改

        #self.axes.hold(True)  # 每次绘图的时候不保留上一次绘图的结果

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        '''定义FigureCanvas的尺寸策略，这部分的意思是设置FigureCanvas，使之尽可能的向外填充空间。'''
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.colours={'blue':'b', 'green':'g', 'red':'r', 'cyan':'c', 'magenta':'m', 'yellow':'y', 'black':'k'}

    '''绘制静态图，可以在这里定义自己的绘图逻辑'''
    def point_on_smithchart_plot(self, smith_xs,smith_ys, smith_colours):
        self.axes.cla()
        self.start_initialsmithchart_plot()
        i=0
        for smith_x in smith_xs:
            self.axes.plot(smith_x, smith_ys[i], '.',ms=12,mfc=self.colours[smith_colours[i]])
            i=i+1
        self.draw()
    def start_initialsmithchart_plot(self):
        #self.fig.suptitle('史密斯圆图')

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
    
        #fig, ax = plt.subplots()
        #ax.set_aspect('equal')
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
            self.axes.set_aspect('equal')
            self.axes.plot(x0, y0, linestyle, lw=0.5)
            #self.axes.cla()
    def clear_chart(self):
        #self.fig = Figure(figsize=(5, 4), dpi=100)  # 新建一个figure
        #self.axes = self.fig.add_subplot(111)  # 建立一个子图，如果要建立复合图，可以在这里修改
        self.axes.cla()
        '''
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.axes.set_aspect('equal')
        '''
        self.draw()

    '''启动绘制动态图'''

    def start_dynamic_plot(self, *args, **kwargs):
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)  # 每隔一段时间就会触发一次update_figure函数。
        timer.start(1000)  # 触发的时间间隔为1秒。

    '''动态图的绘图逻辑可以在这里修改'''

    def update_figure(self):
        self.fig.suptitle('测试动态图')
        l = [random.randint(0, 10) for i in range(4)]
        self.axes.plot([0, 1, 2, 3], l, 'r')
        self.axes.set_ylabel('动态图：Y轴')
        self.axes.set_xlabel('动态图：X轴')
        self.axes.grid(True)
        self.draw()


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.layout = QVBoxLayout(self)
        self.mpl = MyMplCanvas(self, width=5, height=4, dpi=100)
        self.mpl.start_initialsmithchart_plot() # 如果你想要初始化的时候就呈现静态图，请把这行注释去掉
        #self.mpl.clear_chart()
        #self.mpl.start_dynamic_plot() # 如果你想要初始化的时候就呈现动态图，请把这行注释去掉
        self.mpl_ntb = NavigationToolbar(self.mpl, self)  # 添加完整的 toolbar

        self.layout.addWidget(self.mpl)
        self.layout.addWidget(self.mpl_ntb)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MatplotlibWidget()
    #ui.mpl.start_static_plot()  # 测试静态图效果
    # ui.mpl.start_dynamic_plot() # 测试动态图效果
    #ui.mpl.clear_chart()
    ui.show()
    sys.exit(app.exec_()) 
