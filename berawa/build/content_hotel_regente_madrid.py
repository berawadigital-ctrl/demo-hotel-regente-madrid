# Contenido de la demo Hotel Regente (Madrid) (es/ca/en/fr). Hechos de hotelregente.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Doble Vista Gran Vía','Triple Estándar','Familiar Vista Gran Vía'],'ca':['Doble Vista Gran Vía','Triple Estàndard','Familiar Vista Gran Vía'],'en':['Double Gran Vía View','Standard Triple','Family Gran Vía View'],'fr':['Double vue Gran Vía','Triple standard','Familiale vue Gran Vía']}
RD={
'es':['15 m² para 1 o 2 personas, con baño completo, nevera y Smart TV.','18 m² para un máximo de 3 personas, con sofá cama o cama supletoria.','22 m² para un máximo de 4 personas, exteriores con vistas a la Gran Vía.'],
'ca':['15 m² per a 1 o 2 persones, amb bany complet, nevera i Smart TV.','18 m² per a un màxim de 3 persones, amb sofà llit o llit supletori.','22 m² per a un màxim de 4 persones, exteriors amb vistes a la Gran Vía.'],
'en':['15 m² for 1 or 2 guests, with full bathroom, fridge and Smart TV.','18 m² for up to 3 guests, with a sofa bed or extra bed.','22 m² for up to 4 guests, exterior with views of the Gran Vía.'],
'fr':['15 m² pour 1 ou 2 personnes, avec salle de bain complète, réfrigérateur et Smart TV.','18 m² pour 3 personnes maximum, avec canapé-lit ou lit d\'appoint.','22 m² pour 4 personnes maximum, côté rue avec vue sur la Gran Vía.']}
ART={
'hero':('skyline',2931,['#22324f','#e0905f','#f7d39c','#21304c','#18243a','#0f1828']),
'intro':('columns',2932,['#eef0f3','#f6f3ea','#b8893e','#1f3a5f','#122339']),
'r1':('skyline',2941,['#2f3c5e','#e48a5f','#f9d19b','#2e3b5c','#212c46','#151d30']),
'r2':('arches',2942,['#eef0f2','#c9d3de','#8aa0b8','#1f3a5f','#122339']),
'r3':('columns',2943,['#eceff3','#f5f2ea','#bb8c42','#24426a','#142640']),
'g1':('arches',2951,['#eef1f4','#cdd6e0','#8ea3ba','#1f3a5f','#122339']),
'g2':('skyline',2952,['#3a3150','#e8935f','#fbd9a0','#39304e','#2a243b','#1b1726']),
'g3':('columns',2953,['#eef0f3','#f5f2e9','#c08c40','#28466e','#152842']),
'g4':('hills',2954,['#e6e6d1','#f3e5c3','#f6cf8a','#a9c19e','#80a085','#587767']),
'g5':('arches',2955,['#eceff3','#c8d2dd','#889eb6','#1f3a5f','#122339']),
'g6':('skyline',2956,['#33456a','#e48a5f','#f9d19b','#2f4260','#223249','#16222f'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Regente · Hotel familiar en plena Gran Vía de Madrid',see_rooms='Ver habitaciones',hero_k='Madrid · Gran Vía',hero_t='Despiértate en el corazón de la Gran Vía',hero_s='Hotel familiar con más de 70 años de historia, 140 habitaciones reformadas y espacios 100% accesibles.',
 intro_t='Un hotel familiar con historia',intro_p1='El Hotel Regente está en la calle Mesoneros Romanos 9, en plena Gran Vía, a 4 minutos a pie de la Puerta del Sol.',
 intro_p2='Empezó con 80 habitaciones y un pequeño bar; hoy tiene 140 habitaciones, habitaciones familiares y comunicadas, gimnasio, sala de reuniones, cafetería y desayuno buffet. Es bike friendly.',
 stats=['140 habitaciones','Más de 70 años','100% accesible','Bike friendly'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Tres de los tipos de habitación del hotel.',
 svcs=['Desayuno buffet de 07:30 a 11:30 h','Bar/cafetería de 10.30 a 23.00 h','Gimnasio gratuito con reserva previa','Sala de reuniones Salón Gran Via','Consigna de maletas gratuita','Habitaciones familiares y comunicadas','4 habitaciones adaptadas','Espacio seguro para bicicletas'],
 loc_p='C/ Mesoneros Romanos, 9 – 28013 Madrid. A 4 minutos a pie de la Puerta del Sol y a 11 minutos del Palacio Real.',
 chips=['¿Qué habitaciones tiene?','¿Hay parking?','¿Dónde está?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Regente · Hotel familiar en plena Gran Vía de Madrid',see_rooms='Veure habitacions',hero_k='Madrid · Gran Vía',hero_t='Desperta\'t al cor de la Gran Vía',hero_s='Hotel familiar amb més de 70 anys d\'història, 140 habitacions reformades i espais 100% accessibles.',
 intro_t='Un hotel familiar amb història',intro_p1='L\'Hotel Regente és al carrer Mesoneros Romanos 9, en plena Gran Vía, a 4 minuts a peu de la Puerta del Sol.',
 intro_p2='Va començar amb 80 habitacions i un petit bar; avui té 140 habitacions, habitacions familiars i comunicades, gimnàs, sala de reunions, cafeteria i esmorzar bufet. És bike friendly.',
 stats=['140 habitacions','Més de 70 anys','100% accessible','Bike friendly'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Tres dels tipus d\'habitació de l\'hotel.',
 svcs=['Esmorzar bufet de 07:30 a 11:30 h','Bar/cafeteria de 10.30 a 23.00 h','Gimnàs gratuït amb reserva prèvia','Sala de reunions Salón Gran Via','Consigna d\'equipatge gratuïta','Habitacions familiars i comunicades','4 habitacions adaptades','Espai segur per a bicicletes'],
 loc_p='C/ Mesoneros Romanos, 9 – 28013 Madrid. A 4 minuts a peu de la Puerta del Sol i a 11 minuts del Palau Reial.',
 chips=['Quines habitacions té?','Hi ha pàrquing?','On és?','Com es reserva?']),
'en':dict(title='Hotel Regente · Family-run hotel right on Madrid\'s Gran Vía',see_rooms='See the rooms',hero_k='Madrid · Gran Vía',hero_t='Wake up in the heart of the Gran Vía',hero_s='A family-run hotel with over 70 years of history, 140 renovated rooms and 100% accessible spaces.',
 intro_t='A family hotel with history',intro_p1='Hotel Regente is at Calle Mesoneros Romanos 9, right on the Gran Vía, 4 minutes\' walk from Puerta del Sol.',
 intro_p2='It started with 80 rooms and a small bar; today it has 140 rooms, family and connecting rooms, a gym, a meeting room, a café and a buffet breakfast. It is bike friendly.',
 stats=['140 rooms','Over 70 years','100% accessible','Bike friendly'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Three of the hotel\'s room types.',
 svcs=['Buffet breakfast from 07:30 to 11:30','Bar/café from 10.30 to 23.00','Free gym, booking required','Salón Gran Via meeting room','Free luggage storage','Family and connecting rooms','4 adapted rooms','Secure bicycle storage'],
 loc_p='C/ Mesoneros Romanos, 9 – 28013 Madrid. 4 minutes\' walk from Puerta del Sol and 11 minutes from the Royal Palace.',
 chips=['What rooms does it have?','Is there parking?','Where is it?','How do I book?']),
'fr':dict(title='Hotel Regente · Hôtel familial en pleine Gran Vía de Madrid',see_rooms='Voir les chambres',hero_k='Madrid · Gran Vía',hero_t='Réveillez-vous au cœur de la Gran Vía',hero_s='Hôtel familial de plus de 70 ans d\'histoire, 140 chambres rénovées et des espaces 100% accessibles.',
 intro_t='Un hôtel familial chargé d\'histoire',intro_p1='L\'Hotel Regente se trouve au 9 calle Mesoneros Romanos, en pleine Gran Vía, à 4 minutes à pied de la Puerta del Sol.',
 intro_p2='Il a commencé avec 80 chambres et un petit bar ; il compte aujourd\'hui 140 chambres, des chambres familiales et communicantes, une salle de sport, une salle de réunion, une cafétéria et un petit-déjeuner buffet. Il est bike friendly.',
 stats=['140 chambres','Plus de 70 ans','100% accessible','Bike friendly'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Trois des types de chambre de l\'hôtel.',
 svcs=['Petit-déjeuner buffet de 07:30 à 11:30','Bar/cafétéria de 10.30 à 23.00','Salle de sport gratuite sur réservation','Salle de réunion Salón Gran Via','Consigne à bagages gratuite','Chambres familiales et communicantes','4 chambres adaptées','Local sécurisé pour vélos'],
 loc_p='C/ Mesoneros Romanos, 9 – 28013 Madrid. À 4 minutes à pied de la Puerta del Sol et à 11 minutes du Palais royal.',
 chips=['Quelles chambres a-t-il ?','Y a-t-il un parking ?','Où est-il ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='mail',email='reservas@hotelregente.com')
D=dict(name='Hotel Regente',ac='#1f3a5f',ac2='#b8893e',ac2_a11y='#7a5410',book=BOOK,around=[],foot=FOOT,
 address='C/ Mesoneros Romanos, 9 · 28013 Madrid',phones=['915 21 29 41'],emails=['reservas@hotelregente.com'],maps='Hotel Regente, Mesonero Romanos 9, Madrid',t=T)
META=dict(repo='demo-hotel-regente-madrid',name='Hotel Regente',legal_name='Canor S.L.',registry_ids=['CIF B-46111126'],
 url='https://www.hotelregente.com/',domain='hotelregente.com',municipality='Madrid',province='Madrid',sector='hotel familiar en la Gran Vía',
 read_at='2026-10-29T08:00:00+01:00',created_at='2026-10-29T08:10:00+01:00',built_at='2026-10-29T08:10:00+01:00',audit_date='2026-10-29T07:42:00+01:00',
 rating=dict(value=4.2,coincide=['telefono','web'],date='2026-10-29T06:51:04+01:00',url='https://www.google.com/maps/place/Hotel+Regente+Madrid/@40.4197096,-3.7043006,17z/data=!3m1!5s0xd42287dbc952d0d:0xf7cdfddf529fd16b!4m9!3m8!1s0xd42287dbd5d8a4d:0xf4a33ea4d6d7dab!5m2!4m1!1i2!8m2!3d40.4197096!4d-3.7043006!16s%2Fg%2F1tdqjsq0'),
 book=dict(mode='mail',email='reservas@hotelregente.com',note='La web del negocio reserva con un buscador de Mirai cargado por JavaScript sin URL publica estable (sin idtokenprovider no hay enlace directo y ese parametro contiene la palabra token, que el control S10 no admite); la demo usa el correo de reservas publicado y el telefono.'),
 first_of_type='no aplica: hotel con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tiene?','K01'),('¿Qué equipamiento tienen las habitaciones?','K02'),('¿Hay desayuno?','K03'),('¿Hay parking?','K04'),('¿Tienen salones para reuniones?','K05'),('¿Hay gimnasio?','K06'),('¿Dónde está el hotel?','K07'),('¿Es accesible para silla de ruedas?','K08'),('¿Admiten mascotas?','K09'),('¿Cómo reservo?','K10'),('¿Cuál es el teléfono?','K11'),('¿Quién es el titular?','K12'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K10'),('¿Tienen spa?',None),('¿Hay piscina?',None)],
'ca':[('Quines habitacions té?','K01'),('Quin equipament tenen les habitacions?','K02'),('Hi ha esmorzar?','K03'),('Hi ha pàrquing?','K04'),('Teniu salons per a reunions?','K05'),('Hi ha gimnàs?','K06'),('On és l\'hotel?','K07'),('És accessible amb cadira de rodes?','K08'),('Admeteu mascotes?','K09'),('Com reservo?','K10'),('Quin és el telèfon?','K11'),('Qui és el titular?','K12'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K10'),('Teniu spa?',None),('Hi ha piscina?',None)],
'en':[('What rooms does it have?','K01'),('What equipment do the rooms have?','K02'),('Is there breakfast?','K03'),('Is there parking?','K04'),('Do you have meeting rooms?','K05'),('Is there a gym?','K06'),('Where is the hotel?','K07'),('Is it wheelchair accessible?','K08'),('Are pets allowed?','K09'),('How do I book?','K10'),('What is the phone number?','K11'),('Who is the owner?','K12'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K10'),('Do you have a spa?',None),('Is there a swimming pool?',None)],
'fr':[('Quelles chambres a-t-il ?','K01'),('Quel équipement ont les chambres ?','K02'),('Y a-t-il un petit-déjeuner ?','K03'),('Y a-t-il un parking ?','K04'),('Avez-vous des salles de réunion ?','K05'),('Y a-t-il une salle de sport ?','K06'),('Où est l\'hôtel ?','K07'),('Est-il accessible en fauteuil roulant ?','K08'),('Les animaux sont-ils admis ?','K09'),('Comment réserver ?','K10'),('Quel est le téléphone ?','K11'),('Qui est le titulaire ?','K12'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K10'),('Avez-vous un spa ?',None),('Y a-t-il une piscine ?',None)]}
