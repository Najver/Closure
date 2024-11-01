def nastav_semafor(barva):

    barva_semaforu = barva

    def muzes_jet():
        if (barva_semaforu == "zelená"):
            return True
        else:
            return False

    return muzes_jet


muze_jet = nastav_semafor("zelená")
print(muze_jet())

muze_jet = nastav_semafor("červená")
print(muze_jet())