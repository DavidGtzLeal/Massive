def parser(txt, at1, at2, at3):
    txt = txt.replace("{1}",at1)
    txt = txt.replace("{2}",at2)
    txt = txt.replace("{3}",at3)
    return txt
