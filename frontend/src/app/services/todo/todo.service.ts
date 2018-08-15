import { Injectable } from "@angular/core";
import { HttpClient, HttpErrorResponse } from "@angular/common/http";
import { Observable } from "rxjs";
import { Todo } from "../../models/todo/todo.model";
import { API_BASE } from "../../env";

@Injectable({
    providedIn: "root"
})
export class TodoService {
    constructor(private http: HttpClient) {}

    getTodos(): Observable<Todo[]> {
        return this.http.get<Todo[]>(`${API_BASE}/todos`);
    }
}
