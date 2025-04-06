import requests
from bs4 import BeautifulSoup

# New job site URL
url = "https://www.remotepython.com/jobs/"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}

# Send request
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Find job listings
    jobs = soup.find_all("div", class_="job")

    print("\n🔹🔹 Remote Python Jobs 🔹🔹\n")
    found_jobs = 0  # Counter for valid jobs

    for job in jobs[:5]:  # Limit to first 5 jobs
        title = job.find("h2")
        company = job.find("h3")
        link = job.find("a", href=True)

        if title and company and link:
            job_title = title.text.strip()
            company_name = company.text.strip()
            job_link = "https://www.remotepython.com" + link["href"]

            found_jobs += 1
            print(f"🔹 **{job_title}**")
            print(f"🏢 **Company:** {company_name}")
            print(f"🔗 **Apply Here:** {job_link}")
            print("-" * 50)

    if found_jobs == 0:
        print("😢 No Python remote jobs found. Try again later.")

else:
    print(f"Failed to fetch jobs. Status Code: {response.status_code}")
