# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
def searchWord(word):
	split = word.split()
	searchWord = ''
	for i in split:
		searchWord = searchWord + i + '%20'
	searchWord = searchWord[:-3]
	url = 'https://obastan.com/az/search/?q=' + searchWord
	print(url)
	resp = requests.get(url)

	soup = BeautifulSoup(resp.content,'html.parser')

	words = soup.find("div",attrs = {"class":"grid_12"}).select("div:nth-of-type(1) > div")
	i = 0
	wordList = []
	while True:
		try: 
			wordx = words[i].find("b").text
			i += 1
			wordList.append(wordx)
			
		except AttributeError:
			i += 1
			pass
		except IndexError:
			break
	print(wordList)
	if word.upper() in wordList:
		return True
	else:
		return False
	
from itertools import permutations
word = input('>>>')
start = time.time()
permutation = permutations(word,len(word))
for p in permutation:
	if searchWord(''.join(p)):
		stop = time.time()
		total = stop-start
		line = '-'*50
		print(line,f"\nWord was found '{''.join(p)}'\n{total} second\n",line)
		break
else:
	print("Word not found!")
