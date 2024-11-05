def create_task_list():
    """
    Creates task list using closure. It creates one list of tasks with two properties (description, is_complete) and some functions for manipulation with it.
    :return: Dictionary with closure functions
    """
    tasks = []
    def add_task(description : str):
        """
        Adds new uncompleted task.
        :param description: the task text
        """
        if len(description.strip()) < 0:
            raise Exception("Task must contains one char at least.")

        tasks.append({"description" : description, "is_complete" : False})

    def get_uncompleted():
        """
        Selects uncompleted tasks and returns them.
        :return: list of descriptions in str
        """
        uncompleted = []
        for t in tasks:
            if not t["is_complete"]:
                uncompleted.append(t["description"])
        return uncompleted

    def get_completed():
        completed = []
        for task in tasks:
            if task["is_complete"]:
                completed.append(task["description"])
        return completed

    def finish_task(task_id : int):
        if isinstance(task_id, int):
            try:
                tasks[task_id]["is_complete"] = True
            except IndexError:
                raise Exception(f"There is no task with id: {task_id}")
        else:
            raise Exception("Task_id must be an Integer!")

    def specify_tasks():
        for task in tasks:
            if task["is_complete"]:
                task["description"] = "[ X ] " + task["description"]
            else:
                task["description"] = "[  ] " + task["description"]

    return {"add_task" : add_task, "get_uncompleted": get_uncompleted, "get_completed": get_completed, "finish_task": finish_task, "specify_tasks": specify_tasks}


peter_todo = create_task_list()
peter_todo["add_task"]("Vynest smeti")
peter_todo["add_task"]("Uklidit si pokojicek")

print(peter_todo["get_uncompleted"]())

peter_todo["specify_tasks"]()

peter_todo["finish_task"](1)
print(peter_todo["get_completed"]())

