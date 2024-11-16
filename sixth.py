import sys
import requests
from lxml import html


def download_url_and_get_all_hrefs(url):

    hrefs = []
    response = requests.get(url)

    if response.status_code != 200:
        print("Nastala chyba")
        return []

    root = html.fromstring(response.content)
    for a in ("a"):
        elements = root.xpath("//a[@href]")
        for el in elements:
            href = el.attrib["href"]
            if href.startswith("http://") or href.startswith("https://"):
                hrefs.append(href)

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        all_hrefs = download_url_and_get_all_hrefs(url)
        print(all_hrefs)
    except IndexError as e:
        print(f"Nebyla zadana zadna URL adresa")    
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
