import { useState, useEffect } from 'react';
import { api } from '../api/client';

export default function GradeManager() {
    const [students, setStudents] = useState([]);
    const [subjects, setSubjects] = useState([]);
    const [grades, setGrades] = useState([]);
    const [studentId, setStudentId] = useState('');
    const [subjectId, setSubjectId] = useState('');
    const [period, setPeriod] = useState('2024-весна');
    const [current, setCurrent] = useState(35);
    const [final, setFinal] = useState(50);

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
        const cur = Number(current);
        const fin = Number(final);
        if (cur < 0 || cur > 40) {
            alert('Текущая аттестация: 0-40 баллов');
            return;
        }
        if (fin < 0 || fin > 60) {
            alert('Промежуточная аттестация: 0-60 баллов');
            return;
        }
        try {
            await api.createGrade({
                student_id: Number(studentId),
                subject_id: Number(subjectId),
                period,
                current: cur,
                final: fin,
            });
            setStudentId('');
            setSubjectId('');
            setCurrent(35);
            setFinal(50);
            await load();
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

    const getStatusColor = (total) => {
        if (total >= 91) return '#16a34a';
        if (total >= 76) return '#2563eb';
        if (total >= 61) return '#ca8a04';
        return '#dc2626';
    };

    return (
        <div>
            <h2>Оценки</h2>
            <form onSubmit={handleAdd} className="form-row">
                <select value={studentId} onChange={e => setStudentId(e.target.value)} required>
                    <option value="">Студент</option>
                    {students.map(s => <option key={s.id} value={s.id}>{s.name}</option>)}
                </select>
                <select value={subjectId} onChange={e => setSubjectId(e.target.value)} required>
                    <option value="">Предмет</option>
                    {subjects.map(s => <option key={s.id} value={s.id}>{s.name}</option>)}
                </select>
                <input type="text" value={period} onChange={e => setPeriod(e.target.value)} placeholder="Период" />
                <input type="number" min="0" max="40" value={current} onChange={e => setCurrent(e.target.value)} placeholder="Текущая (0-40)" />
                <input type="number" min="0" max="60" value={final} onChange={e => setFinal(e.target.value)} placeholder="Промежуточная (0-60)" />
                <button type="submit">Добавить</button>
            </form>
            <table className="data-table">
                <thead>
                <tr>
                    <th>Студент</th>
                    <th>Предмет</th>
                    <th>Период</th>
                    <th>Текущая (40)</th>
                    <th>Промеж. (60)</th>
                    <th>Итог</th>
                    <th>Оценка</th>
                    <th>Статус</th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                {grades.map(g => (
                    <tr key={g.id}>
                        <td>{getName(g.student_id, students)}</td>
                        <td>{getName(g.subject_id, subjects)}</td>
                        <td>{g.period}</td>
                        <td>{g.current}</td>
                        <td>{g.final}</td>
                        <td style={{fontWeight: 'bold', color: getStatusColor(g.total_score)}}>{g.total_score}</td>
                        <td>{g.grade}</td>
                        <td>{g.status}</td>
                        <td><button className="btn-danger" onClick={() => handleDelete(g.id)}>Удалить</button></td>
                    </tr>
                ))}
                </tbody>
            </table>
        </div>
    );
}