import bottle
import sah_model
import os

sah = sah_model.Igra()

@bottle.get("/")
def igranje():
    return bottle.template("igranje.tpl", sah = sah, veljavni = sah.vse_figure())

@bottle.get("/premik/")
def premik():
    i = int(bottle.request.query["i"])
    j = int(bottle.request.query["j"])
    return bottle.template("premik.tpl", sah = sah, veljavni = sah.mozni_premiki(i, j), i = i, j = j)

@bottle.post("/premakni/")
def premakni():
    premiki = [int(mesto) for mesto in bottle.request.forms["premiki"]]
    print(premiki)
    sah.igraj(*premiki)
    if sah.stanje == 3:
        return "Zmaga za {}!".format(sah_model.barve[(sah.igralec + 1) % 2])
    else:
        bottle.redirect("/")




bottle.run(debug= True, reloader= True)