class StringClass:
    string23 = ""
    def __init__(self, string):
        self.string = string
        StringClass.string23 = self.string

    def String_class_string(self):
        return StringClass.string23

    def length(self):
        return len(self)

    def list_conversion(self, string):
        list1 = []
        for i in string:
            if i == ' ':
                pass
            else:
                list1.append(i)
        return list1


class PairPossible(StringClass):
    string2 = ""

    def __init__(self, string1):
        self.string1 = string1
        PairPossible.string2 = self.string1
    def get_string_pairPossible(self):
        return PairPossible.string2

    def create_pair(self):
        new_list =[]

        list2 = PairPossible.list_conversion(self, self.string1)
        for i in range(0, len(list2)):
            temp_string = str()
            for j in range(i+1, len(list2)):
                temp_string = list2[i] + list2[j]
                new_list.append(temp_string)

        return new_list


class Findcommon (PairPossible):
    def __init__(self):
        pass
    def find(self):
        common_dict = {}



# string1 = StringClass("1231232321")
# print(string1.length())
# print(string1.list_conversion())
p = PairPossible("1212")
print(p.create_pair())
#
# o = Findcommon()
# o.find()