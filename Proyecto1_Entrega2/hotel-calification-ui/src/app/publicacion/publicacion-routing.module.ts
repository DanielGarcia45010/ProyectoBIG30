import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { PublicacionListComponent } from './publicacion-list/publicacion-list.component';
import { PublicacionCreateComponent } from './publicacion-create/publicacion-create.component';
const routes: Routes = [{
  path: 'posts',
  children: [
    {
      path: 'list',
      component: PublicacionListComponent
    },
    {
      path: 'create',
      component: PublicacionCreateComponent
    }
  ]
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PublicacionRoutingModule { }
