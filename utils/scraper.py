from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
import fitz
import time

URL = "https://gsstb.gujarat.gov.in/Home/gsstb/Std9to12"

PDF_FOLDER = "pdfs"
TEXT_FOLDER = "textbooks"

os.makedirs(PDF_FOLDER, exist_ok=True)
os.makedirs(TEXT_FOLDER, exist_ok=True)


def download_pdfs():

    options = webdriver.ChromeOptions()

    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(URL)

    time.sleep(8)

    pdf_links = set()

    links = driver.find_elements(By.TAG_NAME, "a")

    for link in links:

        href = link.get_attribute("href")

        if href:

            if ".pdf" in href.lower():

                pdf_links.add(href)

            elif "drive.google.com" in href.lower():

                print("Opening Google Drive folder...")

                driver.execute_script("window.open(arguments[0]);", href)

                driver.switch_to.window(driver.window_handles[-1])

                time.sleep(10)

                drive_links = driver.find_elements(By.TAG_NAME, "a")

                for d in drive_links:

                    h = d.get_attribute("href")

                    if h and ".pdf" in h.lower():

                        pdf_links.add(h)

                driver.close()

                driver.switch_to.window(driver.window_handles[0])

    driver.quit()

    print("Found", len(pdf_links), "PDFs")

    for pdf_url in pdf_links:

        try:

            filename = pdf_url.split("/")[-1].split("?")[0]

            if filename == "":
                filename = str(abs(hash(pdf_url))) + ".pdf"

            pdf_path = os.path.join(PDF_FOLDER, filename)

            txt_path = os.path.join(
                TEXT_FOLDER,
                filename.replace(".pdf", ".txt")
            )

            if os.path.exists(txt_path):
                continue

            print("Downloading", filename)

            response = requests.get(pdf_url, timeout=60)

            with open(pdf_path, "wb") as f:
                f.write(response.content)

            doc = fitz.open(pdf_path)

            text = ""

            for page in doc:
                text += page.get_text()

            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(text)

            doc.close()

        except Exception as e:

            print("Failed:", pdf_url)

            print(e)