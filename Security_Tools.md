# Security Tools

These are my list of useful pentesting and CTF tools, broken down by category.

## Forensics

* Analyzing Disk Images (`Autopsy`, `Sleuthkit`)
  * **Description:** Autopsy is the GUI implementation of Sleuthkit, both of which are used for analyzing disk images and recovering files from them
  * **Installation:** sudo apt-get install autopsy sleuthkit

## Threat Intelligence Database

* `AbuseIPDB` and `Cisco Talos Intelligence`
  * **Link:** <https://www.abuseipdb.com/> and  <https://www.talosintelligence.com/>
  * **Description:** These are open-source databases that report information about suspicious and malicious threat actors. Allow lookup by IP.

## Webpage Analysis

* Framework stack (`Wappalyzer`)
  *  **Description:** Is a website and browser extension that provides information about the framework stack, CMS, payment processors, etc. a website is using
  *  **Link:** <https://www.wappalyzer.com/>
* Directory Busting (`ffuf`, `dirb` and `gobuster`)
  * **Description:** For finding directories, paths, and content on a website. **Note:** These tools are often paired with wordlists like **SecLists**.
  * **Installation:** `sudo apt install ffuf dirb gobuster`
* * DNS Enumeration (`dnsrecon`, `Sublist3r`)
  * **Description:** In addition to directory busting, we can also use tools to automate the DNS search for discovering the subdomains of a website. 
  * **Link:** <https://github.com/darkoperator/dnsrecon> and <https://github.com/aboul3la/Sublist3r>
  * **Example:** `dnsrecon -t brt -d acmeitsupport.thm` to do brute force domains and hosts using a given dictionary.
* Subdomain Enumeration - Virtual Hosts (`ffuf`)
  * **Description:** Often times a subdomain won't have a DNS entry for it in a large public DNS server, and instead it's on a private DNS server or is resolved dynamically by the web server of the service by looking at the `HOST` header in the HTTP request. As a result, we can use `ffuf` to alter this header to see if we get a different result
  * **Example:** `ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host: FUZZ.acmeitsupport.thm" -u http://10.10.100.147 -fs {size}`
    * The `FUZZ` parameter denotes the variable to be dynamically changed using the wordlist.
* Certificate Transparency (CT) logs
  * **Description:** CA has publicly accessible logs for certificates they issue. These can provide information about subdomains that exists on a website.
  * **Link:** `http://crt.sh/` and ` https://ui.ctsearch.entrust.com/ui/ctsearchui`


## Wordlists

* `SecLists`
  * Often you want wordlists for password cracking, fuzzy payloads, directory busting, etc. SecLists provide a wide-encompassing directory of these lists
  * **Link:** <https://github.com/danielmiessler/SecLists>
  * **Note:** Locally I have these installed at `/usr/share/wordlists/SecLists`

## OSINT

* Comprehensive OSINT Tools List
  * **Link:** <https://osintframework.com/> and <https://inteltechniques.com/tools/index.html>
* Google Dorking
  * **Link:** <https://gist.github.com/sundowndev/283efaddbcf896ab405488330d1bbc06> and <https://www.exploit-db.com/google-hacking-database>
  * **Description:** By adding specific operators to our Google Search, we can more easily uncover information about specific person or organization
* Reverse Image Search
  * **Link:** <https://pimeyes.com/> and <https://images.google.com/>
  * **Description:** PinEyes use AI facial recognition to find photos of a person across the web. Google Images also provide reverse image searching for pictures with well-known locations.
* Username Search
  * **Link:** <https://epieos.com> and <https://checkusernames.com>
  * **Description:** Given an email, Epieos can look for accounts on commonly used social media websites associated with that email. In addition, checkusernames crawl across many social media page to check if a username is in use there.
* Social Media Activity: 
  * **Link:** <https://www.social-searcher.com>
  * **Description:** Social Searcher performs Google searches to find activity and posts relevant to a given username or name.