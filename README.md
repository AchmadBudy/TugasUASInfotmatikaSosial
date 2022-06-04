# TugasUASInfotmatikaSosial
Nama Pembuat
- Nama  : Nur Achmad Budy Kurniawan.
- NIM   : 1914311005

Requirement:
```
$ pip install selenium
$ pip install scrapy
$ pip install scrapy-selenium

Chrome Web versi 102

Jika versi chrome diatas itu atau dibawahnya harap download driver chrome dan taruh di 'tugas2/' 
replace atau ganti chromedriver.exe yang ada didalam sana
```

How to run? 
```
$ git clone https://github.com/AchmadBudy/TugasUASInfotmatikaSosial.git
$ cd TugasUASInfotmatikaSosial
```

## How to run Specific Tugas?

### Tugas1
Sebelum nya harap diganti user dan pass di `dataakun` pada `tugas1\tugas1\spiders\absenSpider.py` menjadi akun SIM.UBHARA.AC.ID milik anda sendiri. dan pastikan password sudah di hash.
```
$ cd tugas1
$ scrapy crawl absen -O [namafile].json
```
Perintah diatas akan menghasilkan data absen pada waktu run

### Tugas2
Pada tugas 2 sangat disayangkan bahwa saat ini saya belum mengetahui untuk perintah scroll down on element / send key on elemnt di scrapy yang mengakibatkan crawl ini hanya menghasilkan hasil direview di front page first render.
```
$ cd tugas2
$ scrapy crawl ngambilreview -O [namafile].csv
```
Perintah diatas akan menghasilkan data review pada ubhara dalam csv.

### Tugas3
Pada tugas 3 lagi lagi karena perintah tugas menggunakan API standard Twitter maka dengan keterbatasan akun yang dimiliki juga mengakibatkan hasil dari search tidak menampilan semua yang ditemukan.
```
$ cd tugas3
$ scrapy crawl twittersearch -O [namafile].csv
```
Perintah diatas akan menghasilkan data hasil search twitter dalam csv.
