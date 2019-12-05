import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { MusicmainPage } from './musicmain.page';

const routes: Routes = [
  {
    path: '',
    component: MusicmainPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class MusicmainPageRoutingModule {}
