import { useState, useEffect } from 'react';
import { api } from '../api/client';

const TYPES = { exam: 'Экзамен', test: 'Зачёт', practice: 'Практика' };

export default function SubjectManager() {
    const [subjects, setSubjects] = useState([]);
    const [name, setName] = useState('');
    const [type, setType] = useState('exam');

    useEffect(() => {
        api.getSubjects().then(setSubjects).catch(err => alert('Ошибка: ' + err.message));
    }, []);

    const handleAdd = async (e) => {
        e.preventDefault();
        if (!name.trim()) return;
        const weights = { exam: 1.0, test: 0.6, practice: 1.0 };
        try {
            await api.createSubject({ name, type, weight: weights[type] });
            setName('');
            setSubjects(await api.getSubjects());
        } catch (err) { alert('Ошибка: ' + err.message); }
    };

    const handleDelete = async (id) => {
        if (!confirm('Удалить?')) return;
        try { await api.deleteSubject(id); setSubjects(await api.getSubjects()); }
        catch (err) { alert('Ошибка: ' + err.message); }
    };

    return (
        <div>
            <form onSubmit={handleAdd} className="row g-3 mb-4">
                <div className="col-md-6">
                    <input type="text" className="form-control form-control-sm" placeholder="Название" value={name} onChange={e => setName(e.target.value)} />
                </div>
                <div className="col-md-3">
                    <select className="form-select form-select-sm" value={type} onChange={e => setType(e.target.value)}>
                        <option value="exam">Экзамен</option>
                        <option value="test">Зачёт</option>
                        <option value="practice">Практика</option>
                    </select>
                </div>
                <div className="col-md-3">
                    <button type="submit" className="btn btn-sm btn-outline-secondary w-100">Добавить</button>
                </div>
            </form>
            <table className="table table-sm">
                <tbody>
                {subjects.map(s => (
                    <tr key={s.id}>
                        <td>{s.name}</td>
                        <td className="text-muted small text-center">{TYPES[s.type]}</td>
                        <td className="text-muted small text-center">{s.weight}</td>
                        <td className="text-end"><button className="btn btn-sm text-danger p-0" onClick={() => handleDelete(s.id)}>Удалить</button></td>
                    </tr>
                ))}
                </tbody>
            </table>
        </div>
    );
}