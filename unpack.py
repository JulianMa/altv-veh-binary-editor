import struct


class VehicleModKit:

    def __init__(self, f):
        self.mods = []
        self.modNumTotal = 0;
        self.exists = False;
        self.modKitName = "";

        self.modKitIndex = f.read(2)  # Index of ModKit
        modkit_length_as_bytes = f.read(2)

        if len(modkit_length_as_bytes) > 0:
            self.exists = True
            modkit_name_string_length = struct.unpack_from("<h", modkit_length_as_bytes)[0]

            self.modKitName = str(f.read(modkit_name_string_length)).split('b\'', 1)[1].split('\'')[
                0]  # C-Styles String Workaround


            self.modNumTotal = struct.unpack_from("<b", f.read(1))[0]
            for x in range(self.modNumTotal):

                mod_type = struct.unpack_from("<b", f.read(1))[0]
                total_mods_of_type = struct.unpack_from("<b", f.read(1))[0]

                engineIndex = []
                for mods in range(total_mods_of_type):
                    engineIndex.append(struct.unpack_from("<h", f.read(2))[0])

                self.mods.append(Mod(mod_type, total_mods_of_type, engineIndex))


class Mod:

    def __init__(self, t, n, m):
        self.modType = t
        self.modNum = n
        self.modIndex = m


f = open("vehmods.bin", "rb")
# origOffset = 65517
dirtyOffset = 63040
devoffset = 65517
rcoffset = 65337

try:
    magicByte = f.read(2)
    version = f.read(2)

    # f.read(dirtyOffset)
    test = VehicleModKit(f);
    while (test.exists):
        print(test.modKitName + ": " + str(test.modNumTotal))
        for x in range(len(test.mods)):
            print("Mod: " + str(test.mods[x].modType) + " TotalMods: " + str(test.mods[x].modNum))

        test = VehicleModKit(f)
        print("-------------------------------------------------------------------------------------")

finally:
    f.close()
