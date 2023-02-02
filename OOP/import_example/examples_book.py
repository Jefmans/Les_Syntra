import test_for_import

my_instance = test_for_import.MyClass()


from test_for_import import MyClass, OtherClass

my_instance = MyClass()

import test_for_import as tfi

from test_for_import import MyClass as MC
