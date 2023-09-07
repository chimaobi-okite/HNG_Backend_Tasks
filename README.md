# HNG_Task_1_Solution

## Task Objective
Create and host an endpoint using any programming language of your choice.
The endpoint should take two GET request query parameters and return specific information in JSON format.
## Requirements
The information required includes:
* Slack name
* Current day of the week
* Current UTC time (with validation of +/-2)
* Track
* The GitHub URL of the file being run
* The GitHub URL of the full source code.
* A  Status Code of Success


## Technologies Used
1. FastApi
2. Render (deployment)


## Running the FastAPI Project on Your Computer

### Prerequisites:
  * Python > 3.10 installed on your system.

### Steps:
1. **Clone the GitHub Repository:**

    *bash*
    ```
    git clone https://github.com/chimaobi-okite/HNG_Task_1.git
    cd app HNG_Task_1
    ```

2. **Set up a Virtual Environment:**

    *bash*
    ```
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```
3. **Install Dependencies:**

    *bash*
    ```
    pip install -r requirements.txt
    ```

6. **Start the FastAPI Application:**

    *bash*
    ```
    uvicorn app.main:app --reload
    ```

7. **Access the API:**

    Open your browser and navigate to http://localhost:8000/. 
    You should see the FastAPI default page. 
    You can also access the auto-generated docs by visiting http://localhost:8000/docs.


