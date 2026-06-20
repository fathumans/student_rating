import { useState, useEffect } from 'react';
import { api } from '../api/client';

export default function SubjectManager() {
    const [subjects, setSubjects] = useState([]);
    const [name, setName] = useState('');
    const [type, setType] = useState('exam');
    const [weight, setWeight] = useState(0.5);

    const load = async () => {
        try {
            const data = await api.getSubjects();
            setSubjects(data);
        } catch (err) {
            console.error('Ошибка загрузки предметов:', err);
            alert('Не удалось загрузить предметы: ' + err.message);
        }
    };

    useEffect(() => { load(); }, []);

    const handleAdd = async (e) => {
        e.preventDefault();
        if (!name.trim()) return;
        try {
            await api.createSubject({
                name: name.trim(),
                type,
                weight: Number(weight)
            });
            setName('');
            await load(); // ← await
        } catch (err) {
            console.error('Ошибка добавления:', err);
            alert('Не удалось добавить предмет: ' + err.message);
        }
    };

    const handleDelete = async (id) => {
        if (!confirm('Удалить предмет?')) return;
        try {
            await api.deleteSubject(id);
            await load();
        } catch (err) {
            console.error('Ошибка удаления:', err);
            alert('Не удалось удалить: ' + err.message);
        }
    };

    return (
        <div>
            <h2>Предметы</h2>
            <form onSubmit={handleAdd} className="form-row">
                <input
                    placeholder="Название"
                    value={name}
                    onChange={e => setName(e.target.value)}
                    required
                />
                <select value={type} onChange={e => setType(e.target.value)}>
                    <option value="exam">Экзамен</option>
                    <option value="test">Зачёт</option>
                    <option value="practice">Практика</option>
                </select>
                <input
                    type="number"
                    step="0.1"
                    min="0"
                    max="1"
                    value={weight}
                    onChange={e => setWeight(e.target.value)}
                />
                <button type="submit">Добавить</button>
            </form>
            <table className="data-table">
                <thead>
                <tr><th>ID</th><th>Название</th><th>Тип</th><th>Вес</th><th></th></tr>
                </thead>
                <tbody>
                {subjects.map(s => (
                    <tr key={s.id}>
                        <td>{s.id}</td>
                        <td>{s.name}</td>
                        <td>{s.type}</td>
                        <td>{s.weight}</td>
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