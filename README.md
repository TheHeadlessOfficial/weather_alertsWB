# Conky Weather CURRENT (by Weatherbit)
 
A standalone conky (written in Python) that shows the CURRENT weather, using [Weatherbit API](https://weatherbit.io/) website.<br>

<br>
<br>

## **WIKI**<br>

Download the .zip file, extract the files, copy the file `.conkyrc_wbalerts` and the folder `.conky` inside your Linux `home`.<br>
If your `home` is named *pippo*, copy inside *pippo* so you get: `/home/pippo/.conky` and `/home/pippo/.conkyrc_wbalerts`<br>
Go to `/home/YOURHOMENAME/.conky/weather/Weatherbit/alerts/` and open with a text editor the file `alertswbdata.py`, go to row 14 and 15 and type your latitude and your longitude, go to row 16 and write your APPID, go to row 52 to set how many alerts blocks you want in the conky (2 is default), go to row 72 to set the number of rows (3 is default), go to row 178 to set your language (just modify the pattern). If you change some of this parameters you could need to edit row 253 (18 is default; this indicates how many rows for a block of a single alert, if you add more rows changing the previous parameters you add rows to the block. One single block start with the `title` and ends with `regions`,; you can see this opening the `-aòertsraw.txt` file.<br>
If you don't know how to get your APPID, follow this video instructions: [APPID guide](https://youtu.be/O0nNilsTJSM?si=Tm1P7A1MYvipxb6L&t=30)<br>
<br>                                                                                  

<br> 

In the `font` folder, you can find some fonts you need.<br>
The python script saves data in files so you can build your conky weather as you wish.<br>
The `.conkyrc_wbalerts` file i attach, works.<br>
Run the file `.conkyrc_wbalerts` from terminal (the first time you run this conky), so you can get possible errors. 




<br>
<br>

## Screenshot

![](https://github.com/TheHeadlessOfficial/weather_alertsWB/blob/main/.conky/docs/screenshot.png)<br>

<br>
<br>
<br>
<br>
<br>

---
[Markdown guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

