# 🌟 Amazon Review Analyzer

**Your companion for smarter shopping decisions!**  
The Amazon Review Analyzer is a Python program designed to analyze product reviews and provide insightful summaries to help you decide whether a product is worth buying.

---

## 🔍 **Overview**

This tool fetches and analyzes reviews from Amazon products, empowering you with the information you need to make informed purchases.  

> *The ultimate decision is yours – we just provide the insights!*

---

## 💻 **How It Works**

1. **🔗 Input the Product Link**  
   Provide an Amazon product link to kickstart the analysis.  

2. **📋 Scraping Reviews**  
   - Extracts reviews from:  
     `https://amazon.in/product-reviews/ASIN`
   - Fetches the product’s unique **ASIN** using Python's **`re`** module.  
   - Handles pagination and stores reviews in a **`reviews.csv`** file.

3. **🌐 User Agent Setup**  
   Update the `headers` variable in `scrapper.py` with your User-Agent.  
   *To find it, simply search **"My User Agent"** on Google.*

4. **📊 Sentiment Analysis**  
   - Powered by **`vaderSentiment`** to analyze the tone of reviews.  
   - Handles emojis with the **`demoji`** package for enhanced accuracy.  

---

## 🚀 **Getting Started**

### Prerequisites
- Python 3+
- Required Python packages:  
  Install them via:  
  ```bash
  pip install -r requirements.txt

### Running the program 
- To launch the analyzer:
  ```bash
  python3 analyzer.py
## 🛠 Customization
1. Replace the headers variable in scrapper.py with your User-Agent string.
2. Modify the code to add advanced features or tailor it to specific needs.

## 🎉 Features
1. 🚀 Extracts reviews from Amazon automatically.
2. 🤖 Provides insightful sentiment analysis.
3. 📁 Saves results in an easy-to-read CSV file.
4. 🌟 Handles emojis effortlessly!

## 🔒 Disclaimer
This tool is for personal use only. Respect Amazon’s Terms of Service while scraping data.

## 📬 Contributions Welcome!
Feel free to submit issues or suggest enhancements. Let’s make this tool even better!

Made with ❤️ in Python 🐍

 
