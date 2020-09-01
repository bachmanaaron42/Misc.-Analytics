import requests

# authentication parameters
header = {
    'Authorization': 'bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk',
    'User-Agent': 'Dataquest/1.0'
}

# specific endpoint parameters
params = {
    't': 'day'
}

# make GET request to Reddit API endpoint to get top posts for the past day
response = requests.get('https://oauth.reddit.com/r/python/top', headers=header, params=params)

# assign JSON response into Python object
python_top = response.json()

# find the most upvoted post
posts = python_top['data']['children']

upvotes = {}

for i in range(len(posts)):
    post_id = posts[i]['data']['id']
    num_upvotes = posts[i]['data']['ups']
    upvotes[post_id] = num_upvotes
    
most_upvoted = max(upvotes, key=upvotes.get)

# retrieve comments for top post
comments_response = requests.get('https://oauth.reddit.com/r/python/comments/4b7w9u', headers=header)
comments = comments_response.json()

# fond the most upvoted comment

comments_list = comments[1]['data']['children']

comms_dict = {}

for c in comments_list:
    comment_id = c['data']['id']
    num_up_votes = c['data']['ups']
    comms_dict[comment_id] = num_up_votes

most_upvoted_comment = max(comms_dict, key=comms_dict.get)

# send a POST request to the API to upvote the top post
vote_payload = {
    'dir': 1,
    'id': 'd16y4ry'
}

vote_response = requests.post('https://oauth.reddit.com/api/vote', headers=header, json=vote_payload)

# save the status code for the POST request
status = vote_response.status_code