class ThreatDetector:
    def __init__(self, device_name, ip_address, threat_level):
        self.device_name = device_name
        self.ip_address = ip_address
        self.threat_level = threat_level

    def scan(self):
        level = self.threat_level.strip().lower()

        if level == "low":
            status_msg = "System Safe"
        elif level == "medium":
            status_msg = "Suspicious Activity"
        elif level == "high":
            status_msg = "Critical Threat Detected"
        else:
            status_msg = "Unknown Threat Level"

        print(f"Device Name: {self.device_name}")
        print(f"IP Address: {self.ip_address}")
        print(f"Threat Level: {self.threat_level}")
        print(f"Status: {status_msg}")
        print("-" * 30)


device1 = ThreatDetector("Router-A1", "192.168.1.1", "Low")
device2 = ThreatDetector("Laptop-B2", "192.168.1.15", "Medium")
device3 = ThreatDetector("Server-C3", "192.168.1.100", "High")

device1.scan()
device2.scan()
device3.scan()
