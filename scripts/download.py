# This Python script download data from the TLC website and save it to the sub-folder, landing in the data folder
# The script download the initial untouched data which directly obtained from the API. 

import requests
import os

def download(link, save_path):
    """
    Retrieve and store a file from a URL.
    """
    # Check if path exists, if not, create it
    if not os.path.isdir(save_path):
        os.makedirs(save_path)

    # Get the content from the link
    web_content = requests.get(link, stream=True)
    web_content.raise_for_status()  

    # Extract the filename from the link for storage
    filename = os.path.join(save_path, link.split('/')[-1])

    # Write the content to the file
    with open(filename, 'wb') as local_file:
        for block in web_content.iter_content(chunk_size=8192):
            local_file.write(block)

    print(f"Saved to {filename}")

def main():
    data_links = [
        "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-01.parquet",
        "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-02.parquet",
        "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-03.parquet",
        "https://www.bts.dot.gov/sites/bts.dot.gov/files/docs/legacy/additional-attachment-files/ONTIME.TD.202001.REL01.04MAR2020.zip",
        "https://www.bts.dot.gov/sites/bts.dot.gov/files/docs/legacy/additional-attachment-files/ONTIME.TD.202002.REL01.31MAR2020.zip",
        "https://www.bts.dot.gov/sites/bts.dot.gov/files/docs/legacy/additional-attachment-files/ONTIME.TD.202003.REL02.23JUN2020.zip"
    ]

    path = "data/landing"
    for link in data_links:
        download(link, path)

if __name__ == "__main__":
    main()


