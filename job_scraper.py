import csv
import time
from playwright.sync_api import sync_playwright

# ──────────────────────────────────────────────────────────────
# FULL COMPANY LIST (70+ companies)
# ──────────────────────────────────────────────────────────────
COMPANIES = [
    # Analytics & Data Firms
    {"name": "LatentView Analytics", "url": "https://latentview.darwinbox.in/ms/candidatev2/main/careers/allJobs"},
    {"name": "Fractal Analytics", "url": "https://fractal.wd1.myworkdayjobs.com/Careers"},
    {"name": "Tiger Analytics", "url": "https://www.tigeranalytics.com/about-us/current-openings/"},
    {"name": "Tredence", "url": "https://www.tredence.com/careers"},
    {"name": "Manthan", "url": "https://www.manthan.com/careers"},
    {"name": "BridgeI2I", "url": "https://www.bridgei2i.com/careers"},
    # Major E-commerce
    {"name": "Myntra", "url": "https://www.myntra.com/careers"},
    {"name": "Flipkart", "url": "https://www.flipkartcareers.com/#!/joblist"},
    {"name": "Amazon India", "url": "https://www.amazon.jobs/en/locations/india"},
    {"name": "Nykaa", "url": "https://jobs.nykaa.com"},
    {"name": "Ajio", "url": "https://www.ajio.com/careers"},
    {"name": "Tata CLiQ", "url": "https://www.tatacliq.com/careers"},
    {"name": "Snapdeal", "url": "https://www.snapdeal.com/info/careers"},
    {"name": "Meesho", "url": "https://www.meesho.io/jobs"},
    {"name": "Purplle", "url": "https://careers.peakxv.com/jobs/purplle?jobTypes=Analyst"},
    # Food & Quick Commerce
    {"name": "Swiggy", "url": "https://careers.swiggy.com"},
    {"name": "Zomato", "url": "https://www.zomato.com/careers"},
    {"name": "BigBasket", "url": "https://www.bigbasket.com/careers"},
    {"name": "Zepto", "url": "https://www.zeptonow.com/careers"},
    {"name": "Licious", "url": "https://licious.in/careers"},
    # D2C & Consumer Brands
    {"name": "Mamaearth", "url": "https://www.mamaearth.in/careers"},
    {"name": "boAt", "url": "https://www.boat-lifestyle.com/pages/careers"},
    {"name": "Wakefit", "url": "https://wakefit.co/careers"},
    {"name": "Sugar Cosmetics", "url": "https://www.sugarcosmetics.com/careers"},
    {"name": "The Man Company", "url": "https://www.themancompany.com/pages/careers"},
    {"name": "Bewakoof", "url": "https://www.bewakoof.com/careers"},
    {"name": "The Souled Store", "url": "https://www.thesouledstore.com/careers"},
    {"name": "Limeroad", "url": "https://www.limeroad.com/jobs"},
    # Global Fashion & Retail
    {"name": "H&M", "url": "https://career.hm.com"},
    {"name": "IKEA India", "url": "https://www.ikea.com/in/en/jobs"},
    {"name": "Inditex (Zara)", "url": "https://www.inditex.com/en/join-us"},
    {"name": "Decathlon India", "url": "https://www.decathlon.in/content/careers"},
    {"name": "Adidas", "url": "https://careers.adidas-group.com"},
    {"name": "Nike", "url": "https://jobs.nike.com"},
    {"name": "PVH (Calvin Klein/Tommy)", "url": "https://www.pvh.com/careers"},
    {"name": "Levi Strauss", "url": "https://www.levistrauss.com/careers"},
    {"name": "L'Oreal", "url": "https://careers.loreal.com"},
    {"name": "Uniqlo India", "url": "https://www.uniqlo.com/in/en/careers"},
    # Kids & Niche Fashion
    {"name": "FirstCry", "url": "https://www.firstcry.com/careers"},
    {"name": "Hopscotch", "url": "https://www.hopscotch.in/careers"},
    {"name": "FableStreet", "url": "https://www.fablestreet.com/careers"},
    {"name": "Voonik", "url": "https://www.voonik.com/careers"},
    {"name": "Stylophile", "url": "https://www.stylophile.in/careers"},
    # Furniture & Home
    {"name": "Pepperfry", "url": "https://www.pepperfry.com/careers"},
    {"name": "Urban Ladder", "url": "https://www.urbanladder.com/careers"},
    {"name": "Furlenco", "url": "https://www.furlenco.com/careers"},
    {"name": "Rentomojo", "url": "https://www.rentomojo.com/careers"},
    # E-commerce Enablers
    {"name": "Shopify", "url": "https://www.shopify.com/careers"},
    {"name": "GoKwik", "url": "https://gokwik.co/careers"},
    {"name": "Vymo", "url": "https://www.vymo.com/careers"},
    {"name": "Unicommerce", "url": "https://unicommerce.com/careers"},
    {"name": "ElasticRun", "url": "https://elasticrun.in/careers"},
    {"name": "OfBusiness", "url": "https://www.ofbusiness.com/careers"},
    {"name": "Udaan", "url": "https://udaan.com/careers"},
    {"name": "Jumbotail", "url": "https://www.jumbotail.com/careers"},
    {"name": "Universal Sportsbiz", "url": "https://www.universalsportsbiz.com/careers"},
    # Fintech
    {"name": "Razorpay", "url": "https://razorpay.com/jobs"},
    {"name": "PayU", "url": "https://corporate.payu.com/careers"},
    {"name": "Cashfree", "url": "https://www.cashfree.com/careers"},
    {"name": "BharatPe", "url": "https://bharatpe.com/careers"},
    {"name": "Setu", "url": "https://setu.co/careers"},
    # Mobility & Services
    {"name": "Ola", "url": "https://www.olacabs.com/careers"},
    {"name": "Rapido", "url": "https://rapido.bike/careers"},
    {"name": "Urban Company", "url": "https://www.urbancompany.com/careers"},
    # Health & Pharma
    {"name": "PharmEasy", "url": "https://pharmeasy.in/careers"},
    {"name": "Netmeds", "url": "https://www.netmeds.com/careers"},
    {"name": "Cure.fit", "url": "https://www.cure.fit/careers"},
    {"name": "Pristyn Care", "url": "https://www.pristyncare.com/careers"},
    {"name": "1mg", "url": "https://www.1mg.com/careers"},
    # International
    {"name": "Saks Fifth Avenue", "url": "https://www.careersatsaks.com/us/en/search-jobs"},
]

# ──────────────────────────────────────────────────────────────
# FILTER PATTERNS
# ──────────────────────────────────────────────────────────────
JOB_URL_PATTERNS = [
    "/job", "/jobs", "/career", "/careers", "/opening",
    "/position", "/role", "/apply", "/vacancy", "/recruit",
    "/opportunity", "/hire", "jobid", "jobdetail", "job-detail",
    "workday", "greenhouse", "lever", "keka", "darwinbox"
]

JOB_TITLE_PATTERNS = [
    "analyst", "engineer", "manager", "developer", "designer",
    "associate", "executive", "lead", "head", "officer",
    "specialist", "consultant", "intern", "scientist",
    "architect", "director", "coordinator", "advisor",
    "data", "analytics", "product", "business", "marketing",
    "operations", "finance", "growth", "strategy", "insights"
]

IGNORE_PATTERNS = [
    "facebook", "twitter", "instagram", "linkedin", "youtube",
    "privacy", "terms", "cookie", "logout", "login", "signin",
    "signup", "contact", "about", "blog", "news", "press",
    "mailto", "tel:", "whatsapp", "javascript", "#",
    "pinterest", "snapchat", "tiktok", "help", "support",
    "faq", "sitemap", "policy", "legal", "download", "app"
]


def looks_like_job_link(text, href):
    text_lower = text.lower().strip()
    href_lower = href.lower()
    if any(ig in href_lower for ig in IGNORE_PATTERNS):
        return False
    if any(ig in text_lower for ig in IGNORE_PATTERNS):
        return False
    if len(text.strip()) < 4 or len(text.strip()) > 120:
        return False
    if any(p in href_lower for p in JOB_URL_PATTERNS):
        return True
    if any(p in text_lower for p in JOB_TITLE_PATTERNS):
        return True
    return False


# ──────────────────────────────────────────────────────────────
# SCRAPER
# ──────────────────────────────────────────────────────────────
def scrape_company(company, page):
    jobs = []
    try:
        print("  Loading: " + company["url"])
        page.goto(company["url"], timeout=25000, wait_until="networkidle")
        time.sleep(3)
        page_size = len(page.content())
        print("  Page size: " + str(page_size) + " chars")
        anchors = page.query_selector_all("a")
        print("  Raw links: " + str(len(anchors)))
        seen_urls = set()
        for a in anchors:
            try:
                text = a.inner_text().strip()
                href = a.get_attribute("href") or ""
                if not href or href.strip() == "" or href.strip() == "#":
                    continue
                if href.startswith("/"):
                    base = "/".join(company["url"].split("/")[:3])
                    href = base + href
                if href in seen_urls:
                    continue
                seen_urls.add(href)
                if looks_like_job_link(text, href):
                    jobs.append({
                        "company": company["name"],
                        "title": text if text else "View Job",
                        "url": href
                    })
            except:
                continue
        print("  -> Job-like links: " + str(len(jobs)))
    except Exception as e:
        print("  ERROR: " + str(e))
    return jobs


# ──────────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────────
def run():
    all_jobs = []
    failed_companies = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800}
        )
        page = context.new_page()

        total = len(COMPANIES)
        for i, company in enumerate(COMPANIES):
            print("\n[" + str(i + 1) + "/" + str(total) + "] " + company["name"])
            jobs = scrape_company(company, page)
            if len(jobs) == 0:
                failed_companies.append(company["name"])
            all_jobs.extend(jobs)
            time.sleep(1)

        browser.close()

    output_file = "all_jobs_raw.csv"
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["company", "title", "url"])
        writer.writeheader()
        writer.writerows(all_jobs)

    print("\n" + "=" * 55)
    print("DONE.")
    print("Total job-like links found : " + str(len(all_jobs)))
    print("Companies with 0 results   : " + str(len(failed_companies)))
    print("Saved to                   -> " + output_file)
    print("=" * 55)

    if failed_companies:
        print("\nCompanies that returned 0 results:")
        for c in failed_companies:
            print("  - " + c)
    print("\nOpen results: open all_jobs_raw.csv")


if __name__ == "__main__":
    run()
