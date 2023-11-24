from contextlib import contextmanager

@contextmanager
def my_context():
    print("Вход в контекст")
    yield
    print("Выход из контекста")

with my_context():
    print("Внутри контекста")
