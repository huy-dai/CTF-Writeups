# Starting Challenges

## Challenge 1: Web - Walking an Application

We are given a website and asked to find flags using different methods of analysis:

- View Source
  - Hidden comments
  - Viewing URL of /assets, which happens to have directory listing turned on
  - Viewing framework used to build website -> Identity it is an outdated version
- Inspector Tool
  - Remove `<div>` hiding content
- Debugger Tool
  - The **debugger tool** is useful for inspecting Javascript code that is run on the website. For this particular example, we spot a flashing red box on the screen on load of the `/contact` page.
  - We are able to identify the file `flash.min.js` in the assets folder in Debugger tab, put a *breakpoint* on a specific line of code that removes the box from view, and re-run the website to see the flag.
- Network Tab
  - When we click submit on the Contact form, we are able to capture packets sent to backend server + response from it. Websites often use **AJAX** to make requests that don't alter the look of the website. We find the flag in the response.

## Challenge 2: Content Discovery

To discover what content are available for viewing or access on a website, we can look at the follow areas:

- robots.txt
- sitemap.xml
  - File to indicate to pages that can be listed on search engines.
- Hash of favicon
  - Sometimes developers forget to replace the original favicon, and it can give hints to current web framework being used for the website
  - Example to check against favicon database: `curl https://static-labs.tryhackme.cloud/sites/favicon/images/favicon.ico | md5sum`
  - Link: <https://wiki.owasp.org/index.php/OWASP_favicon_database>
- HTTP headers returned by page
  - Example: `curl http://10.10.136.69 -v`
- Wappalyzer
- Web Fuzzing / Directory Busting
  - Output from ffuf:

```sh
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.136.69/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403
________________________________________________

assets                  [Status: 301, Size: 178, Words: 6, Lines: 8]
contact                 [Status: 200, Size: 3108, Words: 747, Lines: 65]
customers               [Status: 302, Size: 0, Words: 1, Lines: 1]
development.log         [Status: 200, Size: 27, Words: 5, Lines: 1]
monthly                 [Status: 200, Size: 28, Words: 4, Lines: 1]
news                    [Status: 200, Size: 2538, Words: 518, Lines: 51]
private                 [Status: 301, Size: 178, Words: 6, Lines: 8]
robots.txt              [Status: 200, Size: 46, Words: 4, Lines: 3]
sitemap.xml             [Status: 200, Size: 1383, Words: 260, Lines: 43]
:: Progress: [4715/4715] :: Job [1/1] :: 235 req/sec :: Duration: [0:00:20] :: Errors: 0 ::
```

## Challenge 3: Subdomain Enumeration

In addition to content discovery, we also want to be aware of subdomains that are associated with a given website. 

* SSL/TLS Certificate Database:
  * CA has **Certificate Transparency (CT)** logs, which can provide useful information about subdomains related to a website.
  * Use sites like: `http://crt.sh/` and ` https://ui.ctsearch.entrust.com/ui/ctsearchui`
* DNS Bruteforce
  * Using `dnsrecon` to search publicly available DNS records of website
* Search engine results
  * Using `Sublist3r` to iterate through common search engines to find results that list different subdomains of a given domain.
* Virtual hosts - Query the main server directly
  * Often times a subdomain won't have a DNS entry for it in a large public DNS server, and instead it's on a private DNS server or is resolved dynamically by the web server of the service by looking at the `HOST` header in the HTTP request. As a result, we can use `ffuf` to alter this header to see if we get a different result
  * **Command:** `ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host: FUZZ.acmeitsupport.thm" -u http://10.10.100.147 -fs {size}`
    * The `FUZZ` parameter denotes the variable to be dynamically changed using the wordlist. Note that if the subdomain the Host header doesn't resolve, the webpage will likely return a default response. As a result, we need to provide a `fs` parameter to denote ignoring results of this specific byte size (e.g.the default response).
    * Output:
    * 
```sh
$ ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host: FUZZ.acmeitsupport.thm" -u http://10.10.100.147 -fs 2395

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.1.0
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.100.147
 :: Wordlist         : FUZZ: /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt
 :: Header           : Host: FUZZ.acmeitsupport.thm
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403
 :: Filter           : Response size: 2395
________________________________________________

api                     [Status: 200, Size: 31, Words: 4, Lines: 1]
delta                   [Status: 200, Size: 51, Words: 7, Lines: 1]
yellow                  [Status: 200, Size: 56, Words: 8, Lines: 1]
:: Progress: [151265/151265] :: Job [1/1] :: 321 req/sec :: Duration: [0:07:51] :: Errors: 0 ::


```