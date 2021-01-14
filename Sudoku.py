from random import randint
import numpy as np


def main():
	board = [
		[7,8,0,4,0,0,1,2,0],
		[6,0,0,0,7,5,0,0,9],
		[0,0,0,6,0,1,0,7,8],
		[0,0,7,0,4,0,2,6,0],
		[0,0,1,0,5,0,9,3,0],
		[9,0,4,0,6,0,0,0,5],
		[0,7,0,3,0,0,0,1,2],
		[1,2,0,0,0,7,4,0,0],
		[0,4,9,2,0,6,0,0,7]
	]

	#Add null values to the board for solving
	#for i in range(len(board)):
	#	board[i][randint(0,8)] = 0
	#for j in range(len(board[0])):
	#	board[randint(0,8)][j] = 0
	board_print(board)
	solve(board)
	print('\n')
	board_print(board)


#Print board function, to produce a nicely layed out Sudoku Board --> StackOverflow Reference
def board_print(grid):

	for i in range(len(grid)):
		if i % 3 == 0 and i != 0:
			print("-"*13)

		for j in range(len(grid[0])):
			if j % 3 == 0 and j != 0:
				print(" | ", end="")

			if j == 8:
				print(grid[i][j])
			else:
				print(str(grid[i][j]) + "", end="")

#Solve function to accomodate all other functionality for final product --> Generic programming logic
def solve(grid):

	find = empty(grid, 9, 9)
	if not find:
		return True
	else:
		row,col = find
	for i in range(1,10):
		if deal_with_it(grid,row, col, i):
			grid[row][col] = i

			if solve(grid):
				return True

			grid[row][col] = 0

	return

#This function truly deals with the problem area, considering a pool of numbers alongside the position of the '0' by row and coloum value
def deal_with_it(grid, row, col, pool):

	#Check the row
	for i in range(len(grid)):
		if grid[row][i] == pool and col != i:
			return False

	#Check the col --> within the range of coloumns
	for i in range(len(grid[0])):
		if grid[i][col] == pool and row != i:
			return False


	#Check box --> Stackoverflow reference
	box_x = col // 3
	box_y = row // 3

	temp = (row,col)

	for i in range(box_y*3, box_y*3 + 3):
		for j in range(box_x*3, box_x*3 + 3):
			if grid[i][j] == pool and (i,j) != temp:
				return False

	return True

#Function to check for "Empty" squares, aka, '0' and return the coordinates of that '0' position
def empty(grid, r, c):

	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 0:
				return (i,j)

	return None

main()
