serie = []
serieFibo = []
for i in range(15):
    serie.append(i)

for a in range(15):
    suma = int(serie[a]) + int(serie[a-1])
    serieFibo.append(suma)

   
print("1 ,",serieFibo[0],",",serieFibo[1],",",serieFibo[2],",",serieFibo[3],",",serieFibo[4],",",serieFibo[5],",",
      serieFibo[6],",",serieFibo[7],",",serieFibo[8],",",serieFibo[9],",",
      serieFibo[10],",",serieFibo[11],",",serieFibo[12],",",serieFibo[13],",",serieFibo[14])   
  