import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { RequestService } from './service/request.service';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
})

export class AppComponent{
    title = 'HTTP-API';
}
