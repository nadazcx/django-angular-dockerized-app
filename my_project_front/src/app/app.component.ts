import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NavbarComponent } from './navbar/navbar.component';
import { BrowserModule, bootstrapApplication } from '@angular/platform-browser';
import { CommonModule, NgFor } from '@angular/common';
import { ViewEmployeesComponent } from './view-employees/view-employees.component';
import { HttpClientModule } from '@angular/common/http';
import { AddEmployeeComponent } from './add-employee/add-employee.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,NavbarComponent,CommonModule,ViewEmployeesComponent,NgFor,  HttpClientModule,AddEmployeeComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  

})
export class AppComponent {
  title = 'my_project_front';
}

