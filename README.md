The application will send HTTP requests to any API using URL.

### The program must check if 

- the mandatory keys exists in the requested data or not.
- the given datatypes match or not 
- the values are outside the expected range or not.

### How to use the application

- Open settings.json file and put the mandatory keys, data types and specific ranges that you wanna check.
  ```jsx

  {
    "userId": [1, [1,50]],      #[datatype, [range]]
    "id": [1, [1,50]],
    "title": ["str", [1,500]],
    "body": ["str", [1,500]]
  }

```
- Run the program
- Input the URL
- The program will automatically check if the requested data matches or not.

### Initializing all the packages

Application is using a multiple packages. Please make sure that you have installed all the required packages.

1. 

```jsx
import os
```

2. 

```jsx
import json
```

3.

```jsx
import requests
```




