import re

a = "В лесу ФСБ России Ёрос красивый ФСТЭК России Ёёё куст. Куст цвёл яркими цветами. Это был шиповник. Хороши душистые розы. Стала Ася рвать " \
    "розы. А там шипы. У Аси заноза. "
b = "Просто текст без запретной буквы"


def find_letter(text):
    united_list = re.findall(r' [а-я]*ё[а-я]*', text)
    if len(united_list) == 0:
        return "В тексте нет букв ё"
    return [*set(united_list)]

print(find_letter(a))
print(find_letter(b))

def find_fstek_fsb(text):
    fstek_fsb_count = len(re.findall(r'ФСТЭК|ФСБ', text))
    fstek_fsb_russia_count = len(re.findall(r'ФСТЭК России|ФСБ России', text))
    if fstek_fsb_count == fstek_fsb_russia_count:
        return "Сокращения организаций-регуляторов указаны корректно"
    return "Сокращения " + str(fstek_fsb_count - fstek_fsb_russia_count) + " организаций-регуляторов указаны неверно"

print(find_fstek_fsb(a))

def find_ex_customer(name, text):
    ex_customer_count = len(re.findall(name, text))
    if ex_customer_count > 0:
        return "Имя прошлого заказчика встречается " + str(ex_customer_count) + " раз"
    return "Имя прошлого заказчика не встречается"

def find_multiple_spaces(text):
    multiple_spaces_count = len(re.findall(r'[а-я|А-Я|ё|Ё|,|:|.|;|!|?|)]  +[а-я|А-Я|ё|Ё]', text))
    if multiple_spaces_count == 0:
        return "Множественных пробелов нет"
    return "Множественные пробелы встречаются " + str(multiple_spaces_count) + " раз"

def find_internet_spelling(text):
    right_spelling_count = len(re.findall(r'[с|С]ет[ь|и] Интернет|сетью Интернет', text))
    all_spelling_count = len(re.findall(r'[И|и]нтернет[а|у|е]*|[И|и]нтернетом', text))
    if right_spelling_count == all_spelling_count:
        return "Множественных пробелов нет"
    return "Множественные пробелы встречаются " + str(all_spelling_count - right_spelling_count) + " раз"