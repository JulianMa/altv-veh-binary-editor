import struct
   
class VehicleModKit:
    mods = [];
    modNumTotal = 0;
    exists = False;
    modKitName = ""
    
    def __init__(self, f):
        modKitIndex = f.read(2);
        modKitNameByteLength = f.read(2);
        if len(modKitNameByteLength) > 0:
            self.exists = True
            modKitNameLength = struct.unpack_from("<h", modKitNameByteLength)[0]
            self.modKitName = str(f.read(modKitNameLength)).split('b\'', 1)[1].split('\'')[0] # C-Styles String Workaround
            modNumByte = f.read(1);
            self.modNumTotal = struct.unpack_from("<b", modNumByte)[0]
            for x in range(self.modNumTotal):
            
                modType = struct.unpack_from("<b", f.read(1))[0]
                modNum = struct.unpack_from("<b", f.read(1))[0]
                
                engineIndex = []
                for mods in range(modNum):
                    engineIndex.append(struct.unpack_from("<h", f.read(2))[0])
                
                self.mods.append(Mod(modType, modNum, engineIndex))
       
class Mod:
    modType = 0;
    modNum = 0;
    modIndex = [];
    
    def __init__(self, t, n, m):
        self.modType = t
        self.modNum = n
        self.modIndex = m
        
        
f = open("dirtymods.bin", "rb")
#origOffset = 65517
dirtyOffset = 63040
devoffset = 65517
rcoffset = 65337

try:
    magicByte = f.read(2)
    version = f.read(2)
    
    
    #f.read(dirtyOffset)
    test = VehicleModKit(f);
    while(test.exists):
        print(test.modKitName + ": " +str(test.modNumTotal))
        for x in range(len(test.mods)):
           print("Mod: " + str(test.mods[x].modType) + " TotalMods: " + str(test.mods[x].modNum))
        
        test = VehicleModKit(f)
        print("-------------------------------------------------------------------------------------")
   
finally:
    f.close()