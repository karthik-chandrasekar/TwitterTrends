import twitter
import time, random, logging
import json
import os, codecs

class CrawlTweets:
    
    def __init__(self):

        #File Input output
        self.logger_file = "crawl_tweets.log"

        #User credentials
        self.consumer_key=""
        self.consumer_secret=""
        self.access_token_key=""
        self.access_token_secret=""

        #Data structures
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

        self.open_file()
        self.get_my_home_timeline(api)
        self.get_followers_timeline(api)
        self.close_file()

    def open_file(self):
        self.tweets_file_name = os.path.join('OUTPUT', 'tweets_file')
        self.tweets_file_fd = codecs.open(self.tweets_file_name, 'w', 'utf-8')

    def close_file(self):
        self.tweets_file_fd.close() 

    def get_my_home_timeline(self, api):

        home_timeline_tweets_obj = api.GetHomeTimeline(count=200, exclude_replies=True)
        time.sleep(self.SLEEP_TIME)  
 
        for status_obj in home_timeline_tweets_obj:
            status_dict = status_obj.AsDict()
            
            if not status_dict: continue
            homeline_tweet = status_dict.get('text')
            self.tweets_file_fd.writelines("%s\n" % (homeline_tweet))

            user_obj = status_dict.get('user')
            if not user_obj: continue

            user_id = user_obj.get('id')

            if user_id in self.user_id_set: continue
        
            self.user_id_list.append(user_id)
            self.user_id_set.add(user_id)


    def get_followers_timeline(self, api):

        friends_set = set()
        
        for index, user in enumerate(self.user_id_list):
            if user in friends_set:
                continue       
            
            try:
                user_timeline_tweets_obj = api.GetUserTimeline(user_id=user, count=200, exclude_replies=True)
                time.sleep(self.SLEEP_TIME)

            except Exception:
                logging.info("Exception  !!!!  - %s - Continue" % (Exception))
                continue

            for status_obj in user_timeline_tweets_obj:
                status_dict = status_obj.AsDict()

                if not status_dict: 
                    logging.info("status dict is not present - Continue")
                    continue

                user_timeline_tweet = status_dict.get('text')
                self.tweets_file_fd.writelines("%s\n" % (user_timeline_tweet))
     
 
            user_ids = api.GetFollowerIDs(user_id=user)
            friends_set.add(user)
            time.sleep(self.SLEEP_TIME)

            new_user_ids = []
            for id in user_ids:
                if id not in self.user_id_set:
                    new_user_ids.append(id)

            if not new_user_ids: continue

            self.user_id_list.extend(new_user_ids)
            self.user_id_set.update(set(new_user_ids))
        

if __name__ == "__main__":
    ct = CrawlTweets()
    ct.run_main()
