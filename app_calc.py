import customtkinter as s
import math
COR_FUNDO = "#62825D"
COR_BOTOES = "#526E48"
def calcular_volume_tanque():
    if altura_entry.get() and altura_entry.get().isnumeric():
        altura_combustivel = float(altura_entry.get())/100
        diametro = 2.549
        if bomba_select.get() == "Bomba 10L":
            comprimento = 2
        elif bomba_select.get() == "Bomba 15L":
            comprimento = 3
        elif bomba_select.get() == "Bomba 20L":
            comprimento = 4

        raio = diametro / 2 
        volume = (comprimento * (raio**2 * math.acos((raio - altura_combustivel) / raio) - (raio - altura_combustivel) * math.sqrt(2 * raio * altura_combustivel - altura_combustivel**2)))
     
        litros = math.floor(volume * 1000)
        resultado_label.configure(text=f"Volume do combustível: {litros}L")
    else:
        resultado_label.configure(text="Digite um valor no campo de altura!")


app = s.CTk()
app.geometry("250x300")
app.configure(fg_color=COR_FUNDO)
app.resizable(False, False)
app.title("Cálculo de nível da bomba")

altura_entry = s.CTkEntry(app, placeholder_text="Altura (cm)", width=200)
altura_entry.grid(row=0, column=0, padx=20, pady=20)


bomba_select = s.CTkOptionMenu(app, values=["Bomba 10L", "Bomba 15L", "Bomba 20L"], width=150, height=30, text_color="white", fg_color=COR_BOTOES)
bomba_select.grid(row=1, column=0, padx=20, pady=20)

resultado_label = s.CTkLabel(app, text="", text_color="white", width=50, height=30)
resultado_label.grid(row=2, column=0, padx=20, pady=20)

button = s.CTkButton(app, width=100, height=30,text="Calcular", fg_color=COR_BOTOES, bg_color="transparent", command=calcular_volume_tanque)
button.grid(row=3, column=0, pady=50)

app.mainloop()