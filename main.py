import sys
from PyQt6 import QtWidgets
from home import Ui_home
from hientaskstracker import * # class này là giao diện Tasks Tracker
from hiengiaodien import MainWindow as ToDoListWindow
from hientaskstracker import TaskApp as TaskTrackerWindow



class HomeWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_home()
        self.ui.setupUi(self)

        # 👉 Liên kết nút "Đến Tasks tracker"
        self.ui.pbdentasks.clicked.connect(self.chuyen_sang_taskstracker)
        self.ui.pbdentodo.clicked.connect(self.chuyen_sang_todolist)

    def chuyen_sang_taskstracker(self):
        self.task_window = TaskTrackerWindow()  # tạo cửa sổ mới
        self.task_window.show()
        self.close()  # đóng trang home

    def chuyen_sang_todolist(self):
        self.todo_window = ToDoListWindow()
        self.todo_window.show()
        self.close()

#class TaskTrackerWindow(QtWidgets.QMainWindow):
    #def __init__(self):
        #super().__init__()
        #self.ui = Ui_MainWindow()
        #self.ui.setupUi(self)
        #self.ui.backtohome1.clicked.connect(self.quay_ve_home)

    #def quay_ve_home(self):
        #self.home_window = HomeWindow()
        #self.home_window.show()
        #self.close()

#class ToDoListWindow(QtWidgets.QMainWindow):
    #def __init__(self):
        #super().__init__()
        #self.ui = Ui_Ui_MainWindow()
        #self.ui.setupUi(self)
        #self.ui.backtohome.clicked.connect(self.quay_ve_home)

    #def quay_ve_home(self):
        #self.home_window = HomeWindow()
        #self.home_window.show()
        #self.close()



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = HomeWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
