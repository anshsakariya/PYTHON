# import multiprocessing
# import requests
# def downloadFile(url,name):
#     response = requests.get(url)
#     open(f"file{name}.jpg","wb").write(response.content)
    
# url="https://picsum.photos/2000/3000"
# for i in range(5):
#     downloadFile(url,i)


# import os
# import requests
# import multiprocessing

# def download_file(url, filename):
#     print(f"Downloading {url} to {filename}")
#     response = requests.get(url)
#     with open(filename, "wb") as f:
#         f.write(response.content)
#     print(f"Downloaded {url} to {filename}")

# def main():
#     urls = ["https://picsum.photos/2000/3000",
#             "https://picsum.photos/2000/3000",
#             "https://picsum.photos/2000/3000",
#             "https://picsum.photos/2000/3000",
#             "https://picsum.photos/2000/3000",
#             "https://picsum.photos/2000/3000"
            
#             ]

#     folder = "files"
#     os.makedirs(folder, exist_ok=True)

#     processes = []
#     for i, url in enumerate(urls):
#         filename = os.path.join(folder, f"file{i+1}.jpg")
#         p = multiprocessing.Process(target=download_file, args=(url, filename))
#         p.start()
#         processes.append(p)

#     for p in processes:
#         p.join()

# if __name__ == "__main__":
#     main()



import concurrent.futures
import requests

def downloadFile(url, name):
  print(f"Started Downloading {name}")
  response = requests.get(url)
  open(f"files/file{name}.jpg", "wb").write(response.content)
  print(f"Finished Downloading {name}")
 


url = "https://picsum.photos/2000/3000"
with concurrent.futures.ProcessPoolExecutor() as executor:
  l1 = [url for i in range(60)]
  l2 = [i for i in range(60)]
  results = executor.map(downloadFile, l1, l2)
  for r in results:
    print(r)