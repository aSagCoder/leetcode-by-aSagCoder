class Solution:
    def defangIPaddr(self, address: str) -> str:
        components = address.split(".")

        defanged_address = "[.]".join(components)
        return defanged_address
