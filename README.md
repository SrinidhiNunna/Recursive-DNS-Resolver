# Recursive-DNS-Resolver
Implementation of Recursive DNS Resolver in Python and Unbound

Here, I have implemented DNS recursive resolver in Linux with assortment of security and privacy enhancements against DNS cache poisoning attacks, censorship using Unbound 1.9.4, Python code which mimics the recursive resolver using dnspython library.

Objective 1: understanding UDP, TCP,IP and DNS TRANSPORT PROTOCOLS based-queries and working of DNS

Objective 2: Creating web framework(GUI) and Unbound configuration.

Objective 3: Benefits to the endpoint users/client.

Objective 4:Implemented a DNS recursive resolver in Unbound and Python with an assortment of security and privacy enhancements against DNS cache poisoning attacks

Problem Statement:
->Memorizing the IP address of all the required websites is not possible.
->DNS is an integral part of the internet, invented almost 30 years ago. So, initially privacy and security aspects are not considered like the unencrypted nature of the DNS exchanges which can cause:
 Blocking of traffic, Spoofing IPs in phishing scams, DNS cache poisoning attacks, Spy on the user’s internet activity

Layers Involvement:
Application Layer : DNS,
Presentation Layer : DNSSEC cryptographic signature,
Session Layer : Maintains connection between client and server until it find the required IP address,
Transport Layer : Using DNS Transport protocols like DNS-over-UDP/53 ("Do53"), DNS-over-TCP/53 ("Do53/TCP") RFC1123, DNS-over-TLS ("DoT") RFC 7858, DNS Crypt, DNSSEC,
Network Layer : IP address.

Here You can view my code:
https://docs.google.com/document/d/1NiSVl2sRdeBdOf8NnQ4kGY69RMp8YiUST8K7uqrKWtI/edit?usp=sharing











