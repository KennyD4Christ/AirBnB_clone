AirBnB Clone-The AirBnb Console
Overview
AirbBnB is a comprehensive web application that mirrors the functionality of AirBnB. It encompasses database storage, a back-end API, and front-end integration. Currently, the project has implemented the back-end console.
Core Classes
The application consists of several classes including BaseModel, FileStorage, User, State, City, Amenity, Place, and Review. These classes possess attributes such as id, created_at, and updated_at, and support methods for operations like save and to_dict. Additional attributes specific to each class, such as email and password for User, or name and state_id for State, are defined to ensure robust data handling.
Storage
An abstracted storage engine, FileStorage, manages class instances. Upon initialization, an instance of FileStorage named storage is created, handling all interactions with the file file.json where class instances are stored as JSON. This ensures persistence of data across sessions.
Console
The AirBnB console, a command-line interpreter, enables backend management. It supports commands for creating, updating, showing, destroying, counting, and listing class instances. The console operates in both interactive and non-interactive modes, offering flexibility in how commands are executed.
Usage:
•	Interactive Mode: Run ./console.py and enter commands directly.
•	Non-Interactive Mode: Pipe commands into the console script, e.g., echo "help" | ./console.py.
Key Commands:
•	create <class>: Creates a new instance.
•	show <class> <id> or <class>.show(<id>): Displays an instance based on its ID.
•	destroy <class> <id> or <class>.destroy(<id>): Deletes an instance.
•	all <class> or <class>.all(): Lists all instances of a class or all classes if no class is specified.
•	count <class> or <class>.count(): Counts instances of a class.
•	update <class> <id> <attribute> "<value>": Updates an instance's attribute.
