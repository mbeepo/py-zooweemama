import sys
i = input(f"""Python {sys.version} on {sys.platform}
Type "help", "copyright", "credits" or "license" for more information.
>>> """)
          
while True:
    if i == "zoo wee mama!":
        print("We did it boyes")
    else:
        eval(i)
    
    i = input(">>> ")
