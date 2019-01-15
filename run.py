from utils.task1 import PythonDeveloper, JavaDeveloper, RubyDeveloper
from utils.task2 import E
from utils.task3 import ItCompany

if __name__ == '__main__':
    print("\n" + " Task1")
    PY_DEV = PythonDeveloper(6, "Anton")
    PY_DEV.about()
    PY_DEV.write_code()
    print(PY_DEV, "\n")

    PY_DEV1 = PythonDeveloper(4, "Alexandr")
    PY_DEV1.about()
    PY_DEV1.write_code()
    print(PY_DEV1, "\n")

    JA_DEV = JavaDeveloper(2, "Greg")
    JA_DEV.about()
    JA_DEV.write_code()
    print(JA_DEV, "\n")

    JA_DEV1 = JavaDeveloper(5, "Roman")
    JA_DEV1.about()
    JA_DEV1.write_code()
    print(JA_DEV1, "\n")

    RU_DEV = RubyDeveloper(3, "Igor")
    RU_DEV.about()
    RU_DEV.write_code()
    print(RU_DEV, "\n")

    RU_DEV1 = RubyDeveloper(1, "Gleb")
    RU_DEV1.about()
    RU_DEV1.write_code()
    print(RU_DEV1, "\n")

    print("\n" + " Task2")
    print(E.mro())
    # порядок поиска: E, D, C, B, A, object

    print("\n" + " Task3")
    IT_CO = ItCompany()
    IT_CO.add(PY_DEV)
    IT_CO.add(PY_DEV1)
    IT_CO.add(JA_DEV)
    IT_CO.add(JA_DEV1)
    IT_CO.add(RU_DEV)
    IT_CO.add(RU_DEV1)

    print('\n')
    IT_CO.lay_off_emp("Igor")

    print('\n')
    IT_CO.sort_team()
