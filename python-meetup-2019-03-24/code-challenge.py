"""
CHALLENGE URL:
    https://practice.geeksforgeeks.org/problems/arraylist-operation/1

TEST DATA:
2
6
i g i e i e i k i s f e
4
i c i p i p f f


PROBLEM DESCRIPTION:
    i = insert next character
    f = find freqeuncy of character
        -after finding frequency, we will print 'not present' or the frequency
    Array List = is a list of charaters
    for list.add() we can use list.append for python
    for list.contains() we can use list.count()
    for list.frequency, we can create our own function that counts the items
        and returns the count of that list
    for every query, program should print 'not present' or print frequency
"""


class Foo():
    def __init__(self, file_name: str ='code-challenge.txt'):
        self.list = []
        self.input_file_name = file_name

    def insert_element(self, element: str):
        self.list.append(element)

    def find_element_frequency(self, element: str):
        return self.list.count(element)

    def process_query(self, query_instruction: str, query_character: str):
        if query_instruction == 'i':
            self.insert_element(query_character)
        else:
            frequency = self.find_element_frequency(query_character)
            if frequency == 0:
                print('Not Present')
            else:
                message = 'Frequency of {} is: {}'.format(query_character, frequency)
                print(message)

    def process_line(self, line: str):
        length = len(line)
        index = 0

        while index < length:
            query_instruction = line[index]
            query_character = line[index+2]
            self.process_query(query_instruction, query_character)
            index += 4

    def clear_list(self):
        self.list = []

    def line_has_queries(self, line: str):
        return 'i' in line or 'f' in line

    def parse_input_file(self):
        f = open(self.input_file_name, 'r')

        for line in f.readlines():
            if self.line_has_queries(line):
                self.process_line(line)
                self.clear_list()

    def main(self):
        self.parse_input_file()


if __name__ == '__main__':
    foo = Foo()
    foo.main()
