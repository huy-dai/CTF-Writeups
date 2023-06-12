# Introduction

## Offensive Security

Definition: **Offensive security** is the process of breaking into computer systems, exploiting software bugs, and finding loopholes in applications to gain unauthorized access to them.

### Challenge 1: GoBuster

We're given an HTTP web service and asked to "hack" into it by finding a hidden page and logging into it.

Used `gobuster` to iterate through a word list for possible page candidates.

`gobuster -u http://fakebank.com -w wordlist.txt dir`

Flag: BANK-HACKED

### Defensive Security

Definition: **Defensive security** is somewhat the opposite of offensive security, as it is concerned with two main tasks:

- Preventing intrusions from occurring
- Detecting intrusions when they occur and responding properly

**Security Operations Center (SOC)** is a team of cybersec professionals who monitor the network and systems for malicious events. 

One major area to cover is ***threat intelligence***, which defines the information you have about actual and potential adversaries. This helps you be more prepared against attackers of interest and also more readily mitigate or detect their intrusion.

Another is ***Digital Forensics and Incident Response (DFIR)***. Digital Forensics is responsible for analyzing evidence of an attack, such as with the file system, system memory, system logs, and network logs, while Incident Response handles the methodology of responding to an attack (from the preparation phase to detection & analysis, containment & eradication, and post-incident).

An additional area is ***Malware Analysis***, which looks at malicious program using static and dynamic analysis.

### Challenge 1: SIEM Analysis

We are given a SIEM dashboard and see there is a suspicious login from 143.110.250.149. We can cross-reference this IP with open-source databases like `AbuseIPDB` and `Cisco Talos Intelligence`. 

Using the GUI, we escalated to SOC team lead and blocked the IP on the firewall.

Flag: THM{THREAT-BLOCKED}

## Careers in Cyber

* **Security Analyst**: Evaluate company networks and security systems to uncover actionable steps + recommendations for preventation measures. Compile reports on state of security, document security issues, and develop security plans
* **Security Engineer:** Develop and implement security solutions using threats + vulnerability info
* **Incident Responder**: Create plans, policies, and protocols for organization to enact during security incidents
* **Digital Forensics Examiner:** Collecting and analyzing evidence for legal procedures.
* **Malware Analyst:** Reverse engineer  malwares + figure out what they do. Document and report on findings.
* **Penetration Tester:** Test security of systems and software within a company. Perform security assessments, audits, and analyze policies.
* **Red Teamer:** Emulate role of an adversary and test the company's detection and response capabilities. This job role requires imitating cyber criminals' actions, emulating malicious attacks, retaining access, and avoiding detection