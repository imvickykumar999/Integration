import axios from 'axios';

const API_URL = 'http://localhost:8000/';

// Create axios instance with default config
const api = axios.create({
    baseURL: API_URL,
    withCredentials: true,  // Important for handling cookies/sessions
    headers: {
        'Content-Type': 'application/json',
    },
});

// Auth services
export const authService = {
    login: async (email, password) => {
        const response = await api.post('/accounts/api/login/', { email, password });
        return response.data;
    },

    register: async (userData) => {
        try {
            // Format the data according to the backend's expectations
            const registrationData = {
                email: userData.email,
                password: userData.password,
                confirm_password: userData.confirm_password,
                first_name: userData.first_name,
                last_name: userData.last_name,
                role: userData.role,
                phone: userData.phone || '',
                company_name: userData.company_name,
                registration_number: userData.registration_number,
                industry: userData.industry,
                address: userData.address || '',
                city: userData.city || '',
                state: userData.state || '',
                postal_code: userData.postal_code || '',
                country: userData.country || '',
                website: userData.website || ''
            };

            const response = await api.post('/accounts/api/register/', registrationData);
            return response.data;
        } catch (error) {
            if (error.response?.data) {
                // Handle specific backend validation errors
                const errorData = error.response.data;
                if (typeof errorData === 'object') {
                    const errorMessages = Object.entries(errorData)
                        .map(([field, messages]) => `${field}: ${messages.join(', ')}`)
                        .join('\n');
                    throw new Error(errorMessages);
                }
                throw new Error(errorData.error || 'Registration failed');
            }
            throw error;
        }
    },

    logout: async () => {
        const response = await api.post('/accounts/api/logout/');
        return response.data;
    },

    getCurrentUser: async () => {
        const response = await api.get('/accounts/api/user/');
        return response.data;
    },

    getCompanyProfile: async (companyId) => {
        const response = await api.get(`/companies/api/profile/${companyId}/`);
        return response.data;
    },
};

// Add request interceptor to handle errors
api.interceptors.response.use(
    (response) => response,
    (error) => {
        if (error.response) {
            // The request was made and the server responded with a status code
            // that falls out of the range of 2xx
            console.error('API Error:', error.response.data);
            return Promise.reject(error.response.data);
        } else if (error.request) {
            // The request was made but no response was received
            console.error('API Error: No response received');
            return Promise.reject({ error: 'No response received from server' });
        } else {
            // Something happened in setting up the request that triggered an Error
            console.error('API Error:', error.message);
            return Promise.reject({ error: error.message });
        }
    }
);

export default api; 