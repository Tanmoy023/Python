import argparse
import requests

def downloadFile(url,fileName):
    if(fileName is None):
        fileName = url.split("/")[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(fileName, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return fileName


parser = argparse.ArgumentParser()

parser.add_argument("url", help="Give the url of the file you want to download")
# parser.add_argument("fileName", help="By which name you want to save your file")
parser.add_argument("-o","--optional", type=str, help="The name of the file", default=None)


args = parser.parse_args()

print(args.url)
print(args.fileName)

# https://qph.cf2.quoracdn.net/main-qimg-e29aca66294dcaecf8eef976e9f2874e-lq
