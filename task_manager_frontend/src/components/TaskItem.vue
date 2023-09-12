<template>
  <div class="card">
    <div class="card-body d-flex justify-content-between align-items-center">
      <div class="title">
        {{ task.title }}
      </div>
      <div v-if="employee.name != 'Не назначен'" class="empl">
        {{ employee.name }}
      </div>
      <div class="d-flex justify-content-between align-items-center">
        <div class="status">
          {{ statusEnum[task.status] }}
        </div>
        <div>
          <button type="button" @click="deleteTask(task.id)" class="btn btn-primary">Х</button>
        </div>
      </div>

    </div>
  </div>
</template>
<script>
export default {
  name: 'TaskItem',
  props: {
    task: {}
  },
  data() {
    return {
      employee: {},
      statusEnum: {
        1: "BACKLOG",
        2: "SPRINT_CANDIDATE",
        3: "SPIRIT_BACKLOG",
        4: "ON_GOING",
        5: "REVIEW",
        6: "QA",
        7: "DOCUMENTATION",
        8: "APPROVAL_BY_CUSTOMER",
        9: "DONE"

      }
    }
  },
  methods: {
    fetchEmployee(employee_id) {
      if (!employee_id) {
        this.employee = {name: 'Не назначен'}
        return
      }
      const url = 'http://localhost:8000/api/v1/employees/' + employee_id
      axios.get(url)
          .then(response => {
            this.employee = response.data
          })
    },
    deleteTask(task_id) {
      const url = 'http://localhost:8000/api/v1/tasks/' + task_id
      axios.delete(url)
          .then(response => {
            this.tasks = null
          }).then(() => {
        this.$emit('task-deleted')
        console.log('task deleted')
      })
    }
  },
  mounted() {
    this.fetchEmployee(this.task.employee_id)
  }
}

</script>
<style scoped>
.title {
  width: 300px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;

}

.empl {
  width: 200px;

}

.status {
  width: 200px;

}
</style>
