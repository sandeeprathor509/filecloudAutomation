import os

import pytest
from concurrent.futures import ThreadPoolExecutor

# using 50 as num of threads
NUM_THREADS = 50


@pytest.fixture(scope='session')
def docx_file_path():
    return os.path.join(os.path.dirname(__file__), '../data/Sandeep_Rathor.docx')


def test_concurrent_uploads(filecloud_api, docx_file_path):
    # 1. Approach we can use the for loop to uload the same file again and again because i tried to upload multiple
    # file but API taking all the file one by one

    # 2. Approach we can use the ThreadPool executor to get the load test
    # on API
    with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        futures = [executor.submit(docx_file_path) for _ in range(NUM_THREADS)]
        results = [future.result() for future in futures]

        success_count = results.count(True)
        failure_count = results.count(False)

        assert success_count > 0
        assert failure_count < NUM_THREADS

    # I also took reference like the way we can test through threadcount but not sure about it
