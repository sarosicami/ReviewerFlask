from app import db, models
import datetime

# product1 = models.Product(brand='Lenovo', product_model='IdeaPad 100-15', model_number = '80QQ005CRI',
#                           processor = 'Intel Core i3 - 5005U 2000 MHz Broadwell', display = 15.6, RAM_memory = '4 GB DDR3' ,
#                           memory_speed = 1600 , hard_drive = 500, video_card = 'Intel HD Graphics',
#                           card_description = 'Integrated', battery_life = 3, item_weight = 2.3,
#                           housing_material = 'plastic', color = 'black', operating_system = 'Free DOS')
# db.session.add(product1)
# db.session.commit()
#
# product2 = models.Product(brand='Lenovo', product_model='IdeaPad G50-80', model_number = '80L000C2RI',
#                           processor = 'Intel Core i3 - 4005U 1700 MHz Haswell', display = 15.6, RAM_memory = '4 GB DDR3' ,
#                           memory_speed = 1600 , hard_drive = 1000, video_card = 'Radeon R5 M330',
#                           card_description = 'Dedicated', battery_life = 4, item_weight = 2.5,
#                           housing_material = 'plastic', color = 'black', operating_system = 'Free DOS')
# db.session.add(product2)
# db.session.commit()
#
# product3 = models.Product(brand='Lenovo', product_model='IdeaPad G50-45', model_number = '80E301G0RI',
#                           processor = 'AMD Quad-Core A6-6310 1800 MHz', display = 15.6, RAM_memory = '4 GB DDR3' ,
#                           memory_speed = 1600 , hard_drive = 1000, video_card = 'Radeon R5 M330',
#                           card_description = 'Dedicated', battery_life = -1, item_weight = 2.1,
#                           housing_material = 'plastic', color = 'black', operating_system = 'Free DOS')
# db.session.add(product3)
# db.session.commit()

# p = models.Product.query.get(1)
# r = models.Review(body='Mai sunt dezavantaje: bateria este incorporata, procesorul lipit pe placa. Avantaje: procesorul destul de bun, la fel si video.', timestamp=datetime.datetime.utcnow(), product_ref=p)
# db.session.add(r)
# r = models.Review(body="""Este un laptop bun la pretul de 1149 ron(black friday), am instalat pe el windows 10 home 32 bit si merge bine!
# Pro: -autonomie mare 4ore si 30 min in modul battery saver si contrast 50%, procesor bun, destul de compact si usor.
# Contra: -butonul de power este pozitionat aiurea in partea stanga lateral jos;
# -doar doua sloturi usb(3. 0+2. 0)care sunt foarte apropiate intre ele si fata de jackul audio
# -speakerul este o rusine(calitate si volum)
# -ruleaza filme fara intreruperi full hd de dimensiuni mari(10-15 gb)""", timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body="""PRO: instalarea a decurs foarte rapid, recomandabil W10 x64, autonomie baterie 3h, driverele se instaleaza complet din update-ul windows-ului
# Contra: buton power pozitionat in partea stanga si foarte mic(parca ar fi tableta), portul de USB 3. 0 prioritar pentru periferice(imprimante, scanere, etc), TASTATURA UK!!!!!
# P. S. Pentru pretul de vanzare este o alegere buna daca se foloseste pentru office si low usage acasa.
# Ma bucur pentru alegere Emag-ului de a schimba curierul cu cei de la DPD, astfel in 48H am primit comanda la usa, nu ca la FAN curier sa fac politie coletareasca dupa aproape o saptamana.""", timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body='Pentru ofice-gaming e perfect', timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body='Sunt multumit de el', timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
#
# p = models.Product.query.get(2)
# r = models.Review(body='Merge gta5 decent', timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body="""Configuratie buna pentru acest pret. Un procesor care se misca acceptabil.
# Placa grafica dedicata de 2g f. Buna pentru pretul acesta. La capitolul aspect, pot spune ca plasticul de calitate
# destul de proasta. O problema care a mai sesizat-o un cumparator, este faptul ca displayul nu se poate rabata f.
# Mult pe spate ceea ce iti creaza un disconfort vizavi de modul in care il poti tine in exploatare.
# Am mai sesizat unele probleme la touch pad uneori nu ia comanda sau alteori raspunde de mai multe ori tu atingand
# touchpadul doar odata ( o chestie destul de enervanta). Una peste alta e ok, pentru banii astia.
# La instalare windows drivere etc totul a mers perfect, deci nimic de zis vizavi de asta. Cu tote astea am horarat
# sa il returnez optand pentru Asus X540L care vine zilele astea la acelasi pret, deci ramane de vazut daca am luat
# o hotarare buna (configuratie sensibil asemanatoare). I-am dat 3 stele dar cred ca ar fi undeva pe la 3. 5 stele.
# """, timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body="""Un laptop foarte bun la banii astia care face fata cu brio atat in aplicatii cat si la
#  jocuri video dar eu nu-l folosesc ptr jocuri doar ptr navigare pe internet. Ii dau 4 stele din 5 deoarece are
#   carcasa din plastic.""", timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body="""Totul din plastic.
# nu face fata la putere maxima""", timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body='Autonomie de lucru pana la 3 ore maxim!', timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body="""Salut,
# Eu folosesc acest model de aproximativ 1 luna, l-am achizitionat de black friday la un pret rezonabil 1399 lei. Tinand cont de configuratia produsului eu zic ca e un pret mai mult decat rezonabil. Daca te uiti la partea practica atunci nu ai ce comenta, intr-adevar totul este din plastic, ai impresia ca e firav, ca e ieftin facut la norma, dar iti faci treaba si chiar foarte bine cu el.
# daca iti doresti o experienta mai placuta, atunci mai scoate ceva din buzunar, din punctul meu de vedere nu este cel mai reusit laptop dvd estetic, user friendly, BIOS -ul la Lenovo e traficul in UK pe dos dar pana la urma te obisnuiesti.
# Autonomia bateriei este undeva la 3 ore, iar eu il folosesc pentru browsing, torente, pachetul office si cam atat fara jocuri, editari foto-video, iar pentru ce il folosesc e mai mult decat OK.
# """, timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body="""L am cumparat de cateva zile L am luat cu 1500 lei si i am mai pus inca 2 ani garantie. Pentru filme, muzica si browsing e excelent. Imi place ca are bluetooth
#  si pot conecta receiverul la el. Daca vreti un laptop bun dar nu pentru jocuri eu zic ca merita sa il luati.""", timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body="""L-am achizitionat pt filme si browsing in urma cu o saptamana, l-am prins la reducere - 1500ron; per total sunt f multumita de el, chiar daca carcasa din plastic e ciudatica. Isi merita banutii:)
# Ca intotdeauna, cei de la E-mag sunt foarte buni pe ceea ce fac, serviabili, vorbesc frumos. Bravo E-mag!""", timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body="""Este destul de bun, deși are câteva minusuri:
# -aș fi vrut un buton mecanic pentru activarea/dezactivarea wifi-ului
# -keypad-ul nu are funcția de scroll
# -usb-ul este situat prost în partea dreaptă (chiar lângă unitatea optică)
# Per total însă sunt mulțumit este destul silențios, placa video își face treaba procesorul la fel, rulează bine windows 10, bateria este încă în testare sunetul are o calitate bună, la cât de mare pare el display-ul este cam mic însă pentru mine este ok.
#  Raportul calitate preț este ok""", timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body="""- Autonomie de lucru de maxim 2, 5h
# - Se misca greu
# - Sta prost la capitolul usb-uri (se tot conecteaza si deconecteaza device-ul)
# - Ecranul este limitat in a se lasa pe spate si nu iti confera o pozitie buna de lucru (nu il poti inclina pe spate atat cat simti nevoia)""", timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body="""Din plastic dar foarte bine inchegat
# Plastic subtire (ai senzatia ca se rupe la o manevrare brusca) tastatura lasa de dorit. Performante bune
# """, timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body="""Acum toate sunt făcute la normă cum sa r zice. Nu se fac cum trebuie.""", timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body="""Am optat pentru acest laptop pentru ca are placa video dedicata, il am de o saptamana si pana acum sunt multumit.""", timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body="""Bateria Poate Dura Până La 4 Ore! Merg Jocuri Foarte Bine La Fel Si Alte Aplicatii! Merita Cumpărat!""", timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body="""Un laptop foarte bun avand in vedere pretul. Detine caracteristici acceptabile ptr 1. 600 lei.
# Pe mine personal nu ma deranjează faptul ca este din plastic. O sa il testeze si in gaming dar doar dupa
#  achizitionarea unui cooler care sa ofere o temperatura optimă.""", timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body='Se misca bine, numai bun pt ceea ce imi trebuie, dar calitatea materialului lasa un pic de dorit.', timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body="""Se misca excelent, merg chiar si ubnele jocuri (mafia 2, eurotruck 2,...), placa video de 2 gb 4gb ram i3 super multumit... Raport calitate pret...""", timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body='Functioneaza perfect', timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body="""Este un laptop bun pentru cei care nu au foarte multe de făcut pe el. Merge super şi pentru jocuri. Eu l-am schimbat odată pentru
# că îmi arăta o eroare la baterie. La 60% nu se mai încărca. Dar şi pe aceea au rezolvat-o cei de la service deci nu e nimic foarte grav. Se mişcă foarte bine şi nu se încălezeşte foarte tare.""", timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body="""Raport calitate/pret foarte bun.""", timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body="""Din punctul meu de vedere zic ca isi face banii si merita cumpărat... Pot spune ca pe placa video duc aproape orice joc mai recent....
# Procesorul se misca repede.""", timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body="""Este un
# laptop foarte bun!!!...""", timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body='Merge perfect..', timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
# r = models.Review(body="""Raportul calitate-pret e ok.
# Daca stii sa il configurezi cum trebuie, merge brici, atat pentru jocuri cat si pentru multimedia.
# Am acest model de vreo 2 saptamani si sunt multumit de el. E silentios, nu se incalzeste deloc (folosesc cooling pad).
# Nu recomand cu Win7, e cam greu cu driverele.
# RECOMAND!""", timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)
#
# p = models.Product.query.get(3)
# r = models.Review(body="""Acest laptop dupa ce l-am comandat si am instalat windows 8. 1 pro si toate driverele necesare am facut testele in materie de viteza de procesare, rapiditate in materie de aplicatii si jocuri care ruleaza foarte bine pot sa spun ca sunt foarte multumit de acest laptop il recomand sa-l cumparati e foarte bun!""", timestamp=datetime.datetime.utcnow(), product_ref = p)
# db.session.add(r)

products = models.Product.query.all()
print(products)
for p in products:
    # db.session.delete(p)
    print(p.id,p.product_model)
# db.session.commit()

p = models.Product.query.get(2)
reviews = p.reviews.all()
print(reviews)