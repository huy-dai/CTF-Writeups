# Red Team Fundamentals

## Threat Vectors

Most prominent attackers nowadays are **Advanced Persistent Threats (APT)**, which are groups of highly-skilled attackers, normally sponsored by nations or organized crime groups. They are called persistent because they can remain undetected on networks for long periods of time.

## Testing Methods

1. **Vulnerability assessments:** Scan for but not exploit vulnerabilities found on hosts in the network. Relatively automated process.
2. **Penetration Test:** Find vulnerabilities and attempt to exploit them. Perform post-exploit tasks to try to continue exploiting more machines. Analyzes how an attack could move around the network.
   1. Usually less emphasis on being covert due to time constraints of testing. Also some security mechanisms may be temporarily relaxed.
3. **Red teaming:** Emulates a real threat's actor **Tactics, Techniques, and Procedures (TTPs)** to see how well the blue team responds to them.
   1. Define goals, known as **crown jewels** or **flags** to work towards
   2. Red team will work towards goals while being covert and evade existing security mechanisms.
   3. Objective behind work is to be able to simulate enough TTPs for the blue team to learn how to react to a real ongoing threat adequately. 

## Red Teaming

Red team can be run in different levels of engagement:

- **Full engagement:** Simulate full attacker's workflow
- **Assumed breach:** Assume attacker has already gained control of some assets
- **Tabletop exercise:** Scenarios are discussed between red and blue. Ideal for when doing live simulations might be complicated.

The **Rules of Engagement** defines the permission given to the pen tester to do to the targets.

Within the red team there is a team lead, assistant lead, and operator.

At the end of the red teaming, it's important to discuss successful hack attempts as well as failed ones. You want to see if the blue team was able to detect your failed attempts or if proper investigation was being done.

## Lockheed Martin Cyber Kill Chain

1. Recon - Get info, OSINT
2. Weaponization - Combine the objective with an exploit (e.g. create malicious document)
3. Delivery - How will weaponized function be delivered to target
4. Exploitation - Exploit the system to execute code
5. Installation - Install malware and other tools
6. Command & Control - Control compromised asset from a remote controller
7. Actions on Objectives - Any end objectives (ransomware, data exfiltration)