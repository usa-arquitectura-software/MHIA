import React from "react";

const InfoCard = ({ title, description, patientImage, rating }) => {
  return (
    <div className="info-card">
      <h2>{title}</h2>
      {patientImage && <img src={patientImage} alt="Imagen" />}
      <p>{description}</p>
      {rating && (
        <div>
          {Array.from({ length: rating }).map((_, index) => (
            <span key={index}>★</span>
          ))}
        </div>
      )}
    </div>
  );
};

export default InfoCard;