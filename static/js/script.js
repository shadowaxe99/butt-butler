
document.addEventListener('DOMContentLoaded', (event) => {
    // Code to handle task assignment, tracking, and progress monitoring
    const taskElements = document.querySelectorAll('.task');

    taskElements.forEach((taskElement) => {
        taskElement.addEventListener('click', (event) => {
            const taskId = taskElement.dataset.taskId;
            fetch(`/api/tasks/${taskId}/`)
                .then(response => response.json())
                .then(task => {
                    // Update task UI
                    const taskStatusElement = document.querySelector(`#task-${taskId}-status`);
                    taskStatusElement.textContent = task.status;
                });
        });
    });
});
