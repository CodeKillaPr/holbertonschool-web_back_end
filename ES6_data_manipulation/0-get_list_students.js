export class GetListStudents {
  constructor(students) {
    this.students = students;
  }

  execute() {
    return this.students;
  }
}