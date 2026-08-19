import requests
import os

directorys = [
    "admin", "administrator", "admin_area", "admincp", "adminpanel",
    "admin1", "admin2", "moderator", "webadmin", "wp-admin", "wp-login",
    "dashboard", "controlpanel", "cpanel", "panel", "console",
    "login", "logon", "signin", "signup", "register", "auth",
    "auth_user", "user", "users", "account", "accounts", "session",
    "api", "api/v1", "api/v2", "apidocs", "rest", "graphql",
    "swagger", "swagger-ui", "docs",
    "backup", "backups", "backup.zip", "backup.sql", "backup.tar.gz",
    "db_backup", "site_backup", "old", "old_site", "archive",
    "config", "configuration", "settings", ".env", ".env.local",
    ".env.production", "env", "config.php", "config.json",
    "wp-config.php", ".htaccess", ".htpasswd",
    ".git", ".git/config", ".git/HEAD", ".svn", ".hg", ".gitignore",
    "uploads", "upload", "images", "img", "media", "files",
    "documents", "downloads", "assets", "static", "public",
    "test", "tests", "testing", "dev", "development", "staging",
    "sandbox", "demo", "beta", "debug",
    "phpmyadmin", "pma", "adminer", "database", "db", "mysql",
    "sql", "db_admin",
    "logs", "log", "error_log", "access_log", "server-status",
    "server-info", "status",
    "includes", "inc", "scripts", "js", "css", "lib", "libs",
    "vendor", "node_modules", "cgi-bin",
    "private", "secret", "internal", "hidden", "restricted",
    "robots.txt", "sitemap.xml", "humans.txt", "crossdomain.xml",
    "favicon.ico", ".well-known",
    "wp-content", "wp-includes", "administrator/index.php",
    "joomla", "drupal", "typo3",
    "home", "index", "main", "search", "about", "contact",
    "help", "support", "faq", "terms", "privacy", "temp", "tmp",
    "cache", "data", "storage", "shared"
]


BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"


print(GREEN + """
██████╗ ██╗██████╗     ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗
██╔══██╗██║██╔══██╗    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██║  ██║██║██████╔╝    ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██║  ██║██║██╔══██╗    ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██████╔╝██║██║  ██║    ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═════╝ ╚═╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝

                            by JyxDevLab
""" + END)

url_site = input(
    YELLOW + "Enter target URL: " + LIGHT_WHITE
).strip()

if url_site.endswith("/"):
    url_site = url_site[:-1]

tested = 0
found = 0
total = len(directorys)

with open("results_backup.txt", "w") as results:

    for i, directory in enumerate(directorys, start=1):

        tested += 1

        bar_length = 30
        filled = int(bar_length * i / total)

        bar = "█" * filled + "-" * (bar_length - filled)

        print(
            f"\r{LIGHT_CYAN}[{bar}] {i}/{total} | Found: {found}{END}",
            end=""
        )

        target = f"{url_site}/{directory}"

        try:
            response = requests.get(
                target,
                timeout=5,
                allow_redirects=True
            )

            if 200 <= response.status_code < 300:

                found += 1

                print(
                    f"\n{LIGHT_GREEN}[FOUND]{END} "
                    f"{target} "
                    f"{GREEN}(HTTP {response.status_code}){END}"
                )

                results.write(
                    f"[FOUND] {target} (HTTP {response.status_code})\n"
                )

            elif response.status_code in (301, 302):

                found += 1

                print(
                    f"\n{YELLOW}[REDIRECT]{END} "
                    f"{target} "
                    f"{YELLOW}(HTTP {response.status_code}){END}"
                )

                results.write(
                    f"[REDIRECT] {target} (HTTP {response.status_code})\n"
                )

            elif response.status_code in (401, 403):

                found += 1

                print(
                    f"\n{LIGHT_RED}[PROTECTED]{END} "
                    f"{target} "
                    f"{RED}(HTTP {response.status_code}){END}"
                )

                results.write(
                    f"[PROTECTED] {target} (HTTP {response.status_code})\n"
                )

        except requests.RequestException:
            pass

print("\n")
print(LIGHT_PURPLE + "=" * 50 + END)
print(LIGHT_GREEN + "[+] Scan Completed" + END)
print(LIGHT_BLUE + f"[+] Tested: {tested}" + END)
print(LIGHT_GREEN + f"[+] Found: {found}" + END)
print(LIGHT_CYAN + f"[+] Results saved to: {os.path.abspath('results.txt')}" + END)
print(LIGHT_PURPLE + "=" * 50 + END)