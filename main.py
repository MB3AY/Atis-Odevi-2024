import random
import math
import numpy as np
import plotly.graph_objects as go
#"plotly.graph_objects" bu kütüphaneyi buldum ve tabloda bunu kullandım.

son_iki_h = input("Okul numaranızın son iki hanesini giriniz: ")

if son_iki_h.isdigit():
    son_iki = int(son_iki_h)
else:
    print("Lütfen sadece sayısal değerler giriniz.")

aci = math.radians(30)
g = 9.81
top_konum = [0, son_iki]

uzaklik_mesafesi = 20000 + 200 * random.randint(-10, 10)
genislik_baslangic = uzaklik_mesafesi
genislik_bitis = uzaklik_mesafesi + 1000 + 100 * random.randint(-2, 2)

def atis_simulasyonu(hiz_alt_siniri, hiz_ust_siniri):
    atis_sayisi = 0
    while True:
        atis_sayisi += 1
        hiz = (hiz_alt_siniri + hiz_ust_siniri) / 2
        ucus_suresi = (2 * hiz * math.sin(aci)) / g
        menzil = hiz * math.cos(aci) * ucus_suresi
        dusme_noktasi = top_konum[0] + menzil

        if dusme_noktasi < genislik_baslangic:
            mesafe_farki = genislik_baslangic - dusme_noktasi
            print(f"{atis_sayisi}. Atış: |Önüne düştü.   Az Kaldı Ha Gayret.|  |Hız: {hiz:.2f} m/s")
            hiz_alt_siniri = hiz
        elif dusme_noktasi > genislik_bitis:
            mesafe_farki = dusme_noktasi - genislik_bitis
            print(f"{atis_sayisi}. Atış: |Uzağına düştü. Tekrar Deniyoruz.  |  |Hız: {hiz:.2f} m/s")
            hiz_ust_siniri = hiz
        else:
            mesafe_farki = 0
            print(f"{atis_sayisi}. Atış: |        !!!Tam İsabet!!!          |  |Hız: {hiz:.2f} m/s")

            t = np.linspace(0, ucus_suresi, num=300)
            x = hiz * np.cos(aci) * t
            y = hiz * np.sin(aci) * t - (0.5 * g * t ** 2)

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Atış Yolu'))
            fig.add_shape(type="rect", x0=genislik_baslangic, y0=0, x1=genislik_bitis, y1=50, fillcolor="olivedrab", opacity=0.5, line=dict(color="rgba(0,0,0,0)"))
            fig.update_layout(title='Top Mermisi Atış Grafiği', xaxis_title='Mesafe (metre)', yaxis_title='Yükseklik (metre)', showlegend=True)
            fig.show()
            break

hiz_alt_siniri = 330
hiz_ust_siniri = 1800

atis_simulasyonu(hiz_alt_siniri, hiz_ust_siniri)


