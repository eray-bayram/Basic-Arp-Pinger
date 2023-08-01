import argparse
import scapy.all as scapy
class ArpPing():

    def __init__(self):
        print("Arp Pinger running!!")


    def user_input(self):

        x = argparse.ArgumentParser(prog="Arp Pinger")
        x.add_argument('-i','--ipaddress', type=str, help= "-i , ip range ")
        y = x.parse_args()
        if y.ipaddress != None :
            return y
        else:
            print("Enter IP range")

    def send_arp(self,ip):
        arp_request_packet = scapy.ARP(pdst=ip)

        broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

        combined_packet = broadcast_packet / arp_request_packet

        (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)

        answered_list.summary()

if __name__ == "__main__" :
    print("Welcome :) ")
    arp_ping = ArpPing()
    arp_ip = arp_ping.user_input()
    arp_ping.send_arp(arp_ip.ipaddress)