import requests

with open('id') as f:
    id = f.read()
result = requests.get('https://api.vk.com/method/friends.get?user_id=' +
                        id + '&v=5.52&access_token=token').json()

for people in result['response']['items']:
    people_info = requests.get('https://api.vk.com/method/users.get?user_id=' + str(people) +
                          '&v=5.52&access_token=token').json()

    first_name = people_info['response'][0]['first_name']
    last_name = people_info['response'][0]['last_name']
    print(first_name + ' ' + last_name)
