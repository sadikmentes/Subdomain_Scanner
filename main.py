import requests
my_list = 'subdomainlist.txt'
target_input = "google.com"

with open("subdomainlist.txt","r") as subdomainlist :

    for word in subdomainlist:
        word = word.strip()
        url = "http://" + word + "." + target_input
        try :
             response = requests.get(url)
             print("Bu subdomin mevcut : {}".format(word))
        except requests.exceptions.ConnectionError :
            print("Bu subdomain mevcut değil : {}".format(word))
            pass


