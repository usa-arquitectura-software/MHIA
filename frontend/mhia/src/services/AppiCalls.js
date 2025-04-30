const API_BASE_URL = 'http://localhost:8000';

export const api = {
  // Auth endpoints
  async login(email, password) {
    const response = await fetch(`${API_BASE_URL}/login_psycologist`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password }),
    });
    if (!response.ok) throw new Error('Login failed');
    return response.json();
  },

  async register(psychologistData) {
    const response = await fetch(`${API_BASE_URL}/register_psycologist`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(psychologistData),
    });
    if (!response.ok) throw new Error('Registration failed');
    return response.json();
  },

  // Protected endpoints
  async listPsychologists() {
    const response = await fetch(`${API_BASE_URL}/psycologist`);
    if (!response.ok) throw new Error('Failed to fetch psychologists');
    return response.json();
  }
};