# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random

class OXO(QWidget):
	def __init__(self,parent=None):
		super(OXO,self).__init__(parent)
		self.initUI()

	def initUI(self):
	
		self.playerLetter=''
		self.computerLetter=''
		self.turn=''
		self.theBoard = [' '] * 10
		self.move = ' '
		self.AIFlag = True			#True:強人工智慧 False :弱人工智慧
		self.GameFlag = True  #True 遊戲中
	
		newfont = QFont("Times", 48, QFont.Bold) 
		newfont2 = QFont("Times", 14, QFont.Bold) 
		newfont3 = QFont("Times", 24, QFont.Bold) 
		newfont4 = QFont("Times", 12, QFont.Bold) 
		self.btn1 = QPushButton("")
		self.btn2 = QPushButton("")
		self.btn3 = QPushButton("")
		self.btn4 = QPushButton("")
		self.btn5 = QPushButton("")
		self.btn6 = QPushButton("")
		self.btn7 = QPushButton("")
		self.btn8 = QPushButton("")
		self.btn9 = QPushButton("")
		
		self.btnO = QPushButton("O")
		self.btnX = QPushButton("X")
		self.btn_reset = QPushButton("重新開始")
		
		
		self.Radiobtn1 = QRadioButton("強人工智慧")
		self.Radiobtn1.setChecked(True)
		self.Radiobtn1.toggled.connect(lambda:self.btnstate(self.Radiobtn1))
		
		self.Radiobtn2 = QRadioButton("弱人工智慧")
		self.Radiobtn2.setChecked(False)
		self.Radiobtn2.toggled.connect(lambda:self.btnstate(self.Radiobtn2))
		
		

		self.btn1.setFixedSize(100,120)
		self.btn2.setFixedSize(100,120)
		self.btn3.setFixedSize(100,120)
		self.btn4.setFixedSize(100,120)
		self.btn5.setFixedSize(100,120)
		self.btn6.setFixedSize(100,120)
		self.btn7.setFixedSize(100,120)
		self.btn8.setFixedSize(100,120)
		self.btn9.setFixedSize(100,120)
		self.btnO.setFixedSize(80,60)
		self.btnX.setFixedSize(80,60)
		self.btn_reset.setFixedSize(160,60)
		
		
		self.btn1.setFont(newfont)
		self.btn2.setFont(newfont)
		self.btn3.setFont(newfont)
		self.btn4.setFont(newfont)
		self.btn5.setFont(newfont)
		self.btn6.setFont(newfont)
		self.btn7.setFont(newfont)
		self.btn8.setFont(newfont)
		self.btn9.setFont(newfont)
		self.btnO.setFont(newfont3)
		self.btnX.setFont(newfont3)
		self.btn_reset.setFont(newfont3)
		self.Radiobtn1.setFont(newfont4)
		self.Radiobtn2.setFont(newfont4)
		
		self.btn1.clicked.connect(self.btn1_click)
		self.btn2.clicked.connect(self.btn2_click)
		self.btn3.clicked.connect(self.btn3_click)
		self.btn4.clicked.connect(self.btn4_click)
		self.btn5.clicked.connect(self.btn5_click)
		self.btn6.clicked.connect(self.btn6_click)
		self.btn7.clicked.connect(self.btn7_click)
		self.btn8.clicked.connect(self.btn8_click)
		self.btn9.clicked.connect(self.btn9_click)
		self.btnO.clicked.connect(self.btnO_click)
		self.btnX.clicked.connect(self.btnX_click)
		self.btn_reset.clicked.connect(self.btn_reset_click)
		
		self.contentEdit = QTextEdit()
		self.contentEdit.setFont(newfont2)
		self.contentEdit.append('歡迎來玩OXO小遊戲!')
		self.contentEdit.append('1.請選擇電腦是<強人工智慧>還是<弱人工智慧>')
		self.contentEdit.append('2.請在下面按鈕選擇你要X還是O?')
		grid = QGridLayout()
		grid.setSpacing(10)
 
		grid.addWidget(self.btn1, 1, 0)
		grid.addWidget(self.btn2, 1, 1)
		grid.addWidget(self.btn3, 1, 2)
  
		grid.addWidget(self.btn4, 2, 0)
		grid.addWidget(self.btn5, 2, 1)
		grid.addWidget(self.btn6, 2, 2)
		
		grid.addWidget(self.btn7, 3, 0)
		grid.addWidget(self.btn8, 3, 1)
		grid.addWidget(self.btn9, 3, 2)
		
		grid.addWidget(self.Radiobtn1 ,4, 0)
		grid.addWidget(self.Radiobtn2 ,4, 1)
		
		grid.addWidget(self.btnO, 4, 4)
		grid.addWidget(self.btnX, 4, 5)
		grid.addWidget(self.btn_reset, 4, 6,1,2)
	
		grid.addWidget(self.contentEdit, 1, 4, 3, 4)
		  
		self.setLayout(grid)
		
		self.setGeometry(200, 100, 720, 480)
		self.setWindowTitle('OXO 小遊戲')
	
	def btnstate(self,btn):
		if btn.text()=="強人工智慧":
			if btn.isChecked() == True:
				self.AIFlag = True
			else:
				self.AIFlag = False
			print(self.AIFlag)
		if btn.text()=="弱人工智慧":
			if btn.isChecked()== True :
				self.AIFlag = False
			else:
				self.AIFlag = True
			print(self.AIFlag)
	
	def chooseRandomMoveFromList(self,board, movesList):
		# Returns a valid move from the passed list on the passed board.
		# Returns None if there is no valid move.
		possibleMoves = []
		for i in movesList:
			if self.isSpaceFree(board, i):
				possibleMoves.append(i)

		if len(possibleMoves) != 0:
			return random.choice(possibleMoves)
		else:
			return None	
		
	def getBoardCopy(self,board):
	# Make a duplicate of the board list and return it the duplicate.
		dupeBoard = []
		for i in board:
			dupeBoard.append(i)
		return dupeBoard
	def getComputerMove(self,board):
		# Given a board and the computer's letter, determine where to move and return that move.
		# Here is our algorithm for our Tic Tac Toe AI:
		# First, check if we can win in the next move
		for i in range(1, 10):
			copy = self.getBoardCopy(board)
			if self.isSpaceFree(copy, i):
				self.makeMove(copy, self.computerLetter, i)
				if self.isWinner(copy, self.computerLetter):
					return i

		# Check if the player could win on his next move, and block them.
		for i in range(1, 10):
			copy = self.getBoardCopy(board)
			if self.isSpaceFree(copy, i):
				self.makeMove(copy, self.playerLetter, i)
				if self.isWinner(copy, self.playerLetter):
					return i

		# Try to take one of the corners, if they are free.
		self.move = self.chooseRandomMoveFromList(board, [1, 3, 7, 9])
		if self.move != None:
			return self.move

		# Try to take the center, if it is free.
		if self.isSpaceFree(board, 5):
			return 5

		# Move on one of the sides.
		return self.chooseRandomMoveFromList(board, [2, 4, 6, 8])

	def getComputerMove_2(self,board):
		# Given a board and the computer's letter, determine where to move and return that move.
		# Here is our algorithm for our Tic Tac Toe AI:
		# First, check if we can win in the next move
		for i in range(1, 10):
			copy = self.getBoardCopy(board)
			if self.isSpaceFree(copy, i):
				self.makeMove(copy, self.computerLetter, i)
				if self.isWinner(copy, self.computerLetter):
					return i

		# Move on one of the sides.
		return self.chooseRandomMoveFromList(board, [1,2,3,4,5,6,7,8,9])	
		
		
	def whoGoesFirst(self):
		# Randomly choose the player who goes first.
		if random.randint(0, 1) == 0:
			return 'computer'
		else:
			return 'player'	
	
	def inputPlayerLetter(self):
		if self.playerLetter=='':
			self.contentEdit.append('請先在下面按鈕選擇你要X還是O?')
			return False 
		else:
			return True
			
	def makeMove(self,board, letter, move):
		if move!=None:
			board[int(move)] = letter
		
	def makeMove_2(self, letter):
		if int(self.move)==1:
			self.btn1.setText(letter)
			self.btn1.setEnabled(False)
		elif int(self.move)==2:
			self.btn2.setText(letter)
			self.btn2.setEnabled(False)
		elif int(self.move)==3:
			self.btn3.setText(letter)	
			self.btn3.setEnabled(False)
		elif int(self.move)==4:
			self.btn4.setText(letter)	
			self.btn4.setEnabled(False)			
		elif int(self.move)==5:
			self.btn5.setText(letter)	
			self.btn5.setEnabled(False)			
		elif int(self.move)==6:
			self.btn6.setText(letter)		
			self.btn6.setEnabled(False)
		elif int(self.move)==7:
			self.btn7.setText(letter)	
			self.btn7.setEnabled(False)
		elif int(self.move)==8:
			self.btn8.setText(letter)		
			self.btn8.setEnabled(False)
		else:	
			self.btn9.setText(letter)
			self.btn9.setEnabled(False)

	def GameOver(self):
		self.GameFlag=False
		self.btn1.setEnabled(False)
		self.btn2.setEnabled(False)
		self.btn3.setEnabled(False)
		self.btn4.setEnabled(False)
		self.btn5.setEnabled(False)
		self.btn6.setEnabled(False)
		self.btn7.setEnabled(False)
		self.btn8.setEnabled(False)
		self.btn9.setEnabled(False)

	def isWinner(self,bo, le):
		# Given a board and a player's letter, this function returns True if that player has won.
		# We use bo instead of board and le instead of letter so we don't have to type as much.
		return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
		(bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
		(bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
		(bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
		(bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
		(bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
		(bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
		(bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal
		
	def isSpaceFree(self,board, move):
		# Return true if the passed move is free on the passed board.
		return board[move] == ' '	
		
	def isBoardFull(self,board):
		# Return True if every space on the board has been taken. Otherwise return False.
		for i in range(1, 10):
			if self.isSpaceFree(board, i):
				return False
		return True	
		
	def GameMoving_P(self):
		# Player's turn.
		self.makeMove(self.theBoard, self.playerLetter, self.move)
		self.makeMove_2(self.playerLetter)
		if self.isWinner(self.theBoard, self.playerLetter):
			self.contentEdit.append('恭喜!你贏了遊戲!')
			self.GameOver()

		else:
			if self.isBoardFull(self.theBoard):
				self.contentEdit.append('遊戲平手!')
				self.GameOver()

	def GameMoving_C(self):
		# Computer's turn.
		if self.AIFlag==True:
			self.move = self.getComputerMove(self.theBoard)  #強人工智慧
		else:
			self.move = self.getComputerMove_2(self.theBoard)  #弱人工智慧
			
		if self.move!=None:
			self.makeMove(self.theBoard, self.computerLetter, self.move)
			self.makeMove_2(self.computerLetter)
		
			if self.isWinner(self.theBoard, self.computerLetter):
				self.contentEdit.append('你輸了!電腦贏了遊戲!')
				self.GameOver()

			else:
				if self.isBoardFull(self.theBoard):
					self.contentEdit.append('遊戲平手!')
					self.GameOver()

			
	def btn1_click(self):		
		if self.inputPlayerLetter():
			self.move = '1'
			if self.GameFlag==True:
				self.GameMoving_P()
			if self.GameFlag==True:
				self.GameMoving_C()
	def btn2_click(self):		
		if self.inputPlayerLetter():
			self.move = '2'	
			if self.GameFlag==True:
				self.GameMoving_P()
			if self.GameFlag==True:
				self.GameMoving_C()
	def btn3_click(self):	
		if self.inputPlayerLetter():
			self.move = '3'
			if self.GameFlag==True:
				self.GameMoving_P()
			if self.GameFlag==True:
				self.GameMoving_C()
	def btn4_click(self):		
		if self.inputPlayerLetter():
			self.move = '4'	
			if self.GameFlag==True:
				self.GameMoving_P()
			if self.GameFlag==True:
				self.GameMoving_C()
	def btn5_click(self):		
		if self.inputPlayerLetter():
			self.move = '5'	
			if self.GameFlag==True:
				self.GameMoving_P()
			if self.GameFlag==True:
				self.GameMoving_C()
	def btn6_click(self):		
		if self.inputPlayerLetter():
			self.move = '6'	
			if self.GameFlag==True:
				self.GameMoving_P()
			if self.GameFlag==True:
				self.GameMoving_C()
	def btn7_click(self):		
		if self.inputPlayerLetter():
			self.move = '7'
			if self.GameFlag==True:
				self.GameMoving_P()
			if self.GameFlag==True:
				self.GameMoving_C()
	def btn8_click(self):		
		if self.inputPlayerLetter():
			self.move = '8'	
			if self.GameFlag==True:
				self.GameMoving_P()
			if self.GameFlag==True:
				self.GameMoving_C()
	def btn9_click(self):		
		if self.inputPlayerLetter():
			self.move = '9'	
			if self.GameFlag==True:
				self.GameMoving_P()
			if self.GameFlag==True:
				self.GameMoving_C()
		
	def btnO_click(self):		
		self.contentEdit.append('你選擇了O')
		self.playerLetter='O'
		self.computerLetter='X'
		self.btnO.setEnabled(False)
		self.btnX.setEnabled(False)
		self.turn=self.whoGoesFirst()
		if self.turn=='computer':
			self.contentEdit.append('隨機決定順序，電腦先下...')
			self.GameMoving_C()
		else:
			self.contentEdit.append('隨機決定順序，玩家先下...')
	def btnX_click(self):		
		self.contentEdit.append('你選擇了X')
		self.playerLetter='X'
		self.computerLetter='O'
		self.btnO.setEnabled(False)
		self.btnX.setEnabled(False)
		self.turn=self.whoGoesFirst()
		if self.turn=='computer':
			self.contentEdit.append('隨機決定順序，電腦先下...')
			self.GameMoving_C()
		else:
			self.contentEdit.append('隨機決定順序，玩家先下...')
		
	def btn_reset_click(self):		
		self.btn1.setEnabled(True)	
		self.btn2.setEnabled(True)	
		self.btn3.setEnabled(True)	
		self.btn4.setEnabled(True)	
		self.btn5.setEnabled(True)	
		self.btn6.setEnabled(True)	
		self.btn7.setEnabled(True)	
		self.btn8.setEnabled(True)	
		self.btn9.setEnabled(True)	
		self.btnO.setEnabled(True)
		self.btnX.setEnabled(True)		
		self.btn1.setText('')	
		self.btn2.setText('')	
		self.btn3.setText('')	
		self.btn4.setText('')	
		self.btn5.setText('')	
		self.btn6.setText('')	
		self.btn7.setText('')	
		self.btn8.setText('')	
		self.btn9.setText('')	
		self.contentEdit.setText('歡迎來玩OXO小遊戲!')
		self.contentEdit.append('1.請選擇電腦是<強人工智慧>還是<弱人工智慧>')
		self.contentEdit.append('2.請在下面按鈕選擇你要X還是O?')
		self.playerLetter=''
		self.computerLetter=''
		self.turn=''
		self.theBoard = [' '] * 10
		self.move = ' '
		self.GameFlag=True
		
if __name__ == "__main__":
		app = QApplication(sys.argv)
		form = OXO()
		form.show()
		sys.exit(app.exec_())
