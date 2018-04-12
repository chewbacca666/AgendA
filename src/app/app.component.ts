import { Component, ViewChild } from '@angular/core';
import { Nav, Platform, ToastController, Icon } from 'ionic-angular';
import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';
import { HomePage } from '../pages/eventos/home';
import { ListPage } from '../pages/list/list';
import { ConfigPage } from '../pages/sidemenu/config/config';
import { SairPage } from '../pages/sidemenu/sair/sair';
import { MeusPage } from '../pages/sidemenu/meus/meus';
import { PerfilPage } from '../pages/sidemenu/perfil/perfil';
import { PainelPage } from '../pages/sidemenu/painel/painel';
import { InicioPage } from '../pages/inicio/inicio';
@Component({
  templateUrl: 'app.html'
})
export class MyApp {
  [x: string]: any;
  @ViewChild(Nav) nav: Nav;

  rootPage: any = InicioPage;

  pages: Array<{title: string, component: any}>;
  public 
  constructor(public platform: Platform, public statusBar: StatusBar, public splashScreen: SplashScreen, public toastCtrl: ToastController) {
    /*this.initializeApp();*/
    platform.ready().then(() => {
      statusBar.styleDefault();
      splashScreen.hide();
 
      platform.registerBackButtonAction(() => {
        if (this.counter == 0) {
          this.counter++;
          this.presentToast();
          setTimeout(() => { this.counter = 0 }, 3000)
        } else {
          console.log("exitapp");
          platform.exitApp();
        }
      }, 0)
    });
  

    // used for an example of ngFor and navigation
    this.pages = [
      { title: 'Painel', component: PainelPage},
      { title: 'Perfil', component: PerfilPage},
      { title: 'Meus eventos', component: HomePage}, 
      { title: 'List', component: ListPage},
      { title: 'Meus grupos', component:MeusPage},
      { title: 'Configuração', component: ConfigPage},
      { title: 'Sair', component: SairPage},
    ];

  }
  presentToast(){
    let toast = this.toastCtrl.create({
      message: "Press again to exit",
      duration: 3000,
      position: "middle"
    })
    toast.present();
  }
  initializeApp() {
    this.platform.ready().then(() => {
      // Okay, so the platform is ready and our plugins are available.
      // Here you can do any higher level native things you might need.
      this.statusBar.styleDefault();
      this.splashScreen.hide();
    });
  }

  openPage(page) {
    // Reset the content nav to have just this page
    // we wouldn't want the back button to show in this scenario
    this.nav.setRoot(page.component);
  }
}
