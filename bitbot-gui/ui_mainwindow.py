################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import webbrowser, time, easygui, os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from hex import *

class Ui_GUI(object):
	def setupUi(self, GUI):
		self.inputs = []
		# self.out_dir = "./out/"
		self.out_dir = os.path.expanduser("~/Desktop")

		self.count = 1
		self.use_photo_fix = False
		self.delete_original = False
		self.ratio = 5

		if not GUI.objectName():
			GUI.setObjectName(u"GUI")
		GUI.resize(419, 373)
		sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(GUI.sizePolicy().hasHeightForWidth())
		GUI.setSizePolicy(sizePolicy)
		GUI.setMinimumSize(QSize(419, 373))
		GUI.setMaximumSize(QSize(419, 373))
		icon = QIcon()
		icon.addFile(u"bitbot-logo.png", QSize(), QIcon.Normal, QIcon.Off)
		GUI.setWindowIcon(icon)
		self.action_Start = QAction(GUI)
		self.action_Start.setObjectName(u"action_Start")
		self.actionOpen_Source_Repository = QAction(GUI)
		self.actionOpen_Source_Repository.setObjectName(u"actionOpen_Source_Repository")
		self.start_button = QPushButton(GUI)
		self.start_button.setObjectName(u"start_button")
		self.start_button.setGeometry(QRect(170, 270, 80, 41))
		font = QFont()
		font.setPointSize(12)
		self.start_button.setFont(font)
		self.start_button.setCursor(QCursor(Qt.PointingHandCursor))
		self.label_main = QLabel(GUI)
		self.label_main.setObjectName(u"label_main")
		self.label_main.setGeometry(QRect(70, 20, 291, 41))
		font1 = QFont()
		font1.setFamily(u"Monad")
		self.label_main.setFont(font1)
		self.label_main.setStyleSheet(u"QLabel{\n"
			"	color:black;\n"
			"	padding: 5px 5px 5px 5px;\n"
			"	text-align: center;\n"
			"}")
		self.progressBar = QProgressBar(GUI)
		self.progressBar.setObjectName(u"progressBar")
		self.progressBar.setGeometry(QRect(20, 330, 381, 23))
		self.progressBar.setValue(0)
		self.num_copies = QSpinBox(GUI)
		self.num_copies.setObjectName(u"num_copies")
		self.num_copies.setGeometry(QRect(351, 280, 51, 31))
		font2 = QFont()
		font2.setPointSize(10)
		self.num_copies.setFont(font2)
		self.num_copies.setMinimum(1)
		self.num_copies.setMaximum(25)
		self.label_num_copies = QLabel(GUI)
		self.label_num_copies.setObjectName(u"label_num_copies")
		self.label_num_copies.setGeometry(QRect(250, 280, 91, 31))
		self.bit_ratio_slider = QSlider(GUI)
		self.bit_ratio_slider.setObjectName(u"bit_ratio_slider")
		self.bit_ratio_slider.setGeometry(QRect(30, 210, 301, 31))
		self.bit_ratio_slider.setStyleSheet(
			u"QSlider {\n"
			"	color:black;\n"
			"	border: solid black 1px;\n"
			"}")
		self.bit_ratio_slider.setMinimum(1)
		self.bit_ratio_slider.setMaximum(100)
		self.bit_ratio_slider.setValue(5)
		self.bit_ratio_slider.setOrientation(Qt.Horizontal)
		self.bit_ratio_slider.setTickPosition(QSlider.TicksBelow)
		self.bit_depth_counter = QSpinBox(GUI)
		self.bit_depth_counter.setObjectName(u"bit_depth_counter")
		self.bit_depth_counter.setGeometry(QRect(350, 210, 51, 31))
		self.bit_depth_counter.setFont(font2)
		self.bit_depth_counter.setMinimum(1)
		self.bit_depth_counter.setMaximum(100)
		self.bit_depth_counter.setValue(5)
		self.label_num_copies_2 = QLabel(GUI)
		self.label_num_copies_2.setObjectName(u"label_num_copies_2")
		self.label_num_copies_2.setGeometry(QRect(150, 180, 121, 31))
		self.input_button = QPushButton(GUI)
		self.input_button.setObjectName(u"input_button")
		self.input_button.setGeometry(QRect(80, 80, 80, 41))
		self.input_button.setFont(font)
		self.input_button.setCursor(QCursor(Qt.PointingHandCursor))
		self.input_button_2 = QPushButton(GUI)
		self.input_button_2.setObjectName(u"input_button_2")
		self.input_button_2.setGeometry(QRect(270, 80, 80, 41))
		self.input_button_2.setFont(font)
		self.input_button_2.setCursor(QCursor(Qt.PointingHandCursor))
		self.label = QLabel(GUI)
		self.label.setObjectName(u"label")
		self.label.setGeometry(QRect(60, 129, 121, 31))
		self.frame = QFrame(GUI)
		self.frame.setObjectName(u"frame")
		self.frame.setGeometry(QRect(20, 260, 141, 61))
		self.frame.setFrameShape(QFrame.StyledPanel)
		self.frame.setFrameShadow(QFrame.Raised)
		self.checkBox = QCheckBox(self.frame)
		self.checkBox.setObjectName(u"checkBox")
		self.checkBox.setGeometry(QRect(10, 10, 121, 19))
		self.checkBox.setCursor(QCursor(Qt.PointingHandCursor))
		self.checkBox_2 = QCheckBox(self.frame)
		self.checkBox_2.setObjectName(u"checkBox_2")
		self.checkBox_2.setGeometry(QRect(10, 30, 121, 19))
		self.checkBox_2.setCursor(QCursor(Qt.PointingHandCursor))
		self.label_2 = QLabel(GUI)
		self.label_2.setObjectName(u"label_2")
		self.label_2.setGeometry(QRect(250, 129, 121, 31))
		self.line = QFrame(GUI)
		self.line.setObjectName(u"line")
		self.line.setGeometry(QRect(17, 240, 381, 20))
		self.line.setFrameShape(QFrame.HLine)
		self.line.setFrameShadow(QFrame.Sunken)
		self.src_btn = QPushButton(GUI)
		self.src_btn.setObjectName(u"src_btn")
		self.src_btn.setGeometry(QRect(370, 20, 41, 41))
		self.src_btn.setCursor(QCursor(Qt.PointingHandCursor))
		icon1 = QIcon()
		icon1.addFile(u"git-logo.png", QSize(), QIcon.Normal, QIcon.Off)
		self.src_btn.setIcon(icon1)

		self.retranslateUi(GUI)
		self.bit_ratio_slider.valueChanged.connect(self.bit_depth_counter.setValue)
		self.bit_depth_counter.valueChanged.connect(self.bit_ratio_slider.setValue)

		####
		self.start_button.clicked.connect(self.ACTION_START) # DEFINE BUTTON PRESS EVENT
		self.input_button.clicked.connect(self.SELECT_INPUT)
		self.input_button_2.clicked.connect(self.SELECT_OUTPUT)
		self.src_btn.clicked.connect(self.OPEN_SOURCE)

		self.bit_ratio_slider.valueChanged.connect(self.UPDATE_RATIO)
		self.num_copies.valueChanged.connect(self.UPDATE_COUNT)

		self.checkBox.stateChanged.connect(self.DELETE_ORIGINALS)
		self.checkBox_2.stateChanged.connect(self.USE_PHOTO_FIX)

		####

		QMetaObject.connectSlotsByName(GUI)
	# setupUi

	def retranslateUi(self, GUI):
		GUI.setWindowTitle(QCoreApplication.translate("GUI", u"BITBOT GUI", None))
		self.action_Start.setText(QCoreApplication.translate("GUI", u"Start", None))
		self.actionOpen_Source_Repository.setText(QCoreApplication.translate("GUI", u"Open Source Repository", None))
		#if QT_CONFIG(tooltip)
		self.start_button.setToolTip(QCoreApplication.translate("GUI", u"<html><head/><body><p><span style=\" font-size:8pt;\">Begin execution of binary distortion.</span></p></body></html>", None))
		#endif // QT_CONFIG(tooltip)
		self.start_button.setText(QCoreApplication.translate("GUI", u"Start", None))
		self.label_main.setText(QCoreApplication.translate("GUI", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">BitBot binary Distorter</span></p></body></html>", None))
		#if QT_CONFIG(tooltip)
		self.num_copies.setToolTip(QCoreApplication.translate("GUI", u"<html><head/><body><p><span style=\" font-size:8pt;\">Number of copies of each file to create.</span></p></body></html>", None))
		#endif // QT_CONFIG(tooltip)
		self.label_num_copies.setText(QCoreApplication.translate("GUI", u"<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Num copies:</span></p></body></html>", None))
		#if QT_CONFIG(tooltip)
		self.bit_ratio_slider.setToolTip(QCoreApplication.translate("GUI", u"<html><head/><body><p>Percent of binary information that will be disorted upon execution.</p></body></html>", None))
		#endif // QT_CONFIG(tooltip)
		#if QT_CONFIG(tooltip)
		self.bit_depth_counter.setToolTip(QCoreApplication.translate("GUI", u"<html><head/><body><p><span style=\" font-size:8pt;\">Percent of binary information that will be distorted upon execution.</span></p></body></html>", None))
		#endif // QT_CONFIG(tooltip)
		self.label_num_copies_2.setText(QCoreApplication.translate("GUI", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Distortion intensity: </span></p></body></html>", None))
		#if QT_CONFIG(tooltip)
		self.input_button.setToolTip(QCoreApplication.translate("GUI", u"<html><head/><body><p><span style=\" font-size:8pt;\">Select input files.</span></p></body></html>", None))
		#endif // QT_CONFIG(tooltip)
		self.input_button.setText(QCoreApplication.translate("GUI", u"Input", None))
		#if QT_CONFIG(tooltip)
		self.input_button_2.setToolTip(QCoreApplication.translate("GUI", u"<html><head/><body><p><span style=\" font-size:8pt;\">Select output directory.</span></p></body></html>", None))
		#endif // QT_CONFIG(tooltip)
		self.input_button_2.setText(QCoreApplication.translate("GUI", u"Output", None))
		self.label.setText(QCoreApplication.translate("GUI", u"<html><head/><body><p align=\"center\">0 file(s) selected.</p></body></html>", None))
		self.checkBox.setText(QCoreApplication.translate("GUI", u"Delete originals", None))
		#if QT_CONFIG(tooltip)
		self.checkBox_2.setToolTip(QCoreApplication.translate("GUI", u"<html><head/><body><p>Attempt to rasterize distorted images into proper files. Success is not guaranteed!</p></body></html>", None))
		#endif // QT_CONFIG(tooltip)
		self.checkBox_2.setText(QCoreApplication.translate("GUI", u"Attempt photo fix", None))
		self.label_2.setText(QCoreApplication.translate("GUI", u"<html><head/><body><p align=\"center\">Output directory:<br/>./out/</p></body></html>", None))
		self.label_2.setText(QS(f"Output directory:<br/>{self.out_dir}", align='center'))
		#if QT_CONFIG(tooltip)
		self.src_btn.setToolTip(QCoreApplication.translate("GUI", u"<html><head/><body><p>Open source repository</p></body></html>", None))
		#endif // QT_CONFIG(tooltip)
		self.src_btn.setText("")
	# retranslateUi

	def ACTION_START(self):
		OP_COUNT = len(self.inputs) * self.count
		ops = 0

		for i in range(len(self.inputs)):
			for _ in range(self.count):
				distort(self.inputs[i], self.ratio, out_dir=self.out_dir, photofix=self.use_photo_fix)
				ops += 1
				self.progressBar.setValue(round(100 * ops / OP_COUNT))

			if (self.delete_original):
				# print(f"Would delete {self.inputs[i]}")
				os.remove(self.inputs[i])

	def SELECT_INPUT(self):
		self.inputs = []
		self.label.setText(QS(f"0 file(s) selected.", align="center"))

		self.inputs = easygui.fileopenbox("Select file(s) to distort", multiple=True)

		try:
			self.label.setText(QS(f"{len(self.inputs)} file(s) selected.", align='center'))
		except:
			self.label.setText(QS(f"0 file(s) selected.", align="center"))

	def SELECT_OUTPUT(self):
		try:
			dir = easygui.diropenbox()
			if dir is not None:
				self.out_dir = dir
		except:
			pass
		self.label_2.setText(QS(f"Output directory:<br/>{dir}", align='center'))
		self.label_2.setToolTip(QCoreApplication.translate("GUI", u"<html><head/><body><p><span style=\" font-size:8pt;\">" + dir + "</span></p></body></html>", None))

	def UPDATE_RATIO(self, ratio : int):
		self.ratio = ratio

	def UPDATE_COUNT(self, count : int):
		self.count = count

	def DELETE_ORIGINALS(self, val : int):
		self.delete_original = bool(val)

	def USE_PHOTO_FIX(self, val : int):
		self.use_photo_fix = bool(val)

	def OPEN_SOURCE(self):
		REPO_URL = r"https://github.com/j-red/bitbot"
		webbrowser.open(REPO_URL)


def QS(txt, align='left'):
	# Helper function to generate HTML strings for formatting inside labels, etc.
	return f"<html><head/><body><p align='{align}'>{txt}</p></body></html>"
