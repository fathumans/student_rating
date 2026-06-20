import { useState, useEffect } from 'react';
import { api } from '../api/client';

export default function GradeManager() {
    const [students, setStudents] = useState([]);
    const [subjects, setSubjects] = useState([]);
    const [grades, setGrades] = useState([]);
    const [studentId, setStudentId] = useState('');
    const [subjectId, setSubjectId] = useState('');
    const [period, setPeriod] = useState('2024-осень');
    const [value, setValue] = useState(5);

    const load = async () => {
        try {
            const [s, sub, g] = await Promise.all([
                api.getStudents(),
                api.getSubjects(),
                api.getGrades()
            ]);
            setStudents(s);
            setSubjects(sub);
            setGrades(g);
        } catch (err) {
            console.error('Ошибка загрузки:', err);
            alert('Не удалось загрузить данные: ' + err.message);
        }
    };

    useEffect(() => { load(); }, []);

    const handleAdd = async (e) => {
        e.preventDefault();
        if (!studentId || !subjectId) {
            alert('Выберите студента и предмет');
            return;
        }
        try {
            await api.createGrade({
                student_id: Number(studentId),
                subject_id: Number(subjectId),
                period,
                value: Number(value)
            });
            setStudentId('');
            setSubjectId('');
            await load(); // ← await
        } catch (err) {
            console.error('Ошибка добавления оценки:', err);
            alert('Не удалось добавить оценку: ' + err.message);
        }
    };

    const handleDelete = async (id) => {
        if (!confirm('Удалить оценку?')) return;
        try {
            await api.deleteGrade(id);
            await load();
        } catch (err) {
            console.error('Ошибка удаления:', err);
            alert('Не удалось удалить: ' + err.message);
        }
    };

    const getName = (id, list) => list.find(x => x.id === id)?.name || id;

    return (
        <div>
            <h2>Оценки</h2>
            <form onSubmit={handleAdd} className="form-row">
                <select
                    value={studentId}
                    onChange={e => setStudentId(e.target.value)}
                    required
                >
                    <option value="">Студент</option>
                    {students.map(s => (
                        <option key={s.id} value={s.id}>{s.name}</option>
                    ))}
                </select>
                <select
                    value={subjectId}
                    onChange={e => setSubjectId(e.target.value)}
                    required
                >
                    <option value="">Предмет</option>
                    {subjects.map(s => (
                        <option key={s.id} value={s.id}>{s.name}</option>
                    ))}
                </select>
                <input
                    value={period}
                    onChange={e => setPeriod(e.target.value)}
                />
                <input
                    type="number"
                    min="2"
                    max="5"
                    value={value}
                    onChange={e => setValue(e.target.value)}
                />
                <button type="submit">Добавить</button>
            </form>
            <table className="data-table">
                <thead>
                <tr>
                    <th>Студент</th>
                    <th>Предмет</th>
                    <th>Период</th>
                    <th>Оценка</th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                {grades.map(g => (
                    <tr key={g.id}>
                        <td>{getName(g.student_id, students)}</td>
                        <td>{getName(g.subject_id, subjects)}</td>
                        <td>{g.period}</td>
                        <td>{g.value}</td>
                        <td>
                            <button className="btn-danger" onClick={() => handleDelete(g.id)}>
                                Удалить
                            </button>
                        </td>
                    </tr>
                ))}
                </tbody>
            </table>
        </div>
    );
}