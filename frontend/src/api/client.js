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
    // Студенты
    getStudents: () => request('/students'),
    createStudent: (data) => request('/students', { method: 'POST', body: JSON.stringify(data) }),
    deleteStudent: (id) => request(`/students/${id}`, { method: 'DELETE' }),

    // Предметы
    getSubjects: () => request('/subjects'),
    createSubject: (data) => request('/subjects', { method: 'POST', body: JSON.stringify(data) }),
    deleteSubject: (id) => request(`/subjects/${id}`, { method: 'DELETE' }),

    // Оценки (новая структура: current + final)
    getGrades: (params = {}) => {
        const qs = new URLSearchParams(params).toString();
        return request(`/grades${qs ? '?' + qs : ''}`);
    },
    createGrade: (data) => request('/grades', { method: 'POST', body: JSON.stringify(data) }),
    deleteGrade: (id) => request(`/grades/${id}`, { method: 'DELETE' }),

    // Рейтинг
    getRatingCombined: () => request('/rating'),
    getRatingAbsolute: () => request('/rating/absolute'),
    getRatingWeighted: () => request('/rating/weighted'),
    getStudentDetail: (id) => request(`/rating/student/${id}`),

    // Аналитика
    getDynamics: (p1, p2) => request(`/rating/dynamics?period1=${encodeURIComponent(p1)}&period2=${encodeURIComponent(p2)}`),

    // Экспорт
    exportCSV(group) {
        // Получаем текущий рейтинг
        return this.getRatingCombined().then(students => {
            // Фильтруем по группе
            const filtered = group
                ? students.filter(s => s.group === group)
                : students;

            // Формируем CSV вручную
            const BOM = '\uFEFF';
            const header = 'Место (абс);Место (взв);ФИО;Группа;Абс. балл;Взв. балл\n';
            const rows = filtered.map(s =>
                `${s.absolute_rank};${s.weighted_rank};${s.name};${s.group};${s.absolute_rating};${s.weighted_rating}`
            ).join('\n');

            const csv = BOM + header + rows;

            // Скачивание
            const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = `rating_${group || 'all'}.csv`;
            a.click();
            URL.revokeObjectURL(a.href);
        });
    }}