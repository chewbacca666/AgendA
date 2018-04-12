import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { AlertController } from 'ionic-angular';
import { Platform } from 'ionic-angular'; 
import { StatusBar } from '@ionic-native/status-bar'
/**
 * Generated class for the SairPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-sair',
  templateUrl: 'sair.html'
})
export class SairPage {
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
  ionViewDidLoad() {
    console.log('ionViewDidLoad SairPage');
  }

}
