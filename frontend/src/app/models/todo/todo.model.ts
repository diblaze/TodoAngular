export class Todo {
  constructor(
    public id: number,
    public title: string,
    public completed: boolean,
    public marked_as_removed: boolean,
    public updatedAt: Date,
    public createdAt: Date
  ) {}
}
