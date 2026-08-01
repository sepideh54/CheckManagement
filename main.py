import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
from customer_crud import (
    create_customer,
    get_customer_by_name,
    update_customer,
    delete_customer
)
from PyQt5.QtCore import QTimer
from customer_crud import create_customer, generate_customer_code
from check_crud import create_check,generate_checkinfo_code
from PyQt5.QtWidgets import QTableWidgetItem
from customer_crud import get_customer_by_name
from validators import is_persian_text
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate
import jdatetime

from check_crud import create_check, generate_checkinfo_code
from operation_crud import create_operation

from customer_crud import get_all_customers

class MainApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.selected_customer_id = None

        self.setup_logic()


    
    def setup_logic(self):
            
            # ========= Customer =========

            self.ui.lineEdit_Codemoshtari.setReadOnly(True)
            self.ui.lineEdit_Codemoshtari.setStyleSheet(
                "background-color:#F5F5DC;"
            )

            self.ui.pushButton_Sabtmoshtari.clicked.connect(
                self.save_customer
            )

            self.ui.pushButton_jostojomoshtari.clicked.connect(
                self.search_customer
            )

            self.ui.pushButton_Virayeshmoshtari.clicked.connect(
                self.edit_customer
            )

            self.ui.pushButton_Hazfmoshtari.clicked.connect(
                self.delete_customer
            )

            # ========= Operation =========
            self.ui.lineEdit_Codecheck.setReadOnly(True)
            self.ui.lineEdit_Codecheck.setStyleSheet(
                "background-color:#F5F5DC;"
            )
            self.ui.pushButton_Sabtcheck.clicked.connect(
                self.save_checkinfo
            )
            self.ui.dateEdit_Tarixamaliyat_2.setDate(QDate.currentDate())
            # ========= Customer =========
            self.load_customers()

            self.load_banks()

    # ------------------------
    # ثبت چک 
    # ------------------------
    def save_checkinfo(self):

        try:

                # -------------------------
                # Check Code
                # -------------------------
                check_code = generate_checkinfo_code()


                # -------------------------
                # Customer
                # -------------------------
                customer_id = self.ui.comboBox_Saderkonandeh.currentData()

                print("Customer text:", self.ui.comboBox_Shax.currentText())
                print("Customer data:", self.ui.comboBox_Shax.currentData())
                if not customer_id:

                    QMessageBox.warning(
                        self,
                        "خطا",
                        "ابتدا مشتری را انتخاب کنید"
                    )
                    return

                # -------------------------
                # Check Information
                # -------------------------

                sayadi_number = self.ui.lineEdit_Shomarehsayadi.text().strip()

                amount = self.ui.lineEdit_Mablagcheck.text().strip()

                description = (
                    self.ui.textEdit_Tozihatetelatcheck
                    .toPlainText()
                    .strip()
                )


                due_date = (
                    self.ui.dateEdit_Tarixamaliyat_2
                    .date()
                    .toString("yyyy-MM-dd")
                )


                # بانک
                bank_name = (
                    self.ui.comboBox_Banksaderkonandeh
                    .currentText()
                )


                # TODO:
                # بعداً از bank_crud می‌گیریم
                bank_id = None



                # -------------------------
                # Images
                # -------------------------

                front_image = None
                back_image = None



                # -------------------------
                # Insert Check
                # -------------------------

                check_id = create_check(
                    check_code,
                    sayadi_number,
                    customer_id,
                    amount,
                    due_date,
                    bank_id,
                    front_image,
                    back_image,
                    description
                )


                if not check_id:

                    QMessageBox.warning(
                        self,
                        "خطا",
                        "ثبت چک انجام نشد"
                    )
                    return



                # -------------------------
                # First Operation
                # -------------------------

                operation_date = (
                    self.ui.dateEdit_Tarixamaliyat_2
                    .date()
                    .toString("yyyy-MM-dd")
                )


                operation_type = (
                    self.ui.comboBox_Noeamaliyat
                    .currentText()
                )


                related_person = ""


                operation_description = (
                    "ثبت اولیه چک"
                )


                sayad_status = (
                    self.ui.comboBox_Vaziyatsamaneh
                    .currentText()
                )


                create_operation(
                    check_id,
                    operation_type,
                    operation_date,
                    related_person,
                    operation_description,
                    sayad_status
                )


                # -------------------------
                # Show Code
                # -------------------------

                self.ui.lineEdit_Codecheck.setText(
                    check_code
                )


                QMessageBox.information(
                    self,
                    "موفق",
                    "چک با موفقیت ثبت شد"
                )


            # پاک کردن فرم
            # self.clear_check_form()



        except Exception as e:

            QMessageBox.critical(
                    self,
                    "خطا",
                    str(e)
                )
    # ------------------------
    # پاک کردن جدول مشتری
    # ------------------------
    def clear_customer_fields(self):

        self.ui.lineEdit_Codemoshtari.clear()
        self.ui.lineEdit_Namemoshtari.clear()
        self.ui.lineEdit_Namesherkat.clear()
        self.ui.lineEdit_Shomarehtelsabet.clear()
        self.ui.lineEdit_Shomarehtelhamrah.clear()
        self.ui.textEdit_Address.clear()
        self.ui.lineEdit_Extar.clear()

        self.selected_customer_id = None

    # ------------------------
    # ثبت مشتری
    # ------------------------

    def save_customer(self):

        customer_code = generate_customer_code()

        self.ui.lineEdit_Codemoshtari.setText(customer_code)

        customer_name = self.ui.lineEdit_Namemoshtari.text().strip()
        organization_name = self.ui.lineEdit_Namesherkat.text().strip()
        customer_phone = self.ui.lineEdit_Shomarehtelsabet.text().strip()
        customer_mobile = self.ui.lineEdit_Shomarehtelhamrah.text().strip()
        customer_address = self.ui.textEdit_Address.toPlainText().strip()

        if customer_name == "":

            QMessageBox.warning(
                self,
                "خطا",
                "نام مشتری را وارد کنید."
            )
            return

        if not is_persian_text(customer_name):

            QMessageBox.warning(
                self,
                "خطا",
                "نام مشتری فقط باید فارسی باشد."
            )
            return

        if organization_name:

            if not is_persian_text(organization_name):

                QMessageBox.warning(
                    self,
                    "خطا",
                    "نام شرکت فقط باید فارسی باشد."
                )
                return

        create_customer(
            customer_code,
            customer_name,
            organization_name,
            customer_phone,
            customer_mobile,
            customer_address
        )

        self.ui.lineEdit_Extar.setText( "مشتری با موفقیت ثبت شد.")
        QTimer.singleShot(
        3000,
        self.clear_customer_fields)


    # ------------------------
    # جستجو
    # ------------------------

    def search_customer(self):

        customer_name = self.ui.lineEdit_Namemoshtari.text().strip()
        organization_name = self.ui.lineEdit_Namesherkat.text().strip()

        customer = get_customer_by_name(
            customer_name,
            organization_name
        )

        if customer is None:

            QMessageBox.information(
                self,
                "جستجو",
                "مشتری یافت نشد."
            )

            self.ui.lineEdit_Extar.setText(
                "مشتری یافت نشد."
            )

            return

        self.selected_customer_id = customer["customer_id"]

        self.ui.lineEdit_Codemoshtari.setText(
            customer["customer_code"]
        )

        self.ui.lineEdit_Namemoshtari.setText(
            customer["customer_name"]
        )

        self.ui.lineEdit_Namesherkat.setText(
            customer["organization_name"] or ""
        )

        self.ui.lineEdit_Shomarehtelsabet.setText(
            customer["customer_phone"] or ""
        )

        self.ui.lineEdit_Shomarehtelhamrah.setText(
            customer["customer_mobile"] or ""
        )

        self.ui.textEdit_Address.setPlainText(
            customer["customer_address"] or ""
        )

        self.ui.lineEdit_Extar.setText(
            "مشتری پیدا شد."
        )


    # ------------------------
    # ویرایش
    # ------------------------

    def edit_customer(self):

        if self.selected_customer_id is None:

            QMessageBox.warning(
                self,
                "خطا",
                "ابتدا مشتری را جستجو کنید."
            )

            return

        result = QMessageBox.question(
            self,
            "ویرایش",
            "آیا تغییرات ذخیره شود؟",
            QMessageBox.Yes | QMessageBox.No
        )

        if result == QMessageBox.No:
            return

        customer_name = self.ui.lineEdit_Namemoshtari.text().strip()
        organization_name = self.ui.lineEdit_Namesherkat.text().strip()
        customer_phone = self.ui.lineEdit_Shomarehtelsabet.text().strip()
        customer_mobile = self.ui.lineEdit_Shomarehtelhamrah.text().strip()
        customer_address = self.ui.textEdit_Address.toPlainText().strip()

        update_customer(
            self.selected_customer_id,
            customer_name,
            organization_name,
            customer_phone,
            customer_mobile,
            customer_address
        )

        self.ui.lineEdit_Extar.setText(
            "ویرایش با موفقیت انجام شد."
        )

        QTimer.singleShot(
            3000,
            lambda: self.ui.lineEdit_Extar.clear()
        )


    # ------------------------
    # حذف
    # ------------------------

    def delete_customer(self):

        if self.selected_customer_id is None:

            QMessageBox.warning(
                self,
                "خطا",
                "ابتدا مشتری را جستجو کنید."
            )

            return

        result = QMessageBox.question(
            self,
            "حذف",
            "آیا از حذف مشتری مطمئن هستید؟",
            QMessageBox.Yes | QMessageBox.No
        )

        if result == QMessageBox.No:
            return

        delete_customer(
            self.selected_customer_id
        )

        self.selected_customer_id = None

        self.ui.lineEdit_Codemoshtari.clear()
        self.ui.lineEdit_Namemoshtari.clear()
        self.ui.lineEdit_Namesherkat.clear()
        self.ui.lineEdit_Shomarehtelsabet.clear()
        self.ui.lineEdit_Shomarehtelhamrah.clear()
        self.ui.textEdit_Address.clear()

        self.ui.lineEdit_Extar.setText(
            "مشتری حذف شد."
        )

        QTimer.singleShot(
            3000,
            lambda: self.ui.lineEdit_Extar.clear()
        )


    def load_customers(self):

        customers = get_all_customers()

        print("Customers:", customers)

        self.ui.comboBox_Saderkonandeh.clear()

        for customer in customers:

            self.ui.comboBox_Saderkonandeh.addItem(
                customer["customer_name"],
                customer["customer_id"]
        )
            
    def load_banks(self):

        banks = [
            "بانک ملی",
            "بانک مهر ایران",
            "بانک صادرات",
            "بانک کشاورزی",
            "بانک ملت",
            "بانک مسکن",
            "بانک تجارت"
        ]

        self.ui.comboBox_Banksaderkonandeh.clear()

        for bank in banks:
            self.ui.comboBox_Banksaderkonandeh.addItem(bank)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())