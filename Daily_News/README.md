# Daily_News

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#overview">Overview</a>
      <ul>
      <li><a href="#features">Features</a></li>
      </ul>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
  </ol>
</details>

## Overview

Daily_News is a Python script designed to fetch and display personalized news articles based on your preferences.

## Features

* **Personalized News Selection:** Choose from various news categories like world news, music, films, ecology, economy, arts, games, sports, and technology.
* **Language Selection:** Select your preferred language (Polish or English) for the news articles.
* **Customizable Number of Articles:** Specify the number of news articles you want to receive for each category.
* **Concise Summaries:** Get a quick overview of each news article with the first three sentences.

## Prerequisites

The script requires the following Python libraries to be installed:

* **requests:** For fetching data from websites and APIs.
* **BeautifulSoup4:** For parsing HTML content.
* **feedparser:** For parsing RSS feeds.
* **newspaper3k:** For extracting article content.
* **lxml:** For HTML and XML parsing (required by some of the above libraries).

You can install these libraries using `pip`:

```bash
pip install requests beautifulsoup4 feedparser newspaper3k lxml
