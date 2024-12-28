import sys
from src.logger import get_logger
from src.custom_exception import CustomException

logger = get_logger(__name__)

def divide_num(a,b):
    try:
        result = a/b
        logger.info('Diving the number')
        return result
    except Exception as e:
        logger.info("Error Occured")
        raise CustomException('Division by Zero', sys)
    
if __name__=='__main__':
    try:
        logger.info('Main Logger Started')
        divide_num(10/0)
    except Exception as ce:
        logger.error(str(ce))
    finally:
        logger.info('end logging')