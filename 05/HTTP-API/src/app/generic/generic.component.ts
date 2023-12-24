import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap } from '@angular/router';
import { Observable } from 'rxjs';
import { Root } from '../model/data.model';
import { RequestService } from '../service/request.service';

@Component({
  selector: 'app-generic',
  templateUrl: './generic.component.html',
  styleUrls: ['./generic.component.css']
})

export class GenericComponent implements OnInit{
    query: any;
    routeObs: Observable<ParamMap> | undefined;
    obs: Observable<Object> | undefined;
    result: any;

    constructor(private route: ActivatedRoute, private request: RequestService) {}

    ngOnInit(): void {
        this.routeObs = this.route.paramMap;
        this.routeObs.subscribe(this.getRouterParam);
        
    }
    
    getRouterParam = (params: ParamMap) => {
        console.log(params);

        this.query = params.get('id');
        this.obs = this.request.searchInfo(this.query)
        this.obs.subscribe((data) => {
            this.result = data;
        })
    };
}

