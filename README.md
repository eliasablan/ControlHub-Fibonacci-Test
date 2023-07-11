## Setup
1. Clone the repository:
```
git clone <repository-url>
```
2. Install the required dependencies using pip:
```
pip install -r requirements.txt
```
3. Run the API server:
```
python fibonacci.py
```
The server will start running at http://localhost:5000.

## Usage
Send a GET request to the `/fibonacci/<n>` endpoint, where `<n>` is the desired index of the Fibonacci sequence. The API will respond with the Fibonacci value at that index in JSON format.

Example request:
```
GET http://localhost:5000/fibonacci/6
```

Example response:

``` json
{
  "fibonacci": 8
}
```
---
- I decided to use Flask and Python because of its ease of use and implementation, its speed to have it working, and because i have worked prevously with it.
- A possible optimization could be the errors handling, giving explained messages to the users if the provided values are not a numbers, or positive integers.
