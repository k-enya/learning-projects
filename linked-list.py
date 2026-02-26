class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_obj(self, obj):
        '''добавление нового объекта obj класса ObjList в конец связного списка'''
        if self.head == None and self.tail == None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self):
        '''удаление последнего объекта из связного списка'''
        if self.head == self.tail:
            self.tail = None
            self.head = None
        elif self.head != None:
            self.tail = self.tail.get_prev()

    def get_data(self):
        '''получение списка из строк локального свойства __data всех объектов связного списка'''
        d = []
        if self.head != None:
            self.tem = self.head
            while self.tem != self.tail:
                d.append(self.tem.get_data())
                self.tem = self.tem.get_next()
            d.append(self.tem.get_data())
        return d

class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None
    def set_next(self, obj):
        self.__next = obj
    def set_prev(self, obj):
        self.__prev = obj
    def get_next(self):
        return self.__next
    def get_prev(self):
        return self.__prev
    def set_data(self, data):
        self.__data = data
    def get_data(self):
        return self.__data

