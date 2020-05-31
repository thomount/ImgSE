from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QMessageBox
from PyQt5 import QtGui
import sys, time
import qinit


class MainWindow(QMainWindow):
    pics = []
    page_id = 0
    page_tot = 0
    n = 0
    maxw, maxh = 640, 480

    def __init__(self):
        super().__init__()
        self.ui = qinit.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.prev_page)
        self.ui.pushButton_3.clicked.connect(self.next_page)
        self.ui.pushButton.clicked.connect(self.search)
        self.ui.textEdit.setCallBack(self.search)

    def load_pics(self, pics: list):
        self.pics = pics
        self.page_id = 1
        self.n = len(pics)
        self.page_tot = (self.n-1) // 6 + 1
        self._load_page(1)
        self.ui.label.setText("第%d页 / 共%d页" % (self.page_id, self.page_tot))

    def _load_page(self, page_id: int):
        # self.ui.gridLayoutWidget.
        pics = self.pics[(page_id-1)*6: min(len(self.pics), page_id*6)]
        positions = [(i, j) for i in range(2) for j in range(3)]
        for position in positions:
            self.ui.labels[position].setPixmap(QtGui.QPixmap(""))
        for pic, position in zip(pics, positions):
            pixmap = QtGui.QPixmap(pic)
            self.ui.labels[position].setPixmap(pixmap)
            self.ui.labels[position].setName(pic)
            # if position == (0, 0):
            #    print(self.ui.labels[position].height(), self.ui.labels[position].width())

    def next_page(self):
        if self.page_id < self.page_tot:
            self.page_id += 1
            self._load_page(self.page_id)
            self.ui.label.setText("第%d页 / 共%d页" % (self.page_id, self.page_tot))

    def prev_page(self):
        if self.page_id > 1:
            self.page_id -= 1
            self._load_page(self.page_id)
            self.ui.label.setText("第%d页 / 共%d页" % (self.page_id, self.page_tot))

    def get_search_option(self):
        return self.ui.comboBox.currentIndex()

    def search(self):
        content = self.ui.textEdit.toPlainText()
        self.ui.textEdit.clear()
        if len(content) == 0:
            msg = QMessageBox(self)
            msg.setText('请输入内容！')
            msg.setWindowTitle('注意')
            msg.show()
            return
        option = self.get_search_option()

        msg = QMessageBox(self)
        msg.setText('开始搜索！')
        msg.setWindowTitle('提示')
        msg.show()

        t_start = time.time()

        pics = ["jpg\\100000.jpg", "jpg\\100001.jpg", "jpg\\100002.jpg", "jpg\\100100.jpg", "jpg\\100101.jpg"]
        # pics = search(content, option) TODO finish search here， and delete prev line

        t_end = time.time()
        msg.close()
        msg = QMessageBox(self)
        msg.setText('   共%d条结果    \n   耗时%.2f秒    ' % (len(pics), t_end - t_start))
        msg.setWindowTitle('搜索完成')
        msg.show()

        self.load_pics(pics)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    pics = ["jpg\\100000.jpg", "jpg\\100001.jpg", "jpg\\100002.jpg", "jpg\\100100.jpg", "jpg\\100101.jpg",
            "jpg\\100200.jpg", "jpg\\100201.jpg", "jpg\\100300.jpg", "jpg\\100301.jpg", "jpg\\100302.jpg",
            "jpg\\100400.jpg", "jpg\\100401.jpg", "jpg\\100500.jpg", "jpg\\100501.jpg"]

    mainWindow.load_pics(pics)
    mainWindow.show()
    sys.exit(app.exec_())
