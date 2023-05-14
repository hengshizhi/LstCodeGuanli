# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(930, 555)
        self.codeGuanli = QWidget(MainWindow)
        self.codeGuanli.setObjectName(u"codeGuanli")
        self.horizontalLayout_9 = QHBoxLayout(self.codeGuanli)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tabWidget = QTabWidget(self.codeGuanli)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_8 = QHBoxLayout(self.tab)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.main = QHBoxLayout()
        self.main.setObjectName(u"main")
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.sou = QLineEdit(self.groupBox_2)
        self.sou.setObjectName(u"sou")

        self.horizontalLayout_6.addWidget(self.sou)

        self.CloudSwitch = QCheckBox(self.groupBox_2)
        self.CloudSwitch.setObjectName(u"CloudSwitch")

        self.horizontalLayout_6.addWidget(self.CloudSwitch)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.codePdList = QListWidget(self.groupBox_2)
        self.codePdList.setObjectName(u"codePdList")

        self.verticalLayout_3.addWidget(self.codePdList)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.delPd = QPushButton(self.groupBox_2)
        self.delPd.setObjectName(u"delPd")

        self.horizontalLayout_7.addWidget(self.delPd)

        self.addPd = QPushButton(self.groupBox_2)
        self.addPd.setObjectName(u"addPd")

        self.horizontalLayout_7.addWidget(self.addPd)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.main.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.name = QLineEdit(self.groupBox)
        self.name.setObjectName(u"name")

        self.horizontalLayout.addWidget(self.name)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.path = QLineEdit(self.groupBox)
        self.path.setObjectName(u"path")

        self.horizontalLayout.addWidget(self.path)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.yvyan = QLineEdit(self.groupBox)
        self.yvyan.setObjectName(u"yvyan")

        self.horizontalLayout_2.addWidget(self.yvyan)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.prefix = QLineEdit(self.groupBox)
        self.prefix.setObjectName(u"prefix")

        self.horizontalLayout_2.addWidget(self.prefix)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.miaoshu = QTextEdit(self.groupBox)
        self.miaoshu.setObjectName(u"miaoshu")

        self.horizontalLayout_3.addWidget(self.miaoshu)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.code = QTextEdit(self.groupBox)
        self.code.setObjectName(u"code")

        self.horizontalLayout_4.addWidget(self.code)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.OK = QPushButton(self.groupBox)
        self.OK.setObjectName(u"OK")

        self.verticalLayout_2.addWidget(self.OK)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)


        self.main.addWidget(self.groupBox)


        self.horizontalLayout_8.addLayout(self.main)

        self.tabWidget.addTab(self.tab, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.verticalLayout_6 = QVBoxLayout(self.tab2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.tab2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.morenyvyan = QLineEdit(self.tab2)
        self.morenyvyan.setObjectName(u"morenyvyan")

        self.horizontalLayout_10.addWidget(self.morenyvyan)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_9 = QLabel(self.tab2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)

        self.vscodeDMDpath = QLineEdit(self.tab2)
        self.vscodeDMDpath.setObjectName(u"vscodeDMDpath")

        self.horizontalLayout_11.addWidget(self.vscodeDMDpath)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(self.tab2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.lci_session_key = QLineEdit(self.tab2)
        self.lci_session_key.setObjectName(u"lci_session_key")

        self.horizontalLayout_12.addWidget(self.lci_session_key)

        self.yanzhengkeyong = QPushButton(self.tab2)
        self.yanzhengkeyong.setObjectName(u"yanzhengkeyong")

        self.horizontalLayout_12.addWidget(self.yanzhengkeyong)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.tabWidget.addTab(self.tab2, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.textBrowser = QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(220, 10, 671, 192))
        self.logoImg = QLabel(self.tab_2)
        self.logoImg.setObjectName(u"logoImg")
        self.logoImg.setEnabled(False)
        self.logoImg.setGeometry(QRect(10, 10, 191, 191))
        self.logoImg.setMinimumSize(QSize(162, 0))
        self.widget = QWidget(self.tab_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 220, 211, 16))
        self.horizontalLayout_13 = QHBoxLayout(self.widget)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_13.addWidget(self.label_11)

        self.vv = QLabel(self.widget)
        self.vv.setObjectName(u"vv")

        self.horizontalLayout_13.addWidget(self.vv)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_9.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.codeGuanli)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 930, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u4ee3\u7801\u7247\u6bb5\u5217\u8868", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.CloudSwitch.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u5f00\u5173", None))
        self.delPd.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.addPd.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u4ee3\u7801\u7247\u6bb5\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8def\u5f84", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8bed\u8a00", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"prefix", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u63cf\u8ff0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u4ee3\u7801", None))
        self.OK.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u7ba1\u7406", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u8bed\u8a00", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u4ee3\u7801\u7247\u6bb5\u6587\u4ef6\u8def\u5f84", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"lci_session_key", None))
        self.yanzhengkeyong.setText(QCoreApplication.translate("MainWindow", u"\u9a8c\u8bc1\u53ef\u7528\u6027", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">LstCodeGuanli</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u4f5c\u8005\uff1a\u661f\u7ec7</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u76ee\u6807\uff1a\u5b9e\u7528\u6027</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; t"
                        "ext-indent:0px;\"><span style=\" font-size:14pt;\">Github:github.com/hengshizhi/LstCodeGuanli</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u4f5c\u8005\u535a\u5ba2\uff1awww.df100.ltd</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Help\uff1a\u5f85\u5b9a</span></p></body></html>", None))
        self.logoImg.setText(QCoreApplication.translate("MainWindow", u"logo                       ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u7248\u672c\u53f7\uff1a", None))
        self.vv.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi




#路径信息
import os
def getFileFolderSize(fileOrFolderPath):
  """get size for file or folder
  计算文件夹的大小(包含子文件夹的大小)
  """
  totalSize = 0
 
  if not os.path.exists(fileOrFolderPath):
    return totalSize
  
  if os.path.isfile(fileOrFolderPath):
    totalSize = os.path.getsize(fileOrFolderPath) # 5041481
    return totalSize
 
  if os.path.isdir(fileOrFolderPath):
    with os.scandir(fileOrFolderPath) as dirEntryList:
      for curSubEntry in dirEntryList:
        curSubEntryFullPath = os.path.join(fileOrFolderPath, curSubEntry.name)
        if curSubEntry.is_dir():
          curSubFolderSize = getFileFolderSize(curSubEntryFullPath) # 5800007
          totalSize += curSubFolderSize
        elif curSubEntry.is_file():
          curSubFileSize = os.path.getsize(curSubEntryFullPath) # 1891
          totalSize += curSubFileSize
 
      return totalSize
def PathSize(path:str,File_or_folders:bool = None) -> int:
    '''
    计算一个目录的大小，参数:
    path :目标路径
    File_or_folders :是否自动检测路径类型,如果不传,就是自动检测,如果传,则需要传一个路径是否是文件
    '''
    try:
        if(File_or_folders == None):
            File_or_folders = File_or_folder(path)
        if(File_or_folders):
            return os.path.getsize(path)
        else:
            return getFileFolderSize(path)
    except:
        return False
def File_or_folder(path):
    '''
    一个路径是否是文件？
    返回:
    True :目标是文件
    False :目标是目录
    None :目标不存在
    '''
    try:
        if(os.path.isfile(path)):
            return True
        else:
            return False
    except:
        return None
def List(path):
    return [os.path.join(path,i) for i in os.listdir(path)]
def NameList(path):
    return os.listdir(path)

def FileData(path,wwwroot='/mnt/'):
    '''获取文件信息
    传入: path :需要获取的
    返回：
    (
        路径,
        绝对路径,
        是否是文件:bool,
        大小,
        最近访问时间,
        文件创建时间,
        最近修改时间,
        文件所在路径【如果是目录就和目录路径一致】,
        文件名
    )
    '''
    '''
    path :文件路径
    file_path :文件所在目录路径
    file_name :文件名
    '''
    file_path, file_name = os.path.split(path) #文件所在目录路径，文件名
    File_or_folder_data = File_or_folder(path) #检测是否是文件
    return ((os.path.normpath(path.replace(wwwroot, '')),  #相对路径
    os.path.abspath(path), #绝对路径
    File_or_folder_data, #是否是文件:bool
    PathSize(path,File_or_folder_data) , #文件（目录）大小
    os.path.getatime(path), #最近访问时间
    os.path.getctime(path) , #文件创建时间
    os.path.getmtime(path) , #最近修改时间
    file_path, #文件所在目录路径【如果是目录就和目录路径一致】
    file_name #文件名
    ))
def Dict(path,wwwroot='/mnt/'):
    '''
    传入 : path :需要遍历的目录
    返回 :{file_name:FileData(ListData[i])}
    '''
    returnDict = {}
    ListData = List(path)
    NameListData = NameList(path)
    for i in range(len(NameListData)):
        '''
        ListData[i] :文件路径
        '''
        returnDict[NameListData[i]] = FileData(ListData[i],wwwroot) #获取文件信息
    return returnDict
def All_Dict(path,wwwroot='/mnt/'):
    '''
    传入: path :需要遍历的目录(注意，包括子目录的遍历)
    返回 :{file_name:FileData(ListData[i])}
    '''
    ListData = []
    NameListData = []
    for root, dirs, files in os.walk(path, topdown=False): #遍历所有子目录
        for name in files:
            ListData.append(os.path.join(root, name))
            NameListData.append(name) #加入文件名
        for name in dirs:
            ListData.append(os.path.join(root, name))
            NameListData.append(name)
    returnDict = {}
    for i in range(len(NameListData)):
        '''
        ListData[i] :文件路径
        '''
        returnDict[NameListData[i]] = FileData(ListData[i],wwwroot) #获取文件信息
    return returnDict
#print(Dict('d:\Downloads\Luxis file management\wwwroot\\'))

import json
from PySide2.QtWidgets import QMessageBox
from PySide2.QtWidgets import QApplication,QMainWindow
from urllib.request import urlopen
from threading import Thread
vv = b'1.1'
vvstr = '1.1'
# path = R'C:\Users\Administrator\AppData\Roaming\Code\User\snippets'
# yvyan = 'javascript,typescript'
# config.data['vscodeDMDpath'] is path
# config.data['morenyvyan'] is yvyan
# from ui_main import Ui_Form
# import ui_main
# 注意 这里选择的父类 要和你UI文件窗体一样的类型
# 主窗口是 QMainWindow， 表单是 QWidget， 对话框是 QDialog
def 获得代码段列表(path) -> list:
    fileList = List(path)
    codeDuanList = []
    for fpath in fileList:
        name = os.path.basename(fpath).replace('.code-snippets','')
        with open(fpath,'r',encoding='utf-8') as f:
            data = f.read()
            data = json.loads(data)['Print to console']
        语言 = data['scope']
        前缀 = data['prefix']
        描述 = data['description']
        code = ''
        for n in data['body']:
            code += n+'\n'
        codeDuanList.append({
            'name':name,
            '语言':语言,
            '前缀':前缀,
            '描述':描述,
            'code':code,
        })
    return codeDuanList

class config():
    def __init__(self,fipath='./configuration.json'):
        self.fipath = fipath
        if (not os.path.isfile(fipath)):
            self.初始化配置()
            self.data = self.get()
        else:
            self.data = self.get()
    def get(self):
        with open(self.fipath,'r') as f:
            return json.loads(f.read())
    def 初始化配置(self):
        with open(self.fipath,'w') as f:
            f.write(json.dumps(
                {
                    'morenyvyan':'javascript,typescript',
                    'vscodeDMDpath':R'C:\Users\Administrator\AppData\Roaming\Code\User\snippets',
                    'lci_session_key':'',
                }
            ))

    def 更新配置(self):
        with open(self.fipath,'w') as f:
            f.write(json.dumps(
                self.data
            ))
class MainWindow(QMainWindow):
    moshi = 'new' # 写入模式:'che'更改,'new'创建
    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)
        self.刷新代码段列表()
        self.输入框提示()
        self.按钮绑定()
        self.刷新默认值()
        self.ui.codePdList.itemSelectionChanged.connect(self.选中列表项)
        self.ui.vv.setText(vvstr)
        self.ui.morenyvyan.textChanged.connect(self.morenyvyan)
        self.ui.vscodeDMDpath.textChanged.connect(self.vscodeDMDpath)
        self.ui.lci_session_key.textChanged.connect(self.lci_session_key)
        self.ui.sou.textChanged.connect(self.搜索)
        self.logoimg()
        self.更新提醒()
    def vqingqiu(self):
        from PySide2.QtWidgets import QInputDialog,QLineEdit

        myURL = urlopen("http://lstcodeguanli.df100.ltd/v.php")
        v = myURL.read()
        print(v)
        if (v != vv):
            title, okPressed = QInputDialog.getText(
                self, 
                "是否安装最新版本",
                "如果需要更新请运行./updater.exe",
                QLineEdit.Normal,
                "")
            if okPressed:
                os.system('./updater.exe')
    def 更新提醒(self):
        # 返回值分别是输入数据 和 是否点击了 OK 按钮（True/False）
        thread = Thread(target = self.vqingqiu,
                        args= ()
                        )
        thread.start()

    def morenyvyan(self):
        '''默认语言设置'''
        config.data['morenyvyan'] = self.ui.morenyvyan.text()
        config.更新配置()
        self.刷新默认值()
    def vscodeDMDpath(self):
        '''代码段存放路径设置'''
        config.data['vscodeDMDpath'] = self.ui.vscodeDMDpath.text()
        config.更新配置()
        self.刷新默认值()
    def lci_session_key(self):
        '''lci_session_key设置'''
        config.data['lci_session_key'] = self.ui.lci_session_key.text()
        config.更新配置()
        self.刷新默认值()
    def 刷新默认值(self):
        self.ui.path.setText(config.data['vscodeDMDpath'])
        self.ui.yvyan.setText(config.data['morenyvyan'])
        self.ui.morenyvyan.setText(config.data['morenyvyan'])
        self.ui.vscodeDMDpath.setText(config.data['vscodeDMDpath'])
        self.ui.lci_session_key.setText(config.data['lci_session_key'])
    def logoimg(self):
        '''显示logo'''
        # self.ui.logoImg
        hbox=QHBoxLayout()
        pixmap = QPixmap('./logo.png')  # 按指定路径找到图片
        self.ui.logoImg.setPixmap (pixmap)  # 在label上显示图片
        self.ui.logoImg.setScaledContents (True)  # 让图片自适应label大小
        hbox.addWidget(self.ui.logoImg)
        self.setLayout(hbox)
        self.move (300, 200)
        self.setWindowTitle ('pic')
        self.show ()
    def 搜索(self):
        text = self.ui.sou.text()
        if (text.replace(' ','') == None or text.replace(' ','') == ''): # 去除空格如果
            self.刷新代码段列表(刷新数据=False)
        else:
            codeDuanList = []
            iss = 0
            for i in self.codeDuanList:
                if (text in i['name']):
                    codeDuanList.append(self.codeDuanList[iss])
                iss += 1
            self.刷新代码段列表(刷新数据=False,自定义列表=codeDuanList)
    def 按钮绑定(self):
        self.ui.name.textChanged.connect(self.自动填写prefix) # 回车的时候自动填写prefix
        self.ui.OK.clicked.connect(self.写入代码片段)
        self.ui.addPd.clicked.connect(self.addPd)
        self.ui.delPd.clicked.connect(self.删除代码段)
    def 删除代码段(self):
        from PySide2.QtWidgets import QInputDialog,QLineEdit
        # 返回值分别是输入数据 和 是否点击了 OK 按钮（True/False）
        title, okPressed = QInputDialog.getText(
            self, 
            "是否删除",
            "如果要删除请点击OK",
            QLineEdit.Normal,
            "")

        if okPressed:
            name = self.ui.name.text()
            self.delCpY(name)
            self.代码段信息全部清除()
            self.刷新代码段列表()
        else:
            pass

    def 输入框提示(self):
        self.ui.name.setPlaceholderText('代码片段名') # 提示
        self.ui.path.setPlaceholderText('vscode的代码片段路径') # 提示
        self.ui.yvyan.setPlaceholderText('代码片段使用语言') # 提示
        self.ui.miaoshu.setPlaceholderText('代码片段描述') # 提示
    def 代码段信息全部清除(self):
        self.ui.name.clear()
        self.ui.yvyan.setText(config.data['morenyvyan'])
        self.ui.code.clear()
        self.ui.miaoshu.clear()
        self.ui.prefix.clear()
    def addPd(self):
        self.moshi = 'new'
        self.代码段信息全部清除()
        self.ui.name.setPlaceholderText('新建代码片段名')
        # self.刷新代码段列表()
    def 自动填写prefix(self,name):
        self.ui.prefix.setText(name)
    def 写入代码片段(self): 
        code = self.ui.code.toPlainText()
        name = self.ui.name.text()
        if (name == None or name == ''):return True
        prefix = self.ui.prefix.text()
        paths = self.ui.path.text()
        scope = self.ui.yvyan.text()
        description = self.ui.miaoshu.toPlainText()

        if(self.moshi == 'new'):
            if(self.new(paths,name,scope,prefix,code,description)):            
                self.ui.code.clear()
                self.ui.name.clear()
                self.ui.prefix.clear()
                self.ui.miaoshu.clear()
                self.输入框提示()
            else:
                QMessageBox.warning(
                self.ui,
                '创建错误',
                '创建代码段失败,请重试')
        else:
            if (name == self.xuanzhongDuanName):
                if(self.new(paths,name,scope,prefix,code,description)):            
                    self.刷新代码段列表数据()
                    self.更新代码段信息为列表选中的()
                else:
                    QMessageBox.warning(
                    self.ui,
                    '更改错误',
                    '更改代码段失败,请重试')
            else:
                os.rename(self.getfPath(self.xuanzhongDuanName),self.getfPath(name))
                self.刷新代码段列表()
        self.刷新代码段列表()
    def 刷新代码段列表数据(self):
        self.codeDuanList = 获得代码段列表(config.data['vscodeDMDpath']) # 刷新
    def 刷新代码段列表(self,刷新数据=True,自定义列表=[]):
        print('刷新')
        if (刷新数据):
            self.刷新代码段列表数据()
        if (自定义列表 != []):
            codeDuanListYuanshujv = 自定义列表
        else:
            codeDuanListYuanshujv = self.codeDuanList
        codeDuanList = []
        for i in codeDuanListYuanshujv:
            codeDuanList.append(f"{i['name']}({i['语言']})")
        self.ui.codePdList.clear() # 清空列表
        self.ui.codePdList.addItems(codeDuanList) # 添加列表项
    def 通过name反查代码段信息(self,name):
        iss = 0
        for i in self.codeDuanList:
            if (i['name'] in name):
                return iss
            iss += 1
    def 更新代码段信息为列表选中的(self):
        self.currentItem = self.ui.codePdList.currentRow() # 当前选择项目 https://learnku.com/articles/35634
        xuanzhong = self.codeDuanList[self.通过name反查代码段信息(self.ui.codePdList.currentItem().text())]
        self.xuanzhongDuanName = xuanzhong['name'] # 选中的代码段名
        self.ui.name.setText(xuanzhong['name'])
        self.ui.yvyan.setText(xuanzhong['语言'])
        self.ui.code.setPlainText(xuanzhong['code'])
        self.ui.miaoshu.setPlainText(xuanzhong['描述'])
        self.ui.prefix.setText(xuanzhong['前缀'])
    def 选中列表项(self):
        self.moshi = 'che'
        self.更新代码段信息为列表选中的()
    def new(self,paths,name,scope,prefix,code,description):
        '''创建一个代码段'''
        filepath = paths+'\\'+name+'.code-snippets'
        data = {
            "Print to console" : {
                    "scope": scope,
                    "prefix": prefix,
                    "body": [
                        code
                    ],
                    "description": description
                }
        }
        try:
            f = open(filepath,'w')
            f.write(json.dumps(data))
            f.close()
            return True
        except:
            return False
    def getfPath(self,name):
        return os.path.normpath(path+'\\'+name+'.code-snippets')
    def delCpY(self,name):
        '''删除一个代码段'''
        os.remove(self.getfPath(name))
if __name__ == "__main__":
    from PySide2.QtGui import  QIcon
    from qt_material import apply_stylesheet
    config = config()
    app = QApplication([])
    app.setWindowIcon(QIcon('logo.png'))
    # setup stylesheet
    apply_stylesheet(app, theme='dark_lightgreen.xml')
    mainw = MainWindow()
    mainw.setWindowTitle('LstCodeGuanli')
    mainw.show()
    app.exec_()

