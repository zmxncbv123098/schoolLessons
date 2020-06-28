import requests

with open("test.txt", 'w') as outfile:
    outfile.write(requests.get("vk.com").text)

# with open("test.txt", 'w') as outfile:
#    outfile.write("Something")

# with open("test.txt", 'r') as outfile:
#    print(outfile.read())

# with open("test.txt", 'w') as outfile:
#   outfile.write(requests.get("http://ya.ru").text)
