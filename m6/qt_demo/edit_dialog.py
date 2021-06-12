import sys

from PyQt5 import uic, QtWidgets

Ui_MainWindow, QtBaseWindow = uic.loadUiType("edit_dialog.ui")


class EditDialog(QtBaseWindow, Ui_MainWindow):
    def __init__(self, contact=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        if contact:
            self.notes_text_edit.setPlainText(contact.notes)

    def update_contact(self, contact):
        contact.notes = self.notes_text_edit.toPlainText()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = EditDialog()
    window.show()
    sys.exit(app.exec_())
