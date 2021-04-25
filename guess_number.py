#this is the guess number game

#import
import random

#random number
def randomNumber():
	#generate 4 numbers in list data type
	l = random.sample(range(10), 4)
	#convert list data type to int data type
	rn = int((''.join([str(x) for x in l])))
	return rn

#main
def main(rn):
#	print("random number is: ", rn)
	#get each number in rn
	rn_var1 = rn%10
	rn_var10 = int(rn/10)%10
	rn_var100 = int(rn/100)%10
	rn_var1000 = int(rn/1000)
	rn_num = [rn_var1000,rn_var100,rn_var10,rn_var1]
	cn = 0 #assign a number
	turn = 0 #record the turn times
	#compare XA
	while cn !=rn:
		turn += 1
		#input the number
		print("please enter a number between 1000 to 9999:")
		cn = int(input())
		#get each number in cn
		cn_var1 = cn % 10
		cn_var10 = int(cn/10)%10
		cn_var100 = int(cn/100)%10
		cn_var1000 = int(cn/1000)
		cn_num = [cn_var1000,cn_var100,cn_var10,cn_var1]
		ch_B = [] #to notice the same number
		global A,B
		A = 0
		B = 0
		for i in range(0,4):
			if rn_num[i] == cn_num[i]:
				A += 1
			else:
				ch_B.append(i)
		for z in ch_B:
			for y in ch_B:
				if cn_num[z] == rn_num[y]:
						B +=1
		print("there are ",A,"A",B,"B.")
	print("You speed ", turn, " rounds to finish this game.")
	print("You are winner!!!!")



if __name__ == "__main__":
	print("EXPLANATION:")
	print("This is a guess number game. You should enter a number between 1000 and 9999.")
	print("The application will output XAXB to you. (X = number)")
	print("A means current number and location. B means current number wrong location.")
	print("the winner will show up until 4A0B appeared\n")
	main(randomNumber())