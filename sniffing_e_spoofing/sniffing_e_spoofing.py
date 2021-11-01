'''

Segurança da Informação - Sniffing e Spoofing
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

from scapy.all import *

a = IP(dst = '200.155.83.77', ttl =1)
b = ICMP()
p = a / b
send(p)
