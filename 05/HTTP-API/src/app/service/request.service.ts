import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
    providedIn: 'root'
})

export class RequestService {

    constructor(private http: HttpClient) { }

    searchInfo(query: any) {
        const url = `http://127.0.0.1:5000/${query}Html`;

        let obsTracks = this.http.get(url);
        return obsTracks;
    }
}
