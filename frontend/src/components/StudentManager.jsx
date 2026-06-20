import { useState, useEffect } from 'react';
import { api } from '../api/client';

export default function StudentManager() {
    const [students, setStudents] = useState([]);
    const [name, setName] = useState('');
    const [group, setGroup] = useState('БИН-24-1');

    const load = async () => {
        try {
            const data = await api.getStudents();
            setStudents(data);
        } catch (err) {
            console.error('Ошибка загрузки студентов:', err);
            alert('Не удалось загрузить студентов: ' + err.message);
        }
    };

    useEffect(() => { load(); }, []);

    const handleAdd = async (e) => {
        e.preventDefault();
        if (!name.trim()) return;
        try {
            await api.createStudent({ name: name.trim(), group: group.trim() });
            setName('');
            await load(); // ← await обязателен!
        } catch (err) {
            console.error('Ошибка добавления:', err);
            alert('Не удалось добавить студента: ' + err.message);
        }
    };

    const handleDelete = async (id) => {
        if (!confirm('Удалить студента?')) return;
        try {
            await api.deleteStudent(id);
            await load(); // ← await обязателен!
        } catch (err) {
            console.error('Ошибка удаления:', err);
            alert('Не удалось удалить: ' + err.message);
        }
    };

    return (
        <div>
            <h2>Студенты</h2>
            <form onSubmit={handleAdd} className="form-row">
                <input
                    placeholder="ФИО"
                    value={name}
                    onChange={e => setName(e.target.value)}
                    required
                />
                <input
                    placeholder="Группа"
                    value={group}
                    onChange={e => setGroup(e.target.value)}
                />
                <button type="submit">Добавить</button>
            </form>
            <table className="data-table">
                <thead>
                <tr><th>ID</th><th>ФИО</th><th>Группа</th><th></th></tr>
                </thead>
                <tbody>
                {students.map(s => (
                    <tr key={s.id}>
                        <td>{s.id}</td>
                        <td>{s.name}</td>
                        <td>{s.group}</td>
                        <td>
                            <button className="btn-danger" onClick={() => handleDelete(s.id)}>
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