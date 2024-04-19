import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PublicacionModule } from './publicacion/publicacion.module';
import { PublicacionRoutingModule } from './publicacion/publicacion-routing.module';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    PublicacionModule,
    HttpClientModule,
    PublicacionRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
