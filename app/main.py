import logging, accepter2

if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s", datefmt="%D %T", level=logging.INFO)
    auto = accepter2.Accepter()
    auto.start()