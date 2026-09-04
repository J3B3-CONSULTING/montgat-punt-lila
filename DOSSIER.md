# MONTGAT PUNT LILA
## Eina de formació, test d'aprofitament i acreditació de la Xarxa de Comerços Punt Lila

J3B3 Consulting · agost de 2026

---

## 1. Encàrrec

L'Ajuntament de Montgat vol reproduir, per a l'acreditació **Punt Lila**, el model que ja funciona
amb el segell de qualitat del comerç: que els comerços, després de veure els vídeos formatius,
puguin fer un test que es corregeixi sol i descarregar-se l'**acreditació de Punt Lila** i un
**certificat de formació**.

El contingut del test ve donat: document **06 · Fase 4 · Avaluació**, amb 12 preguntes, el
solucionari amb el mòdul de referència de cadascuna i el criteri d'acreditació.

## 2. Solució

Una eina autònoma en un sol fitxer HTML que cobreix el circuit sencer: identificació del comerç,
control dels cinc mòduls formatius, test, correcció automàtica amb retroacció, veredicte i emissió
dels documents. No necessita internet, ni instal·lació, ni servidor. Funciona en ordinador,
tauleta i mòbil.

Parteix de l'eina del segell de qualitat
(`PROJECTES\2026\MONTGAT\MONTGAT_EINA\Inspeccio_segell_Montgat.html`, versió de 22/7/2026), de la
qual reaprofita l'arquitectura: generació de documents Word i PDF sense cap llibreria externa,
distintius i diplomes en format vectorial amb els logotips incrustats, i registre local amb
exportació a full de càlcul. Canvia la lògica, que passa de checklist d'inspector a test
autocorrectiu del comerç, i la paleta, que passa a lila.

## 3. Contingut de la carpeta

| Fitxer | Què és | Per a qui |
|---|---|---|
| `Test_Punt_Lila_Montgat.html` | L'eina | Comerços i Ajuntament |
| `Montgat_Punt_Lila_eina_per_provar.zip` | L'eina i les instruccions, a punt d'enviar | Tècnica municipal |
| `COM PROVAR-LA.md` | Instruccions de prova i punts on demanem opinió | Tècnica municipal |
| `README.md` | Documentació tècnica: configuració, regeneració, decisions | J3B3 |
| `DOSSIER.md` | Aquest document | J3B3 i Ajuntament |
| `FONTS\06_test_aprofitament.docx` | Document d'origen del test | — |
| `_build\` | Plantilla editable, logotips i script de muntatge | J3B3 |

## 4. Com funciona

**Per al comerç.** Omple les dades de la persona i de l'establiment i marca els cinc mòduls un cop
vistos els vídeos: fins llavors el test no s'activa. Respon les 12 preguntes (8 d'opció múltiple i
4 de vertader o fals) i prem "Corregir el test".

**La correcció** és immediata. Cada pregunta queda marcada com a correcta o incorrecta, amb la
resposta bona i una explicació del perquè, i el resultat es desglossa per mòdul, de manera que el
comerç sap exactament què ha de repassar.

**El veredicte** segueix el criteri del document 06: nou encerts o més sobre dotze, el 75 %, dona
**APTE**. Per sota, es diu quins mòduls cal repassar i s'ofereix repetir el test, amb **intents
il·limitats**, perquè és un test d'aprofitament i no selectiu.

**En superar-lo** s'activen les descàrregues:

- **Adhesiu Punt Lila** per a l'aparador, en PNG i en vectorial.
- **Diploma d'acreditació** personalitzat en A4, amb el nom del comerç, la data, la validesa i un
  codi d'acreditació amb el format `PL-MGT-AAAAMMDD-XXXX`. En PNG, vectorial i PDF.
- **Certificat de formació** en Word i en PDF, amb la persona, l'establiment, el contingut dels
  cinc mòduls, el resultat pregunta a pregunta i espai per a la signatura i el segell municipal.

**Per a l'Ajuntament.** En corregir el test, l'eina el desa sola al registre del dispositiu i el
manté consultable des de la mateixa pantalla: taula de tots els tests amb nota i resultat, reemissió de l'acreditació i del certificat
de qualsevol registre, exportació a full de càlcul i còpia de seguretat. Inclou també l'exportació
del qüestionari amb el solucionari en CSV, pensada per carregar el test a una plataforma externa
amb correcció automàtica, tal com preveu el document 06.

## 5. Decisions preses

**L'ordre de les respostes es barreja a cada intent.** Al solucionari original, la resposta
correcta és la B en set de les vuit preguntes d'opció múltiple (només la 5 és la C). Sense
corregir-ho, el test es pot superar memoritzant la lletra. La barreja resol el problema sense tocar
el contingut aprovat.

**El control dels mòduls és previ al test.** El test no s'activa fins que els cinc mòduls estan
marcats com a vistos. És el que dona sentit al certificat de formació, que acredita la formació
completa i no només el resultat del test.

**Cada resposta porta explicació.** El document 06 dona la resposta correcta però no el perquè.
Sense explicació, un test autocorrectiu es limita a puntuar; amb explicació, tanca la formació.
Les explicacions estan redactades a partir del contingut de les mateixes preguntes.

**Les dades no surten del dispositiu.** L'eina no envia res enlloc: tot queda al navegador de qui
la fa servir. Simplifica el desplegament i el compliment en matèria de protecció de dades, a canvi
que l'Ajuntament hagi de fer còpies de seguretat periòdiques del registre, igual que amb l'eina
del segell de qualitat.

## 6. Pendent de validar amb l'Ajuntament

1. **Títols dels mòduls M1 a M5.** El document 06 indica a quin mòdul pertany cada pregunta, però
   no com es diuen. Els títols actuals estan deduïts del contingut i cal quadrar-los amb els
   documents 01 a 05 de la formació.
2. **Enllaços dels vídeos formatius.** El camp ja hi és a l'eina; en posar-hi l'URL apareix
   automàticament el botó de cada mòdul.
3. **Adhesiu Punt Lila.** El distintiu que genera l'eina és una proposta de J3B3. Si l'Ajuntament
   té l'art oficial, se substitueix per la imatge definitiva, com es va fer amb els adhesius
   PREMIUM i ESTÀNDARD del segell de qualitat.
4. **Vigència de l'acreditació.** Fixada provisionalment en dos anys per analogia amb el segell de
   qualitat. No consta al document 06.
5. **Logotip de la Diputació de Barcelona.** Inclòs per coherència amb l'eina del segell de
   qualitat. Si el programa Punt Lila no hi va associat, es retira.
6. **Explicacions de cada resposta.** Cal que l'àrea que ha fet la formació confirmi que diuen el
   mateix que els mòduls.

Els punts 3, 4 i 5 es canvien en una línia de configuració. Els punts 1, 2 i 6 són contingut.

## 7. Estat i propers passos

L'eina és funcional i provada. La revisió del 4 de setembre de 2026 hi ha passat una bateria de 41
proves automàtiques del circuit sencer, des del bloqueig inicial fins a la reemissió de documents des
del registre, amb el motor de correcció verificat als casos límit (dotze, nou, vuit i cap encert), el
Word obert i convertit sense errors, i l'adhesiu i el diploma renderitzats i comprovats. Se n'han
corregit els defectes detectats, detallats al `README.md`.

1. Enviar el zip a la tècnica municipal perquè la provi i respongui els sis punts de l'apartat 6.
2. Incorporar el que en surti i tancar la versió definitiva.
3. Decidir el desplegament: distribució del fitxer per part de l'Ajuntament, publicació en una
   pàgina del web municipal, o càrrega del test a una plataforma externa amb el CSV que genera
   l'eina. Les tres opcions són compatibles.

**Advertiment sobre el registre.** El registre viu al navegador del dispositiu on es fa el test. Si
els comerços el fan des de casa, l'Ajuntament no en rep res: el comerç haurà de fer arribar el
certificat o la còpia JSON. Perquè l'Ajuntament tingui el registre complet sense dependre'n, el test
s'ha de fer en un dispositiu municipal, en una sessió presencial o a l'oficina, o bé s'ha de
desplegar a la plataforma externa amb el CSV del qüestionari. És la decisió de desplegament que cal
prendre abans de publicar l'eina.

---

Encàrrec rebut el 27 d'agost de 2026. Versió de l'eina de la mateixa data.
