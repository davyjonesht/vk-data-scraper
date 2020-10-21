import vk_api

vk_session = vk_api.VkApi(login='xxxxx', password='xxxxx', api_version="5.124")
vk_session.auth()

vk = vk_session.get_api()

#print(vk.wall.post(message='Hello world!'))

print(vk.users.search(q="Dave Ryan"))