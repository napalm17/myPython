import praw
import praw.models.reddit.subreddit as sb
r = praw.Reddit(client_id='B_VCxIofacXrMQ', client_secret='lLMQnqrU2mpc5PkCqAnLWxJN1lGRbQ',
                     username='Jokerberkay17', password='VjBtVG2shVqyWxIc', user_agent='reddo17')

subreddit = r.subreddit('askreddit')
hot = subreddit.hot(limit=5)
contra = subreddit.controversial(limit=5)
top = subreddit.top(time_filter="year", limit=200)
new = subreddit.new(limit=1)
#submisson.selftext
for comment in subreddit.stream.comments():
    try:
        """
        parent_id = str(comment.parent())
        original = r.comment(parent_id)
        print('Parent: ')
        print(original.body)
        print('Reply:')
        print("     ", comment.body)
        """
    except:
        pass
def get_posts():
    for post in hot:
        if not post.stickied:
            try:
                print(post.title)
                print(post.url)
                #print("{}, {}, {}, {}".format(post.title, post.ups, post.downs, post.visited))
                #post.upvote()
                #post.downvote()
                #post.reply("sounds wacky")
                post.comments.replace_more(limit=0)
                for com in post.comments.list():
                    print("\n", com.body)
                    print('Parent ID:', com.parent())
                    print('Comment ID', com.id)
                    '''
                    if len(com.replies) > 0:
                        for reply in com.replies:
                            print("reply", reply.body)
                    '''
            except:
                pass