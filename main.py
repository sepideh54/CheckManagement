import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
from customer_crud import create_customer, get_customer_by_name
from PyQt5.QtCore import QTimer
from customer_crud import create_customer, generate_customer_code

class MainApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setup_logic()


    def setup_logic(self):
       self.ui.lineEdit_Codemoshtari.setReadOnly(True)
       self.ui.lineEdit_Codemoshtari.setStyleSheet("background-color: #F5F5DC;"    )
       self.ui.pushButton_Sabtmoshtari.clicked.connect(self.save_customer)
       self.ui.pushButton_jostojomoshtari.clicked.connect(self.search_customer)
      

    def save_customer(self):
        customer_code = generate_customer_code()
        self.ui.lineEdit_Codemoshtari.setText(customer_code)
        customer_code = self.ui.lineEdit_Codemoshtari.text()
        customer_name = self.ui.lineEdit_Namemoshtari.text()
        organization_name = self.ui.lineEdit_Namesherkat.text()
        customer_phone = self.ui.lineEdit_Shomarehtelsabet.text()
        customer_mobile = self.ui.lineEdit_Shomarehtelhamrah.text()
        customer_address = self.ui.textEdit_Address.toPlainText()

        create_customer(
           customer_code,
           customer_name,
           organization_name,
           customer_phone,
           customer_mobile,
           customer_address
           
    )
      
        self.ui.lineEdit_Extar.setText ( "مشتری با موفقیت ثبت شد" )
        QTimer.singleShot(3000, lambda: self.ui.lineEdit_Extar.clear()) 
        

    def search_customer(self):

        customer_name = self.ui.lineEdit_Namemoshtari.text()

        customers = get_customer_by_name(customer_name)

        if customers:
           self.ui.lineEdit_Extar.setText("مشتری با این نام پیدا شد...")
           QTimer.singleShot(3000, lambda: self.ui.lineEdit_Extar.clear())
        else:
           self.ui.lineEdit_Extar.setText("مشتری با این نام پیدا نشد!!!")
           QTimer.singleShot(3000, lambda: self.ui.lineEdit_Extar.clear())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())