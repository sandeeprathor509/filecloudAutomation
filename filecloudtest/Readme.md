# FileCloud Tests

This project contains automated tests for FileCloud using Python and pytest. The tests cover user import, file management, and concurrent uploads.

## Project Structure
filecloud_tests/
├── data/
│ |── Sandeep_Rathor.docx
├── tests/
│ ├── conftest.py
│ ├── test_user_imports.py
│ ├── test_file_mgmt.py
│ └── test_concurrent_uploads.py
├── filecloud_api.py
├── requirements.txt
└── README.md


- **data/**: Contains test data files.
  - `Sandeep_Rathor.docx`: A sample .docx file used for testing file uploads.
- **tests/**: Contains test scripts.
  - `conftest.py`: Contains pytest fixtures.
  - `test_user_imports.py`: Tests for importing users into FileCloud.
  - `test_file_mgmt.py`: Tests for file upload, versioning, and retrieval.
  - `test_concurrent_uploads.py`: Tests for concurrent file uploads.
- **filecloud_api.py**: Contains helper functions to interact with the FileCloud API.
- **requirements.txt**: Lists the dependencies required for the project.
- **README.md**: This file.


## Run the file
To Run all test use
pytest

To Run specific test
pytest tests/test_user_import.py