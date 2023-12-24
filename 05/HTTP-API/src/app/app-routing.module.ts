import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { GenericComponent } from './generic/generic.component';

const routes: Routes = [
    { path: 'generic/:id', component: GenericComponent }
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule { }
