#!/usr/bin/env python3

import logging
import sys

logging.basicConfig(
    format="{asctime} {levelname}: {message}", style='{',
    level=logging.INFO, datefmt="%H:%M:%S",
)
logging.info("Initializing...")
