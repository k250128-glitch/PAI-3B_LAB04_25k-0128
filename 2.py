class PasswordVault:
    def __init__(self, username, password):
        self.username = username
        self._vault_status = "Locked"
        self.__password = password

    def change_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            self._vault_status = "Updated"
            print("Password changed successfully")
        else:
            self._vault_status = "Change Failed"
            print("Incorrect current password. Change denied")

    def verify_password(self, entered_password):
        if entered_password == self.__password:
            self._vault_status = "Unlocked"
            print("Access Granted")
        else:
            self._vault_status = "Access Denied"
            print("Access Denied")

    def display_status(self):
        print(f"Username: {self.username}")
        print(f"Vault Status: {self._vault_status}")
        print("-" * 30)


from abc import ABC, abstractmethod


class SecurityTool(ABC):
    def __init__(self, tool_name):
        self.tool_name = tool_name

    @abstractmethod
    def respond(self):
        pass


class Firewall(SecurityTool):
    def respond(self):
        print(f"{self.tool_name}: Blocking unauthorized network traffic")


class AntivirusScanner(SecurityTool):
    def respond(self):
        print(f"{self.tool_name}: Quarantining infected files")


class IntrusionDetector(SecurityTool):
    def respond(self):
        print(f"{self.tool_name}: Alerting admin of suspicious intrusion")


if __name__ == "__main__":
    vault1 = PasswordVault("huzaifa_dev", "Secure@123")
    vault1.display_status()
    vault1.verify_password("wrongpass")
    vault1.verify_password("Secure@123")
    vault1.change_password("Secure@123", "NewPass@456")
    vault1.display_status()

    print("=" * 30)

    security_tools = [
        Firewall("Perimeter Firewall"),
        AntivirusScanner("Endpoint Antivirus"),
        IntrusionDetector("Network IDS")
    ]

    for tool_item in security_tools:
        tool_item.respond()
