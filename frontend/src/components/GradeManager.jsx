import { useState, useEffect, useMemo } from 'react';
import { api } from '../api/client';

export default function GradeManager({ group }) {
    const [students, setStudents] = useState([]);
    const [subjects, setSubjects] = useState([]);
    const [allGrades, setAllGrades] = useState([]);
    const [grades, setGrades] = useState([]);

    const [filterStudent, setFilterStudent] = useState('');
    const [filterSubject, setFilterSubject] = useState('');
    const [filterPeriod, setFilterPeriod] = useState('');

    const [studentId, setStudentId] = useState('');
    const [subjectId, setSubjectId] = useState('');
    const [period, setPeriod] = useState('2026-весна');
    const [current, setCurrent] = useState(35);
    const [final, setFinal] = useState(50);

    useEffect(() => {
        Promise.all([api.getStudents(), api.getSubjects(), api.getGrades()])
            .then(([s, sub, g]) => { setStudents(s); setSubjects(sub); setAllGrades(g); setGrades(g); })
            .catch(err => alert('Ошибка загрузки: ' + err.message));
    }, []);

    // Фильтруем студентов по группе
    const groupStudents = useMemo(() => {
        if (!group) return students;
        return students.filter(s => s.group === group);
    }, [students, group]);

    useEffect(() => {
        let f = [...allGrades];
        // Фильтр по студентам группы
        const groupStudentIds = new Set(groupStudents.map(s => s.id));
        f = f.filter(g => groupStudentIds.has(g.student_id));

        if (filterStudent) f = f.filter(g => g.student_id === Number(filterStudent));
        if (filterSubject) f = f.filter(g => g.subject_id === Number(filterSubject));
        if (filterPeriod) f = f.filter(g => g.period === filterPeriod);
        setGrades(f);
    }, [filterStudent, filterSubject, filterPeriod, allGrades, groupStudents]);

    const periods = [...new Set(allGrades.map(g => g.period))].sort();

    const getSubjectType = (subjectId) => subjects.find(s => s.id === subjectId)?.type;

    const getDisplayStatus = (grade) => {
        const subjectType = getSubjectType(grade.subject_id);
        const total = grade.total_score;
        if (subjectType === 'test' || subjectType === 'practice') {
            return total >= 61 ? 'Зачёт' : 'Незачёт';
        }
        return grade.status;
    };

    const getDisplayGrade = (grade) => {
        const subjectType = getSubjectType(grade.subject_id);
        if (subjectType === 'test' || subjectType === 'practice') {
            return grade.total_score >= 61 ? 'Зачёт' : 'Незачёт';
        }
        return grade.grade;
    };


    const handleAdd = async (e) => {
        e.preventDefault();
        if (!studentId || !subjectId) return alert('Выберите студента и предмет');
        const cur = Number(current), fin = Number(final);
        if (cur < 0 || cur > 40 || fin < 0 || fin > 60) return alert('Неверные баллы');
        try {
            await api.createGrade({ student_id: Number(studentId), subject_id: Number(subjectId), period, current: cur, final: fin });
            setStudentId(''); setSubjectId(''); setCurrent(35); setFinal(50);
            const g = await api.getGrades();
            setAllGrades(g);
            // Переприменяем фильтры
            const groupStudentIds = new Set(groupStudents.map(s => s.id));
            let f = g.filter(gr => groupStudentIds.has(gr.student_id));
            setGrades(f);
        } catch (err) { alert('Ошибка: ' + err.message); }
    };

    const handleDelete = async (id) => {
        if (!confirm('Удалить?')) return;
        try {
            await api.deleteGrade(id);
            const g = await api.getGrades();
            setAllGrades(g);
            const groupStudentIds = new Set(groupStudents.map(s => s.id));
            setGrades(g.filter(gr => groupStudentIds.has(gr.student_id)));
        } catch (err) { alert('Ошибка: ' + err.message); }
    };

    const getName = (id, list) => list.find(x => x.id === id)?.name || id;

    const resetFilters = () => {
        setFilterStudent(''); setFilterSubject(''); setFilterPeriod('');
    };

    return (
        <div>
            <h5 className="mb-3">Оценки — {group}</h5>

            <div className="row g-2 mb-2">
                <div className="col-md-3">
                    <select className="form-select form-select-sm" value={filterStudent} onChange={e => setFilterStudent(e.target.value)}>
                        <option value="">Все студенты</option>
                        {groupStudents.map(s => <option key={s.id} value={s.id}>{s.name}</option>)}
                    </select>
                </div>
                <div className="col-md-3">
                    <select className="form-select form-select-sm" value={filterSubject} onChange={e => setFilterSubject(e.target.value)}>
                        <option value="">Все предметы</option>
                        {subjects.map(s => <option key={s.id} value={s.id}>{s.name}</option>)}
                    </select>
                </div>
                <div className="col-md-3">
                    <select className="form-select form-select-sm" value={filterPeriod} onChange={e => setFilterPeriod(e.target.value)}>
                        <option value="">Все периоды</option>
                        {periods.map(p => <option key={p} value={p}>{p}</option>)}
                    </select>
                </div>
                <div className="col-md-3">
                    <button className="btn btn-sm btn-outline-secondary w-100" onClick={resetFilters}>Сбросить</button>
                </div>
            </div>

            <p className="text-muted small mb-3">Показано {grades.length} оценок</p>

            <div className="card mb-3">
                <div className="card-body">
                    <h6 className="card-subtitle mb-2 text-muted">Добавить оценку</h6>
                    <form onSubmit={handleAdd} className="row g-2 align-items-end">
                        <div className="col-md-3">
                            <select className="form-select form-select-sm" value={studentId} onChange={e => setStudentId(e.target.value)} required>
                                <option value="">Студент</option>
                                {groupStudents.map(s => <option key={s.id} value={s.id}>{s.name}</option>)}
                            </select>
                        </div>
                        <div className="col-md-3">
                            <select className="form-select form-select-sm" value={subjectId} onChange={e => setSubjectId(e.target.value)} required>
                                <option value="">Предмет</option>
                                {subjects.map(s => <option key={s.id} value={s.id}>{s.name}</option>)}
                            </select>
                        </div>
                        <div className="col-md-3">
                            <select className="form-select form-select-sm" value={period} onChange={e => setPeriod(e.target.value)}>
                                <option value="2025-осень">2025-осень</option>
                                <option value="2026-весна">2026-весна</option>
                            </select>
                        </div>
                        <div className="col-md-1"><input type="number" className="form-control form-control-sm" min="0" max="40" value={current} onChange={e => setCurrent(e.target.value)} /></div>
                        <div className="col-md-1"><input type="number" className="form-control form-control-sm" min="0" max="60" value={final} onChange={e => setFinal(e.target.value)} /></div>
                        <div className="col-md-2"><button type="submit" className="btn btn-sm btn-outline-secondary w-100">Добавить</button></div>
                    </form>
                </div>
            </div>

            <div className="table-responsive">
                <table className="table table-sm table-hover">
                    <thead>
                    <tr className="table-light">
                        <th>Студент</th>
                        <th>Предмет</th>
                        <th className="col-1">Период</th>
                        <th className="col-1 text-center">Текущая</th>
                        <th className="col-1 text-center">Промеж.</th>
                        <th className="col-1 text-center">Итог</th>
                        <th className="col-1 text-center">Оценка</th>
                        <th className="col-1"></th>
                    </tr>
                    </thead>
                    <tbody>
                    {grades.map(g => (
                        <tr key={g.id}>
                            <td>{getName(g.student_id, students)}</td>
                            <td>{getName(g.subject_id, subjects)}</td>
                            <td className="text-muted small">{g.period}</td>
                            <td className="text-center">{g.current}</td>
                            <td className="text-center">{g.final}</td>
                            <td className="text-center">{g.total_score}</td>
                            <td className="text-center">{getDisplayGrade(g)}</td>
                            <td><button className="btn btn-sm text-danger" onClick={() => handleDelete(g.id)}>Удалить</button></td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </div>

            {grades.length === 0 && <p className="text-muted text-center py-4">Нет данных</p>}
        </div>
    );
}