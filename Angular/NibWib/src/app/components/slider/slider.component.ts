import { Component } from '@angular/core';


interface Image {
  url: string;
  alt: string;
  active?: boolean; 
}

@Component({
  selector: 'app-slider',
  templateUrl: './slider.component.html',
  styleUrls: ['./slider.component.css']
})
export class SliderComponent {
  images: Image[] = [
    { url: 'assets/img/sushi_slider.jpg', alt: 'Image 1' },
    { url: 'assets/img/burger_slider.jpg', alt: 'Image 2' },
    { url: 'assets/img/pizza_slider.jpeg', alt: 'Image 3' }
  ];

  currentIndex = 0;

  prevSlide() {
    if (this.currentIndex > 0) {
      this.currentIndex--;
    } else {
      this.currentIndex = this.images.length - 1;
    }
    this.updateActiveSlide();
  }
  
  nextSlide() {
    if (this.currentIndex < this.images.length - 1) {
      this.currentIndex++;
    } else {
      this.currentIndex = 0;
    }
    this.updateActiveSlide();
  }
  
  updateActiveSlide() {
    this.images.forEach((image, index) => {
      image.active = index === this.currentIndex;
    });
  }
}
