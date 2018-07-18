"""Converts RGB to HEX and HEX to RGB 

@BodaVijay.
"""

def rgb_hex():
    invalid_msg="Invalid values"
    red=int(raw_input("R: "))
    if red <0 or red >255:
      print invalid_msg

    green=int(raw_input("G: "))
    if green <0 or green >255:
      print invalid_msg

    blue=int(raw_input("B: "))
    if blue <0 or blue >255:
      print invalid_msg

    val=(red<<16 ) + (green<<8) + blue
    k=hex(val)
    print k[2:].upper()
 
def hex_rgb():
    hex_val=raw_input("Hex values: ")
    if len(hex_val) >=6:
      print invalid_msg
    else:
      hex_val=int(hex_val,16)
    two_hex_digits=2**8
    blue=hex_val%two_hex_digits
    hex_val=hex_val>>8
    green=hex_val%two_hex_digits
    hex_val=hex_val>>8
    red=hex_val%two_hex_digits
    print "%d%d%d"%(red,green,blue)
def convert():
  while True:
    option=raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit:")
    if option == '1':
      print "RGB to Hex..."
      rgb_hex()
    elif option=='2':
      print "HEX to RGB..."
      hex_rgb()
    elif option =='X' or option=='x':
      break
    else:
      print "Error."
      
convert()
  
      
      
      
    
    

 
  


  
