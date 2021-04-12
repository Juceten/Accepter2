import json, logging

def askUser():
    fp="app/settings.json"
    with open(fp, "r") as f:
        settings = json.load(f)
    logging.debug(settings)

    def menu():
        choices = {"1":closeOnAccept, "2":quitKey, "3":stop}
        logging.info(f'Settings Menu\n1.Quit after accepting(current setting:{settings["close_on_accept"]})\n2.Select exit key(current key:"{settings["quit_key"]}")\n3.Exit...')
        msg = input()
        if msg not in choices.keys():
            logging.error(f"please select a valid option(1, 2, or 3)...")
            return menu()
        choices[msg]()
        
    def closeOnAccept():
        choices = {"true":True,"false":False,"t":True,"f":False}
        logging.info("Quit after accepting a match?(true/false)")
        msg = input().lower()
        if msg not in choices.keys():
            logging.error("please select a valid option(true(t) or false(f))...")
            return closeOnAccept()
        settings["close_on_accept"] = choices[msg.lower()]
        with open(fp, "w") as f:
            json.dump(settings, f)
        return askUser()
      
    def quitKey():
        logging.info("Select exit key...")
        msg = input()
        if len(msg) > 1:
            logging.error("please only enter one key...")
            return quitKey()
        settings["quit_key"] = msg.lower()
        with open(fp, "w") as f:
            json.dump(settings, f)
        return askUser()
    
    def stop():
        pass

    menu()  

if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", datefmt="%D %T", level=logging.INFO)
    askUser()