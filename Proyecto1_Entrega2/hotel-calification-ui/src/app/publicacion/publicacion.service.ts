import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

import { Publicacion } from './publicacion';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PublicacionService {

  private apiUrl: string = environment.baseUrl;

  constructor(private http: HttpClient) { }

  getPublicaciones(): Observable<Publicacion[]> {

    return this.http.get<Publicacion[]>(this.apiUrl + 'reviews/');
  }

  getCalification(): Observable<any> {

    return this.http.get<Publicacion[]>(this.apiUrl + 'classification/');
  }

  predictText(text: string): Observable<any> {
    return this.http.post<any>(this.apiUrl + 'predict/', { "review": text });
  }

  postPublicacion(publicacion: any): Observable<Publicacion> {
    return this.http.post<any>(this.apiUrl + 'reviews/create/', publicacion);
  }

}
