import requests

subdomains = [
    "www",
    "api",
    "admin",
    "mail",
    "webmail",
    "smtp",
    "pop",
    "imap",
    "ftp",
    "cpanel",
    "panel",
    "dashboard",
    "portal",
    "app",
    "apps",
    "mobile",
    "m",
    "blog",
    "shop",
    "store",
    "cdn",
    "static",
    "img",
    "images",
    "media",
    "files",
    "download",
    "uploads",
    "docs",
    "wiki",
    "support",
    "help",
    "status",
    "dev",
    "test",
    "staging",
    "beta",
    "demo",
    "uat",
    "qa",
    "prod",
    "vpn",
    "remote",
    "git",
    "gitlab",
    "github",
    "jenkins",
    "monitor",
    "grafana",
    "db",
    "database"
    "ns1", "ns2", "dns", "mx", "mx1", "mx2", "proxy", "gateway",
    "firewall", "router", "lb", "loadbalancer", "cluster", "node",
    "server", "host", "internal", "intranet", "vpn2",
    "preprod", "pre-prod", "sandbox", "local", "test1", "test2",
    "dev1", "dev2", "release", "canary", "preview",
    "sso", "auth", "login", "oauth", "identity", "idp", "sec",
    "security", "keycloak", "okta",
    "chat", "meet", "voip", "sip", "video", "conference", "call",
    "newsletter", "notify", "notifications", "sms",
    "checkout", "payment", "pay", "billing", "invoice", "cart",
    "orders", "shop2", "store2",
    "ci", "cd", "pipeline", "build", "artifactory", "nexus",
    "sonar", "sonarqube", "bamboo", "teamcity", "travis",
    "kibana", "prometheus", "metrics", "logs", "logging",
    "elk", "elastic", "splunk", "sentry", "newrelic",
    "s3", "storage", "backup", "cloud", "cdn2", "assets",
    "bucket", "blob",
    "api-v1", "api-v2", "apiv1", "apiv2", "graphql", "rest",
    "ws", "websocket", "socket", "gateway-api",
    "crm", "erp", "hr", "intranet2", "wiki2", "confluence",
    "jira", "trello", "notion",
    "old", "legacy", "new", "beta2", "alpha", "sandbox2",
    "partner", "partners", "client", "clients", "vendor",
    "corp", "corporate", "office", "secure", "ssl", "tls"
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


print(GREEN+"""
███████╗██╗   ██╗██████╗ 
██╔════╝██║   ██║██╔══██╗
███████╗██║   ██║██████╔╝
╚════██║██║   ██║██╔══██╗
███████║╚██████╔╝██████╔╝
╚══════╝ ╚═════╝ ╚═════╝ 

██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗███████╗
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║██╔════╝
██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║███████╗
██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║╚════██║
██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║███████║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝

                    by JyxDevLab
"""+LIGHT_WHITE)

domain = input(YELLOW+"Enter target URL (example.com): "+LIGHT_WHITE)

tested = 0
found = 0
total = len(subdomains)

with open("results_backup.txt", "w") as results:

    for i, sub in enumerate(subdomains, start=1):

        tested += 1

        bar_length = 30
        filled = int(bar_length * i / total)

        bar = "█" * filled + "-" * (bar_length - filled)

        print(
            f"\r{YELLOW}[{bar}] {i}/{total} | Found: {found}{LIGHT_WHITE}",
            end=""
        )

        try:
            url = f"https://{sub}.{domain}"
            response = requests.get(url, timeout=5)

            if response.status_code < 400:

                found += 1

                print(
                    f"\n{GREEN}[FOUND] {url} -> HTTP {response.status_code}{LIGHT_WHITE}"
                )

                results.write(
                    f"{url} -> HTTP {response.status_code}\n"
                )

        except requests.RequestException:
            pass

print("\n")

print(
    GREEN +
    f"[+] Scan completed\n"
    f"[+] Tested: {tested}\n"
    f"[+] Found: {found}\n"
    f"[+] Results saved to results.txt" +
    LIGHT_WHITE
)



url = f"https://{subdomains}.tecnicasdeinvasao.com"



for sub in subdomains:
    try:
        url = f"https://{sub}.{domain}"
        response = requests.get(url, timeout=5)

        print(LIGHT_CYAN+f"{url} -> {response.status_code}"+LIGHT_WHITE)
    except requests.RequestException:
        print(RED+f"{url} -> 404"+LIGHT_WHITE)