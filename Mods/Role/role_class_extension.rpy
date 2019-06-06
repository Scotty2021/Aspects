# Add object comparison and hash function to the Role class

init -1 python:
    # Compare on role_name when comparing to another role otherwise use hash function
    def role_compare(self,other):
        if isinstance(other, Role):
            if self.role_name == other.role_name:
                return 0

        if self.__hash__() < other.__hash__(): #Use hash values to break ties.
            return -1
        else:
            return 1

    Role.__cmp__ = role_compare

    def role_hash(self):
        return hash(self.role_name)

    Role.__hash__ = role_hash
