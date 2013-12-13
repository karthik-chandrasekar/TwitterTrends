import twitter
import time, random, logging
import json
import os, codecs

class CrawlTweets:
    
    def __init__(self):

        #File Input output
        self.logger_file = "crawl_tweets.log"

        #User credentials
        self.consumer_key="nhvaSdfkzTa2QQmEWAbu9g"
        self.consumer_secret="Shi3XBkLwocYdfHbptEoLK3KbHDQ5MRYyA4Qq9jEW4"
        self.access_token_key="224897371-ZipzKRKDopJdNjSc3zkTJUwfKwHdigKCBpCqcY7A"
        self.access_token_secret="9eSEibVq6axdZKTjXB0Vc8qlALV0xLsEoCsUXFqpNU"

        #Data structures
        self.tweet_list = []
        self.user_id_list = []
        self.user_id_set = set()

        #Constants
        self.dump_count = 0
        self.MY_SCREEN_NAME = 'iam_KarthikC'
        self.SLEEP_TIME = 70

    def run_main(self):
        self.initialize_logger()
        self.run()

    def initialize_logger(self):
        logging.basicConfig(filename=self.logger_file, level=logging.INFO)
        logging.info("Initialized logger")

    def run(self):
        #Create API Object

        api = twitter.Api(consumer_key=self.consumer_key, consumer_secret=self.consumer_secret, access_token_key=self.access_token_key, access_token_secret=self.access_token_secret)
       
        self.get_tweets(api)

    def get_tweets(self, api):
        #collect tweets

        self.get_my_home_timeline(api)
        self.get_friends_timeline(api)

    def get_my_home_timeline(self, api):

        home_timeline_tweets_obj = api.GetHomeTimeline(count=200, exclude_replies=True)
        time.sleep(self.SLEEP_TIME)  
 
        for status_obj in home_timeline_tweets_obj:
            status_dict = status_obj.AsDict()
            
            if not status_dict: continue
            homeline_tweet = status_dict.get('text')
            self.tweet_list.append(homeline_tweet)            

            user_obj = status_dict.get('user')
            if not user_obj: continue

            user_id = user_obj.get('id')

            if user_id in self.user_id_set: continue
        
            try:
                self.user_id_list.append(user_id)
                self.user_id_set.add(user_id)
            except:
                self.put_tweets()

    def get_friends_timeline(self, api):
        
        dump_limit = 0
        
        for index, user in enumerate(self.user_id_list):
            
            try:
                user_timeline_tweets_obj = api.GetUserTimeline(user_id=user, count=200, exclude_replies=True)
                time.sleep(self.SLEEP_TIME)
                dump_limit += 1

            except Exception:
                logging.info("Exception  !!!!  - %s - Continue" % (Exception))
                continue

            for status_obj in user_timeline_tweets_obj:
                status_dict = status_obj.AsDict()

                if not status_dict: 
                    logging.info("status dict is not present - Continue")
                    continue

                user_timeline_tweet = status_dict.get('text')
                self.tweet_list.append(user_timeline_tweet)
      
                user_ids = api.GetFriendIDs(user_id=user)
                time.sleep(self.SLEEP_TIME)
 
                user_ids = [x for x in user_ids and x not in self.user_id_set]
 
                self.user_id_list.extend(user_ids)
                self.user_id_set.update(set(user_ids))
        
            if dump_limit == 20:
                self.put_tweets()
                self.tweet_list=[]
                dump_limit = 0
                self.dump_count += 1

    def put_tweets(self):
            tweets_file_name = os.path.join('OUTPUT', 'tweets_file_%s' % (self.dump_count))
            tweets_file_fd = codecs.open(tweets_file_name, 'w', 'utf-8')
            tweets_file_fd.write(json.dumps(self.tweet_list))
            tweets_file_fd.close()

if __name__ == "__main__":
    ct = CrawlTweets()
    ct.run_main()
