import { Injectable } from '@angular/core';
import * as regularIcons from '@fortawesome/free-regular-svg-icons';
import * as solidIcons from '@fortawesome/free-solid-svg-icons';

@Injectable({
  providedIn: 'root'
})
export class IconService {

  icons = {
    home: solidIcons.faHouse, // icons.home
    // Add more icons here...
  };

  constructor() { }

  get importIcons() {
    return this.icons;
  }
}
