import flet as ft


def main(page: ft.Page):
    page.title = "Todo App"
    page.theme_mode = ft.ThemeMode.LIGHT # For now, this is DARK by default
    page.scroll = "adaptive"

    tasks = ft.Column()

    def addTask(event: ft.Event):
        if inputField.value == "":
            inputField.error_text = "Please enter a task"
            inputField.focus()
            page.update()
            return
        task = ft.Row(
            [
                ft.Checkbox(
                    value=False,
                    # on_change=onCheckboxChange, TODO: Add on_change to Checkbox
                    tooltip="Mark task as complete",
                    label=inputField.value,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        tasks.controls.append(task)
        inputField.value = ""
        inputField.focus()
        page.update()

    inputField = ft.TextField(
        label="Add a task",
        hint_text="Enter task...",
        on_submit=addTask,
        width=500,
        height=50,
        autofocus=True,
    )

    submitBtn = ft.ElevatedButton(
        text="Submit",
        on_click=addTask,
        tooltip="Add a task",
        height=50,
        width=100,
    )

    taskInput = ft.Row(
        controls=[inputField, submitBtn],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    page.add(taskInput, tasks)


if __name__ == "__main__":
    # Start the app
    ft.app(target=main)
