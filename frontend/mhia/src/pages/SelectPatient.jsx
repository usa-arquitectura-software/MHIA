import React, { useState } from 'react';
import '../assets/css/SelectPatient.css'; // Importa los estilos CSS

function SelectPatient() {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedPatient, setSelectedPatient] = useState(null);

  // Datos de ejemplo de pacientes (reemplaza con tus datos reales)
  const patients = [
    { id: 1, name: 'Juan Pérez', cedula: '123456789', gender: 'Masculino', age: 35, consultaId: 'C001' },
    { id: 2, name: 'María Gómez', cedula: '987654321', gender: 'Femenino', age: 28, consultaId: 'C002' },
    { id: 3, name: 'Carlos Rodríguez', cedula: '456789123', gender: 'Masculino', age: 42, consultaId: 'C003' },
  ];

  // Filtrar pacientes según el término de búsqueda
  const filteredPatients = patients.filter(patient =>
    patient.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    patient.cedula.includes(searchTerm)
  );

  // Función para manejar la selección de un paciente
  const handlePatientSelect = (patient) => {
    setSelectedPatient(patient);
  };

  return (
    <div className="select-patient-container">
      <div className="header">
        <h1>MEDICO</h1>
        <p>Nombre del médico</p> 
      </div>

      <div className="search-bar">
        <input
          type="text"
          placeholder="Buscar pacientes..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
      </div>

      <table className="patients-table">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Cédula</th>
            <th>Género</th>
            <th>Edad</th>
            <th>ID Consulta</th>
            <th>Seleccionar paciente</th> 
          </tr>
        </thead>
        <tbody>
          {filteredPatients.map(patient => (
            <tr key={patient.id}>
              <td>{patient.name}</td>
              <td>{patient.cedula}</td>
              <td>{patient.gender}</td>
              <td>{patient.age}</td>
              <td>{patient.consultaId}</td>
              <td>
                <button onClick={() => handlePatientSelect(patient)}>+</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {selectedPatient && (
        <div className="selected-patient">
          <h2>Paciente seleccionado:</h2>
          <p>Nombre: {selectedPatient.name}</p>
          <p>Cédula: {selectedPatient.cedula}</p>
          {/* ... muestra más información del paciente */}
        </div>
      )}
    </div>
  );
}

export default SelectPatient;