def check_if_empty(t):
    if t is None:
        print("No results found!")
        return 1
    return 0

def print_tweet_list(tl):
    for t in tl:
        print_tweet(t)
    if tl is None:
        print("No more tweets to display!")
    
def print_tweet(t):
    if check_if_empty(t): return
    print("TID: " + str(t['tid']))
    print("Writer: " + str(t['writer']))
    print("Date Posted: " + str(t['tdate']))
    print(t['text'].rstrip())
    print('********************************************')
    
def print_tweet_details(t):
    if check_if_empty(t): return
    print("Text: "+str(t['text']).rstrip())
    print("TID: "+str(t['tid']))
    print("Reply Count: "+str(t['replies']))
    print("Retweet Count: "+str(t['retweets']))
	
def print_users(followers):
    if check_if_empty(followers): return
    for f in followers:
        print("ID: "+str(f['usr']))
        print("Username: "+f['name'])
        print("Email: "+f['email'])
        print("City: "+str(f['city']))
        print('********************************************')
        
def print_user_details(details):
    if check_if_empty(details): return
    print("User Information")
    print("ID: "+str(details['usr']))
    print("Name: "+details['name'])
    print("Number of tweets: "+str(details['tweet_count']))
    print("Number of followers: "+str(details['follower_count']))
    print("Number of followees: "+str(details['following_count']))
    print('********************************************')
    
def help_cmd(params):
    print("Available commands: "+' '.join(params))