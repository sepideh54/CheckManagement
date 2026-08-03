import sys
import os
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
from operation_crud import create_operation
from customer_crud import get_all_customers
from PyQt5.QtWidgets import QFileDialog
from check_crud import (
    create_check,
    get_check_by_sayadi,
    generate_checkinfo_code,
    update_check,
    delete_check)
import shutil




class MainApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.selected_customer_id = None
        self.selected_check_id = None
        self.front_image_path = None
        self.back_image_path = None

        self.setup_logic()

  #-------------------------------------logic -----------------------------------
    
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

            # ========= Check =========
            self.ui.lineEdit_Codecheck.setReadOnly(True)
            self.ui.lineEdit_Codecheck.setStyleSheet(
                "background-color:#F5F5DC;"
            )
            self.ui.pushButton_Sabtcheck.clicked.connect(
                self.save_checkinfo
            )
            self.ui.dateEdit_Tarixamaliyat_2.setDate(QDate.currentDate())

            self.ui.pushButton_Axroyecheck.clicked.connect(
            self.select_front_image
            )
            self.ui.pushButton_Axposhtecheck.clicked.connect(
            self.select_back_image
            )
            self.front_image_path = None
            self.back_image_path = None

            self.ui.pushButton_jostojocheck.clicked.connect(
            self.search_check
            )

            self.ui.tableWidget.setColumnCount(8)

            self.ui.tableWidget.setHorizontalHeaderLabels(
                [
                    "شماره صیادی",
                    "کد چک",
                    "مشتری",
                    "مبلغ",
                    "وضعیت فعلی",
                    "تعداد عملیات",
                    "آخرین عملیات",
                    "تاریخ سررسید"
                ]
            )
            self.ui.pushButton_Virayeshcheck.clicked.connect(
            self.edit_check
            )
            self.ui.pushButton_Hazfcheck.clicked.connect(
            self.delete_check_info
)

            # ========= Customer =========
            self.load_customers()
            self.load_banks()
            

    #---------------------------------- جدول اطلاعات چک ----------------------------       

    # ------------------------
    # ثبت چک 
    # ------------------------
    def select_front_image(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "انتخاب تصویر روی چک",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )

        if file_path:

            self.front_image_path = file_path

            QMessageBox.information(
                self,
                "موفق",
                "تصویر انتخاب شد."
            )

    def save_front_image(self, check_code):

        if not self.front_image_path:
            return None

        folder = os.path.join(
            os.getcwd(),
            "images",
            "checks"
        )

        os.makedirs(folder, exist_ok=True)

        extension = os.path.splitext(
            self.front_image_path
        )[1]

        new_name = f"{check_code}_front{extension}"

        destination = os.path.join(
            folder,
            new_name
        )

        shutil.copy2(
            self.front_image_path,
            destination
        )

        return os.path.join(
            "images",
            "checks",
            new_name
        )


    def select_back_image(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "انتخاب تصویر پشت چک",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )

        if file_path:

            self.back_image_path = file_path

            QMessageBox.information(
                self,
                "موفق",
                "تصویر انتخاب شد."
            )

    def save_back_image(self, check_code):

        if not self.back_image_path:
            return None

        folder = os.path.join(
            os.getcwd(),
            "images",
            "checks"
        )

        os.makedirs(folder, exist_ok=True)

        extension = os.path.splitext(
            self.back_image_path
        )[1]

        new_name = f"{check_code}_back{extension}"

        destination = os.path.join(
            folder,
            new_name
        )

        shutil.copy2(
            self.back_image_path,
            destination
        )

        return os.path.join(
            "images",
            "checks",
            new_name
        )        


    def save_checkinfo(self):

        try:
                            
            check_code = generate_checkinfo_code()
            customer_id = self.ui.comboBox_Saderkonandeh.currentData()

            if not customer_id:

                QMessageBox.warning(
                    self,
                    "خطا",
                    "ابتدا مشتری را انتخاب کنید"
                )
                return

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
            
            bank_name = (
                self.ui.comboBox_Banksaderkonandeh
                .currentText()
            )

            # TODO:
            # بعداً از bank_crud می‌گیریم
            bank_id = None
        
            front_image = self.save_front_image(check_code)
            back_image = self.save_back_image(check_code)


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
                
    def edit_check(self):

        if self.selected_check_id is None:

            QMessageBox.warning(
                self,
                "خطا",
                "ابتدا یک چک را جستجو و انتخاب کنید."
            )
            return

        reply = QMessageBox.question(
            self,
            "تأیید ویرایش",
            "آیا از ویرایش این چک مطمئن هستید؟",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.No:
            return

        check_code = self.ui.lineEdit_Codecheck.text().strip()

        sayadi_number = self.ui.lineEdit_Shomarehsayadi.text().strip()

        customer_id = self.ui.comboBox_Saderkonandeh.currentData()

        amount = self.ui.lineEdit_Mablagcheck.text().strip()

        due_date = (
            self.ui.dateEdit_Tarixamaliyat_2
            .date()
            .toString("yyyy-MM-dd")
        )

        bank_id = self.ui.comboBox_Banksaderkonandeh.currentData()

        description = (
            self.ui.textEdit_Tozihatetelatcheck
            .toPlainText()
            .strip()
        )

        front_image = self.front_image_path

        back_image = self.back_image_path

        success = update_check(
            self.selected_check_id,
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

        if success:

            QMessageBox.information(
                self,
                "موفق",
                "اطلاعات چک با موفقیت ویرایش شد."
            )

            self.search_check()



    def search_check(self):

        sayadi_number = self.ui.lineEdit_Shomarehsayadi.text().strip()

        if not sayadi_number:

            QMessageBox.warning(
                self,
                "خطا",
                "شماره صیادی را وارد کنید."
            )
            return

        check = get_check_by_sayadi(sayadi_number)

        if not check:

            QMessageBox.information(
                self,
                "نتیجه",
                "چکی پیدا نشد."
            )

            return


        self.selected_check_id = check["check_id"]
        print("Selected check:", self.selected_check_id)

        self.ui.tableWidget.insertRow(0)

        self.ui.tableWidget.setItem(
            0, 0,
            QTableWidgetItem(check["sayadi_number"])
        )

        self.ui.tableWidget.setItem(
            0, 1,
            QTableWidgetItem(check["check_code"])
        )

        self.ui.tableWidget.setItem(
            0, 2,
            QTableWidgetItem(check["customer_name"])
        )

        self.ui.tableWidget.setItem(
            0, 3,
            QTableWidgetItem(str(check["amount"]))
        )

        self.ui.tableWidget.setItem(
            0, 7,
            QTableWidgetItem(str(check["due_date"]))
        )

    def delete_check_info(self):
        print("DELETE BUTTON CLICKED")

        if self.selected_check_id is None:

            self.ui.lineEdit_Extar.setText(
                "ابتدا یک چک را انتخاب کنید."
            )
            return


        reply = QMessageBox.question(
            self,
            "تأیید حذف",
            "آیا مطمئن هستید؟\nچک از لیست فعال حذف می‌شود.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )


        if reply == QMessageBox.No:
            return


        result = delete_check(
            self.selected_check_id
        )


        if result:

            self.ui.lineEdit_Extar.setText(
                "چک با موفقیت حذف شد."
            )

            self.selected_check_id = None

            self.search_check()

    #  --------------------------- جدول مشتری ------------------------------ 
    
          
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