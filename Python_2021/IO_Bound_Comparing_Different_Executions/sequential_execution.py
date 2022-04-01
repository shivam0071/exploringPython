import requests
import time


def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    # for url in sites:
    #     data = requests.get(url)
    #     print(f"Read {len(data.content)} from {url}")
    # request.get is very very slow

    # creating a Session object allows requests to do some fancy networking tricks and really speed things up.
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    # SEQUENTIAL EXECUTION
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")

    # Downloaded 160 in 35.23140335083008 seconds
    # Downloaded 160 in 86.87043142318726 seconds -- with request.get and no session