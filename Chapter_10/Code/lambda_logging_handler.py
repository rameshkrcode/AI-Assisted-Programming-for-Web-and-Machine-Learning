import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
def lambda_handler(event, context):
    logger.info(f"Received input: {event}")
    # Inference logic follows
