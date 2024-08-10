import logging


def setup_logger():
    logging.basicConfig(level=logging.DEBUG,  # Log seviyesini belirleyin
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Mesaj formatı
                        datefmt='%Y-%m-%d %H:%M:%S',  # Tarih formatı
                        handlers=[logging.FileHandler('app.log' ,"w"),  # Dosyaya loglama
                                logging.StreamHandler()])
