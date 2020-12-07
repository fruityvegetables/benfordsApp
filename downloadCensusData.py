import requests

# downloads the current census file from my google docs
download_url = "https://drive.google.com/uc?export=download&id=109WFWlJ67x7ezC20NhE-SwqokRlPzMT0"
target_path = "census_2009b"

response = requests.get(download_url)
response.raise_for_status()    
# checks that the request was successful, prints to CLI
with open(target_path, "wb") as f:
    f.write(response.content)
print("Download ready.")