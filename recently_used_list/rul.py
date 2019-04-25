# TDD Iterations

# 1. Write the simplest failing test.

# 2. Write the simplest production
# code that passes all tests.

# 3. Refactor both production code
# and tests, if necessary.

class RecentlyUsedList:
    def __init__(self):
        self._list = []

    def __len__(self):
        return len(self._list)

    def insert(self, item):
        ### Ask for permission
        # if item in self._list:
        #     self._list.remove(item)

        ### Ask for forgiveness
        try:
            self._list.remove(item)
        except ValueError:
            pass
        
        self._list.insert(0, item)

    def __getitem__(self, index):
        return self._list[index]


if __name__ == '__main__':
    rul = RecentlyUsedList()
    rul.insert('first')
    rul.insert('second')
    rul.insert('third')
    print(list(rul))  # ==> ['third', 'second', 'first']
    print(len(rul))  # ==> 3
    rul.insert('second')
    print(list(rul))  # ==> ['second', 'third', 'first']

    # Należy zaimplementować metody:
    # - insert(self, item)
    # - __getitem__(self, index)
    # - __len__(self)
