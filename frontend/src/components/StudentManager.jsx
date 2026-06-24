import { useState, useEffect } from 'react';
import { api } from '../api/client';

export default function StudentManager({ group }) {
    const [students, setStudents] = useState([]);
    const [name, setName] = useState('');
    const [groupInput, setGroupInput] = useState(group);

    useEffect(() => {
        api.getStudents().then(s => setStudents(s)).catch(err => alert('Ошибка: ' + err.message));
    }, []);

    useEffect(() => {
        setGroupInput(group);
    }, [group]);

    const handleAdd = async (e) => {
        e.preventDefault();
        if (!name.trim()) return;
        try {
            await api.createStudent({ name, group: groupInput });
            setName('');
            setStudents(await api.getStudents());
        } catch (err) { alert('Ошибка: ' + err.message); }
    };

    const handleDelete = async (id) => {
        if (!confirm('Удалить?')) return;
        try { await api.deleteStudent(id); setStudents(await api.getStudents()); }
        catch (err) { alert('Ошибка: ' + err.message); }
    };

    const groupStudents = group ? students.filter(s => s.group === group) : students;

    return (
        <div>
            <h5 className="mb-3">Студенты — {group}</h5>
            <form onSubmit={handleAdd} className="row g-2 mb-3">
                <div className="col-md-6"><input type="text" className="form-control form-control-sm" placeholder="ФИО" value={name} onChange={e => setName(e.target.value)} /></div>
                <div className="col-md-3"><input type="text" className="form-control form-control-sm" placeholder="Группа" value={groupInput} onChange={e => setGroupInput(e.target.value)} /></div>
                <div className="col-md-3"><button type="submit" className="btn btn-sm btn-outline-secondary w-100">Добавить</button></div>
            </form>
            <table className="table table-sm">
                <tbody>
                {groupStudents.map(s => (
                    <tr key={s.id}>
                        <td>{s.name}</td>
                        <td className="text-muted small">{s.group}</td>
                        <td className="text-end"><button className="btn btn-sm text-danger p-0" onClick={() => handleDelete(s.id)}>Удалить</button></td>
                    </tr>
                ))}
                </tbody>
            </table>
        </div>
    );
}