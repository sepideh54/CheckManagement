
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1465, 900)
        MainWindow.setMinimumSize(QtCore.QSize(1465, 900))
        MainWindow.setMaximumSize(QtCore.QSize(1465, 900))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_Sabtamaliyat = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Sabtamaliyat.setGeometry(QtCore.QRect(10, 10, 371, 371))
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_Sabtamaliyat.setFont(font)
        self.groupBox_Sabtamaliyat.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_Sabtamaliyat.setStyleSheet("QGroupBox{\n"
"    border:1px solid #C8CDD3;\n"
"    border-radius:8px;\n"
"    margin-top:12px;\n"
"    font-size:15pt;\n"
"    font-weight:bold;\n"
"    color:#2C3E50;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"    subcontrol-origin: margin;\n"
"    left:15px;\n"
"    padding:0px 6px;\n"
"}")
        self.groupBox_Sabtamaliyat.setObjectName("groupBox_Sabtamaliyat")
        self.groupBox_Moshtaridokmeha_4 = QtWidgets.QGroupBox(self.groupBox_Sabtamaliyat)
        self.groupBox_Moshtaridokmeha_4.setGeometry(QtCore.QRect(10, 300, 361, 61))
        self.groupBox_Moshtaridokmeha_4.setStyleSheet("QPushButton{\n"
"    border-radius:8px;\n"
"    border:1px solid #B8BDC5;\n"
"    color:white;\n"
"    font-size:12pt;\n"
"    font-weight:bold;\n"
"    padding:6px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border:1px solid #4A90E2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top:7px;\n"
"    padding-left:7px;\n"
"}")
        self.groupBox_Moshtaridokmeha_4.setTitle("")
        self.groupBox_Moshtaridokmeha_4.setObjectName("groupBox_Moshtaridokmeha_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_Moshtaridokmeha_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_Sabtmoshtari_2 = QtWidgets.QPushButton(self.groupBox_Moshtaridokmeha_4)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Sabtmoshtari_2.setFont(font)
        self.pushButton_Sabtmoshtari_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_Sabtmoshtari_2.setStyleSheet("background-color: rgb(34, 197, 94);\n"
"QPushButton{\n"
"    border-radius:8px;\n"
"    border:1px solid #B8BDC5;\n"
"    color:white;\n"
"    font-size:10pt;\n"
"    font-weight:bold;\n"
"    padding:6px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border:1px solid #4A90E2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top:7px;\n"
"    padding-left:7px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Downloads/save-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Sabtmoshtari_2.setIcon(icon)
        self.pushButton_Sabtmoshtari_2.setIconSize(QtCore.QSize(20, 17))
        self.pushButton_Sabtmoshtari_2.setObjectName("pushButton_Sabtmoshtari_2")
        self.horizontalLayout_4.addWidget(self.pushButton_Sabtmoshtari_2)
        self.pushButton_Virayeshmoshtari_2 = QtWidgets.QPushButton(self.groupBox_Moshtaridokmeha_4)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Virayeshmoshtari_2.setFont(font)
        self.pushButton_Virayeshmoshtari_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_Virayeshmoshtari_2.setStyleSheet("\n"
"background-color: rgb(59, 130, 246);\n"
"QPushButton{\n"
"    border-radius:8px;\n"
"    border:1px solid #B8BDC5;\n"
"    color:white;\n"
"    font-size:10pt;\n"
"    font-weight:bold;\n"
"    padding:6px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border:1px solid #4A90E2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top:7px;\n"
"    padding-left:7px;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Downloads/edit-svgrepo-com (3).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Virayeshmoshtari_2.setIcon(icon1)
        self.pushButton_Virayeshmoshtari_2.setIconSize(QtCore.QSize(17, 17))
        self.pushButton_Virayeshmoshtari_2.setObjectName("pushButton_Virayeshmoshtari_2")
        self.horizontalLayout_4.addWidget(self.pushButton_Virayeshmoshtari_2)
        self.widget = QtWidgets.QWidget(self.groupBox_Sabtamaliyat)
        self.widget.setGeometry(QtCore.QRect(10, 30, 351, 271))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textEdit_Address_2 = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit_Address_2.setFont(font)
        self.textEdit_Address_2.setStyleSheet("QTextEdit{\n"
"    border:1px solid #C8CDD3;\n"
"    border-radius:6px;\n"
"    padding:6px;\n"
"    font-size:10pt;\n"
"}\n"
"\n"
"QTextEdit:focus{\n"
"    border:2px solid #4A90E2;\n"
"}")
        self.textEdit_Address_2.setObjectName("textEdit_Address_2")
        self.gridLayout_3.addWidget(self.textEdit_Address_2, 10, 1, 1, 1)
        self.label_Codemoshtari_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Codemoshtari_3.setFont(font)
        self.label_Codemoshtari_3.setObjectName("label_Codemoshtari_3")
        self.gridLayout_3.addWidget(self.label_Codemoshtari_3, 5, 0, 1, 1)
        self.label_Codemoshtari_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Codemoshtari_2.setFont(font)
        self.label_Codemoshtari_2.setStyleSheet("")
        self.label_Codemoshtari_2.setObjectName("label_Codemoshtari_2")
        self.gridLayout_3.addWidget(self.label_Codemoshtari_2, 0, 0, 1, 1)
        self.label_Codemoshtari_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Codemoshtari_6.setFont(font)
        self.label_Codemoshtari_6.setObjectName("label_Codemoshtari_6")
        self.gridLayout_3.addWidget(self.label_Codemoshtari_6, 1, 0, 1, 1)
        self.label_Codemoshtari_9 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Codemoshtari_9.setFont(font)
        self.label_Codemoshtari_9.setObjectName("label_Codemoshtari_9")
        self.gridLayout_3.addWidget(self.label_Codemoshtari_9, 8, 0, 1, 1)
        self.label_Codemoshtari_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Codemoshtari_8.setFont(font)
        self.label_Codemoshtari_8.setObjectName("label_Codemoshtari_8")
        self.gridLayout_3.addWidget(self.label_Codemoshtari_8, 7, 0, 1, 1)
        self.lineEdit_Codemoshtari_2 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_Codemoshtari_2.setFont(font)
        self.lineEdit_Codemoshtari_2.setObjectName("lineEdit_Codemoshtari_2")
        self.gridLayout_3.addWidget(self.lineEdit_Codemoshtari_2, 0, 1, 1, 1)
        self.label_Address_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Address_2.setFont(font)
        self.label_Address_2.setObjectName("label_Address_2")
        self.gridLayout_3.addWidget(self.label_Address_2, 10, 0, 1, 1)
        self.comboBox_Shax = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        self.comboBox_Shax.setFont(font)
        self.comboBox_Shax.setObjectName("comboBox_Shax")
        self.gridLayout_3.addWidget(self.comboBox_Shax, 7, 1, 1, 1)
        self.comboBox_Vaziyatsamaneh = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        self.comboBox_Vaziyatsamaneh.setFont(font)
        self.comboBox_Vaziyatsamaneh.setObjectName("comboBox_Vaziyatsamaneh")
        self.gridLayout_3.addWidget(self.comboBox_Vaziyatsamaneh, 8, 1, 1, 1)
        self.dateEdit_Tarixamaliyat = QtWidgets.QDateEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_Tarixamaliyat.setFont(font)
        self.dateEdit_Tarixamaliyat.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 2, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_Tarixamaliyat.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit_Tarixamaliyat.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit_Tarixamaliyat.setObjectName("dateEdit_Tarixamaliyat")
        self.gridLayout_3.addWidget(self.dateEdit_Tarixamaliyat, 5, 1, 1, 1)
        self.comboBox_Noeamaliyat = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        self.comboBox_Noeamaliyat.setFont(font)
        self.comboBox_Noeamaliyat.setObjectName("comboBox_Noeamaliyat")
        self.gridLayout_3.addWidget(self.comboBox_Noeamaliyat, 1, 1, 1, 1)
        self.groupBox_Etelaatcheck = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Etelaatcheck.setGeometry(QtCore.QRect(390, 10, 701, 371))
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_Etelaatcheck.setFont(font)
        self.groupBox_Etelaatcheck.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_Etelaatcheck.setStyleSheet("QGroupBox{\n"
"    border:1px solid #C8CDD3;\n"
"    border-radius:8px;\n"
"    margin-top:12px;\n"
"    font-size:15pt;\n"
"    font-weight:bold;\n"
"    color:#2C3E50;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"    subcontrol-origin: margin;\n"
"    left:15px;\n"
"    padding:0px 6px;\n"
"}")
        self.groupBox_Etelaatcheck.setObjectName("groupBox_Etelaatcheck")
        self.widget1 = QtWidgets.QWidget(self.groupBox_Etelaatcheck)
        self.widget1.setGeometry(QtCore.QRect(13, 30, 681, 131))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label__Saderkonandeh = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label__Saderkonandeh.setFont(font)
        self.label__Saderkonandeh.setObjectName("label__Saderkonandeh")
        self.gridLayout_2.addWidget(self.label__Saderkonandeh, 3, 2, 1, 1)
        self.lineEdit_Mablagcheck = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_Mablagcheck.setFont(font)
        self.lineEdit_Mablagcheck.setObjectName("lineEdit_Mablagcheck")
        self.gridLayout_2.addWidget(self.lineEdit_Mablagcheck, 3, 1, 1, 1)
        self.label_Shomarehsayadi = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Shomarehsayadi.setFont(font)
        self.label_Shomarehsayadi.setObjectName("label_Shomarehsayadi")
        self.gridLayout_2.addWidget(self.label_Shomarehsayadi, 0, 0, 1, 1)
        self.comboBox_Banksaderkonandeh = QtWidgets.QComboBox(self.widget1)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        self.comboBox_Banksaderkonandeh.setFont(font)
        self.comboBox_Banksaderkonandeh.setObjectName("comboBox_Banksaderkonandeh")
        self.gridLayout_2.addWidget(self.comboBox_Banksaderkonandeh, 4, 1, 1, 1)
        self.label_Tarixsarresid = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Tarixsarresid.setFont(font)
        self.label_Tarixsarresid.setObjectName("label_Tarixsarresid")
        self.gridLayout_2.addWidget(self.label_Tarixsarresid, 4, 2, 1, 1)
        self.label_Codecheck = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Codecheck.setFont(font)
        self.label_Codecheck.setObjectName("label_Codecheck")
        self.gridLayout_2.addWidget(self.label_Codecheck, 0, 2, 1, 1)
        self.lineEdit_Codecheck = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_Codecheck.setFont(font)
        self.lineEdit_Codecheck.setObjectName("lineEdit_Codecheck")
        self.gridLayout_2.addWidget(self.lineEdit_Codecheck, 0, 3, 1, 1)
        self.lineEdit_Shomarehsayadi = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_Shomarehsayadi.setFont(font)
        self.lineEdit_Shomarehsayadi.setObjectName("lineEdit_Shomarehsayadi")
        self.gridLayout_2.addWidget(self.lineEdit_Shomarehsayadi, 0, 1, 1, 1)
        self.label__Mablagcheck = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label__Mablagcheck.setFont(font)
        self.label__Mablagcheck.setObjectName("label__Mablagcheck")
        self.gridLayout_2.addWidget(self.label__Mablagcheck, 3, 0, 1, 1)
        self.comboBox_Saderkonandeh = QtWidgets.QComboBox(self.widget1)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        self.comboBox_Saderkonandeh.setFont(font)
        self.comboBox_Saderkonandeh.setObjectName("comboBox_Saderkonandeh")
        self.gridLayout_2.addWidget(self.comboBox_Saderkonandeh, 3, 3, 1, 1)
        self.label_Banksaderkonandeh = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Banksaderkonandeh.setFont(font)
        self.label_Banksaderkonandeh.setObjectName("label_Banksaderkonandeh")
        self.gridLayout_2.addWidget(self.label_Banksaderkonandeh, 4, 0, 1, 1)
        self.dateEdit_Tarixamaliyat_2 = QtWidgets.QDateEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_Tarixamaliyat_2.setFont(font)
        self.dateEdit_Tarixamaliyat_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 2, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_Tarixamaliyat_2.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit_Tarixamaliyat_2.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit_Tarixamaliyat_2.setObjectName("dateEdit_Tarixamaliyat_2")
        self.gridLayout_2.addWidget(self.dateEdit_Tarixamaliyat_2, 4, 3, 1, 1)
        self.groupBox_Moshtaridokmeha_2 = QtWidgets.QGroupBox(self.groupBox_Etelaatcheck)
        self.groupBox_Moshtaridokmeha_2.setGeometry(QtCore.QRect(50, 300, 621, 61))
        self.groupBox_Moshtaridokmeha_2.setStyleSheet("QPushButton{\n"
"    border-radius:8px;\n"
"    border:1px solid #B8BDC5;\n"
"    color:white;\n"
"    font-size:12pt;\n"
"    font-weight:bold;\n"
"    padding:6px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border:1px solid #4A90E2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top:7px;\n"
"    padding-left:7px;\n"
"}")
        self.groupBox_Moshtaridokmeha_2.setTitle("")
        self.groupBox_Moshtaridokmeha_2.setObjectName("groupBox_Moshtaridokmeha_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_Moshtaridokmeha_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Sabtcheck = QtWidgets.QPushButton(self.groupBox_Moshtaridokmeha_2)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Sabtcheck.setFont(font)
        self.pushButton_Sabtcheck.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_Sabtcheck.setStyleSheet("background-color: rgb(34, 197, 94);")
        self.pushButton_Sabtcheck.setIcon(icon)
        self.pushButton_Sabtcheck.setIconSize(QtCore.QSize(17, 17))
        self.pushButton_Sabtcheck.setObjectName("pushButton_Sabtcheck")
        self.horizontalLayout_2.addWidget(self.pushButton_Sabtcheck)
        self.pushButton_jostojocheck = QtWidgets.QPushButton(self.groupBox_Moshtaridokmeha_2)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_jostojocheck.setFont(font)
        self.pushButton_jostojocheck.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_jostojocheck.setStyleSheet("background-color: rgb(139, 92, 246);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/Downloads/search-file-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_jostojocheck.setIcon(icon2)
        self.pushButton_jostojocheck.setIconSize(QtCore.QSize(17, 17))
        self.pushButton_jostojocheck.setObjectName("pushButton_jostojocheck")
        self.horizontalLayout_2.addWidget(self.pushButton_jostojocheck)
        self.pushButton_Virayeshcheck = QtWidgets.QPushButton(self.groupBox_Moshtaridokmeha_2)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Virayeshcheck.setFont(font)
        self.pushButton_Virayeshcheck.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_Virayeshcheck.setStyleSheet("\n"
"background-color: rgb(59, 130, 246);")
        self.pushButton_Virayeshcheck.setIcon(icon1)
        self.pushButton_Virayeshcheck.setIconSize(QtCore.QSize(17, 17))
        self.pushButton_Virayeshcheck.setObjectName("pushButton_Virayeshcheck")
        self.horizontalLayout_2.addWidget(self.pushButton_Virayeshcheck)
        self.pushButton_Gardeshcheck = QtWidgets.QPushButton(self.groupBox_Moshtaridokmeha_2)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Gardeshcheck.setFont(font)
        self.pushButton_Gardeshcheck.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_Gardeshcheck.setStyleSheet("background-color: rgb(245, 158, 11);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/Downloads/process-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Gardeshcheck.setIcon(icon3)
        self.pushButton_Gardeshcheck.setIconSize(QtCore.QSize(17, 17))
        self.pushButton_Gardeshcheck.setObjectName("pushButton_Gardeshcheck")
        self.horizontalLayout_2.addWidget(self.pushButton_Gardeshcheck)
        self.pushButton_Hazfcheck = QtWidgets.QPushButton(self.groupBox_Moshtaridokmeha_2)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Hazfcheck.setFont(font)
        self.pushButton_Hazfcheck.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_Hazfcheck.setStyleSheet("background-color: rgb(239, 68, 68);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/Downloads/delete-recycle-bin-trash-can-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Hazfcheck.setIcon(icon4)
        self.pushButton_Hazfcheck.setIconSize(QtCore.QSize(17, 17))
        self.pushButton_Hazfcheck.setObjectName("pushButton_Hazfcheck")
        self.horizontalLayout_2.addWidget(self.pushButton_Hazfcheck)
        self.label_Axroyecheck = QtWidgets.QLabel(self.groupBox_Etelaatcheck)
        self.label_Axroyecheck.setGeometry(QtCore.QRect(560, 210, 130, 29))
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Axroyecheck.setFont(font)
        self.label_Axroyecheck.setObjectName("label_Axroyecheck")
        self.label_Axposhtecheck = QtWidgets.QLabel(self.groupBox_Etelaatcheck)
        self.label_Axposhtecheck.setGeometry(QtCore.QRect(210, 210, 130, 29))
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Axposhtecheck.setFont(font)
        self.label_Axposhtecheck.setObjectName("label_Axposhtecheck")
        self.pushButton_Axroyecheck = QtWidgets.QPushButton(self.groupBox_Etelaatcheck)
        self.pushButton_Axroyecheck.setGeometry(QtCore.QRect(440, 230, 91, 71))
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Axroyecheck.setFont(font)
        self.pushButton_Axroyecheck.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/Downloads/save-save-the-document-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Axroyecheck.setIcon(icon5)
        self.pushButton_Axroyecheck.setIconSize(QtCore.QSize(55, 55))
        self.pushButton_Axroyecheck.setObjectName("pushButton_Axroyecheck")
        self.pushButton_Axposhtecheck = QtWidgets.QPushButton(self.groupBox_Etelaatcheck)
        self.pushButton_Axposhtecheck.setGeometry(QtCore.QRect(100, 230, 91, 71))
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Axposhtecheck.setFont(font)
        self.pushButton_Axposhtecheck.setText("")
        self.pushButton_Axposhtecheck.setIcon(icon5)
        self.pushButton_Axposhtecheck.setIconSize(QtCore.QSize(55, 55))
        self.pushButton_Axposhtecheck.setObjectName("pushButton_Axposhtecheck")
        self.label_Tozihatetelatcheck = QtWidgets.QLabel(self.groupBox_Etelaatcheck)
        self.label_Tozihatetelatcheck.setGeometry(QtCore.QRect(580, 160, 111, 31))
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Tozihatetelatcheck.setFont(font)
        self.label_Tozihatetelatcheck.setObjectName("label_Tozihatetelatcheck")
        self.textEdit_Tozihatetelatcheck = QtWidgets.QTextEdit(self.groupBox_Etelaatcheck)
        self.textEdit_Tozihatetelatcheck.setGeometry(QtCore.QRect(10, 160, 581, 41))
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit_Tozihatetelatcheck.setFont(font)
        self.textEdit_Tozihatetelatcheck.setObjectName("textEdit_Tozihatetelatcheck")
        self.groupBox_Moshtarijadid = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Moshtarijadid.setGeometry(QtCore.QRect(1100, 10, 351, 371))
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_Moshtarijadid.setFont(font)
        self.groupBox_Moshtarijadid.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_Moshtarijadid.setStyleSheet("QGroupBox{\n"
"    border:1px solid #C8CDD3;\n"
"    border-radius:8px;\n"
"    margin-top:12px;\n"
"    font-size:15pt;\n"
"    font-weight:bold;\n"
"    color:#2C3E50;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"    subcontrol-origin: margin;\n"
"    left:15px;\n"
"    padding:0px 6px;\n"
"}")
        self.groupBox_Moshtarijadid.setObjectName("groupBox_Moshtarijadid")
        self.groupBox_Moshtaridokmeha = QtWidgets.QGroupBox(self.groupBox_Moshtarijadid)
        self.groupBox_Moshtaridokmeha.setGeometry(QtCore.QRect(20, 300, 321, 61))
        self.groupBox_Moshtaridokmeha.setStyleSheet("QPushButton{\n"
"    border-radius:8px;\n"
"    border:1px solid #B8BDC5;\n"
"    color:white;\n"
"    font-size:12pt;\n"
"    font-weight:bold;\n"
"    padding:6px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border:1px solid #4A90E2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top:7px;\n"
"    padding-left:7px;\n"
"}")
        self.groupBox_Moshtaridokmeha.setTitle("")
        self.groupBox_Moshtaridokmeha.setObjectName("groupBox_Moshtaridokmeha")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_Moshtaridokmeha)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Sabtmoshtari = QtWidgets.QPushButton(self.groupBox_Moshtaridokmeha)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Sabtmoshtari.setFont(font)
        self.pushButton_Sabtmoshtari.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_Sabtmoshtari.setStyleSheet("background-color: rgb(34, 197, 94);")
        self.pushButton_Sabtmoshtari.setIcon(icon)
        self.pushButton_Sabtmoshtari.setIconSize(QtCore.QSize(17, 17))
        self.pushButton_Sabtmoshtari.setObjectName("pushButton_Sabtmoshtari")
        self.horizontalLayout.addWidget(self.pushButton_Sabtmoshtari)
        self.pushButton_jostojomoshtari = QtWidgets.QPushButton(self.groupBox_Moshtaridokmeha)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_jostojomoshtari.setFont(font)
        self.pushButton_jostojomoshtari.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_jostojomoshtari.setStyleSheet("background-color: rgb(139, 92, 246);")
        self.pushButton_jostojomoshtari.setIcon(icon2)
        self.pushButton_jostojomoshtari.setIconSize(QtCore.QSize(17, 17))
        self.pushButton_jostojomoshtari.setObjectName("pushButton_jostojomoshtari")
        self.horizontalLayout.addWidget(self.pushButton_jostojomoshtari)
        self.pushButton_Virayeshmoshtari = QtWidgets.QPushButton(self.groupBox_Moshtaridokmeha)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Virayeshmoshtari.setFont(font)
        self.pushButton_Virayeshmoshtari.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_Virayeshmoshtari.setStyleSheet("\n"
"background-color: rgb(59, 130, 246);")
        self.pushButton_Virayeshmoshtari.setIcon(icon1)
        self.pushButton_Virayeshmoshtari.setIconSize(QtCore.QSize(17, 17))
        self.pushButton_Virayeshmoshtari.setObjectName("pushButton_Virayeshmoshtari")
        self.horizontalLayout.addWidget(self.pushButton_Virayeshmoshtari)
        self.pushButton_Hazfmoshtari = QtWidgets.QPushButton(self.groupBox_Moshtaridokmeha)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Hazfmoshtari.setFont(font)
        self.pushButton_Hazfmoshtari.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_Hazfmoshtari.setStyleSheet("background-color: rgb(239, 68, 68);")
        self.pushButton_Hazfmoshtari.setIcon(icon4)
        self.pushButton_Hazfmoshtari.setIconSize(QtCore.QSize(17, 17))
        self.pushButton_Hazfmoshtari.setObjectName("pushButton_Hazfmoshtari")
        self.horizontalLayout.addWidget(self.pushButton_Hazfmoshtari)
        self.widget2 = QtWidgets.QWidget(self.groupBox_Moshtarijadid)
        self.widget2.setGeometry(QtCore.QRect(10, 30, 331, 271))
        self.widget2.setObjectName("widget2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_Shomaretelsabet = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Shomaretelsabet.setFont(font)
        self.label_Shomaretelsabet.setObjectName("label_Shomaretelsabet")
        self.gridLayout.addWidget(self.label_Shomaretelsabet, 3, 0, 1, 1)
        self.lineEdit_Shomarehtelsabet = QtWidgets.QLineEdit(self.widget2)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_Shomarehtelsabet.setFont(font)
        self.lineEdit_Shomarehtelsabet.setObjectName("lineEdit_Shomarehtelsabet")
        self.gridLayout.addWidget(self.lineEdit_Shomarehtelsabet, 3, 1, 1, 1)
        self.label_Namesherkat = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Namesherkat.setFont(font)
        self.label_Namesherkat.setObjectName("label_Namesherkat")
        self.gridLayout.addWidget(self.label_Namesherkat, 2, 0, 1, 1)
        self.label_Address = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Address.setFont(font)
        self.label_Address.setObjectName("label_Address")
        self.gridLayout.addWidget(self.label_Address, 6, 0, 1, 1)
        self.label_Codemoshtari = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Codemoshtari.setFont(font)
        self.label_Codemoshtari.setObjectName("label_Codemoshtari")
        self.gridLayout.addWidget(self.label_Codemoshtari, 0, 0, 1, 1)
        self.lineEdit_Namesherkat = QtWidgets.QLineEdit(self.widget2)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_Namesherkat.setFont(font)
        self.lineEdit_Namesherkat.setObjectName("lineEdit_Namesherkat")
        self.gridLayout.addWidget(self.lineEdit_Namesherkat, 2, 1, 1, 1)
        self.lineEdit_Codemoshtari = QtWidgets.QLineEdit(self.widget2)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_Codemoshtari.setFont(font)
        self.lineEdit_Codemoshtari.setObjectName("lineEdit_Codemoshtari")
        self.gridLayout.addWidget(self.lineEdit_Codemoshtari, 0, 1, 1, 1)
        self.label__Namemoshtari = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label__Namemoshtari.setFont(font)
        self.label__Namemoshtari.setObjectName("label__Namemoshtari")
        self.gridLayout.addWidget(self.label__Namemoshtari, 1, 0, 1, 1)
        self.textEdit_Address = QtWidgets.QTextEdit(self.widget2)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit_Address.setFont(font)
        self.textEdit_Address.setStyleSheet("QTextEdit{\n"
"    border:1px solid #C8CDD3;\n"
"    border-radius:6px;\n"
"    padding:6px;\n"
"    font-size:10pt;\n"
"}\n"
"\n"
"QTextEdit:focus{\n"
"    border:2px solid #4A90E2;\n"
"}")
        self.textEdit_Address.setObjectName("textEdit_Address")
        self.gridLayout.addWidget(self.textEdit_Address, 6, 1, 1, 1)
        self.lineEdit_Shomarehtelhamrah = QtWidgets.QLineEdit(self.widget2)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        self.lineEdit_Shomarehtelhamrah.setFont(font)
        self.lineEdit_Shomarehtelhamrah.setObjectName("lineEdit_Shomarehtelhamrah")
        self.gridLayout.addWidget(self.lineEdit_Shomarehtelhamrah, 5, 1, 1, 1)
        self.lineEdit_Namemoshtari = QtWidgets.QLineEdit(self.widget2)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_Namemoshtari.setFont(font)
        self.lineEdit_Namemoshtari.setObjectName("lineEdit_Namemoshtari")
        self.gridLayout.addWidget(self.lineEdit_Namemoshtari, 1, 1, 1, 1)
        self.label_Shomaretelhamrah = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Shomaretelhamrah.setFont(font)
        self.label_Shomaretelhamrah.setObjectName("label_Shomaretelhamrah")
        self.gridLayout.addWidget(self.label_Shomaretelhamrah, 5, 0, 1, 1)
        self.groupBox_Natayejhostvajoo = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Natayejhostvajoo.setGeometry(QtCore.QRect(10, 440, 1441, 431))
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_Natayejhostvajoo.setFont(font)
        self.groupBox_Natayejhostvajoo.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_Natayejhostvajoo.setAutoFillBackground(False)
        self.groupBox_Natayejhostvajoo.setStyleSheet("QTableWidget{\n"
"    border:1px solid #C8CDD3;\n"
"    gridline-color:#E6E9ED;\n"
"    alternate-background-color:#F9FAFB;\n"
"    selection-background-color:#4A90E2;\n"
"    selection-color:white;\n"
"    font-size:10pt;\n"
"}\n"
"QGroupBox{\n"
"    border:1px solid #C8CDD3;\n"
"    border-radius:8px;\n"
"    margin-top:12px;\n"
"    font-size:15pt;\n"
"    font-weight:bold;\n"
"    color:#2C3E50;\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"    subcontrol-origin: margin;\n"
"    left:15px;\n"
"    padding:0px 6px;\n"
"}")
        self.groupBox_Natayejhostvajoo.setObjectName("groupBox_Natayejhostvajoo")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_Natayejhostvajoo)
        self.tableWidget.setGeometry(QtCore.QRect(-10, 30, 1451, 351))
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("/* هدر جدول */\n"
"QTableWidget QHeaderView::section {\n"
"    background-color: #2d3748;\n"
"    color: #ffffff;\n"
"    padding: 8px 10px;\n"
"    border: none;\n"
"    border-right: 1px solid #4a5568;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    font-family: \"Vazir\", \"Tahoma\";\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section:last {\n"
"    border-right: none;\n"
"}\n"
"\n"
"/* خود جدول */\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    alternate-background-color: #f7fafc;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 6px;\n"
"    gridline-color: #e2e8f0;\n"
"    font-size: 12px;\n"
"    color: #2d3748;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 6px 10px;\n"
"    border: none;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #4299e1;\n"
"    color: white;\n"
"}")
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(50)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(175)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.groupBox_Moshtaridokmeha_5 = QtWidgets.QGroupBox(self.groupBox_Natayejhostvajoo)
        self.groupBox_Moshtaridokmeha_5.setGeometry(QtCore.QRect(10, 370, 171, 61))
        self.groupBox_Moshtaridokmeha_5.setStyleSheet("QPushButton{\n"
"    border-radius:8px;\n"
"    border:1px solid #B8BDC5;\n"
"    color:white;\n"
"    font-size:12pt;\n"
"    font-weight:bold;\n"
"    padding:6px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border:1px solid #4A90E2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-top:7px;\n"
"    padding-left:7px;\n"
"}")
        self.groupBox_Moshtaridokmeha_5.setTitle("")
        self.groupBox_Moshtaridokmeha_5.setObjectName("groupBox_Moshtaridokmeha_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_Moshtaridokmeha_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_Sabtmoshtari_4 = QtWidgets.QPushButton(self.groupBox_Moshtaridokmeha_5)
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Sabtmoshtari_4.setFont(font)
        self.pushButton_Sabtmoshtari_4.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_Sabtmoshtari_4.setStyleSheet("background-color: rgb(34, 197, 94);")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/Downloads/Icons8-Ios7-Logos-Excel-Copyrighted.512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Sabtmoshtari_4.setIcon(icon6)
        self.pushButton_Sabtmoshtari_4.setIconSize(QtCore.QSize(17, 17))
        self.pushButton_Sabtmoshtari_4.setObjectName("pushButton_Sabtmoshtari_4")
        self.horizontalLayout_5.addWidget(self.pushButton_Sabtmoshtari_4)
        self.lineEdit_Extar = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Extar.setGeometry(QtCore.QRect(404, 394, 691, 41))
        font = QtGui.QFont()
        font.setFamily("B Yekan")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit_Extar.setFont(font)
        self.lineEdit_Extar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_Extar.setAutoFillBackground(False)
        self.lineEdit_Extar.setStyleSheet("\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: red;\n"
"     font-weight: bold;\n"
"")
        self.lineEdit_Extar.setFrame(False)
        self.lineEdit_Extar.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Extar.setObjectName("lineEdit_Extar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_Sabtamaliyat.setTitle(_translate("MainWindow", "ثبت عملیات"))
        self.pushButton_Sabtmoshtari_2.setText(_translate("MainWindow", "ثبت"))
        self.pushButton_Virayeshmoshtari_2.setText(_translate("MainWindow", "ویرایش"))
        self.label_Codemoshtari_3.setText(_translate("MainWindow", "تاریخ عملیات  :"))
        self.label_Codemoshtari_2.setText(_translate("MainWindow", "کد عملیات  :"))
        self.label_Codemoshtari_6.setText(_translate("MainWindow", "نوع عملیات  :"))
        self.label_Codemoshtari_9.setText(_translate("MainWindow", "وضعیت سامانه  :"))
        self.label_Codemoshtari_8.setText(_translate("MainWindow", "شخص /شرکت  :"))
        self.label_Address_2.setText(_translate("MainWindow", "توصیحات  :"))
        self.dateEdit_Tarixamaliyat.setDisplayFormat(_translate("MainWindow", "d/m/yy"))
        self.groupBox_Etelaatcheck.setTitle(_translate("MainWindow", "اطلاعات چک"))
        self.label__Saderkonandeh.setText(_translate("MainWindow", "صادر کننده چک :"))
        self.label_Shomarehsayadi.setText(_translate("MainWindow", "شماره صیادی  :"))
        self.label_Tarixsarresid.setText(_translate("MainWindow", "تاریخ سررسید  :"))
        self.label_Codecheck.setText(_translate("MainWindow", "کد چک   :"))
        self.label__Mablagcheck.setText(_translate("MainWindow", "مبلغ چک  :"))
        self.label_Banksaderkonandeh.setText(_translate("MainWindow", "بانک صادر کننده  :"))
        self.dateEdit_Tarixamaliyat_2.setDisplayFormat(_translate("MainWindow", "d/m/yy"))
        self.pushButton_Sabtcheck.setText(_translate("MainWindow", "ثبت"))
        self.pushButton_jostojocheck.setText(_translate("MainWindow", "جستجو"))
        self.pushButton_Virayeshcheck.setText(_translate("MainWindow", "ویرایش"))
        self.pushButton_Gardeshcheck.setText(_translate("MainWindow", "گردش چک"))
        self.pushButton_Hazfcheck.setText(_translate("MainWindow", "حذف"))
        self.label_Axroyecheck.setText(_translate("MainWindow", "عکس روی چک  :"))
        self.label_Axposhtecheck.setText(_translate("MainWindow", "عکس پشت چک  :"))
        self.label_Tozihatetelatcheck.setText(_translate("MainWindow", "توضیحات  :"))
        self.groupBox_Moshtarijadid.setTitle(_translate("MainWindow", "مشتری جدید"))
        self.pushButton_Sabtmoshtari.setText(_translate("MainWindow", "ثبت"))
        self.pushButton_jostojomoshtari.setText(_translate("MainWindow", "جستجو"))
        self.pushButton_Virayeshmoshtari.setText(_translate("MainWindow", "ویرایش"))
        self.pushButton_Hazfmoshtari.setText(_translate("MainWindow", "حذف"))
        self.label_Shomaretelsabet.setText(_translate("MainWindow", "تلفن ثابت  :"))
        self.label_Namesherkat.setText(_translate("MainWindow", "نام شرکت  :"))
        self.label_Address.setText(_translate("MainWindow", "آدرس  :"))
        self.label_Codemoshtari.setText(_translate("MainWindow", "کد مشتری  :"))
        self.label__Namemoshtari.setText(_translate("MainWindow", "نام مشتری  :"))
        self.label_Shomaretelhamrah.setText(_translate("MainWindow", "تلفن همراه  :"))
        self.groupBox_Natayejhostvajoo.setTitle(_translate("MainWindow", "نتایج جستجو"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "شماره صیادی"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "کد (چک/عملیات/مشتری)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "مشتری "))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "مبلغ"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "وضعیت فعلی"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "تعداد عملیات"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "آخرین عملیات"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "تاریخ سررسید"))
        self.pushButton_Sabtmoshtari_4.setText(_translate("MainWindow", "خروجی اکسل"))
import icons_rc
