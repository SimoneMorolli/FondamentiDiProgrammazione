class BinTree:
    def __init__(self, V, left=None, right=None):
        self.value = V
        self.left = left
        self.right = right


################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################


    @classmethod
    def fromList(cls, a_list):
        """
        Build the tree from a list in the following form:
          [value, left, right]
        wherein left and right are other trees or None
        :param a_list: a list [value, left, right]
        :return: a tree
        """
        value, left, right = a_list
        if left: left = cls.fromList(left)
        if right: right = cls.fromList(right)
        return cls(value, left, right)

    def toList(self):
        """
        Convert this tree into a list in the following form:
          [value, left, right].
        :return: a list [value, left, right]
        """
        left = None if not self.left else self.left.toList()
        right = None if not self.right else self.right.toList()
        return [self.value, left, right]

    def __eq__(self, other):
        """
        Compare two trees
        :param other: a tree
        :return: True if trees are equal; False otherwise
        """
        return other != None and \
               type(self) == type(other) and \
               self.value == other.value and \
               self.left == other.left and \
               self.right == other.right

    def __repr__(self, level=0):
        """
        Print a tree with a given indentation level
        :param level: indentation level
        :return: a string-representation of the tree
        """
        indent = "|  " * level
        res = "{0}Node_{1}: {2.value}".format(indent, id(self), self)
        indent = "|  " * (level + 1)
        if self.left:
            res += "\n{}".format(self.left.__repr__(level + 1))
        else:
            res += "\n{}{}".format(indent, self.left)
        if self.right:
            res += "\n{}".format(self.right.__repr__(level + 1))
        else:
            res += "\n{}{}".format(indent, self.right)
        return res
