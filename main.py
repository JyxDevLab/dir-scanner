import requests

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

url_site = input("Enter a website URL to continue the scan : ")

if url_site[-1] == "/":
    url_site = url_site[:-1]

for pasta in directorys:
    teste = url_site + "/" + pasta

    try:
        dir_response = requests.get(teste, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {teste}: {e}")
        continue

    if dir_response.status_code in (401, 403):
        print("Access Denied / Protected | " + teste + " | Stats Code: " + str(dir_response.status_code))
    elif 200 <= dir_response.status_code < 300:
        print("The directory exists and was found. | " + teste + " | Stats Code: " + str(dir_response.status_code))