import student_solution as st
from score import add
import inspect
import pytest

FORBIDDEN = ['if ', 'else', 'for ', 'while ']

# ---------- ПРОВЕРКА НА ПУСТОТУ student_solution.py ----------
def test_student_solution_not_empty():
    src = inspect.getsource(st)
    assert "print(" in src, "student_solution.py пустой или нет print в функциях"
    add(0, "not_empty")  # баллы не добавляем, это просто проверка

# ---------- ПРОВЕРКА НА ЗАПРЕЩЕННЫЕ КОНСТРУКЦИИ ----------
def test_no_forbidden():
    src = inspect.getsource(st)
    if any(w in src for w in FORBIDDEN):
        add(0, "forbidden")
    else:
        add(10, "forbidden")  # бонус за чистый код

# ---------- TASKS ----------

def test_task1(capfd):
    try:
        st.task1("hello,world")
        out, err = capfd.readouterr()
        expected = "False\nFalse\nTrue\n"
        assert out == expected
        add(10, "task1")
    except:
        add(0, "task1")

def test_task2(capfd):
    try:
        st.task2("  Apple aA ")
        out, err = capfd.readouterr()
        expected = "Apple aA\n8\n2\n  Apple @@ \nTrue\n"
        assert out == expected
        add(20, "task2")
    except:
        add(0, "task2")

def test_task3(capfd):
    try:
        st.task3("Python")
        out, err = capfd.readouterr()
        expected = "ytho\nPto\nnohtyp\n"
        assert out == expected
        add(10, "task3")
    except:
        add(0, "task3")

def test_task4(capfd):
    try:
        st.task4([4, 8, 1, 9, 3])
        out, err = capfd.readouterr()
        expected = "[1, 3, 4, 8, 9]\n25\n1 9\n"
        assert out == expected
        add(20, "task4")
    except:
        add(0, "task4")

def test_task6(capfd):
    try:
        st.task6("Level")
        out, err = capfd.readouterr()
        expected = "True\n"
        assert out == expected
        capfd.readouterr()  # сброс
        st.task6("hello")
        out, err = capfd.readouterr()
        expected2 = "False\n"
        assert out == expected2
        add(20, "task6")
    except:
        add(0, "task6")

def test_task7(capfd):
    try:
        st.task7(255)
        out, err = capfd.readouterr()
        expected = "ff\n2\nFalse\n"
        assert out == expected
        add(10, "task7")
    except:
        add(0, "task7")

def test_task8(capfd):
    try:
        st.task8(1)
        out, err = capfd.readouterr()
        expected = "Jan\n"
        assert out == expected
        st.task8(12)
        out, err = capfd.readouterr()
        expected2 = "Dec\n"
        assert out == expected2
        add(10, "task8")
    except:
        add(0, "task8")

# ---------- OUTPUT TOTAL ----------

from score import score, results

def test_score():
    print("\nRESULTS:")
    for name, pts in results:
        print(f"{name}: {pts}")
    print(f"TOTAL SCORE: {score}/100")
