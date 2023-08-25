import requests

with open('word.txt', 'r') as file:   # give your word list text file name
    for line in enumerate(file):
        word = line[1].strip()
        # print(word)

        url = 'https://www.reddit.com/r/'

        newUrl = url + word
        # print(newUrl)

        try:
            response = requests.get(newUrl)

            if response.status_code == 200:
                response_text = response.text

                if "Community not found" in response_text and len(word) >= 3:
                    file2 = open("new.txt", "a")      # give a name to the text file that saves avaible community names
                    file2.write(word + "\n")
                    file2.close()
                    print(word)
                else:
                    print(f"{line[0]} Community found")
            else:
                print(f"Request failed with status code: {response.status_code}")

        except Exception as e:
            print(f"An error occurred: {e}")
