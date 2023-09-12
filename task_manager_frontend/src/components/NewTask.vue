<template>
  <div>
    <div class="input-group mb-3">
      <span class="input-group-text" id="basic-addon1">Title</span>
      <input v-model="newTask.title" type="text" class="form-control" placeholder="Title" aria-label="Title"
             aria-describedby="basic-addon1">
    </div>
    <select v-model="newTask.employee_id" class="form-select" id="inputGroupSelect01">
      <option selected value=0>не назначен</option>
      <option v-for="employee in employees" :key="employee.id" :value="employee.id">{{ employee.name }}</option>
    </select>
    <select v-model="newTask.parent_id" class="form-select" id="inputGroupSelect01">
      <option selected>Родительская задача</option>
      <option v-for="task in tasks" :value="task.id">{{ task.title }}</option>
    </select>
    <label for="party">DeadLine</label>
    <input v-model="newTask.deadline" class="form-control" type="datetime-local"/>

    <button v-if="newTask.title" @click="createtask" type="button" class="btn btn-primary">New task</button>
  </div>
</template>
<script>
export default {
  name: 'NewTask',
  props: {
    employees: {},
    newTask: {},
    tasks: {}
  },
  methods: {
    createtask() {
      const data = {
        title: this.newTask.title,
        deadline: this.newTask.deadline,
        status: this.newTask.status
      }
      if (this.newTask.employee_id != '0') {
        data.employee_id = this.newTask.employee_id
      }
      if (this.newTask.parent_id != '0') {
        data.parent_id = this.newTask.parent_id

      }
      axios.post('http://localhost:8000/api/v1/tasks', data)
          .then(response => {
            this.tasks = response.data
            this.fetchTasks()
            this.newTask = {
              title: '',
              employee_id: 0,
              parent_id: 0,
              deadline: '',
              status: 1
            }
          })
    }
  }
}
</script>
<style>
body {
  background-color: #ffffff;
  color: rgba(12, 12, 12, 0.83);
}
</style>
