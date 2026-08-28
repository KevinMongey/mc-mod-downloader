import requests
import customtkinter as ctk

app = ctk.CTk()
app.title("Minecraft Mod Downloader")
app.geometry("900x600")

# -------------------
# SETTINGS
# -------------------
settings_frame = ctk.CTkFrame(app)
settings_frame.pack(
    fill="x",
    padx=20,
    pady=20
)
settings_label = ctk.CTkLabel(
    settings_frame,
    text="Settings",
    font=("Arial", 24, "bold")
)
settings_label.pack(
    anchor="w",
    padx=20,
    pady=15
)
# -------------------
# BOTTOM SECTION
# -------------------
bottom_frame = ctk.CTkFrame(app)
bottom_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=(0, 20)
)
# LEFT SIDE
mod_list_frame = ctk.CTkFrame(bottom_frame)
mod_list_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 10)
)
mod_list_label = ctk.CTkLabel(
    mod_list_frame,
    text="Mod List",
    font=("Arial", 20, "bold")
)
mod_list_label.pack(
    anchor="w",
    padx=20,
    pady=15
)
# RIGHT SIDE
results_frame = ctk.CTkFrame(bottom_frame)
results_frame.pack(
    side="right",
    fill="both",
    expand=True,
    padx=(10, 0)
)
results_label = ctk.CTkLabel(
    results_frame,
    text="Found & Downloaded Mods",
    font=("Arial", 20, "bold")
)
results_label.pack(
    anchor="w",
    padx=20,
    pady=15
)

app.mainloop()


'''
def search_mods(mod_name):
    url = "https://api.modrinth.com/v2/search"

    parameters = {
        "query": mod_name,
        "limit": 10
    }

    response = requests.get(url, params=parameters)
    data = response.json()
    return data

mod_name = input("Enter a mod name: ")
results = search_mods(mod_name)
print(results)
'''