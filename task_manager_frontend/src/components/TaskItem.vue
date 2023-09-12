<template>
  <div class="card">
    <div class="card-body row align-items-start ">
      <div class="col">
        {{ task.title }}
      </div>
      <div class="col">
        {{ task.employee_id }}
      </div>
      <div class="col">
        {{ task.status }}
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'TaskItem',
  props: {
    task: {}
  }
}
</script>
<style>
body {
  background-color: #ffffff;
  color: rgba(12, 12, 12, 0.83);
}
</style>