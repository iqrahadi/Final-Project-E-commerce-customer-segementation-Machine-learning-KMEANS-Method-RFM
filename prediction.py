import pickle
from pandas import DataFrame

model = pickle.load(open('finalized_model_iqra.sav','rb'))
scaler = pickle.load(open('standar_scaler.sav','rb'))


def prediction(data):
    df = DataFrame(data,index=[0]) #data ini berasal inputan prediction html
    df = scaler.transform(df) #proses merubah data itu dilakukan di sini (transform)

    #melakukan labelling
    hasil = model.predict(df)
    if hasil == 0 :
        return "RECENT AVARAGE MATE"
    elif hasil == 1 :
        return "EX MATE"
    elif hasil == 2 :
        return "CASUAL AVARAGE MATE"
    else:
        return "SOUL MATE"
    
