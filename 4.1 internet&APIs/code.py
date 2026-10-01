import requests
import xml.etree.ElementTree as ET

def get_pubmed_data(pmid):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": pmid,
        "retmode": "xml",
    }

    response = requests.get(url, params=params, timeout=20)
    response.raise_for_status()
    return response.text


xml_payload = get_pubmed_data(34807729)
print(xml_payload[:1000])

root = ET.fromstring(xml_payload)
title = root.find(".//ArticleTitle")

print("Root tag:", root.tag)
print("Article title:", "".join(title.itertext()))

abstract_parts = root.findall(".//Abstract/AbstractText")

print("Number of abstract sections:", len(abstract_parts))
for part in abstract_parts:
    print("Label:", part.get("Label"))
    print("Text:", "".join(part.itertext())[:200])