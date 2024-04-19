import { Component, OnInit } from '@angular/core';
import { PublicacionService } from '../publicacion.service';
import { Publicacion } from '../publicacion';


@Component({
  selector: 'app-publicacion-list',
  templateUrl: './publicacion-list.component.html',
  styleUrls: ['./publicacion-list.component.css']
})

export class PublicacionListComponent implements OnInit {

  publicaciones: Array<Publicacion> = [];
  classification: number = 0.0;
  constructor(private publicacionService: PublicacionService) { }

  ngOnInit() {
    this.getPublicaciones();
    this.getCalification();

  }

  getPublicaciones(): void{
    this.publicacionService.getPublicaciones().subscribe(
      (publicaciones) => {this.publicaciones = publicaciones;},
    );
  }

  getCalification(): void {
    this.publicacionService.getCalification().subscribe((prediction) => {
      this.classification = prediction['classification'];

    });
    //this.publicacionService.postPublicacion({"text": text, "person": "TrashCam9"}).subscribe()
  }

}
