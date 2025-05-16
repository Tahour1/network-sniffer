from scapy.all import sniff
thr_file = open("network_log.txt", "w")
def analyze_packet(packet):
    print(packet.summary())
    thr_file.write(summary + "\n")

print("Starting packet capture...")
sniff(prn=analyze_packet, count=10)
print("Copture complete.")
thr_file.close()
