import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { MusicmainPage } from './musicmain.page';

describe('MusicmainPage', () => {
  let component: MusicmainPage;
  let fixture: ComponentFixture<MusicmainPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MusicmainPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(MusicmainPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
