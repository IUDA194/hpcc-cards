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
returned_dict = table_ret.get_data()  # Вызов метода get_data() на экземпляре table

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


# Разделение строки по точке с запятой
print(current_pain_of_programming)

input_string = current_pain_of_programming.split("; ")
proga_list = []
for val in input_string:
    proga_list.append(val)

# Вывод всех значений из списка proga_list
print(proga_list[2])