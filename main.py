############################################
# alt:V Binary Vehicle Model & Mods Editor #
############################################
import unpack
import tkinter as tk

window = tk.Tk(className="VehMods Editor")
window.geometry("400x300")

mod_kit_parser = unpack.VehModsParser("bin/vehmods.bin")

frameBot = tk.Frame(window)
frameLeft = tk.Frame(window)
frameMid = tk.Frame(window)
frameRight = tk.Frame(window)

frameBot.pack(expand=True, fill=tk.BOTH, side=tk.BOTTOM)
frameLeft.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
frameMid.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
frameRight.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)


modkitguilist = tk.Listbox(frameLeft)
modtypelist = tk.Listbox(frameMid)
modlist = tk.Listbox(frameRight)


modKitLabel = tk.Label(master=frameLeft, text="ModKits:")
modKitLabel.pack( side=tk.TOP)

modTypesLabel = tk.Label(master=frameMid, text="Available Mod-Types:")
modTypesLabel.pack( side=tk.TOP)

vehModLabel = tk.Label(master=frameRight, text="Mods of Type")
vehModLabel.pack( side=tk.TOP)

descriptionLabel = tk.Label(master=frameBot, text="Please Select the ModKit on the Left side.\r"
                                                  "All Available Mod-Types are Displayed in the Center List.\r"
                                                  "All Available Mods for this Particular ModType are Listed\r"
                                                  "on the Right List then The first number\r"
                                                  "is the modIndex, used in the GTA-Native. The Second\r"
                                                  "Number, is the Internal Engine Index for that vehicle mod.")
descriptionLabel.pack( side=tk.BOTTOM)

modkitguilist.pack(expand=True, fill=tk.BOTH)
modtypelist.pack(expand=True, fill=tk.BOTH)
modlist.pack(expand=True, fill=tk.BOTH)


def addModKit():
    print("")
def addModType():
    print("")
def addMod():
    print("")

modkitaddbutton = tk.Button(frameLeft, text ="Add modKit", command = addModKit)
modkitaddbutton.pack(fill=tk.BOTH,side=tk.BOTTOM)

modtypeaddbutton = tk.Button(frameMid, text ="Add modType", command = addModKit)
modtypeaddbutton.pack(fill=tk.BOTH,side=tk.BOTTOM)

modaddbutton = tk.Button(frameRight, text ="Add mod", command = addModKit)
modaddbutton.pack(fill=tk.BOTH,side=tk.BOTTOM)

selectedmodkit = mod_kit_parser.mod_kits[0]
selected_mod_type = selectedmodkit.mods[0]

def onselectmodkit(evt):
    w = evt.widget
    if len(w.curselection()) > 0:
        index = int(w.curselection()[0])
        modtypelist.delete(0, tk.END)
        selectedmodkit = mod_kit_parser.mod_kits[index]
        for mod in selectedmodkit.mods:
            modtypelist.insert(tk.END, str(mod.modType))

def onselectmodtype(evt):
    w = evt.widget
    if len(w.curselection()) > 0:
        index = int(w.curselection()[0])
        modlist.delete(0, tk.END)
        selected_mod_type = selectedmodkit.mods[index]

        for index_of_engine_index_entry in range(len(selected_mod_type.modIndex)):
            modlist.insert(tk.END, str(index_of_engine_index_entry) + " (" + str(selected_mod_type.modIndex[index_of_engine_index_entry]) + ")")

modkitguilist.bind('<<ListboxSelect>>', onselectmodkit)
modtypelist.bind('<<ListboxSelect>>', onselectmodtype)

for modkit in mod_kit_parser.mod_kits:
    modkitguilist.insert(tk.END, modkit.modKitName)


window.mainloop()
