# Robocopy Tutorial

## 1. Fájl Műveletek  

#### 1.1 Fájlok Másolása
<details>
  <summary>Leírás</summary>

<b>Feladat:</b> Hozzunk létre két üres mappát!  
Az egyikben helyezzünk el egy tetszőleges szöveges állományt!  
A szöveges állományt másoljuk át egy Script segítségével!  

<b>Megjegyzés:</b> Visszapipáljuk az ismert fájltípusok kiterjesztésének elrejtését,  
a mappa beállításaiban. Így látszani fognak a kiterjesztések ( Pl. *.txt vagy *.cmd )  
<details>
  <summary>Szemléltetés Képernyőképpel</summary>
&nbsp;<img src="https://github.com/user-attachments/assets/e7e34aa1-ed3a-40ae-8d8b-dea4be9dc179" width="50%" height="50%" />
</details>
  
<b>Megoldás</b>  

1. Létrehozzuk a forrás mappát ( ahonnan másolunk )!
   ( Ebben az esetben az Asztalon )
<details>
  <summary>Szemléltetés Képernyőképpel</summary>
&nbsp;<img src="https://github.com/user-attachments/assets/e15dac90-f8f4-4a73-b341-e80edbb33dc6" width="50%" height="50%" />
</details>

2. Létrehozzuk a cél mappát ( ahova másolunk )!
   ( Ebben az esetben az Asztalon )
<details>
  <summary>Szemléltetés Képernyőképpel</summary>
&nbsp;<img src="https://github.com/user-attachments/assets/a900e730-a784-45c0-ae43-44b8206bd0d8" width="50%" height="50%" />
</details>

3. A forrás mappát megnyitva, létrehozzuk a szöveges állományt
   és írunk bele valamit, majd elmentjük és bezárjuk.  
<details>
  <summary>Szemléltetés Képernyőképpel</summary>
&nbsp;<img src="https://github.com/user-attachments/assets/5afee23d-c388-4e39-8ade-b30b6057c002" width="50%" height="50%" />
</details>

4. Létrehozunk egy szöveges fájlt, majd átnevezzük *.txt-ről
   *.bat vagy *.cmd kiterjesztésűre! Például "script.cmd"!
   Ha az Operációs Rendszer rákérdez, engedélyezzük az átnevezést.
<details>
  <summary>Szemléltetés Képernyőképpel</summary>
&nbsp;<img src="https://github.com/user-attachments/assets/f3a1cee7-dbf8-465b-b83d-560eab935fae" width="50%" height="50%" />
&nbsp;<img src="https://github.com/user-attachments/assets/be35eccd-13db-4a1e-9410-77a72e64a498" width="50%" height="50%" />
</details>

5. Szövegszerkesztővel ( Például Notepad vagy Notepad++ ) megnyitjuk a scriptet!
<details>
  <summary>Szemléltetés Képernyőképpel</summary>
&nbsp;<img src="https://github.com/user-attachments/assets/46ae604a-7e0f-4a2a-8c8c-f565be2eafa8" width="50%" height="50%" />
</details>

6. A <b>robocopy</b> utasítást használjuk a fájl átmásolására!  
   Az utasítást PowerShell-ben vagy Command Line-ban szerkesztjük,  
   mert az elérési út manuális beírásakor,  
   a biztonságos kiegészítéséhez tabulátort használhatunk!

   Az utasítást beírása után, először manuálisan futtatjuk!

   Az általános megoldás érdekében érdemes a hard-coded felhasználónév helyett  
   Pl.: C:\Users\gipszjakab\Desktop
   inkább környezeti változókkal dolgozni  
   Pl.: C:\Users\%USERNAME%\Desktop

   FONTOS! Mindkét paramétert paramétert ( forrás mappa és cél mappa )
   idézőjelekbe kell helyezni, így elkerülhető a space-t tartalmazó mappanevekből fakadó hibás működés!cls
<details>
  <summary>Szemléltetés Képernyőképpel</summary>
&nbsp;<img src="https://github.com/user-attachments/assets/77b3c07a-a396-42d6-b814-618e3bfc5b8e" width="50%" height="50%" />
</details>

7. Amennyiben az utasításvégrehajtás sikeres volt és sikeresen a célmappába másoltuk a fájlt,
   nincs más dolgunk, mint beilleszteni az utasítást a létrehozott script.cmd állományba, szövegszerkesztővel.

   Amennyiben sikertelen volt, feltétlenül ellenőrizzük hogy megfelelő jogosultsággal futtattuk-e,
   és hogy az "echo %USERNAME%" parancs kimenete a mi felhasználónevünk. Ellenőrizzük az idézőjeleket is!

9. Miután beillesztettük a script.cmd-be az utasítást, mentsük el, majd dupla klikkel futtassuk! A fájl átmásolódott.

### Extra lépések:
#### A script futtatása feladatütemezővel

1. A <b>Win + R</b> billentyűkombinációt lenyomva,
   majd a "taskschd.msc" parancsot beírva, futtassuk a feladatütemezőt!

  <details>
    <summary>Szemléltetés Képernyőképpel</summary>
    &nbsp;<img src="https://github.com/user-attachments/assets/29fcd6e6-2a9e-4274-9209-2486aed93a4e" width="50%" height="50%" />
  </details>

2. Klikkeljünk az "Egyszerű Feladat Létrehozása..." gombra a jobboldali menüben!
  <details>
    <summary>Szemléltetés Képernyőképpel</summary>
    &nbsp;<img src="https://github.com/user-attachments/assets/df257a90-d1a9-484b-90c5-a6930bbeabf1" width="50%" height="50%" />
  </details>

3. A varázslóval adjunk tetszőleges nevet és leírást a feladatnak, majd klikkeljünk a "Tovább" gombra!

  <details>
    <summary>Szemléltetés Képernyőképpel</summary>
    &nbsp;<img src="https://github.com/user-attachments/assets/6c115b86-e7ce-4549-867b-72b0c426ff1a" width="50%" height="50%" />
  </details>

4. Válasszuk ki a feladatismétlés ciklusát ( ez esetben egyszeri ), majd "Tovább"!
   
  <details>
    <summary>Szemléltetés Képernyőképpel</summary>
    &nbsp;<img src="https://github.com/user-attachments/assets/656054d3-6a16-4924-8aa8-a652119e273c" width="50%" height="50%" />
  </details>
  
5. Állítsuk be a pontos időt, vagy időszakokat a feladatvégrehajtáshoz, majd "Tovább"!
    
    <details>
      <summary>Szemléltetés Képernyőképpel</summary>
        &nbsp;<img src="https://github.com/user-attachments/assets/4d91bf46-ec9d-4f4b-aa6f-e868fa215b1a" width="50%" height="50%" />
    </details>

6. Tevékenységnek válasszuk ki a "Program Indítása" opciót, majd "Tovább"!

    <details>
      <summary>Szemléltetés Képernyőképpel</summary>
        &nbsp;<img src="https://github.com/user-attachments/assets/ba426938-58fa-423d-9881-fcb82569b8a3" width="50%" height="50%" />
    </details>
  
7. Tallózzuk be az általunk előállított "script.cmd"-t, majd "Tovább"!
    <details>
      <summary>Szemléltetés Képernyőképpel</summary>
        &nbsp;<img src="https://github.com/user-attachments/assets/f367009e-6db5-4f66-b62e-d8a3b0e3b66f" width="50%" height="50%" />
    </details>

8. Pipáljuk be a feladat tulajdonságainak megnyitását, a varázsló bezárása után!
    <details>
      <summary>Szemléltetés Képernyőképpel</summary>
        &nbsp;<img src="https://github.com/user-attachments/assets/5d95bca3-f1d0-4d9a-8bef-072164a4049c" width="50%" height="50%" />
        &nbsp;<img src="(https://github.com/user-attachments/assets/163d430e-1a84-4811-8411-74be081000de" width="50%" height="50%" />
    </details>
    
    

</details>
&nbsp;&nbsp;&nbsp;&nbsp;
