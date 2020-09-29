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

