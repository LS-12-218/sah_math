import bottle
import sah_model
import os

sah = sah_model.Sah()

def id_igre():
    cookie = bottle.request.get_cookie("sm_id_igre", secret = "nebosuganil")
    if cookie.isdigit():
        return int(cookie)

@bottle.get("/")
def zacetek():
    return bottle.template("zacetna.tpl")

@bottle.post("/igra/nova/")
def nova():
    bottle.response.set_cookie("sm_id_igre", str(sah.id_igre), secret = "nebosuganil", path = "/")
    sah.dodaj_igro()
    bottle.redirect("/igra/")

@bottle.get("/igra/")
def igranje():
    igra = sah.igra(id_igre())
    if igra:
        return bottle.template("igranje.tpl", sah = igra, veljavni = igra.vse_figure())

@bottle.get("/igra/premik/")
def premik():
    igra = sah.igra(id_igre())
    i = int(bottle.request.query["i"])
    j = int(bottle.request.query["j"])
    if igra:
        return bottle.template("premik.tpl", sah = igra, veljavni = igra.mozni_premiki(i, j), i = i, j = j)

@bottle.post("/igra/premakni/")
def premakni():
    premiki = [int(mesto) for mesto in bottle.request.forms["premiki"]]
    stanje = sah.igraj(id_igre(), *premiki)
    if stanje == 3:
        bottle.redirect("/igra/zmaga/")
    elif stanje in (1, 2):
        bottle.redirect("/igra/")

@bottle.get("/igra/zmaga/")
def zmaga():
    igra = sah.igra(id_igre())
    if igra:
        if igra.igralec == 1:
            igralec = "Črni"
        elif igra.igralec == 2:
            igralec = "Beli"
        sah.odstrani_igro(id_igre())
        return bottle.template("zmaga", sah = igra, igralec = igralec)
    


bottle.run(debug= True, reloader= True)