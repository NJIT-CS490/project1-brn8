Documentation on Milestone 1


Steps on how to successful deploy the app with tweets content, author, date and time:  
1.	Use AWS Cloud9 for the project. 
2.	Download flask using [sudo pip install flask] and download tweepy using [sudo pip install tweepy] in AWS Cloud9.  
3.	Apply for Twitter developer’s account using the NJIT email address to access Twitter APIs.
4.	Create a python file and in the python file use the twitter APIs to fetch the tweets related to a random element (food items).
5.  Create a .env file to avoid hardcoding API keys.
6.	In python file hardcode the list of elements (food items) using arrays and use random.choice method to generate random elements whenever the app is refreshed.
7.	Use tweepy API search to find tweet related to search element.   
8.	Use attributes (text, screen_name, created_at) to generate tweet contents, author, date, and time.   
9.	Create an HTML file to deploy a web application to show information about related quotes.
10.	Link CSS file to HTML to design the web application.
11.	To avoid pushing .env file create .gitignore file to hide API keys.
12.	At last, create a private repository on Github in the CS490 ORGANIZATION and commit all the codes in that repository. 


Technical issues:
1.	The random element (food items) should be changing as per refreshing the app, but it wasn’t changing in this case. The problem was that the code was not inside the python function, and looking at the professor’s code, the solution was found.
2.	As per running the code, Internal Server Error was coming up. The reason behind this issue was that the python file was inside the template directory, instead of having it outside and looking at the lecture videos, this issue was fixed as well. 


Issues that are still exist: 
1.	New tweets for each item should be appearing as per refreshing the app, but sometimes the same tweet reappears. After taking the assistance from the TA, it was said that it’s ok as long as the tweet about the random element appears different as per refreshing the page. 



Documentation on Milestone 2 
Steps on how to deploy the app with recipe content that includes serving size, prep time, ingredients, link, and image for a given items
1.	Download json 
2.	Sign up for Spoonacular to obtain the API key to fetch data related to the food item. 
3.	Use each API function with the API key to get specific content. 
4.	Link all the recipe content to HTML to generate an app.
5.	Use an HTML file to link a CSS file to design a well-looking app.  
6.	Merge Milestone1 and Milestone2 code to get complete content of the recipe and tweets. 
7.	Use the concept of git branching and merging to post the code to GitHub. 
8.	Create a Heroku account to create a website where you can deploy your application.
9.	Download npm install -g heroku 
10.	Connect to the Heroku account from the terminal and then push all the files to the Heroku including Procfile and requirements.txt file. 
11.	Add all the API keys to the Heroku account by going to the app you just made now and clink setting where there is an option of Config Vars to add your API keys. 
12.	Lastly, you have done everything to deploy a web app that shows information about the favorite recipes and related quotes. 

Technical issues:
1.	I was having a hard time pushing the code from master into Heroku, and I was getting an error every time I do so. After looking over the slack chat (#project 1 ), I found out that I have forgotten to push the Procfile and requirements.txt file, and that’s why the error was coming up in my case. 
2.	I was getting an authentication problem every time I tried to fetch specific content. After looking over the spoonacular website, I found the correct way to write the authentication part, and I was able to tackle the issue with the help of a spoonacular resources. 

