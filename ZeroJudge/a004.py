"""
求潤年
"""
while True:
    try:
        line=input()
        yr = int(line)
        if yr%4!=0 or (yr%100==0 and yr%400!=0):
            print("平年")
        else:
            print("閏年")
		
    except EOFError:
        print("EOF") #CTRL+D (for *nix) or CTRL+Z (for Windows) 
        break
    except:
        print("other error")
        break