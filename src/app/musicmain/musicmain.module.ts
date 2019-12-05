import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { MusicmainPageRoutingModule } from './musicmain-routing.module';

import { MusicmainPage } from './musicmain.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    MusicmainPageRoutingModule
  ],
  declarations: [MusicmainPage]
})
export class MusicmainPageModule {}
