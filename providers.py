# providers.py

import requests
from bs4 import BeautifulSoup
from loguru import logger
# Refactored ban_detector - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored rotator - 2026-03-11


def fetch_free_proxies():
    """Fetches a list of free proxies from a popular provider."""
    proxies = set()
    url = "https://www.sslproxies.org/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", attrs={"class": "table"})
        for row in table.tbody.find_all("tr"):
            ip = row.find_all("td")[0].text
            port = row.find_all("td")[1].text
            proxies.add(f"http://{ip}:{port}")
    except requests.RequestException as e:
        logger.error(f"Failed to fetch proxies: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred while parsing proxies: {e}")

    logger.info(f"Fetched {len(proxies)} unique proxies.")
    return list(proxies)


if __name__ == "__main__":
    # Example usage
    proxy_list = fetch_free_proxies()
    if proxy_list:
        print(f"Successfully fetched {len(proxy_list)} proxies.")
        print("First 5 proxies:")
        for proxy in proxy_list[:5]:
            print(proxy)
