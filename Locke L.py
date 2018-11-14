import webbrowser as wb
import pyautogui as pg
import time as t

points = 0

animal = pg.prompt("What animal do you enjoy eating")
   
if animal == "goat":
    pg.alert("tastes like chicken")
    points += 5
    wb.open("https://www.youtube.com/watch?v=YI4hzzepEcI")
    t.sleep(5)
elif animal == "dylan":
    pg.alert("Phil Swift you are")
    points += 20
elif animal == "rat":
    pg.alert("i like rat tail soup")
    points += 30
    wb.open("https://www.youtube.com/watch?v=0t2VPBF6Kp4")
    t.sleep(5)

elif animal == "phil swift":
    pg.alert("you are definitly phil swift")
    points += 30
    wb.open("https://www.youtube.com/watch?v=JZLAHGfznlY")
    t.sleep(5)
elif animal == "Dog":
    pg.alert("I am allergic")
    wb.open("https://www.youtube.com/watch?v=NH8pM0cgz2k")
    t.sleep(5)
elif animal == "cat":
    pg.alert("very allergic how rude")
    wb.open("https://www.youtube.com/watch?v=U_iXDhuV9dc")
    t.sleep(5)
else:
    pg.alert("Am I gonna have to flex seal your mouth shut")
    points += 0
    wb.open("https://www.youtube.com/watch?v=JZLAHGfznlY")
    t.sleep(5)

show = pg.prompt("what is your favorite tv show")

if show == "Riverdale":
    pg.alert("thank you phil, very cool")
    points -= 5
elif show == "the office":
    pg.alert ("you have chosen wisely")
    points += 10
    wb.open("https://www.youtube.com/watch?v=Xnk4seEHmgw")
    t.sleep(5)
elif show == "the flash":
    pg.alert("that was a quick choice")
    points += 5
    wb.open("https://www.youtube.com/watch?v=VikGZ5T-S7U")
    t.sleep(5)
elif show == "Grey's Anatomy":
    pg.alert("nasty")
    points += .5
elif show == "planes":
    pg.alert("very cool")
    points += 20,000
elif show == "Phil swift":
    pg.alert("That's my favorite, too")
    points += 10,000
    wb.open("https://www.youtube.com/watch?v=8ci2hj7CSHI")
    t.sleep(5)
else:
    pg.alert("phil swift you are and your favorite show is " + show)
    wb.open("https://www.youtube.com/watch?v=0xzN6FM5x_E")
    t.sleep(5)


dessert = pg.prompt("What is your favorite desert?")

if dessert == "cake":
    pg.alert("Very cool of you phil")
    points += 5
    wb.open("https://www.youtube.com/watch?v=RK78IKPzeNc")
    t.sleep(5)

elif dessert == "cupcake":
    pg.alert("I'll have a cup of cake")
    
elif dessert == "cookie":
    pg.alert("intruguing")
    points += 5
elif dessert == "rat":
    pg.alert("Amazing")
    points += 20
elif dessert == "ice cream":
        pg.alert("That's phil Swift's favorite too")
        wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=1120&bih=537&tbm=isch&sa=1&ei=m3jQW7LfN9K3ggef_Z7ICw&q=phil+swift+extreme+bucket+demo+chainsaw&oq=phil+swift+extreme+bucket+demo+chainsaw&gs_l=img.3...14050.16774..17010...0.0..0.738.1872.5j1j1j0j1j0j1......0....1..gws-wiz-img.......0i30j0i24.5VBapLYv_YQ#imgrc=Gd7TVdg8bYx-OM:")
        t.sleep(5)
elif dessert == "shin kicking":
    pg.alert("Cheese rolling is best")
    wb.open("https://www.youtube.com/watch?v=VZ2CSpNze5Q")
    t.sleep(5)
   
else:
    pg.alert("thank you phil, very cool, your favorite dessert is" + dessert)
    wb.open("https://www.youtube.com/watch?v=Y4NtSOz8BxI")
    t.sleep(5)


sport = pg.prompt("what is your favorite sport")

if sport == "cheese rolling":
    pg.alert("wow you would")
    points += 13
    wb.open("https://www.youtube.com/watch?v=gNj67kwWBoQ")
    t.sleep(5)
elif sport == "shin kicking":
    pg.alert("excellent choice")
    points += 16
elif sport == "Curling":
    pg.alert("that's not a sport")
    points -= 17
elif sport == "ferret racing":
    pg.alert("that is inhumane")
    points -= 10
elif sport == ("football"):
    pg.alert("cool")
    points += 5
elif sport == "baseball":
    pg.alert("that's not a sport")
    points += 5
elif sport == "dance":
    pg.alert("that's not a sport")
    points -= 20
elif sport == "tennis":
    pg.alert("Zach Toback")
    points += 45
    wb.open("https://www.youtube.com/watch?v=uiBrForlj-k")
    t.sleep(5)
elif sport == "soccer":
    pg.alert("FLop")
    wb.open("https://www.youtube.com/watch?v=yHK15TvdnKg")
    t.sleep(5)
elif sport == "basketball":
    pg.alert("false")
    points += 6


else:
    pg.alert("are you sure it is not shin kicking?")
    wb.open("https://www.youtube.com/watch?v=lAuZw-ZFSjc")
    t.sleep(5)
song = pg.prompt("what is your favorite song")
if song == "fat by weird al":
    pg.alert(doubt)
    points +=5

elif song == "happier":
    pg.alert("whatever makes you happy")
    points +=5
elif song == "Lil sebastian":
    pg.alert("excellent choice")
    wb.open("https://www.youtube.com/watch?v=7RXsYqygGKc")
    t.sleep(5)
elif song == "handy":
    pg.alert("ARH")
elif song == "Ace theme song":
    pg.alert("BEST EVER")
    wb.open("https://www.youtube.com/watch?v=sQVeONqunz4")
    t.sleep(5)
elif song == "disney channel theme songs":
    pg.alert("finally a true fan")
    wb.open("https://www.youtube.com/watch?v=zLA3QNRXVlY")
    t.sleep(5)
else:
    pg.alert("doubt")
    wb.open("https://www.youtube.com/watch?v=0xzN6FM5x_E")
    t.sleep(5)





pg.alert(points)
