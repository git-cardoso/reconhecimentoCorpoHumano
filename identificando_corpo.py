import cv2

def reconhecendo_corpo(foto):
    imagem =cv2.imread(foto)
    corpo =  cv2.CascadeClassifier('haarcascade_fullbody.xml')
    cor_padrao = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    decta =   corpo.detectMultiScale(cor_padrao, scaleFactor=1.1, minSize=(50,50))
    print("Encontrei %i pessoas"%len(decta))
    for (x, y, l, a) in decta:
          cv2.rectangle(imagem, (x, y), (x + l, y + a), (0,255,0), 2)
    cv2.imshow('image',imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




reconhecendo_corpo('casos.png')
