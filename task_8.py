import requests

with open('id') as f:
    id = f.read()
result = requests.get('https://api.vk.com/method/friends.get?user_id=' +
                        id + '&v=5.52&access_token=2a112d042a112d042a112d04f32a6316fc22a112a112d0474df45f740b6a00003488848').json()

for people in result['response']['items']:
    people_info = requests.get('https://api.vk.com/method/users.get?user_id=' + str(people) +
                          '&v=5.52&access_token=2a112d042a112d042a112d04f32a6316fc22a112a112d0474df45f740b6a00003488848').json()

    first_name = people_info['response'][0]['first_name']
    last_name = people_info['response'][0]['last_name']
    print(first_name + ' ' + last_name)
