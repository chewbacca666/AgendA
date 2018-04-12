import { BrowserModule } from '@angular/platform-browser';
import { ErrorHandler, NgModule } from '@angular/core';
import { IonicApp, IonicErrorHandler, IonicModule } from 'ionic-angular';

import { MyApp } from './app.component';
import { HomePage } from '../pages/eventos/home';
import { ListPage } from '../pages/list/list';
import { NgCalendarModule  } from 'ionic2-calendar';

import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';
import { ConfigPage } from '../pages/sidemenu/config/config';
import { MeusPage } from '../pages/sidemenu/meus/meus';
import { PerfilPage } from '../pages/sidemenu/perfil/perfil';
import { PainelPage } from '../pages/sidemenu/painel/painel';
import { SairPage } from '../pages/sidemenu/sair/sair';
import { InicioPage } from '../pages/inicio/inicio';

@NgModule({
  declarations: [
    MyApp,
    HomePage,
    ListPage,
    ConfigPage,
    MeusPage,
    PainelPage,
    PerfilPage,
    SairPage,
    InicioPage,
  ],
  imports: [
    NgCalendarModule,
    BrowserModule,
    IonicModule.forRoot(MyApp),
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    HomePage,
    ListPage,
    ConfigPage,
    MeusPage,
    PerfilPage,
    PainelPage,
    SairPage,
    InicioPage,
  ],
  providers: [
    StatusBar,
    SplashScreen,
    {provide: ErrorHandler, useClass: IonicErrorHandler}
  ]
})
export class AppModule {}
