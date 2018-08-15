import { Component, OnInit } from "@angular/core";
import { Todo } from "./models/todo/todo.model";
import { TodoService } from "./services/todo/todo.service";

@Component({
    selector: "app-root",
    templateUrl: "./app.component.html",
    styleUrls: ["./app.component.sass"]
})
export class AppComponent implements OnInit {
    title = "Angular - Todo";

    todoList: Todo[];

    constructor(private todoApi: TodoService) {}

    ngOnInit(): void {
        this.todoApi.getTodos().subscribe(res => {
            this.todoList = res;
        }, console.error);
    }
}
