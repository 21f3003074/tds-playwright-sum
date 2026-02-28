from playwright.sync_api import sync_playwright

urls = [
    "https://sanand0.github.io/tdsdata/js_table/?seed=13",
    "https://sanand0.github.io/tdsdata/js_table/?seed=14",
    "https://sanand0.github.io/tdsdata/js_table/?seed=15",
    "https://sanand0.github.io/tdsdata/js_table/?seed=16",
    "https://sanand0.github.io/tdsdata/js_table/?seed=17",
    "https://sanand0.github.io/tdsdata/js_table/?seed=18",
    "https://sanand0.github.io/tdsdata/js_table/?seed=19",
    "https://sanand0.github.io/tdsdata/js_table/?seed=20",
    "https://sanand0.github.io/tdsdata/js_table/?seed=21",
    "https://sanand0.github.io/tdsdata/js_table/?seed=22",
]

total_sum = 0

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for url in urls:
        page.goto(url)
        page.wait_for_timeout(2000)  # wait for JS tables

        numbers = page.locator("td").all_inner_texts()
        for num in numbers:
            try:
                total_sum += float(num)
            except:
                pass

    browser.close()

print("FINAL_TOTAL:", total_sum)
