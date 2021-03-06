import logging
import multiprocessing
import os
import subprocess
from multiprocessing.pool import ThreadPool

import django

django.setup()

from import_single import import_single
from importer_lib.importer import (
    get_tellingen_count,
    import_core,
    prepare_import_tellingen,
)

DIRECTORY = os.path.dirname(os.path.realpath(__file__))
DO_PARALLEL = True


def import_tellingen_serial(csv_paths):
    for csv_path in csv_paths:
        import_single(csv_path)


def import_tellingen_job(csv_path):
    command = ["python", os.path.join(DIRECTORY, "import_single.py"), csv_path]
    logging.info(f"starting job: {command}")
    p = subprocess.Popen(command)
    p.wait()


def import_tellingen_parallel(csv_paths):
    """
    Run tellingen import process per file
    """
    cpu_count = multiprocessing.cpu_count()
    pool_size = int(cpu_count)
    logging.info(f"pool size: {pool_size}")
    tp = ThreadPool(pool_size)

    for csv_path in csv_paths:
        tp.apply_async(import_tellingen_job, (csv_path,))

    tp.close()
    tp.join()


def import_all():
    """
    Import all: tellussen, tellingen and various other models.
    Downloads csv files from object store
    """
    import_core()
    csv_paths = prepare_import_tellingen()

    if DO_PARALLEL:
        import_tellingen_parallel(csv_paths)
    else:
        import_tellingen_serial(csv_paths)

    logging.info("Done importing tellus data")
    logging.info(f"{get_tellingen_count()} tellingen")


if __name__ == "__main__":
    import_all()
