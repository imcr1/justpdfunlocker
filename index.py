import pikepdf , os , sys

#creating unlocked directory
try:
     os.makedirs("unlocked") 
except: 
     pass


os.system('color a')
#print logo
print('''                                                                               
                                PDF PASWORD UNLOCKER                                                                       
                                ██████████████████████                                  
                              ████                  ████                                
                              ██    ░░░░░░░░░░░░░░  ░░██                                
                              ██    ░░██████████    ░░██                                
                              ██    ░░██▓▓▓▓▓▓██    ░░██                                
                              ██    ░░██████████    ░░██      
                                 ██████ ██████   ██ 
                                ██      ██   ██ ███ 
                                ██      ██████   ██ 
                                ██      ██   ██  ██ 
                                 ██████ ██   ██  ██ 
                              ██                    ░░██                                
                              ████░░░░░░░░░░░░░░░░░░████                                
                                ██████████████████████                                  
                                      ██    ░░██                                        
                                      ██    ░░████████                                  
                                      ██    ░░██    ██                                  
                                      ██    ░░████████                                  
                                      ██    ░░██    ██                                  
                                      ██░░░░░░██░░░░██                                  
                                      ████████████████                                  

''')

#local env from paths
rnDri = os.getcwd()
savepath = rnDri + "/unlocked/"


#i dont know how this work but it works (if it works dont touch it 🤣)
def unlockPDF(filepath):
    filename = os.path.basename(filepath)[0:-4]
    pdf = pikepdf.open(filepath , allow_overwriting_input=True)
    pdf.save(savepath + f'{filename}-unlocked.pdf')

#geting args from commandline 
fip = sys.argv[1]

#init the function
unlockPDF(fip)
