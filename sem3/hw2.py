# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

import re


def get_most_frequent_words(text: str, top: int) -> list[str]:
    """
    Выдает top самых частых элементов text, исключая знаки препинания
    """
    new_text = re.sub(r"[^\w\s]", "", text.lower().strip()).split()
    dict_counts = {i: new_text.count(i) for i in set(new_text)}
    return dict(sorted(dict_counts.items(), key=lambda item: -item[1])[:top:])


TOP = 10

text = "Python является мультипарадигменным языком программирования, поддерживающим императивное, процедурное, структурное, \
        объектно-ориентированное программирование, метапрограммирование и функциональное программирование. \
        Задачи обобщённого программирования решаются за счёт динамической типизации. \
        Аспектно-ориентированное программирование частично поддерживается через декораторы, \
        более полноценная поддержка обеспечивается дополнительными фреймворками. \
        Такие методики как контрактное и логическое программирование можно реализовать с помощью библиотек или расширений. \
        Основные архитектурные черты — динамическая типизация, автоматическое управление памятью, полная интроспекция, \
        механизм обработки исключений, поддержка многопоточных вычислений с глобальной блокировкой интерпретатора, \
        высокоуровневые структуры данных. Поддерживается разбиение программ на модули, которые, в свою очередь, могут объединяться в пакеты. \
        Эталонной реализацией Python является интерпретатор CPython, который поддерживает большинство активно используемых платформ \
        и являющийся стандартом де-факто языка. Он распространяется под свободной лицензией Python Software Foundation License, \
        позволяющей использовать его без ограничений в любых приложениях, включая проприетарные. \
        CPython компилирует исходные тексты в высокоуровневый байт-код, который исполняется в стековой виртуальной машине. \
        К другим трём основным реализациям языка относятся Jython (для JVM), IronPython (для CLR/.NET) и PyPy. \
        PyPy написан на подмножестве языка Python (RPython) и разрабатывался как альтернатива CPython с целью повышения скорости \
        исполнения программ, в том числе за счёт использования JIT-компиляции. Поддержка версии Python 2 закончилась в 2020 году. \
        На текущий момент активно развивается версия языка Python 3. Разработка языка ведётся через предложения по расширению языка PEP \
        (англ. Python Enhancement Proposal), в которых описываются нововведения, делаются корректировки согласно обратной связи от сообщества \
        и документируются итоговые решения."

print(get_most_frequent_words(text, TOP))
