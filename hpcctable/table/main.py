import httplib2 
from googleapiclient.discovery import build
import googleapiclient as apiclient
from oauth2client.service_account import ServiceAccountCredentials	
import os



class table:
    path = os.path.abspath('fillblankskhpcc-af87115fa496.json')
    spreadsheetId = "1rbQe4whW1oz5EOnjjfhPMzmIme-4N9lx8o1hSzOtNgM"
    
    service = None
    httpAuth = None
    credentials = None
    sheet_name = None

    def __init__(self) -> None:
        CREDENTIALS_FILE = self.path  # Имя файла с закрытым ключом, вы должны подставить свое
        self.spreadsheetId = "1rbQe4whW1oz5EOnjjfhPMzmIme-4N9lx8o1hSzOtNgM"
        # Читаем ключи из файла
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

        self.httpAuth = self.credentials.authorize(httplib2.Http()) # Авторизуемся в системе
        self.service = build('sheets', 'v4', http=self.httpAuth) # Выбираем работу с таблицами и 4 версию API 

    
    #ВОТ ВЫБОР ГРУПП

    def choose_sheet(self):
        self.sheet_name = input("Введите имя листа (П или Е): ")

    def get_data(self, sheet : str = None):
        self.sheet_name = sheet
        if self.sheet_name is None:
            self.choose_sheet()  # Запрос имени листа, если оно не указано

        ranges = f"{self.sheet_name}!A1:AX50"  # Обновляем ranges на основе выбранного листа

        results = self.service.spreadsheets().values().batchGet(spreadsheetId=self.spreadsheetId, ranges=ranges, valueRenderOption='FORMATTED_VALUE', dateTimeRenderOption='FORMATTED_STRING').execute()

        sheet_values = results['valueRanges'][0]['values']

        sorted_data = []

        
        for row in sheet_values:
            sorted_data = {row[0] : {"name" : row[0],
                                    "name_b" : row[1], 
                                    "name_t" : row[2], 
                                    "group" : row[3], 
                                    "years" : row[4], 
                                    "occupation" : row[5], 
                                    "spaciallity" : row[6],
                                    "programm" : row[7],
                                    "ladder" : row[8],
                                    "form" : row[9], 
                                    "zarahuv" : row[10],
                                    "dogovor_s_djavolom" : row[11],
                                    "zavid_otdela" : row[12],
                                    "vidpovidalna": row[13],
                                    "zdobuvach": row[14],
                                    "pain_of_programming" : row[15],
                                    "pain_of_programming_mark" : row[16],
                                    "pain_of_db" : row[17],
                                    "pain_of_db_mark" : row[18],
                                    "kp_of_db" : row[19],
                                    "kp_of_db_mark" : row[20],
                                    "topic_of_pain" : row[21],
                                    "name_of_master" : row[22],
                                    "data_of_pain" : row[23],
                                    "data_of_slaving" : row[24],
                                    "slaving_mark" : row[25],
                                    "dungeon_master" : row[26],
                                    "friends_of_dungeon_master" : row[27],
                                    "data_of_mastering" : row[28],
                                    "seriya" : row[29],
                                    "z_vidznakoy" : row[30],
                                    "navch1" : row[31],
                                    "mark_navch1" : row[32],
                                    "navch2" : row[33],
                                    "mark_navch2" : row[34],
                                    "navch3" : row[35],
                                    "mark_navch3" : row[36],
                                    "navch4" : row[37],
                                    "mark_navch4" : row[38],
                                    "navch5" : row[39],
                                    "mark_navch5" : row[40],
                                    "navch6" : row[41],
                                    "mark_navch6" : row[42],
                                    
                                    
                                    
                                    }}
            
    

            return sorted_data

            

#tb = table()
#spreadsheetId = "1rbQe4whW1oz5EOnjjfhPMzmIme-4N9lx8o1hSzOtNgM"
