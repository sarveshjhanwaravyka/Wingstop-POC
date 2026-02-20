import logging
from colorama import Fore, Style

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    print(f"{Fore.YELLOW}=============================={Style.RESET_ALL}")
    logger.info("Hello From Wingstop!")
    print(f"{Fore.YELLOW}=============================={Style.RESET_ALL}")

if __name__ == "__main__":
    main()