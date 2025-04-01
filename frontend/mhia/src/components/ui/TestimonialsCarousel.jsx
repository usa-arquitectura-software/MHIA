import React from "react";
import InfoCard from "./InfoCard";
import { Carousel } from "react-responsive-carousel";
import "react-responsive-carousel/lib/styles/carousel.min.css";
import paciente from "../../assets/img/descargar.jpg";

function TestimonialsCarousel() {
  const testimonials = [
    {
      description:
        "MHIA me ha ayudado mucho a comprender mejor a mis pacientes. ¡Es una herramienta increíble!",
      patientImage: paciente,
      rating: 5,
    },
    {
      description:
        "Gracias a MHIA, puedo dedicar más tiempo a mis pacientes y menos tiempo a la documentación.",
      patientImage: paciente,
      rating: 4,
    },
    {
      description:
        "MHIA ha mejorado significativamente la calidad de mis sesiones. ¡Lo recomiendo ampliamente!",
      patientImage: paciente,
      rating: 5,
    },
  ];

  return (
    <Carousel
      showArrows={true}
      showThumbs={false}
      infiniteLoop={true}
      centerMode={true}
      centerSlidePercentage={80}
    >
      {testimonials.map((testimonial, index) => (
        <div key={index}>
          <InfoCard {...testimonial} />
        </div>
      ))}
    </Carousel>
  );
}

export default TestimonialsCarousel;
