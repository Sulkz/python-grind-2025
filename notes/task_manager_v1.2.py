valid_status = ["todo","in_progress","done"]
valid_priority = ["low","medium","high"]
class Task:
    def __init__(self,task_id,title,status,priority):
        self.task_id = task_id
        self.title = title
        self.status = status
        self.priority = priority


class Manager:
    def __init__(self):
        self.record = dict()
    
    def create_task(self,task_id,title,status,priority):
        task = Task(task_id,title,status,priority)
        if task.task_id in self.record:
            return "The task is already in the record"
        if task.title == "":
            return "can not enter non empty title"
        if task.stauts not in valid_status or task.priority not in valid_priority:
            return "Invalid status or priority"
        self.record[task.task_id] = task
        return f"Task:{task_id} created"

    def update_status(self,task_id,new_status):
        if task_id in self.record and new_status in valid_status:
            task = self.record[task_id]
            if new_status != task.status:
                task.status = new_status
            else:
                return f"Task: {task_id} is already in this status"
        else:
            return "This task doesnt exist"
        
    def delete_task(self,task_id):
        if task_id in self.record:
            del self.record[task_id]
            return f"Task: {task_id} deleted"
        else:
            return f"Task: {task_id} doesnt exist"
    
    def list_tasks(self,status=None,priority=None):
        if status is None and priority is None:
            for task_id, info in self.record.items():
                return f"Task_id: {task_id}, title:{info.title}, status: {info.status}, priority: {info.priority}"
        
        if status in valid_status and priority is None:
            for task_id, info in self.record.items():
                if info.status == status:
                    return f"Task_id: {task_id}, title:{info.title}, status: {info.status}, priority: {info.priority}"
    
    
        if priority in valid_status and status is None:
            for task_id, info in self.record.items():
                if info.priority == priority:
                    return f"Task_id: {task_id}, title:{info.title}, status: {info.status}, priority: {info.priority}"
                
    def summary(self):
        results = {
            "total": len(self.record),
            "by_status": {
                "todo": 0,
                "in_progress": 0,
                "done": 0
            },
            "by_priority": {
                "low": 0,
                "medium": 0,
                "high": 0
            }
        }

        for task in self.record.values():
            results["by_status"][task.status] += 1
            results["by_priority"][task.priority] += 1

        return results
                
                
                