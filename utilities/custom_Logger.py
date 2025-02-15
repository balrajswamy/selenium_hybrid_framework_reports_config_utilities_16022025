import logging


class Log_Maker:
    @staticmethod
    def log_gen():
        from datetime import datetime
        import os
        today = datetime.today().strftime("%Y%m%d%H%M%S")

        log_filename = f"Log_{today}.log"
        log_path = os.path.join(".", "Logs", log_filename)

        # Ensure the 'Logs' directory exists
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

        logging.basicConfig(filename=log_path,filemode="w",
                            format="%(asctime)s: %(levelname)s: %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S",
                            force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger