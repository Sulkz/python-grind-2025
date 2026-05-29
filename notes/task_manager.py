allowed_status = ["todo","in_progress","done"]
allowed_priorities = ["low","medium","high"]

class Task:
    def __init__(self,task_id,title,status,priority):
        self.id = task_id
        self.title = title
        self.status = status
        self.priority = priority

class Manager:
    def __init__(self):
        self.total_tasks = dict()
    
    def create_task(self,task_id,title,status,priority):
        if not task_id or not title or not status or not priority:
            return            
        if status not in allowed_status or priority not in allowed_priorities:
            return
        if not isinstance(task_id,(int)):
            return
        if task_id in self.total_tasks:
            return 'Duplicate task'
        task = Task(task_id,title,status,priority)
        self.total_tasks[task_id] = task
   
        
    def update_task(self,task_id,new_status):
        if task_id in self.total_tasks and new_status in allowed_status:
            task_obj = self.total_tasks[task_id]
            if new_status != task_obj.status:
                task_obj.status = new_status
            else:
                return f"Status already: {task_obj.status}"
        else:
            return "Can not find task"
    
    def delete_task(self,task_id):
        if task_id in self.total_tasks:
            del self.total_tasks[task_id]
        else:
            return "Task not in records"
        
    
    def list_tasks(self):
        results = []
        for task_id, task_attributes in self.total_tasks.items():
            tasks = task_id,[task_attributes.title,task_attributes.status,task_attributes.priority]
            results.append(tasks)
        return results
        
            
  
    
        
    
        
        

        
