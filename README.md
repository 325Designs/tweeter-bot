# tweeter-bot

![alt text](https://img.shields.io/badge/python-3.5-green.svg "Python3.5")

Simple Python script that will retweet all Tweets containing your search term. To limit Twitter requests a savepoint file marks Tweets found before. It's Twitter API v1.1 ready.

### Dependencies
- Tweepy
  'pip install tweepy'
or alternativately `pip install -r requirements.txt`
  
### Creating Twitter App
* Twitter Developers Console [Create App](https://apps.twitter.com/)
* App Secrets (Modify in creds.py file)
  - Consumer Key (API Key)
  - Consumer Secret (API Secret)
  - Access Token
  - Access Token Secret

### Edit tweeter.py file
* Define your hashtag or search query in the config file
* Define the number of Retweets at a time (This avoids overloading -Limit is 180 RT/ 15 mins)
* Add your Twitter app credentials in the config file
* (Tune some other options if you like)
* $ python tweeter.py
* Add this call to your crontab(unix)/task scheduler(windows) (or something similar) to retweet all new tweets regularly
