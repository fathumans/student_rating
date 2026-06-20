const API_URL = '/api';

async function request(path, options = {}) {
    const url = `${API_URL}${path}`;
    const res = await fetch(url, {
        headers: { 'Content-Type': 'application/json', ...options.headers },
        ...options,
    });
    if (!res.ok) {
        const err = await res.text();
        throw new Error(err || res.statusText);
    }
    if (res.status === 204) return null;
    return res.json();
}

export const api = {
    getStudents: () => request('/students'),
    createStudent: (data) => request('/students', { method: 'POST', body: JSON.stringify(data) }),
    deleteStudent: (id) => request(`/students/${id}`, { method: 'DELETE' }),

    getSubjects: () => request('/subjects'),
    createSubject: (data) => request('/subjects', { method: 'POST', body: JSON.stringify(data) }),
    deleteSubject: (id) => request(`/subjects/${id}`, { method: 'DELETE' }),

    getGrades: () => request('/grades'),
    createGrade: (data) => request('/grades', { method: 'POST', body: JSON.stringify(data) }),
    deleteGrade: (id) => request(`/grades/${id}`, { method: 'DELETE' }),

    getRating: () => request('/rating'),
    getProblems: (threshold = 0.15) => request(`/rating/problems?threshold=${threshold}`),
    getDynamics: (p1, p2) => request(`/rating/dynamics?period1=${encodeURIComponent(p1)}&period2=${encodeURIComponent(p2)}`),
    exportCSV: () => window.open(`${API_URL}/rating/export`, '_blank'),
};