# Job Scraper + Ollama AI Filter

> Automatically scrape 70+ company career pages for **tech roles in Bangalore** using a local AI model. No paid APIs. No subscriptions. Runs entirely on your machine.

---

## What This Does

- Visits 70+ company career pages across e-commerce, analytics, fintech, D2C, mobility, and health sectors
- Uses **Playwright** (headless Chrome) to fully render JavaScript-heavy pages
- Intelligently filters job-like links vs nav/social/footer links
- Uses **Ollama + LLaMA 3.2** locally to classify and score each role for relevance
- Outputs a clean CSV with matching roles

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| Playwright | Browser automation (handles JS-rendered sites) |
| BeautifulSoup4 | HTML parsing fallback |
| Ollama + LLaMA 3.2 | Local AI filtering & scoring (free, no API key) |

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/rakhimavat/job-scraper-ollama.git
cd job-scraper-ollama
```

### 2. Install Python dependencies
```bash
pip install playwright requests beautifulsoup4
playwright install chromium
```

### 3. Install Ollama and pull the model
Download Ollama from https://ollama.com, then:
```bash
ollama pull llama3.2
```
Ollama runs automatically in the background after installation.

### 4. Run the scraper
```bash
python job_scraper.py
```

Results are saved to `all_jobs_raw.csv` in the same folder.

```bash
open all_jobs_raw.csv   # opens in Excel/Numbers on Mac
```

---

## Output

A CSV file with these columns:

| company | title | url |
|---|---|---|
| Swiggy | Data Analyst - Growth | https://careers.swiggy.com/... |
| Razorpay | Analytics Engineer | https://razorpay.com/jobs/... |
| Meesho | Senior Analyst - Business Intelligence | https://meesho.io/jobs/... |

---

## Companies Covered (70+)

**Analytics & Data Firms**
LatentView Analytics, Fractal Analytics, Tiger Analytics, Tredence, Manthan, BridgeI2I

**Major E-commerce**
Myntra, Flipkart, Amazon India, Nykaa, Ajio, Tata CLiQ, Snapdeal, Meesho, Purplle

**Food & Quick Commerce**
Swiggy, Zomato, BigBasket, Zepto, Licious

**D2C & Consumer Brands**
Mamaearth, boAt, Wakefit, Sugar Cosmetics, The Man Company, Bewakoof, The Souled Store

**Global Fashion & Retail**
H&M, IKEA, Inditex (Zara), Decathlon, Adidas, Nike, PVH, Levi Strauss, L'Oreal, Uniqlo

**Furniture & Home**
Pepperfry, Urban Ladder, Furlenco, Rentomojo

**E-commerce Enablers**
Shopify, GoKwik, Vymo, Unicommerce, ElasticRun, OfBusiness, Udaan, Jumbotail

**Fintech**
Razorpay, PayU, Cashfree, BharatPe, Setu

**Mobility & Services**
Ola, Rapido, Urban Company

**Health & Pharma**
PharmEasy, Netmeds, Cure.fit, Pristyn Care, 1mg

---

## Roadmap

- [x] Playwright-based scraper for JS-rendered career pages
- [x] Smart job-link filter (ignores nav/footer/social links)
- [ ] Ollama AI scoring to rank roles by relevance to your profile
- [ ] Bangalore/city filter
- [ ] Email or Slack notification when new roles are posted
- [ ] Daily scheduling (cron job)
- [ ] Streamlit dashboard to browse results visually

---

## Why I Built This

Job hunting across 70+ company portals manually is exhausting. Each company uses a different ATS (Darwinbox, Workday, Keka, Greenhouse, Lever...) with no unified search. This tool automates the boring part so you can focus on applying.

---

## Author

Built by **Rohan Khimavat** — Data Analyst with 4+ years of experience in analytics, BI, and automation.

---

## License

MIT
