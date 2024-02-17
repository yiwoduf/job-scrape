# Python Web Scraper for Programming Jobs
# Update: 2024. 02. 17

import requests
from bs4 import BeautifulSoup

all_jobs = []

def scrape_page(url):
    response = requests.get(url);
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]
    for job in jobs:
        # link = job.find("a").text
        title = job.find("span", class_="title").text
        company, job_type, region = job.find_all("span", class_="company")
        link = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
        company = company.text
        job_type = job_type.text
        region = region.text

        # print("Title: ", title)
        # print("Company: ", company)
        # print("Job Type: ", job_type)
        # print("Region: ", region)
        # print("Link: ", link)
        # print()

        job_data = {
            "title": title,
            "company": company,
            "job_type": job_type,
            "region": region,
            "link": f"https://weworkremotely.com{link}",
        }
        all_jobs.append(job_data)

def get_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    buttons = len(soup.find("div", class_="pagination").find_all("span", class_="page"))
    return buttons;



url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"


# All Full Time Jobs in weworkremotely.com

total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")

for x in range(total_pages):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
    scrape_page(url)

print(len(all_jobs))