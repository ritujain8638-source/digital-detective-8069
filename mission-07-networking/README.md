# Mission 7 — How computers communicate

## 1. Task / objective
Explain eight core computer networking concepts (`LAN`, `MAN`, `WAN`, `DNS`, `Router`, `Protocol`, `Packet switching`, and `Client-server`) in my own words with real-world examples, observe connectivity (`ping`) and DNS resolution (`nslookup`) in Terminal while protecting personal network privacy, and write a 6-step walkthrough of what happens when a user opens a website.

## 2. Work completed

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| **LAN (Local Area Network)** | A private network that connects devices within a single small location so they can share local resources and internet access. | All laptops, phones, and a wireless printer connected to the same home Wi-Fi or college computer lab network. |
| **MAN (Metropolitan Area Network)** | A medium-sized network that links multiple LANs across a university campus, town, or city. | A municipal network connecting all public library branches and government offices across a city, or a multi-block university campus backbone. |
| **WAN (Wide Area Network)** | A large-scale network that spans across cities, countries, or the entire globe by connecting many smaller networks together. | The global **Internet**, or an international bank's network linking branches across India, Europe, and North America. |
| **DNS (Domain Name System)** | The "phonebook" of the internet that translates human-friendly website names into numerical IP addresses that routers and computers use. | Translating `example.com` into its public IPv4 address `93.184.215.14`. |
| **Router** | A networking device that sits between networks (such as your home LAN and your ISP's WAN) and directs data packets along the best path toward their destination. | A home Wi-Fi router forwarding web requests from my laptop out to my Internet Service Provider (ISP). |
| **Protocol** | An agreed-upon set of rules and formats that two devices must follow so they can understand each other's messages. | **HTTPS** (for secure web pages), **TCP/IP** (for reliable packet delivery), or **ICMP** (used by `ping`). |
| **Packet switching** | Breaking a large piece of data (like a web page or video) into many small numbered chunks called *packets* that travel independently across the network and are reassembled at the destination. | Downloading an image from a website as dozens of small TCP/IP packets that are put back together in order by the browser. |
| **Client-server** | A communication model where a user's device (**client**) sends a request for information or a service, and a powerful remote computer (**server**) processes the request and sends back a response. | My web browser (**client**) requesting a repository page from GitHub's web **server**. |

---

### Task 7.2 — Observe network information
I tested connectivity and domain lookup against the public test domain `example.com` (with my local DNS resolver address redacted as `[redacted]`):
- **Connectivity test (`ping -c 4 example.com`):** Sent 4 ICMP echo requests to `example.com` (`93.184.215.14`); all 4 packets returned with `0.0% packet loss` and an average round-trip time of `~24.3 ms`.
- **DNS lookup (`nslookup example.com`):** Returned the public IPv4 address (`93.184.215.14`) and IPv6 address (`2606:2800:21f:cb07:6820:80da:af6b:8b2c`) associated with `example.com`.

#### Answers to Task 7.2 questions:
1. **What does a connectivity test (`ping`) help you check?**
   A connectivity test checks whether your computer can actually reach a remote host across the network and receive a reply back. It also tells you whether any packets are being lost along the way (`% packet loss`) and how long the round-trip communication takes in milliseconds (`latency`).
2. **What information does a DNS lookup (`nslookup` / `dig`) display?**
   A DNS lookup displays the DNS resolver queried and the exact numerical IP address(es) (both IPv4 `A` records and IPv6 `AAAA` records) registered for a given domain name.
3. **What is the role of DNS when you enter a website name in a browser?**
   Humans remember names like `github.com` or `example.com`, but network routers can only route packets to numerical IP addresses. When you type a website name into your browser, **DNS** looks up and returns the matching IP address so the browser knows which server on the internet to contact.

---

### Task 7.3 — What happens when you open a website? (6-step explanation)
1. **User enters URL in the client:** You type a URL (such as `https://example.com`) into your web browser, which acts as the **client** application.
2. **DNS lookup translates name to IP:** The **client** contacts a **DNS** resolver to translate the human-readable domain name (`example.com`) into the website's numerical IP address (`93.184.215.14`).
3. **Client creates a protocol request:** Using the **HTTPS** and **TCP/IP** **protocols**, the browser establishes a connection to that IP address and prepares an HTTP `GET` request asking for the web page.
4. **Router forwards packets across the network:** Your request is split into small data packets and sent to your local **router**, which forwards the packets across your ISP and the wider internet (WAN) until they reach the destination **server**.
5. **Server processes the request and replies:** The web **server** receives the request, locates or generates the requested HTML, CSS, and JavaScript files, and sends them back across the network in response packets following the same **protocol** rules.
6. **Browser reassembles and renders the response:** Your **client** browser receives the incoming packets, reassembles them in the right order, and renders the visual web page on your screen.

## 3. Commands / tools used
- **`ping -c 4 example.com`**: Sent 4 test packets using the ICMP protocol to verify that `example.com` is reachable and measure round-trip time.
- **`nslookup example.com`**: Queried the Domain Name System to look up the public IPv4 and IPv6 addresses for `example.com`.

## 4. My understanding
Every time I open a website, several networking layers cooperate in milliseconds. My laptop starts on a local **LAN**, talks to a **router** to reach the global **WAN** (the Internet), relies on **DNS** to turn domain names into IP addresses, and uses **packet switching** and standard **protocols** (`TCP/IP`, `HTTPS`) so my browser (**client**) and the remote web **server** can exchange data reliably.

## 5. Difficulties faced
When I first ran `nslookup example.com`, the top two lines of the output printed the local IP address of my router/DNS server, which could reveal private local network configuration.

## 6. How I resolved them
Before saving the output into [`evidence/mission-07-network-lookup.txt`](../evidence/mission-07-network-lookup.txt), I replaced the `Server:` and `Address:` lines of my local resolver with `[redacted]` while keeping the public `example.com` lookup answer intact, following the assignment's privacy rule.

## 7. Evidence / files
- [`mission-07-networking/README.md`](./README.md) — Contains the 8-concept networking table, connectivity/DNS analysis, and 6-step website communication walkthrough.
- [`evidence/mission-07-network-lookup.txt`](../evidence/mission-07-network-lookup.txt) — Privacy-redacted output of `ping -c 4 example.com` and `nslookup example.com`.

## 8. Commit details
- **Commit message:** `Explain networking concepts and website communication`
- **Status:** Committed on `main` branch and ready/verified for GitHub push.
