from androidhelper import sl4a
import time

dev=sl4a.Adriod()

def speak (text) :
  dev.ttSpeak(text)

def listen () :
  result = dev.recognizeSpeech("speak")
  return result[1]

def evaluate_speak (a) :
  a=a.split("and")
  return a

def print_thing_f (a) :
  print(a)
  if a.split(" ")[0] == "variable" :
    add="""print("""+str(a.split(" ")[1])+""")\n"""
  else :
    add="""print('"""+str(a)+"""')\n"""
  asta=open("my.py","a")
  asta.write(add)
  asta.close()

def print_things (x) :
  add=x.split("print")
  add=add[1:]
  add=" ".join(add)
  print_thing_f(add.strip())

def asine_var_f (dt,vn,vd) :
  if dt=="string" :
    add=str(vn)+' = "'+str(vd)+'"\n'
  elif dt=="integer" :
    add=str(vn)+' = '+str(vd)+'\n'
  asta=open("my.py","a")
  asta.write(str(add))
  asta.close()

def asine_var (x) :
  y=["equals to","equal","equals"]
  add=x.split("let")
  add=" ".join(add)
  for i in y :
    i=add.split(i)
    if len(i)>1 :
      break
  add=i
  for i in range(len(add)) :
    add[i]=add[i].strip()
  var_name=add[0]
  if " ".join(add[1].split(" ")[-3:-1]) == "as a" :
    var_data_type=add[1].split(" ")[-1]
    var_data=add[1].split("as a "+var_data_type)
    var_data=var_data[0].strip()
  else :
    if add[1].isdigit() :
      var_data_type="integer"
    else :
      var_data_type="string"
    var_data=add[1]
  print(var_data_type,var_name,var_data)
  asine_var_f(var_data_type,var_name,var_data)

a=listen()
a=evaluate_speak(a)
for i in a :
  i=i.strip()
  i=i.split(" ")
  if i[0] == "print" :
    print_things (" ".join(i).strip())
  elif i[0]=="let" :
    asine_var(" ".join(i).strip())