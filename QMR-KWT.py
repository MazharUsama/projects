from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import mysql.connector
from datetime import datetime
import datetime
from PIL import ImageTk, Image
import pandas as pd

master = Tk()

# main root window
master.geometry("390x450")
master.title("QMR-KWT")
label = Label(master, text="Welcome to QMR-KWT", font="Arial 14 bold")
label.pack(side=TOP, pady=10)

canvas = Canvas(master, width=250, height=250)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("img.png"))
canvas.create_image(7, 7, anchor=NW, image=img)

parse = Button(master, text="Parse", width=25, height=2, bg="#345", fg="White", font="Arial 9 bold")
parse.pack(pady=10)

btn = Button(master, text="Start Import", width=25, height=2, bg="#345", fg="White", font="Arial 9 bold")
btn.bind("<Button>", lambda e: NewWindow(master))
btn.pack(pady=10)


# Classes
# Data Gui Class
class NewWindow(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        # Setting Window
        master.withdraw()
        self.geometry("1000x700")
        self.title("QMR-KWT")
        self.minsize(1000, 700)
        self.maxsize(1000, 700)

        # Top Bar { Import Button, Save Button, Next Button, Date Label, Date Entry }
        topBar = Frame(self, border=1)
        topBar.pack(side=TOP, anchor="nw", pady=10, padx=5)

        importButton = Button(topBar, text="Import", width=15, height=2, bg="#345", fg="White", font="Arial 9 bold",
                              command=importBtn)
        importButton.pack(side=LEFT, padx=5)

        nextButton = Button(topBar, text="Next", width=15, height=2, bg="#345", fg="White", font="Arial 9 bold",
                            command=next_BTN)
        nextButton.pack(side=LEFT, padx=5)

        saveButton = Button(topBar, text="Save", width=15, height=2, bg="#345", fg="White", font="Arial 9 bold",
                            command=saveBtn)
        saveButton.pack(side=LEFT, padx=5)

        dateLabel = Label(topBar, text="Date: ", font="Arial 11 bold")
        dateLabel.pack(side=LEFT, padx=12)

        dateEntry = Entry(topBar, border=1, relief="solid", textvariable=v[0])
        dateEntry.pack(side=LEFT, ipadx=20, ipady=5)

        messageLabel = Label(topBar,textvariable = my_string_var, fg="Green", font="Arial 10")
        messageLabel.pack(side=LEFT, padx=20)

        # Grid { Labels, Textbox }
        mainFrame = Frame(self, border=1)
        mainFrame.pack(side=TOP, fill="x", pady=20, padx=10)

        # Label Column 0
        ConOps = Label(mainFrame, text="ConOps magic num ID:")
        ConOps.grid(row=0, column=0, pady=8)

        EPSVoltage = Label(mainFrame, text="EPS I Battery Voltage:")
        EPSVoltage.grid(row=1, column=0, pady=8)

        EPSCurrent = Label(mainFrame, text="EPS I Battery Current:")
        EPSCurrent.grid(row=2, column=0, pady=8)

        BCRVoltage = Label(mainFrame, text="BCR Voltage:")
        BCRVoltage.grid(row=3, column=0, pady=8)

        BCRCurrent = Label(mainFrame, text="BCR Current:")
        BCRCurrent.grid(row=4, column=0, pady=8)

        SOLPANXV = Label(mainFrame, text="SOL PAN X V:")
        SOLPANXV.grid(row=5, column=0, pady=8)

        SOLPANXnCurrent = Label(mainFrame, text="SOL PAN X- Current:")
        SOLPANXnCurrent.grid(row=6, column=0, pady=8)

        SOLPANXpCurrent = Label(mainFrame, text="SOL PAN X+ Current:")
        SOLPANXpCurrent.grid(row=7, column=0, pady=8)

        SOLPANYV = Label(mainFrame, text="SOL PAN Y V:")
        SOLPANYV.grid(row=8, column=0, pady=8)

        SOLPANYnCurrent = Label(mainFrame, text="SOL PAN Y- Current:")
        SOLPANYnCurrent.grid(row=9, column=0, pady=8)

        SOLPANYpCurrent = Label(mainFrame, text="SOL PAN Y+ Current:")
        SOLPANYpCurrent.grid(row=10, column=0, pady=8)

        SOLPANZV = Label(mainFrame, text="SOL PAN Z V:")
        SOLPANZV.grid(row=11, column=0, pady=8)

        # Label Column 2
        SOLPANZnCurrent = Label(mainFrame, text="SOL PAN Z- Current:")
        SOLPANZnCurrent.grid(row=0, column=2, pady=8, padx=8)

        SOLPANZpCurrent = Label(mainFrame, text="SOL PAN Z+ Current:")
        SOLPANZpCurrent.grid(row=1, column=2, pady=8, padx=8)

        BusCurrent3 = Label(mainFrame, text="3.3V Bus Current:")
        BusCurrent3.grid(row=2, column=2, pady=8, padx=8)

        BusCurrent5 = Label(mainFrame, text="5V Bus Current:")
        BusCurrent5.grid(row=3, column=2, pady=8, padx=8)

        MCUTemperature = Label(mainFrame, text="MCU Temperature:")
        MCUTemperature.grid(row=4, column=2, pady=8, padx=8)

        BatteryCell1Temp = Label(mainFrame, text="Battery Cell 1 Temp:")
        BatteryCell1Temp.grid(row=5, column=2, pady=8, padx=8)

        BatteryCell2Temp = Label(mainFrame, text="Battery Cell 2 Temp:")
        BatteryCell2Temp.grid(row=6, column=2, pady=8, padx=8)

        BatteryCell3Temp = Label(mainFrame, text="Battery Cell 3 Temp:")
        BatteryCell3Temp.grid(row=7, column=2, pady=8, padx=8)

        BatteryCell4Temp = Label(mainFrame, text="Battery Cell 4 Temp:")
        BatteryCell4Temp.grid(row=8, column=2, pady=8, padx=8)

        InputCondition = Label(mainFrame, text="Input Condition:")
        InputCondition.grid(row=9, column=2, pady=8, padx=8)

        OutputCondition1 = Label(mainFrame, text="Output Condition 1:")
        OutputCondition1.grid(row=10, column=2, pady=8, padx=8)

        OutputCondition2 = Label(mainFrame, text="Output Condition 2:")
        OutputCondition2.grid(row=11, column=2, pady=8, padx=8)

        # Label Column 4
        PowerONCycleCounter = Label(mainFrame, text="Power ON Cycle Counter:")
        PowerONCycleCounter.grid(row=0, column=4, pady=8, padx=8)

        UnderVoltageCondCounter = Label(mainFrame, text="Under Voltage Cond Counter:")
        UnderVoltageCondCounter.grid(row=1, column=4, pady=8, padx=8)

        ShortCircuitCondCounter = Label(mainFrame, text="Short Circuit Cond Counter:")
        ShortCircuitCondCounter.grid(row=2, column=4, pady=8, padx=8)

        OverTempCondCounter = Label(mainFrame, text="Over Temp Cond Counter:")
        OverTempCondCounter.grid(row=3, column=4, pady=8, padx=8)

        Battpack1tempsensor1max = Label(mainFrame, text="Battpack1 temp sensor 1 max:")
        Battpack1tempsensor1max.grid(row=4, column=4, pady=8, padx=8)

        Battpack1tempsensor1min = Label(mainFrame, text="Battpack1 temp sensor 1 min:")
        Battpack1tempsensor1min.grid(row=5, column=4, pady=8, padx=8)

        DefaultValsLUPsfastcharge = Label(mainFrame, text="Default Vals LUPs & fastcharge:")
        DefaultValsLUPsfastcharge.grid(row=6, column=4, pady=8, padx=8)

        DefaultValsOUTs = Label(mainFrame, text="Default Vals OUTs 1:6 :")
        DefaultValsOUTs.grid(row=7, column=4, pady=8, padx=8)

        BatteryInternalResistance = Label(mainFrame, text="Battery Internal Resistance:")
        BatteryInternalResistance.grid(row=8, column=4, pady=8, padx=8)

        BatteryIdealVoltage = Label(mainFrame, text="Battery Ideal Voltage:")
        BatteryIdealVoltage.grid(row=9, column=4, pady=8, padx=8)

        UHFAntennaRegisters = Label(mainFrame, text="UHF Antenna Registers:")
        UHFAntennaRegisters.grid(row=10, column=4, pady=8, padx=8)

        UHFStatusControlWord = Label(mainFrame, text="UHF Status Control Word:")
        UHFStatusControlWord.grid(row=11, column=4, pady=8, padx=8)

        # Entry Column 1
        ConOpsBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[1])
        ConOpsBTN.grid(row=0, column=1, pady=8, padx=4, ipady=5, ipadx=20)

        EPSVoltageBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[2])
        EPSVoltageBTN.grid(row=1, column=1, pady=8, padx=4, ipady=5, ipadx=20)

        EPSCurrentBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[3])
        EPSCurrentBTN.grid(row=2, column=1, pady=8, padx=4, ipady=5, ipadx=20)

        BCRVoltageBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[4])
        BCRVoltageBTN.grid(row=3, column=1, pady=8, padx=4, ipady=5, ipadx=20)

        BCRCurrentBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[5])
        BCRCurrentBTN.grid(row=4, column=1, pady=8, padx=4, ipady=5, ipadx=20)

        SOLPANXVBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[6])
        SOLPANXVBTN.grid(row=5, column=1, pady=8, padx=4, ipady=5, ipadx=20)

        SOLPANXnCurrentBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[7])
        SOLPANXnCurrentBTN.grid(row=6, column=1, pady=8, padx=4, ipady=5, ipadx=20)

        SOLPANXpCurrentBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[8])
        SOLPANXpCurrentBTN.grid(row=7, column=1, pady=8, padx=4, ipady=5, ipadx=20)

        SOLPANYVBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[9])
        SOLPANYVBTN.grid(row=8, column=1, pady=8, padx=4, ipady=5, ipadx=20)

        SOLPANYnCurrentBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[10])
        SOLPANYnCurrentBTN.grid(row=9, column=1, pady=8, padx=4, ipady=5, ipadx=20)

        SOLPANYpCurrentBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[11])
        SOLPANYpCurrentBTN.grid(row=10, column=1, pady=8, padx=4, ipady=5, ipadx=20)

        SOLPANZVBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[12])
        SOLPANZVBTN.grid(row=11, column=1, pady=8, padx=4, ipady=5, ipadx=20)

        # Entry Column 3
        SOLPANZnCurrentBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[13])
        SOLPANZnCurrentBTN.grid(row=0, column=3, pady=8, padx=4, ipady=5, ipadx=20)

        SOLPANZpCurrentBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[14])
        SOLPANZpCurrentBTN.grid(row=1, column=3, pady=8, padx=4, ipady=5, ipadx=20)

        BusCurrent3BTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[15])
        BusCurrent3BTN.grid(row=2, column=3, pady=8, padx=4, ipady=5, ipadx=20)

        BusCurrent5BTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[16])
        BusCurrent5BTN.grid(row=3, column=3, pady=8, padx=4, ipady=5, ipadx=20)

        MCUTemperatureBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[17])
        MCUTemperatureBTN.grid(row=4, column=3, pady=8, padx=4, ipady=5, ipadx=20)

        BatteryCell1TempBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[18])
        BatteryCell1TempBTN.grid(row=5, column=3, pady=8, padx=4, ipady=5, ipadx=20)

        BatteryCell2TempBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[19])
        BatteryCell2TempBTN.grid(row=6, column=3, pady=8, padx=4, ipady=5, ipadx=20)

        BatteryCell3BTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[20])
        BatteryCell3BTN.grid(row=7, column=3, pady=8, padx=4, ipady=5, ipadx=20)

        BatteryCell4BTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[21])
        BatteryCell4BTN.grid(row=8, column=3, pady=8, padx=4, ipady=5, ipadx=20)

        InputConditionBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[22])
        InputConditionBTN.grid(row=9, column=3, pady=8, padx=4, ipady=5, ipadx=20)

        OutputCondition1BTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[23])
        OutputCondition1BTN.grid(row=10, column=3, pady=8, padx=4, ipady=5, ipadx=20)

        OutputCondition2BTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[24])
        OutputCondition2BTN.grid(row=11, column=3, pady=8, padx=4, ipady=5, ipadx=20)

        # Entry Column 5
        PowerONCycleCounterBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[25])
        PowerONCycleCounterBTN.grid(row=0, column=5, pady=8, padx=4, ipady=5, ipadx=20)

        UnderVoltageCondCounterBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[26])
        UnderVoltageCondCounterBTN.grid(row=1, column=5, pady=8, padx=4, ipady=5, ipadx=20)

        ShortCircuitCondCounterBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[27])
        ShortCircuitCondCounterBTN.grid(row=2, column=5, pady=8, padx=4, ipady=5, ipadx=20)

        OverTempCondCounterBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[28])
        OverTempCondCounterBTN.grid(row=3, column=5, pady=8, padx=4, ipady=5, ipadx=20)

        Battpack1tempsensor1maxBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[29])
        Battpack1tempsensor1maxBTN.grid(row=4, column=5, pady=8, padx=4, ipady=5, ipadx=20)

        Battpack1tempsensor1minBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[30])
        Battpack1tempsensor1minBTN.grid(row=5, column=5, pady=8, padx=4, ipady=5, ipadx=20)

        DefaultValsLUPsfastchargeBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[31])
        DefaultValsLUPsfastchargeBTN.grid(row=6, column=5, pady=8, padx=4, ipady=5, ipadx=20)

        DefaultValsOUTsBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[32])
        DefaultValsOUTsBTN.grid(row=7, column=5, pady=8, padx=4, ipady=5, ipadx=20)

        BatteryInternalResistanceBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[33])
        BatteryInternalResistanceBTN.grid(row=8, column=5, pady=8, padx=4, ipady=5, ipadx=20)

        BatteryIdealVoltageBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[34])
        BatteryIdealVoltageBTN.grid(row=9, column=5, pady=8, padx=4, ipady=5, ipadx=20)

        UHFAntennaRegistersBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[35])
        UHFAntennaRegistersBTN.grid(row=10, column=5, pady=8, padx=4, ipady=5, ipadx=20)

        UHFStatusControlWordBTN = Entry(mainFrame, border=1, relief="solid", textvariable=v[36])
        UHFStatusControlWordBTN.grid(row=11, column=5, pady=8, padx=4, ipady=5, ipadx=20)

        # Close Application
        def on_closing():
            master.quit()

        self.protocol("WM_DELETE_WINDOW", on_closing)


# Database Class
class db:
    def __init__(self):

        df = pd.read_csv("config.csv")

        self.mydb = mysql.connector.connect(
            host="localhost",
            user=df.iloc[0][0],
            password=df.iloc[0][1],
            database=df.iloc[0][2]
        )
        self.mycursor = self.mydb.cursor()

    def insert_data(self, listbeacon_list):
        if self.get_file_name(extract_data.file_name):
            for beacon_list in listbeacon_list:
                data_list = beacon_list
                data_list[0] = data_list[0]
                sql = '''INSERT INTO cubesats_table 
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                val = (
                    data_list[0], data_list[1], data_list[2], data_list[3], data_list[4], data_list[5], data_list[6],
                    data_list[7], data_list[8], data_list[9], data_list[10], data_list[11], data_list[12],
                    data_list[13],
                    data_list[14], data_list[15], data_list[16], data_list[17], data_list[18], data_list[19],
                    data_list[20],
                    data_list[21], data_list[22], data_list[23], data_list[24], data_list[25], data_list[26],
                    data_list[27],
                    data_list[28], data_list[29], data_list[30], data_list[31], data_list[32], data_list[33],
                    data_list[34],
                    data_list[35], data_list[36])

                self.mycursor.execute(sql, val)
                self.mydb.commit()
            self.insert_file_name(extract_data.file_name)
            return f"This File Record Saved in Database"
        else:
            return f'This File Record Already Saved in Database'

    def insert_file_name(self, file_name):
        try:
            sql = "INSERT INTO file_info (File_name) VALUES (%s)"

            self.mycursor.execute(sql, (file_name,))
            self.mydb.commit()
            print("file info inseted in db")
            # showinfo(
            #     title='File exist In db',
            #     message="file info inseted in db"
            # )
        except EXCEPTION as error:
            print(f"file already exist ==> {error}")
            # showinfo(
            #     title='File exist In db',
            #     message="file already exist"
            # )

    def get_file_name(self, filename):
        sql = "SELECT * FROM file_info WHERE File_name = %s"
        adr = (filename,)

        self.mycursor.execute(sql, adr)
        myresult = self.mycursor.fetchall()

        if filename in str(myresult):
            return False
        else:
            return True


class Extract_data:
    def __init__(self):
        self.Becon_time_list = []
        self.btn_flag = False
        self.beacon_list = []
        self.list_beacon_list = []
        self.file_name = ''
        self.counter = 0
        self.totalBeacon = 0

    def import_file(self, filename):
        self.counter = 0
        self.file_name = filename
        index_list = []
        self.beacon_list = []
        self.list_beacon_list = []
        with open(filename, 'r') as file:
            lines = file.readlines()

        for index, line in enumerate(lines):
            if 'ConOps magic num ID' in line:
                index_list.append(index)
        self.totalBeacon = len(index_list)
        if len(index_list) > 0:
            float_list = ['EPS I Battery Voltage', 'EPS I Battery Current', 'BCR Voltage', 'BCR Current', 'SOL PAN X V',
                          'SOL PAN X- Current', 'SOL PAN X+ Current', 'SOL PAN Y V', 'SOL PAN Y- Current',
                          'SOL PAN Y+ Current', 'SOL PAN Z V', 'SOL PAN Z- Current', 'SOL PAN Z+ Current',
                          '3.3V Bus Current', '5V Bus Current', 'MCU Temperature', 'Battery Cell 1 Temp',
                          'Battery Cell 2 Temp', 'Battery Cell 3 Temp', 'Battery Cell 4 Temp',
                          'Battpack1 temp sensor 1 max temp', 'Battpack1 temp sensor 1 min temp',
                          'Battery Internal Resistance', 'Battery Ideal Voltage']
            int_list = ['Power ON Cycle Counter', 'Under Voltage Cond Counter', 'Short Circuit Cond Counter',
                        'Over Temp Cond Counter']
            hx_list = ['ConOps magic num ID', 'Input Condition', 'Output Conditions 1', 'Output Conditions 2',
                       'Default Vals LUPs & fastcharge',
                       'Default Vals OUTs 1', 'UHF Status Control Word', 'UHF Antenna Registers']

            for beacon_index in index_list:
                beacon_time = f"{str(self.file_name).split('/')[-1].split(' ')[1].replace('-','/')} {str(lines[beacon_index]).split('>')[0]}"
                self.Becon_time_list.append(beacon_time)
                # key = str(lines[beacon_index]).split('>')[-1].replace('{', '').replace('}', '').split(':')[0].strip()
                value = str(lines[beacon_index]).split('>')[-1].replace('{', '').replace('}', '').split(':')[-1].strip()
                self.beacon_list.append(int(value, 16))
                for i in range(1, 36):
                    key = str(lines[beacon_index + i]).split('>')[-1].replace('{', '').replace('}', '').split(':')[
                        0].strip()
                    value = str(lines[beacon_index + i]).split('>')[-1].replace('{', '').replace('}', '').split(':')[
                        -1].strip()

                    if key in float_list:
                        self.beacon_list.append(float(value.split(' ')[0]))
                    elif key in int_list:
                        self.beacon_list.append(int(value.split(' ')[0]))
                    elif key in hx_list:
                        self.beacon_list.append(int(value.split(' ')[0], 16))
                    else:
                        self.beacon_list.append(value.split(' ')[0])
                self.list_beacon_list.append(self.beacon_list)
                self.beacon_list=[]

            for i in range(1, len(self.Becon_time_list)):
                previous_time = str(self.Becon_time_list[i - 1]).replace('-', '/')
                current_time = str(self.Becon_time_list[i]).replace('-', '/')
                # print(f"previous_time {previous_time} ==> current_time {current_time}")
                try:
                    previous_date_time = datetime.datetime.strptime(previous_time[2:], '%y/%m/%d %H:%M:%S:%f')
                except:
                    previous_date_time = datetime.datetime.strptime(previous_time[2:], '%y/%m/%d %H:%M:%S.%f')
                try:
                    current_date_time = datetime.datetime.strptime(current_time[2:], '%y/%m/%d %H:%M:%S:%f')
                except:
                    current_date_time = datetime.datetime.strptime(current_time[2:], '%y/%m/%d %H:%M:%S.%f')
                a = str(current_date_time - previous_date_time)
                if '-' in a:
                    # print(f'a yes {a}')
                    date_ = str(current_date_time.date() + datetime.timedelta(days=1)).replace('-', '/')
                    for j in range(i, len(self.Becon_time_list)):
                        self.Becon_time_list[j] = f"{date_} {str(self.Becon_time_list[j]).split(' ')[-1]}"

            for beacon_list, Beacon_time in zip(self.list_beacon_list, self.Becon_time_list):
                beacon_list.insert(0,Beacon_time)
            self.btn_flag = True
            return False
        else:
            return True

    def get_data(self):
        if self.counter < len(self.list_beacon_list):
            self.counter = self.counter + 1
            return ['', self.list_beacon_list[self.counter-1]]
        else:
            return ['There are no more Beacons in this file', []]


# Objects
extract_data = Extract_data()

mydb = db()

# Variables
v = []
beaconMessage = ''
my_string_var = StringVar()
name = []
dataList = []
for j in range(0, 37):
    v.append(StringVar())


# Methods
def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '.')
    )
    file_name = fd.askopenfilename(
        title='Open a file',
        initialdir=r'C:\Users\haier\PycharmProjects\Mansoor_FB_project',
        filetypes=filetypes)
    print(file_name)

    return file_name


def importBtn():
    f_name = select_file()
    if f_name != '':
        extract_data.list_beacon_list.clear()
        extract_data.Becon_time_list.clear()
        message = extract_data.import_file(filename=f_name)
        #print(extract_data.list_beacon_list)
        if message:
            showinfo(
                title='Info',
                message=f'There is no Beacon In ({f_name})'
            )
        elif extract_data.btn_flag:
            next_BTN()


def saveBtn():
    if extract_data.btn_flag:
        message = mydb.insert_data(listbeacon_list=extract_data.list_beacon_list)
        showinfo(
            title='Message Box',
            message=message
        )


def next_BTN():
    if extract_data.btn_flag:
        data_dic_list = extract_data.get_data()
        if 'There are no more Beacons in this file' in data_dic_list[0]:
            showinfo(
                title='Info',
                message=data_dic_list[0]
            )
        elif data_dic_list[0] == '':
            data_list = list(data_dic_list[1])
            # data_list.insert(0, data_list[-1])
            if len(data_list) > 0:
                print(f"data_list ==> {data_list}")
                beaconInfo()
                for i, data in enumerate(data_list):
                    v[i].set(data)

def beaconInfo():
    my_string_var.set(f'Beacon No. {extract_data.counter} Out of {extract_data.totalBeacon}')

mainloop()
