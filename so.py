from bs4 import BeautifulSoup
import requests

URL = f"https://stackoverflow.com/jobs?q=python"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


def extract_jobs(last_page):
    jobs = []
    # print(last_page)
    #last_page = 1
    for page in range(last_page):
        result = requests.get(f"{URL}&pg={page+1}")
        # print(result.status_code)
        soup = BeautifulSoup(result.text,"html.parser")
        results = soup.find_all("div", {"class":"-job"})
        #print(results)
        for result in results:
            print(result["data-jobid"])

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs