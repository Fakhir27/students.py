student=[]
student_1={"name":"Ali","class1":{
                                    "name":"AI","marks":
                                                    {"quiz1":72,"quiz2":60,"mid":84,"final":87}},
                                    "class2":{"name":"cnn","marks":
                                                              {"quiz1":63,"quiz2":88,"mid":94,"final":73}}}

student_2={"name":"Ahmed","class1":{
                                    "name":"AI","marks":
                                                    {"quiz1":83,"quiz2":67,"mid":80,"final":77}},
                                    "class2":{"name":"cnn","marks":
                                                              {"quiz1":74,"quiz2":85,"mid":69,"final":92}}}

student_3={"name":"Taha","class1":{
                                    "name":"AI","marks":
                                                    {"quiz1":55,"quiz2":85,"mid":91,"final":54}},
                                    "class2":{"name":"cnn","marks":
                                                              {"quiz1":67,"quiz2":93,"mid":88,"final":46}}}

student_4={"name":"Huziafa","class1":{
                                    "name":"AI","marks":
                                                    {"quiz1":51,"quiz2":63,"mid":69,"final":87}},
                                    "class2":{"name":"cnn","marks":
                                                              {"quiz1":76,"quiz2":74,"mid":65,"final":70}}}

student_5={"name":"Anas","class1":{
                                    "name":"AI","marks":
                                                    {"quiz1":44,"quiz2":37,"mid":70,"final":95}},
                                    "class2":{"name":"cnn","marks":
                                                              {"quiz1":79,"quiz2":85,"mid":80,"final":44}}}

student_6={"name":"Saad","class1":{
                                    "name":"AI","marks":
                                                    {"quiz1":83,"quiz2":65,"mid":70,"final":90}},
                                    "class2":{"name":"cnn","marks":
                                                              {"quiz1":35,"quiz2":75,"mid":80,"final":56}}}


student_7={"name":"Zain","class1":{
                                    "name":"AI","marks":
                                                    {"quiz1":65,"quiz2":43,"mid":72,"final":59}},
                                    "class2":{"name":"cnn","marks":
                                                              {"quiz1":15,"quiz2":38,"mid":30,"final":77}}}

student_8={"name":"Rehan","class1":{
                                    "name":"AI","marks":
                                                    {"quiz1":27,"quiz2":76,"mid":77,"final":90}},
                            "class2":{"name":"cnn","marks":
                                                              {"quiz1":52,"quiz2":93,"mid":67,"final":46}}}
                                              
                                    
        
student_9={"name":"Shahmeer","class1":{
                                    "name":"AI","marks":
                                                    {"quiz1":67,"quiz2":75,"mid":46,"final":95}},
                                    "class2":{"name":"cnn","marks":
                                                              {"quiz1":68,"quiz2":56,"mid":79,"final":80}}}

student_10={"name":"Yahya","class1":{
                                    "name":"AI","marks":
                                                    {"quiz1":45,"quiz2":89,"mid":57,"final":93}},
                            "class2":{"name":"cnn","marks":
                                                              {"quiz1":56,"quiz2":87,"mid":82,"final":90}}}


student.append(student_1)
student.append(student_2)
student.append(student_3)
student.append(student_4)
student.append(student_5)
student.append(student_6)
student.append(student_7)
student.append(student_8)
student.append(student_9)
student.append(student_10)
id_no=int(input("Enter id:\n"))-1
class_name=input("Enter Class (AI OR CNN):\n").lower()
while((class_name!="ai")and(class_name!="cnn")):
  class_name=input("Enter Class (AI OR CNN):\n").lower()
exam=input("Enter Exam:\n").lower()
if (class_name=="ai"):
    print(student[id_no].get("class1").get("marks").get(exam))
if (class_name=="cnn"):
    print(student[id_no].get("class2").get("marks").get(exam))
