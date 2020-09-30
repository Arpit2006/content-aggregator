

# importing requests package 
import requests	 

def GetNews(): 
	
	# BBC news api 
	main_url = "http://newsapi.org/v2/everything?q=India&from=2020-08-13&sortBy=publishedAt&apiKey={your api key}"

	# fetching data in json format 
	open_bbc_page = requests.get(main_url).json() 

	# getting all articles in a string article 
	article = open_bbc_page["articles"] 

	# empty list which will 
	# contain all trending news 
	results = [] 
	
	for ar in article: 
		results.append(ar["title"]) 
		
	for i in range(len(results)): 
		
		# printing all trending news 
		print(i + 1, results[i]) 

	#to read the news out loud for us 
	from win32com.client import Dispatch 
	speak = Dispatch("SAPI.Spvoice") 
	speak.Speak(results)				 

# Driver Code 
if __name__ == '__main__': 
	
	# function call 
	GetNews() 
