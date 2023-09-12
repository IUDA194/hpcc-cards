from docxtpl import DocxTemplate
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from hpcctable.table.main import table

from docxtpl import DocxTemplate


# Загрузка документа
table_ret = table()  # Создание экземпляра класса Table
returned_dict = table_ret.get_data("Е")  # Вызов метода get_data() на экземпляре table

# current_name = returned_dict.get('name')
# print(current_name)
# Перебор всех ключей и значений в словаре returned_dict


for name, data in returned_dict.items():
    current_name = name
    current_name_b = data['name_b']
    current_name_t = data['name_t']
    current_group = data['group']
    current_years = data['years']
    current_occupation = data['occupation']
    current_spaciallity = data['spaciallity']
    current_programm = data['programm']
    current_ladder = data['ladder']
    current_form = data['form']
    current_zarahuv = data['zarahuv']
    current_dogovor_s_djavolom = data['dogovor_s_djavolom']
    current_zavid_otdela = data['zavid_otdela']
    current_vidpovidalna = data['vidpovidalna']
    current_zdobuvach = data['zdobuvach']
    current_pain_of_programming = data['pain_of_programming']
    current_pain_of_programming_mark = data['pain_of_programming_mark']
    current_pain_of_db = data['pain_of_db']
    current_pain_of_db_mark = data['pain_of_db_mark']
    current_kp_of_db = data['kp_of_db']
    current_kp_of_db_mark = data['kp_of_db_mark']
    current_topic_of_pain = data['topic_of_pain']
    current_name_of_master = data['name_of_master']
    current_data_of_pain = data['data_of_pain']
    current_data_of_slaving = data['data_of_slaving']
    current_slaving_mark = data['slaving_mark']
    current_dungeon_master = data['dungeon_master']
    current_friends_of_dungeon_master = data['friends_of_dungeon_master']
    current_data_of_mastering = data['data_of_mastering']
    current_seriya = data['seriya']
    current_z_vidznakoy = data['z_vidznakoy']
    current_navch1 = data['navch1']
    current_mark_navch1 = data['mark_navch1']
    current_navch2 = data['navch2']
    current_mark_navch2 = data['mark_navch2']
    current_navch3 = data['navch3']
    current_mark_navch3 = data['mark_navch3']
    current_navch4 = data['navch4']
    current_mark_navch4 = data['mark_navch4']
    current_navch5 = data['navch5']
    current_mark_navch5 = data['mark_navch5']
    current_navch3 = data['navch5']
    current_mark_navch2 = data['mark_navch5']
    



split_values = current_years.split("; ")
years_list = []

for value in split_values:
    years_list.append(value)

input_string = current_pain_of_programming.split("; ")
proga_list = []
for val in input_string:
    proga_list.append(val)

def get_value_or_space(lst, index):
    if len(lst) > index:
        return lst[index]
    return " "

input_st = current_navch1.split("; ")
proga_li = []
for vals in input_st:
        proga_li.append(vals)

    

input_s = current_navch2.split("; ")
proga_l = []
for valsa in input_s:
    proga_l.append(valsa)


input_sa = current_navch3.split("; ")
proga_laa = []
for valsaa in input_sa:
    proga_laa.append(valsaa)


input_saa = current_navch4.split("; ")
proga_lo = []
for valso in input_saa:
    proga_lo.append(valso)


input_sol = current_navch5.split("; ")
proga_lso = []
for valsol in input_sol:
    proga_lso.append(valsol)
# Загрузка документа
doc = DocxTemplate("ref1.docx")

# Заполнение контекста данными
context = {
    "year1": years_list[0],
    "year2": years_list[1],
    "main_name": current_name,
    "occupation": current_occupation,
    "spaciallity": current_spaciallity,
    "programm": current_programm,
    "ladder":current_ladder,
    "form":current_form,
    "zarahuv":current_zarahuv,
    "dogovor": current_dogovor_s_djavolom,
    "pib":current_zdobuvach,

    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,

    "practise": proga_list[1],
    "credit": proga_list[2],
    "course": proga_list[3],
    "time_ot": proga_list[4],
    "time_to": proga_list[5],
    "def": proga_list[6],
    "mark1": current_pain_of_programming_mark,
    "god_name": proga_list[7],
    "type": "КП",
    "data_defence": current_data_of_slaving,
    "markkp": current_slaving_mark,
    "slave": current_friends_of_dungeon_master,
    "pib_rod": current_name_b,
    "kvala": current_topic_of_pain,
    "pib_boss": current_name_of_master,
    "datakval": current_data_of_pain,
    "datadefkval": current_data_of_slaving,
    "markkval": current_slaving_mark,
    "datayear": current_data_of_mastering,
    "vidznak": current_z_vidznakoy,
    "seryia": current_seriya,

    "practise": get_value_or_space(proga_list, 1),
    "credit": get_value_or_space(proga_list, 2),
    "course": get_value_or_space(proga_list, 3),
    "time_ot": get_value_or_space(proga_list, 4),
    "time_to": get_value_or_space(proga_list, 5),
    "def": get_value_or_space(proga_list, 6),
    "mark1": current_pain_of_programming_mark,
    "god_name": get_value_or_space(proga_list, 7),

    "practise1": get_value_or_space(proga_li, 1),
    "credit1": get_value_or_space(proga_li, 2),
    "course1": get_value_or_space(proga_li, 3),
    "time_ot1": get_value_or_space(proga_li, 4),
    "time_to1": get_value_or_space(proga_li, 5),
    "def1": get_value_or_space(proga_li, 6),
    "mark2": current_mark_navch1,
    "god_name1": get_value_or_space(proga_li, 7),

    "practise2": get_value_or_space(proga_l, 1),
    "credit2": get_value_or_space(proga_l, 2),
    "course2": get_value_or_space(proga_l, 3),
    "time_ot2": get_value_or_space(proga_l, 4),
    "time_to2": get_value_or_space(proga_l, 5),
    "def2": get_value_or_space(proga_l, 6),
    "mark3": current_mark_navch2,
    "god_name2": get_value_or_space(proga_l, 7),

    "practise3": get_value_or_space(proga_laa, 1),
    "credit3": get_value_or_space(proga_laa, 2),
    "course3": get_value_or_space(proga_laa, 3),
    "time_ot3": get_value_or_space(proga_laa, 4),
    "time_to3": get_value_or_space(proga_laa, 5),
    "def3": get_value_or_space(proga_laa, 6),
    "mark4": current_mark_navch3,
    "god_name3": get_value_or_space(proga_laa, 7),

    "practise4": get_value_or_space(proga_lo, 1),
    "credit4": get_value_or_space(proga_lo, 2),
    "course4": get_value_or_space(proga_lo, 3),
    "time_ot4": get_value_or_space(proga_lo, 4),
    "time_to4": get_value_or_space(proga_lo, 5),
    "def4": get_value_or_space(proga_lo, 6),
    "mark5": current_mark_navch4,
    "god_name4": get_value_or_space(proga_lo, 7),

    "practise5": get_value_or_space(proga_lso, 1),
    "credit5": get_value_or_space(proga_lso, 2),
    "course5": get_value_or_space(proga_lso, 3),
    "time_ot5": get_value_or_space(proga_lso, 4),
    "time_to5": get_value_or_space(proga_lso, 5),
    "def5": get_value_or_space(proga_lso, 6),
    "mark6": current_mark_navch5,
    "god_name5": get_value_or_space(proga_lso, 7),








    




     









}

# Заполнение шаблона данными
doc.render(context)

# Сохранение результата
doc.save("output.docx")
