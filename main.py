from datetime import datetime, timedelta

class Voqea:
    def __init__(self, sana, vaqt, tavsif):
        self.sana = sana
        self.vaqt = vaqt
        self.tavsif = tavsif

class EventReminderSystem:
    def __init__(self):
        self.voqealar = []

    def qo'sh(self, sana, vaqt, tavsif):
        self.voqealar.append(Voqea(sana, vaqt, tavsif))

    def eslatish(self):
        bugungi_sana = datetime.now().date()
        yaqin_kunlar = [bugungi_sana + timedelta(days=i) for i in range(1, 8)]

        for voqea in self.voqealar:
            sana = voqea.sana.date()
            if sana in yaqin_kunlar:
                print(f"Bugungi va yaqin kunlardagi voqealar:")
                print(f"Sana: {sana}")
                print(f"Vaqt: {voqea.vaqt}")
                print(f"Tavsif: {voqea.tavsif}")
                print("------------------------")

# Misol foydalanuvchi
system = EventReminderSystem()
system.qo'sh(datetime.now().date(), "10:00", "Talabalar kuni")
system.qo'sh(datetime.now().date() + timedelta(days=1), "12:00", "O'qituvchilar kuni")
system.qo'sh(datetime.now().date() + timedelta(days=3), "14:00", "Katta sinf kuni")
system.eslatish()
