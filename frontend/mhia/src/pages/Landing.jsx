import React from "react";
import InfoCard from "../components/ui/InfoCard";
import TestimonialsCarousel from "../components/ui/TestimonialsCarousel"; // Importar el componente del carrusel
import "../assets/css/Landing.css";

function Landing() {
  return (
    <>
      <h1>MHIA</h1>
      <section className="info-cards-container">
        <InfoCard
          title="¿Quiénes somos?"
          description="Somos un equipo apasionado por la salud mental y la tecnología..."
        />
        <InfoCard
          title="¿Qué hacemos?"
          description="Desarrollamos un asistente virtual con Inteligencia Artificial..."
        />
        <InfoCard
          title="¿Cómo lo hacemos?"
          description="Utilizamos algoritmos avanzados de procesamiento de lenguaje natural..."
        />
      </section>

      <section className="carousel-container">
        <TestimonialsCarousel />
      </section>
    </>
  );
}

export default Landing;