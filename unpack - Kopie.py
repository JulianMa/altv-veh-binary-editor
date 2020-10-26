import struct
   

    
class VehicleModKit:
    mods = [];
    
    def __init__(self, f):
        modKitNameByteLength = f.read(2);
        if modKitNameByteLength != "":
            modKitNameLength = struct.unpack_from("<h", modKitNameByteLength)[0]
            modKitName = str(f.read(modKitNameLength))
            print(modKitName)
            modNumByte = f.read(1);
            modNumTotal = struct.unpack_from("<b", modNumByte)[0]
            for x in range(modNumTotal):
            
                modType = struct.unpack_from("<b", f.read(1))[0]
                modNum = struct.unpack_from("<b", f.read(1))[0]
                
                for mods in range(modNum):
                    total = struct.unpack_from("<h", f.read(2))[0]
                        #print(str(total) + ",", end = '')
                    #print("");
    
    def parseFromFile(f):s
       
class Mod:
    modType = 0;
    modNum = 0;
    
    def __init__(self, t, n):
        self.modType = t
        self.modNum = n
        
        
f = open("dirtymods.bin", "rb")
#origOffset = 65517
dirtyOffset = 63040
devoffset = 65517
rcoffset = 65337

try:
    magicByte = f.read(2)
    version = f.read(2)
    
    somebytesafterversion = f.read(2);
    
    #f.read(dirtyOffset)
    
    test = VehicleModKit(f);
    test = VehicleModKit(f);
    test = VehicleModKit(f);
    test = VehicleModKit(f);
   
    modKitNameByteLength = f.read(2);
    if modKitNameByteLength != "":
        modKitLength = struct.unpack_from("<h", modKitNameByteLength)[0]
        modKitName = str(f.read(modKitLength))
        modNumByte = f.read(1);
        modNumTotal = struct.unpack_from("<b", modNumByte)[0]
        #print(modKitLength)
        #print(modKitName)
        #print(modNumTotal)
        
        for x in range(modNumTotal):
            modType = struct.unpack_from("<b", f.read(1))[0]
            modNum = struct.unpack_from("<b", f.read(1))[0]
            #print("ModType: " + str(modType) + " Total: " + str(modNum) + " Mods:")
            
            for mods in range(modNum):
                total = struct.unpack_from("<h", f.read(2))[0]
                #print(str(total) + ",", end = '')
            #print("");
    
    #print("File Version: " + str(struct.unpack("<h", version)))
   
finally:
    f.close()