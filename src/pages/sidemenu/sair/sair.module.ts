import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { SairPage } from './sair';
import { AlertController } from 'ionic-angular'; 
@NgModule({
  declarations: [
    SairPage,
  ],
  imports: [
    IonicPageModule.forChild(SairPage),
  ],
})
export class SairPageModule {
  platform: any;
  constructor(public alertCtrl: AlertController) {}
    doConfirm(){
      let confirm = this.alertCtrl.create({
        title: 'Tem certeza que queres sair?',
        buttons: [
          {
            text: 'Cancelar',
            handler: () => {
              console.log('Cancelar clicked');
              false;
            }
          },
          {
            text: 'Continuar',
            handler: () => {
              console.log('Continuar clicked');
              this.platform.exitApp();
            }
          }
        ]
      });
      confirm.present()
    }
}
