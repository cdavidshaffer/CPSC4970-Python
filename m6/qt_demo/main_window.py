import functools
import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QColorDialog, QDialog

from m6.qt_demo.contact import Contact
from m6.qt_demo.edit_dialog import EditDialog

Ui_MainWindow, QtBaseWindow = uic.loadUiType("main_window.ui")


class MainWindow(QtBaseWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._contacts = []
        self.add_button.clicked.connect(self.add_button_clicked)
        self.remove_button.clicked.connect(self.remove_button_clicked)
        self.edit_button.clicked.connect(self.edit_button_clicked)
        self.action_open.triggered.connect(self.action_open_triggered)

    def action_open_triggered(self):
        mb = QMessageBox(QMessageBox.Icon.Critical, "Ouch", "Can't open files", QMessageBox.StandardButton.Ok)
        mb.exec()

    def warn(self, title, message):
        mb = QMessageBox(QMessageBox.Icon.NoIcon, title, message, QMessageBox.StandardButton.Ok)
        return mb.exec()

    def edit_button_clicked(self):
        row = self.address_list_selected_row()
        if row == -1:
            return self.warn("Select contact", "You must selected the contact to edit.")
        contact = self._contacts[row]
        dialog = EditDialog(contact)
        dialog.accepted.connect(lambda: self.edit_dialog_accepted(dialog, contact))
        dialog.show()

    def address_list_selected_row(self):
        selection = self.address_list_widget.selectedItems()
        if len(selection) == 0:
            return -1
        assert len(selection) == 1
        selected_item = selection[0]
        try:
            return [str(c) for c in self._contacts].index(selected_item.text())
        except ValueError:
            pass
        return -1

    def edit_dialog_accepted(self, dialog, contact):
        dialog.update_contact(contact)
        self.update_ui()

    def add_button_clicked(self):
        c = Contact(self.name_line_edit.text(), self.email_line_edit.text(), self.phone_line_edit.text())
        self._contacts.append(c)
        self.update_ui()

    def update_ui(self):
        """Make sure the current model is displayed to the user"""
        row = self.address_list_selected_row()
        self.address_list_widget.clear()
        for c in self._contacts:
            self.address_list_widget.addItem(str(c))
        if row != -1 and len(self._contacts) > row:
            self.address_list_widget.setCurrentItem(self.address_list_widget.item(row))

    def remove_button_clicked(self):
        dialog = QMessageBox(self)
        dialog.setIcon(QMessageBox.Icon.Question)
        dialog.setWindowTitle("Remove contact")
        dialog.setText("Are you sure that you want to remove this Contact?")
        dialog.setInformativeText("...just checking...")
        no_way_button = dialog.addButton("No way!", QMessageBox.ButtonRole.RejectRole)
        sure_button = dialog.addButton("Sure", QMessageBox.ButtonRole.AcceptRole)

        dialog.exec()
        if dialog.clickedButton() == sure_button:
            del self._contacts[self.address_list_widget.currentRow()]
            self.update_ui()
        else:
            print("No pressed")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
