> # proxy-rotator
# Refactored ban_detector - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored health_checker - 2026-03-11
> 
> [![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/ScriptStratos/proxy-rotator) 
> [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
> [![GitHub stars](https://img.shields.io/github/stars/ScriptStratos/proxy-rotator.svg)](https://github.com/ScriptStratos/proxy-rotator/stargazers)
> 
> An intelligent, thread-safe proxy rotator for Python. `proxy-rotator` provides a simple way to manage and rotate through a list of proxies, helping to avoid IP bans and CAPTCHAs during web scraping. It automatically handles proxy health checks, removing dead proxies and prioritizing healthy ones.
> 
> This tool is designed for scrapers that need to make thousands of requests from different IP addresses. It supports multiple proxy providers and can be easily integrated into existing `requests` or `httpx` based projects.
> 
> ## Installation
> 
> ```bash
> git clone https://github.com/ScriptStratos/proxy-rotator.git
> cd proxy-rotator
> pip install -r requirements.txt
> ```
> 
> ## Quick Start
> 
> Using the rotator is straightforward. It fetches a list of free proxies and rotates them for each request.
> 
> ```python
> import requests
> from rotator import ProxyRotator
> 
> # Initialize the rotator (it will fetch free proxies automatically)
> rotator = ProxyRotator()
> 
> # Get a proxy for a request
> proxy = rotator.get_proxy()
> 
> try:
>     response = requests.get(
>         "https://httpbin.org/ip",
>         proxies={"http": proxy, "https": proxy},
>         timeout=5
>     )
>     print(f"Request successful via {proxy}! Your IP is: {response.json()['origin']}")
>     rotator.report_success(proxy)
> except requests.RequestException:
>     print(f"Request failed with proxy {proxy}. It will be cooled down.")
>     rotator.report_failure(proxy)
> 
> ```
> 
> ## Features
> 
> - **Automatic Proxy Fetching:** Gathers free proxies from multiple online sources.
> - **Health Checking:** Periodically checks proxies to ensure they are live and responsive.
> - **Intelligent Rotation:** Prioritizes healthy, fast proxies and cools down failing ones.
> - **Thread-Safe:** Can be used in multi-threaded applications without race conditions.
> - **Extensible Providers:** Easily add new sources for fetching proxies.
> 
> ## Contributing
> 
> Contributions are welcome! Please open an issue or submit a pull request.
> 
> ## License
> 
> This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
> 
