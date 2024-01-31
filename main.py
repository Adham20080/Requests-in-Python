import requests

# url = "https://jsonplaceholder.typicode.com/posts"
#
# data = {
#     "userId": 16,
#     "id": 28,
#     "title": "9B bAck",
#     "body": "Coder Python"
# }
#
# response = requests.post(url=url, data=data)
# print(response.text)
# print(response.status_code)

# For HomeWork

# First

# url = "https://jsonplaceholder.typicode.com/comments?postId=1"
#
# response = requests.get(url=url)
# print(response.content)

# Second

# url = "https://jsonplaceholder.typicode.com/users"
#
# response = requests.get(url=url)
# print(response.json())

# third

# url = "https://jsonplaceholder.typicode.com/users"
# response = requests.get(url=url)
#
# for i in response.json():
#     print("User Address:", i['address'])
#     print("User Phone:", i['phone'])
#     print("User Email:", i['email'])
