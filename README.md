> **Obrir l'eina:** https://j3b3-consulting.github.io/montgat-punt-lila/
>
> Funciona directament al navegador. Per fer-la servir sense connexió, deseu la pàgina
> (`Ctrl+S`) o baixeu `Test_Punt_Lila_Montgat.html`: és un sol fitxer i no necessita res més.

# Montgat · Xarxa de Comerços Punt Lila
## Eina de formació, test d'aprofitament i acreditació

Eina autònoma que replica el funcionament de l'eina del **Segell de qualitat del comerç de Montgat**
(`PROJECTES\2026\MONTGAT\MONTGAT_EINA\Inspeccio_segell_Montgat.html`) aplicada a l'acreditació
**Punt Lila**: el comerç veu els vídeos formatius, fa el test, es corregeix sol i, si el supera,
descarrega l'**acreditació Punt Lila** i el **certificat de formació**.

---

## 1. Fitxers

| Fitxer | Què és |
|---|---|
| `Test_Punt_Lila_Montgat.html` | **L'eina.** Un sol fitxer. Es fa doble clic i s'obre al navegador. No necessita internet ni instal·lació. |
| `FONTS\06_test_aprofitament.docx` | Document d'origen: qüestionari i solucionari (Document 06 · Fase 4 · Avaluació). |
| `_build\_template.html` | Plantilla de l'eina amb marcadors `__LOGO__` (aquí és on s'edita el contingut). |
| `_build\logos.json` | Logotips institucionals en base64, extrets de l'eina del segell de qualitat. |
| `_build\build_eina.py` | Munta `Test_Punt_Lila_Montgat.html` a partir de la plantilla i els logotips. |

Per regenerar l'eina després d'editar la plantilla:

```
python _build\build_eina.py
```

---

## 2. Com funciona per al comerç

1. **Dades** de la persona participant i de l'establiment.
2. **Mòduls formatius** (M1–M5): el comerç marca cada mòdul un cop vist el vídeo.
   El test no s'activa fins que els cinc estan marcats i hi ha nom de persona i de comerç.
3. **Test**: 12 preguntes (8 d'opció múltiple i 4 de vertader/fals).
4. **Correcció automàtica** en prémer «Corregir el test»:
   - nota `X/12` i percentatge;
   - cada pregunta queda marcada en verd o vermell, amb la **resposta correcta** i una **explicació**;
   - desglossament **per mòdul**, per saber què cal repassar.
5. **Resultat**:
   - **9 o més encerts (75 %) → APTE.** S'activen els botons d'acreditació i certificat.
   - **Menys de 9 → NO APTE.** Es diu quins mòduls cal repassar i s'ofereix repetir el test.
     **Intents il·limitats** (test d'aprofitament, no selectiu).

## 3. Què es descarrega en superar el test

| Document | Formats | Contingut |
|---|---|---|
| **Adhesiu Punt Lila** | PNG, SVG | Distintiu quadrat per a l'aparador. Sense dades personals. |
| **Diploma d'acreditació** | PNG, SVG, PDF | A4 personalitzat: nom del comerç, data, validesa, codi d'acreditació i logotips. |
| **Certificat de formació** | Word (.docx), PDF | Persona, establiment, contingut dels 5 mòduls, resultat pregunta a pregunta, data i espai de signatura. |

El **codi d'acreditació** té el format `PL-MGT-AAAAMMDD-XXXX` (data + 4 primers caràcters del nom
comercial) i permet comprovar l'acreditació al registre municipal.
Validesa de l'acreditació: **2 anys** (configurable).

## 4. Registre per a l'Ajuntament

En corregir el test, l'eina el desa sola al navegador del dispositiu (`localStorage`), de manera que
cap test fet no es perd encara que no es premi cap botó. El botó «Desar al registre» serveix per
actualitzar el registre si després s'omplen o es corregeixen dades de la fitxa. Des de «Registre
d'acreditacions»:

- taula de tots els tests fets, amb nota i resultat;
- reemissió de l'acreditació i del certificat de qualsevol registre;
- **exportació a CSV** (full de càlcul) del registre complet;
- **còpia de seguretat / restauració** en JSON;
- **exportació del qüestionari + solucionari en CSV**, pensada per carregar el test a una plataforma
  externa amb correcció automàtica (tipus ACADEMIC ID), tal com preveu el document 06.

> Com que la base de dades viu al navegador, cal fer còpies de seguretat periòdiques (botó JSON) i
> desar-les en una carpeta de l'Ajuntament. És el mateix funcionament que l'eina del segell de qualitat.
>
> **El registre és del dispositiu on es fa el test.** Si el comerç el fa a casa seva, l'Ajuntament no
> en rep res automàticament: cal que el comerç enviï el certificat o la còpia JSON. Vegeu el punt
> sobre desplegament del `DOSSIER.md`.

---

## 4 bis. Revisió del 4 de setembre de 2026

Auditoria del circuit sencer amb 41 proves automàtiques i renderitzat real de l'adhesiu, el diploma i
els certificats. Correccions aplicades a `_build\_template.html`:

| Què | Per què |
|---|---|
| Les regles CSS `.ok` i `.ko` s'han acotat al panell de resultat | S'aplicaven a tot el bloc de la pregunta corregida: l'enunciat i totes les opcions sortien en verd o en taronja i en negreta, i una pregunta fallada semblava tenir totes les opcions malament. |
| Carregar un test en JSON ara buida abans les preguntes de la pantalla | Si ja hi havia un test corregit, s'hi barrejaven les marques de correcció antigues amb les respostes noves. |
| El resultat es desa sol al registre en corregir | Depenia que el comerç premés «Desar al registre»; si no ho feia, el test es perdia. |
| `localStorage` protegit amb `try/catch` i amb avís | En finestra privada o amb l'emmagatzematge desactivat, desar al registre petava i deixava l'eina a mitges. |
| Els botons de ràdio ja no s'amaguen amb `display:none` | Així el test es pot respondre amb el teclat i el llegeix un lector de pantalla, com demana l'accessibilitat d'una eina municipal. |
| Marca de l'opció triada també per classe, no només amb `:has()` | Als navegadors antics, `:has()` no funciona i no es veia quina opció s'havia marcat. |
| Dates en lletra al diploma i als certificats | Hi sortien en format `2026-09-04`. |
| Enumeracions, singular i plural, i espai abans del `%` | «els mòduls M1, M2», «1 tests desats», «100%». |
| Reemissió des del registre amb comprovació prèvia | Si el registre havia canviat, reemetia el document del test que hi havia a la pantalla en lloc d'avisar. |

---

## 5. Configuració (a dalt de tot del `<script>`)

```js
const LLINDAR=9;               // encerts mínims per ser APTE
const VIGENCIA_ANYS=2;         // validesa de l'acreditació
const BARREJA_OPCIONS=true;    // barreja l'ordre de les opcions a cada intent
const MOSTRA_LOGO_DIBA=true;   // false si el programa Punt Lila no porta logo de la Diputació
```

**Enllaços dels vídeos.** A la constant `MODULS`, el quart camp de cada mòdul és l'URL del vídeo
(ara buit). En posar-hi l'enllaç, apareix automàticament el botó «Veure el vídeo del mòdul Mx».

```js
["M1","Violència masclista: què és i com es manifesta","...","https://..."],
```

---

## 6. Punts a validar amb l'Ajuntament

1. **Títols dels mòduls M1–M5.** El document 06 només indica a quin mòdul pertany cada pregunta;
   els títols s'han deduït del contingut de les preguntes. Cal alinear-los amb els documents 01–05.
2. **Adhesiu Punt Lila.** El distintiu que genera l'eina és un disseny vectorial propi (lila, cercle
   Punt Lila + «Comerç adherit»). Si l'Ajuntament té l'art oficial de l'adhesiu, es substitueix per
   una imatge incrustada, igual com es va fer amb els adhesius PREMIUM/ESTÀNDARD del segell de qualitat.
3. **Logotip de la Diputació.** S'inclou per coherència amb l'eina del segell de qualitat. Si el
   programa Punt Lila no en depèn, cal posar `MOSTRA_LOGO_DIBA=false`.
4. **Al solucionari original, set de les vuit respostes d'opció múltiple són la B** (només la 5 és
   la C). Per això l'eina **barreja l'ordre de les opcions** a cada intent: la lletra no es pot
   memoritzar i el test manté el valor formatiu. Si es carrega el test en una plataforma externa,
   cal activar-hi la mateixa barreja.
5. **Vigència de l'acreditació (2 anys)** i **revisió periòdica**: no consten al document 06, s'han
   pres per analogia amb el segell de qualitat.
6. **Protecció de dades.** L'eina no envia res enlloc: totes les dades queden al dispositiu. Si es
   recullen dades de participants a escala municipal, cal la clàusula informativa corresponent.

---

*J3B3 Consulting · agost 2026*
