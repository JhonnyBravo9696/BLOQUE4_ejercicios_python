dic1 = {}
nota = []
while True:
  alumno = input("añade a un alumno: ")
  nota = int(input("introduce la nota del alumno: "))
  if nota < 0:
    print("nota no valida")
    break
    
  dic1[alumno] = nota

print ("notas alumnos")
print ("--------------")
print (dic1)
