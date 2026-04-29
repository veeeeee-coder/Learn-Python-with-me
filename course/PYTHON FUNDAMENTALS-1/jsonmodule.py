import json    
#json.loads()
#json.dumps()
#json.load()
#json.dump()

json_str='{"name":"vee", "isTeacher":true,}'
py_obj=json.loads(json_str)
print(type(py_obj),py_obj)

py_obj={
    "name":"veeeee",
    "isTeacher":True
}
json_str=json.dumps(py_obj)
print(type(json_str),json_str)






#The `json` module in Python is used to **work with JSON (JavaScript Object Notation) data**, which is a lightweight, text-based format for storing and exchanging data. JSON is widely used in APIs, web applications, configuration files, and data storage because it is **human-readable and language-independent**. In Python, the `json` module allows you to **convert Python objects (like dictionaries, lists, strings, numbers, booleans, and `None`) into JSON format and vice versa**. This process is called **serialization (Python → JSON)** and **deserialization (JSON → Python)**.



#When converting JSON data into Python objects, two main functions are used: `loads()` and `load()`. The function `json.loads()` is used when you already have JSON data in the form of a **string**. It parses the string and converts it into a Python object, typically a dictionary or list. For example:

#```python
import json

data = '{"name": "John", "age": 25}'
python_obj = json.loads(data)
print(python_obj["name"])   # John
#```

#On the other hand, `json.load()` is used when JSON data is stored in a **file**. It reads the file and converts its contents into a Python object:

#```python
import json

with open("data.json", "r") as f:
    python_obj = json.load(f)
print(python_obj)
#```

#So, the key difference is that `loads()` works with strings, while `load()` works with file objects.

#For converting Python objects into JSON format, we use `dumps()` and `dump()`. The function `json.dumps()` converts a Python object into a **JSON string**, which is useful when you want to send data over a network or print it:

#```python
#import json

#data = {"name": "John", "age": 25}
#json_str = json.dumps(data)
#print(json_str)
#```

#Meanwhile, `json.dump()` writes a Python object directly into a **file in JSON format**:

#```python
#import json

#data = {"name": "John", "age": 25}

#with open("data.json", "w") as f:
 #   json.dump(data, f)
#```

#Again, the difference is that `dumps()` returns a string, while `dump()` writes directly to a file.

#The `json` module also provides useful options to control formatting and readability. For example, using `indent=4` in `dump()` or `dumps()` makes the JSON output nicely formatted and easier to read:

#```python
#json.dumps(data, indent=4)
#```

#You can also use `sort_keys=True` to sort dictionary keys, and parameters like `ensure_ascii=False` to properly handle non-English characters.

#It’s important to understand how Python data types map to JSON types: Python dictionaries become JSON objects, lists and tuples become arrays, strings remain strings, numbers stay numbers, `True`/`False` become `true`/`false`, and `None` becomes `null`. This mapping ensures smooth conversion between formats.

#In summary, the `json` module is essential for **data exchange and storage** in modern applications. Use `loads()` and `load()` to read JSON into Python, and `dumps()` and `dump()` to convert Python data into JSON. The difference between the “s” and no “s” versions is simple: functions with “s” work with **strings**, while those without work with **files**. This makes the module flexible and powerful for handling structured data in real-world scenarios.
