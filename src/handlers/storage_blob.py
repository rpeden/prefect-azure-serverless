import logging

import azure.functions as func
from prefect import flow, get_run_logger

async def main(myblob: func.InputStream):
    logging.info(f"Running Prefect flow!")
    test_aci_flow(myblob.name)

@flow(name="Azure Functions test flow")
def test_aci_flow(file_name: str):
    logger = get_run_logger()
    logger.info("Hello from Azure Functions!")
    logger.info(f"Processing blob file {file_name}.")