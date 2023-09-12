import webbrowser, sys, pyperclip

sys.argv

#check command line arg

if len(sys.argv) > 1:
  address =  ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()


webbrowser.open('goggle.com/maps/place/' + address)
