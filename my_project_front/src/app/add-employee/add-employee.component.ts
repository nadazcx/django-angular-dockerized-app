import { Component } from '@angular/core';
import { EmployeeService } from '../employee.service';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';

@Component({
  selector: 'app-add-employee',
  templateUrl: './add-employee.component.html',
  styleUrls: ['./add-employee.component.css'],
  standalone: true,
  imports: [
    FormsModule // Add FormsModule here
  ],
})
export class AddEmployeeComponent {
  employee = {
    name: '',
    department: '',
    salary: '',
    function: ''
  };

  constructor(private employeeService: EmployeeService) { }

  addEmployee(): void {
    this.employeeService.addEmployee(this.employee).subscribe(
      response => {
        console.log('Employee added:', response);
        // Clear the form or give feedback
      },
      error => {
        console.error('Error adding employee:', error);
      }
    );
  }
}
