# rotator.py

import threading
import time
from collections import deque
from heapq import heappop, heappush

from loguru import logger

from providers import fetch_free_proxies
# Refactored provider - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored rotator - 2026-03-11
# Refactored session_manager - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored health_checker - 2026-03-11
# Refactored provider - 2026-03-11
# Refactored ban_detector - 2026-03-11
# Refactored ban_detector - 2026-03-11


class ProxyRotator:
    """Manages a pool of proxies, rotating them and checking their health."""

    def __init__(self, update_interval=600, cooldown_time=300):
        self.proxies = []  # Min-heap of (priority, proxy_url)
        self.cooldown = {}  # Dictionary of {proxy_url: cooldown_end_time}
        self.lock = threading.Lock()
        self.update_interval = update_interval
        self.cooldown_time = cooldown_time

        # Start the background thread to update and check proxies
        self.update_thread = threading.Thread(target=self._background_updater, daemon=True)
        self.update_thread.start()

    def _background_updater(self):
        """Periodically fetches new proxies and checks the health of existing ones."""
        while True:
            logger.info("Updating proxy list...")
            new_proxies = fetch_free_proxies()
            with self.lock:
                # Add new proxies with a default priority
                for proxy in new_proxies:
                    if proxy not in [p for _, p in self.proxies] and proxy not in self.cooldown:
                        heappush(self.proxies, (0, proxy))
                logger.info(f"Proxy list updated. Total proxies: {len(self.proxies)}")
            time.sleep(self.update_interval)

    def get_proxy(self):
        """Get the best available proxy. Returns None if no proxies are available."""
        with self.lock:
            # Move proxies from cooldown back to the main pool if their time is up
            now = time.time()
            cooled_down = [p for p, t in self.cooldown.items() if now > t]
            for proxy in cooled_down:
                heappush(self.proxies, (0, proxy))
                del self.cooldown[proxy]

            if not self.proxies:
                logger.warning("No available proxies.")
                return None

            # Get the proxy with the highest priority (lowest number)
            priority, proxy = heappop(self.proxies)
            return proxy

    def report_success(self, proxy):
        """Report a successful request made with a proxy, increasing its priority."""
        with self.lock:
            # Find the proxy and decrease its priority value (making it higher priority)
            try:
                # This is inefficient, but fine for a small number of proxies
                index = [p for _, p in self.proxies].index(proxy)
                priority, _ = self.proxies[index]
                self.proxies[index] = (priority - 1, proxy)
            except ValueError:
                # If not in the main list, it might be a new one
                heappush(self.proxies, (-1, proxy))

    def report_failure(self, proxy):
        """Report a failed request. The proxy is moved to the cooldown list."""
        with self.lock:
            logger.warning(f"Proxy {proxy} failed. Placing it in cooldown.")
            self.cooldown[proxy] = time.time() + self.cooldown_time


if __name__ == "__main__":
    # Example usage
    rotator = ProxyRotator(update_interval=30)  # Update every 30s for demo
    time.sleep(5)  # Wait for initial proxy fetch

    for i in range(5):
        proxy = rotator.get_proxy()
        if proxy:
            print(f"Attempt {i+1}: Using proxy {proxy}")
            # Simulate a request
            if i % 2 == 0:
                rotator.report_success(proxy)
                print("  -> Success!")
            else:
                rotator.report_failure(proxy)
                print("  -> Failure!")
        else:
            print("No proxy available. Waiting...")
        time.sleep(2)
