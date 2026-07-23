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
from PyQt5.QtWidgets import QTableWidgetItem
from customer_crud import get_customer_by_name
from validators import is_persian_text
from PyQt5.QtWidgets import QMessageBox

class MainApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.selected_customer_id = None

        self.setup_logic()


    def setup_logic(self):

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
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())