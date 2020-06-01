from flask import Flask, render_template, request
from cleaning_data import data_retail,data_retail2,data_retail3
from prediction import prediction
from plots import pairplot, distribution_r, distribution_f, distribution_m

# variable app untuk akses ke Flask
app = Flask(__name__)

# melakukan prediksi 
@app.route('/', methods=['GET','POST']) #ini buat nyambungin halaman prediksi dengan variabel yang akan di masukan, dengan metode get post
def index_prediction():
    if request.method == 'POST':
        data = request.form #untuk nginput data pake format ini
        data = data.to_dict() #rubah semua data ke kolom
        data['Recency'] = int(data['Recency']) #untuk masukin variabel
        data['Frequency'] = int(data['Frequency']) #untuk masukin variabel
        data['Monetary'] = int(data['Monetary']) #untuk masukin variabel
        hasil = prediction(data) #buat ngeluarin hasil prediksi
        
        return render_template('result.html', hasil_prediction=hasil) #buat ngeluarin hasil prediksi #liat ada htmlnya

    return render_template('prediction.html') #buat return hasil prediksi, liat ada tulisan html, perhatiin halaman prediction html ada tulisanya harus sama!

#keterangan
@app.route('/about')
def about():
    return render_template('about.html')

#manggil data frame
@app.route('/data')
def data():
    data = data_retail()
    data2 = data_retail2()
    data3 = data_retail3()
    return render_template('tabel_data.html', data=data, data2=data2,data3=data3)
#memunculkan plot
@app.route('/plots')
def plots():
    data= pairplot()
    data2 = distribution_r()
    data3 = distribution_f()
    data4 = distribution_m()
    return render_template('plots.html',data=data,data2=data2,data3=data3,data4=data4) # data2=data2

# proses running dari html 
if __name__ == '__main__':
    app.run(debug=True,port=2001)