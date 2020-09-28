<<<<<<< HEAD
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 280, 80)
window.move(600, 15)
helloMsg = QLabel('This is Test', parent=window)
helloMsg.move(60, 30)

window.show()

=======
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 280, 80)
window.move(600, 15)
helloMsg = QLabel('This is Test', parent=window)
helloMsg.move(60, 30)

window.show()

>>>>>>> 9c6c2a5d95b5d0d6a406cc9c3739fab555238ca7
sys.exit(app.exec_())