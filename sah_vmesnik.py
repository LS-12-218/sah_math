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
        bottle.redirect("zmaga")
    else:
        bottle.redirect("/")

@bottle.get("/zmaga/")
def zmaga():
    if sah.igralec == 1:
        igralec = "Črni"
    elif sah.igralec == 2:
        igralec = "Beli"
    return bottle.template("zmaga", sah = sah, igralec = igralec)
    


bottle.run(debug= True, reloader= True)