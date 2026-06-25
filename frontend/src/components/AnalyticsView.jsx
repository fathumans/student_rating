import { useState, useEffect, useMemo } from 'react';
import { api } from '../api/client';
import {
    BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend,
    ResponsiveContainer, Cell, LabelList, ReferenceLine
} from 'recharts';

export default function AnalyticsView({ group }) {
    const [students, setStudents] = useState([]);
    const [subjects, setSubjects] = useState([]);
    const [combined, setCombined] = useState([]);
    const [grades, setGrades] = useState([]);

    const [chartMode, setChartMode] = useState('distribution');
    const [selectedStudent, setSelectedStudent] = useState('');
    const [problems, setProblems] = useState([]);
    const [dynamics, setDynamics] = useState(null);
    const [p1, setP1] = useState('2025-осень');
    const [p2, setP2] = useState('2026-весна');

    useEffect(() => {
        Promise.all([
            api.getStudents(),
            api.getSubjects(),
            api.getRatingCombined(),
            api.getGrades()
        ]).then(([s, sub, r, g]) => {
            setStudents(s);
            setSubjects(sub);
            setCombined(r);
            setGrades(g);
        }).catch(console.error);
    }, []);

    // Фильтруем по группе
    const groupStudents = useMemo(() => {
        if (!group) return students;
        return students.filter(s => s.group === group);
    }, [students, group]);

    const groupCombined = useMemo(() => {
        if (!group) return combined;
        return combined.filter(s => s.group === group);
    }, [combined, group]);

    const groupGrades = useMemo(() => {
        const groupStudentIds = new Set(groupStudents.map(s => s.id));
        return grades.filter(g => groupStudentIds.has(g.student_id));
    }, [grades, groupStudents]);

    // === График 1: Распределение ===
    const distributionData = useMemo(() => {
        const bins = { '91-100': 0, '76-90': 0, '61-75': 0, '0-60': 0 };
        groupCombined.forEach(s => {
            const r = s.absolute_rating;
            if (r >= 91) bins['91-100']++;
            else if (r >= 76) bins['76-90']++;
            else if (r >= 61) bins['61-75']++;
            else bins['0-60']++;
        });
        return Object.entries(bins).map(([range, count]) => ({ range, count }));
    }, [groupCombined]);

    // === График 4: Профиль студента ===
    const studentProfileData = useMemo(() => {
        if (!selectedStudent) return [];
        const sid = Number(selectedStudent);
        const studentGrades = groupGrades.filter(g => g.student_id === sid);

        return studentGrades.map(g => {
            const subject = subjects.find(s => s.id === g.subject_id);
            return {
                subject: subject ? subject.name : `ID${g.subject_id}`,
                score: g.total_score,
                type: subject ? subject.type : 'exam'
            };
        }).sort((a, b) => b.score - a.score);
    }, [selectedStudent, groupGrades, subjects]);

    // === График 2: Сравнение ===
    const comparisonData = useMemo(() => {
        return groupCombined
            .map(s => ({
                name: s.name.split(' ')[0],
                absolute: Math.round(s.absolute_rating),
                weighted: Math.round(s.weighted_rating)
            }))
            .sort((a, b) => b.absolute - a.absolute);
    }, [groupCombined]);

    // === График 3: Проблемные предметы ===
    const problemsData = useMemo(() => {
        // Считаем средний балл по каждому предмету в группе
        const subjectStats = {};
        groupGrades.forEach(g => {
            if (!subjectStats[g.subject_id]) {
                subjectStats[g.subject_id] = { total: 0, count: 0 };
            }
            subjectStats[g.subject_id].total += g.total_score;
            subjectStats[g.subject_id].count += 1;
        });

        return Object.entries(subjectStats)
            .map(([subjectId, stats]) => {
                const subject = subjects.find(s => s.id === Number(subjectId));
                const avg = Math.round(stats.total / stats.count);
                return {
                    subject: subject ? subject.name : `ID${subjectId}`,
                    average: avg,
                    type: subject ? subject.type : 'exam',
                    count: stats.count
                };
            })
            .filter(s => s.average < 75) // Проблемные — ниже 75
            .sort((a, b) => a.average - b.average);
    }, [groupGrades, subjects]);

    const loadDynamics = async () => {
        try {
            const data = await api.getDynamics(p1, p2);
            setDynamics(data);
        } catch (err) { alert('Ошибка: ' + err.message); }
    };

    const getScoreColor = (score) => {
        if (score >= 91) return '#198754';
        if (score >= 76) return '#0d6efd';
        if (score >= 61) return '#ffc107';
        return '#dc3545';
    };

    const getScoreLabel = (score) => {
        if (score >= 91) return 'Отлично';
        if (score >= 76) return 'Хорошо';
        if (score >= 61) return 'Удовл.';
        return 'Неуд.';
    };

    const StudentTooltip = ({ active, payload }) => {
        if (active && payload && payload.length) {
            const data = payload[0].payload;
            const typeLabel = data.type === 'test' ? 'Зачёт' : data.type === 'practice' ? 'Практика' : 'Экзамен';
            return (
                <div className="bg-white border rounded shadow-sm p-2 small">
                    <div className="fw-medium">{data.subject}</div>
                    <div className="text-muted">{typeLabel}</div>
                    <div className="mt-1">
                        <span className="fw-bold" style={{ color: getScoreColor(data.score) }}>{data.score}</span>
                        {' '}
                        <span className="text-muted">({getScoreLabel(data.score)})</span>
                    </div>
                </div>
            );
        }
        return null;
    };

    const ProblemTooltip = ({ active, payload }) => {
        if (active && payload && payload.length) {
            const data = payload[0].payload;
            const typeLabel = data.type === 'test' ? 'Зачёт' : data.type === 'practice' ? 'Практика' : 'Экзамен';
            return (
                <div className="bg-white border rounded shadow-sm p-2 small">
                    <div className="fw-medium">{data.subject}</div>
                    <div className="text-muted">{typeLabel}</div>
                    <div className="mt-1">
                        <span className="fw-bold" style={{ color: getScoreColor(data.average) }}>{data.average}</span>
                        {' '}
                        <span className="text-muted">({getScoreLabel(data.average)})</span>
                    </div>
                    <div className="text-muted mt-1">Оценок: {data.count}</div>
                </div>
            );
        }
        return null;
    };

    return (
        <div>
            <h5 className="mb-3">Аналитика — {group}</h5>

            <div className="btn-group mb-3 w-100" role="group">
                <button
                    className={`btn btn-sm ${chartMode === 'distribution' ? 'btn-secondary' : 'btn-outline-secondary'}`}
                    onClick={() => setChartMode('distribution')}
                >
                    Распределение
                </button>
                <button
                    className={`btn btn-sm ${chartMode === 'subject' ? 'btn-secondary' : 'btn-outline-secondary'}`}
                    onClick={() => setChartMode('subject')}
                >
                    По студенту
                </button>
                <button
                    className={`btn btn-sm ${chartMode === 'comparison' ? 'btn-secondary' : 'btn-outline-secondary'}`}
                    onClick={() => setChartMode('comparison')}
                >
                    Абс. vs Взв.
                </button>
                <button
                    className={`btn btn-sm ${chartMode === 'problems' ? 'btn-secondary' : 'btn-outline-secondary'}`}
                    onClick={() => setChartMode('problems')}
                >
                    Проблемные предметы
                </button>
            </div>

            {/* 1. Распределение */}
            {chartMode === 'distribution' && (
                <div className="card mb-4">
                    <div className="card-body">
                        <h6 className="card-subtitle mb-3 text-muted">Распределение студентов по баллам</h6>
                        <ResponsiveContainer width="100%" height={320}>
                            <BarChart data={distributionData}>
                                <CartesianGrid strokeDasharray="3 3" stroke="#e9ecef" />
                                <XAxis dataKey="range" tick={{fontSize: 12}} />
                                <YAxis allowDecimals={false} tick={{fontSize: 12}} width={30} />
                                <Tooltip
                                    contentStyle={{ borderRadius: 8, border: 'none', boxShadow: '0 2px 8px rgba(0,0,0,0.1)' }}
                                    formatter={(value) => [`${value} чел.`, 'Студентов']}
                                />
                                <Bar dataKey="count" radius={[6, 6, 0, 0]} maxBarSize={60}>
                                    {distributionData.map((entry, index) => (
                                        <Cell key={index} fill={getScoreColor(
                                            entry.range === '91-100' ? 95 :
                                                entry.range === '76-90' ? 83 :
                                                    entry.range === '61-75' ? 68 : 30
                                        )} />
                                    ))}
                                    <LabelList dataKey="count" position="top" style={{ fontSize: 12, fill: '#495057' }} />
                                </Bar>
                            </BarChart>
                        </ResponsiveContainer>
                    </div>
                </div>
            )}

            {/* 4. Профиль студента */}
            {chartMode === 'subject' && (
                <div className="card mb-4">
                    <div className="card-body">
                        <div className="row g-2 mb-3">
                            <div className="col-md-4">
                                <label className="form-label small text-muted mb-1">Студент</label>
                                <select
                                    className="form-select form-select-sm"
                                    value={selectedStudent}
                                    onChange={e => setSelectedStudent(e.target.value)}
                                >
                                    <option value="">Выберите студента</option>
                                    {groupStudents.map(s => <option key={s.id} value={s.id}>{s.name}</option>)}
                                </select>
                            </div>
                        </div>

                        {selectedStudent ? (
                            <>
                                <div className="d-flex align-items-baseline gap-2 mb-3">
                                    <h6 className="card-subtitle text-muted mb-0">Успеваемость по предметам</h6>
                                    <span className="small text-muted">
                                        {students.find(s => s.id === Number(selectedStudent))?.name}
                                    </span>
                                </div>
                                <ResponsiveContainer width="100%" height={Math.max(300, studentProfileData.length * 40 + 40)}>
                                    <BarChart data={studentProfileData} layout="vertical" margin={{ left: 20, right: 50, top: 5, bottom: 5 }}>
                                        <CartesianGrid strokeDasharray="3 3" stroke="#e9ecef" horizontal={false} />
                                        <XAxis type="number" domain={[0, 100]} tick={{fontSize: 11}} />
                                        <YAxis
                                            type="category"
                                            dataKey="subject"
                                            tick={{fontSize: 12}}
                                            width={180}
                                            interval={0}
                                        />
                                        <Tooltip content={<StudentTooltip />} cursor={{fill: 'rgba(0,0,0,0.03)'}} />
                                        <ReferenceLine
                                            x={61}
                                            stroke="#dc3545"
                                            strokeDasharray="4 4"
                                            label={{ value: 'Порог 61', position: 'top', fontSize: 10, fill: '#dc3545' }}
                                        />
                                        <Bar dataKey="score" radius={[0, 4, 4, 0]} maxBarSize={22} animationDuration={800}>
                                            {studentProfileData.map((entry, index) => (
                                                <Cell key={index} fill={getScoreColor(entry.score)} />
                                            ))}
                                            <LabelList dataKey="score" position="right" style={{ fontSize: 12, fontWeight: 500, fill: '#495057' }} />
                                        </Bar>
                                    </BarChart>
                                </ResponsiveContainer>

                                <div className="d-flex flex-wrap gap-3 mt-3 small text-muted">
                                    <span><span className="d-inline-block rounded-circle me-1" style={{width: 10, height: 10, background: '#198754'}}></span>Отлично (91-100)</span>
                                    <span><span className="d-inline-block rounded-circle me-1" style={{width: 10, height: 10, background: '#0d6efd'}}></span>Хорошо (76-90)</span>
                                    <span><span className="d-inline-block rounded-circle me-1" style={{width: 10, height: 10, background: '#ffc107'}}></span>Удовл. (61-75)</span>
                                    <span><span className="d-inline-block rounded-circle me-1" style={{width: 10, height: 10, background: '#dc3545'}}></span>Неуд. (0-60)</span>
                                </div>
                            </>
                        ) : (
                            <div className="text-center text-muted py-5">
                                <p className="mb-0">Выберите студента, чтобы увидеть его успеваемость</p>
                            </div>
                        )}
                    </div>
                </div>
            )}

            {/* 2. Сравнение */}
            {chartMode === 'comparison' && (
                <div className="card mb-4">
                    <div className="card-body">
                        <h6 className="card-subtitle mb-3 text-muted">Абсолютный vs Взвешенный рейтинг</h6>
                        <ResponsiveContainer width="100%" height={400}>
                            <BarChart data={comparisonData} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                                <CartesianGrid strokeDasharray="3 3" stroke="#e9ecef" />
                                <XAxis dataKey="name" tick={{fontSize: 11}} />
                                <YAxis domain={[0, 100]} tick={{fontSize: 11}} width={30} />
                                <Tooltip contentStyle={{ borderRadius: 8, border: 'none', boxShadow: '0 2px 8px rgba(0,0,0,0.1)' }} />
                                <Legend wrapperStyle={{fontSize: 12}} />
                                <Bar dataKey="absolute" fill="#495057" radius={[4, 4, 0, 0]} name="Абсолютный" maxBarSize={28} />
                                <Bar dataKey="weighted" fill="#477cb3" radius={[4, 4, 0, 0]} name="Взвешенный" maxBarSize={28} />
                            </BarChart>
                        </ResponsiveContainer>
                    </div>
                </div>
            )}

            {/* 3. Проблемные предметы */}
            {chartMode === 'problems' && (
                <div className="card mb-4">
                    <div className="card-body">
                        <h6 className="card-subtitle mb-3 text-muted">
                            Проблемные предметы — средний балл ниже 75
                        </h6>
                        {problemsData.length > 0 ? (
                            <>
                                <ResponsiveContainer width="100%" height={Math.max(300, problemsData.length * 40 + 40)}>
                                    <BarChart data={problemsData} layout="vertical" margin={{ left: 20, right: 50, top: 5, bottom: 5 }}>
                                        <CartesianGrid strokeDasharray="3 3" stroke="#e9ecef" horizontal={false} />
                                        <XAxis type="number" domain={[0, 100]} tick={{fontSize: 11}} />
                                        <YAxis
                                            type="category"
                                            dataKey="subject"
                                            tick={{fontSize: 12}}
                                            width={180}
                                            interval={0}
                                        />
                                        <Tooltip content={<ProblemTooltip />} cursor={{fill: 'rgba(0,0,0,0.03)'}} />
                                        <ReferenceLine
                                            x={61}
                                            stroke="#dc3545"
                                            strokeDasharray="4 4"
                                            label={{ value: 'Порог 61', position: 'top', fontSize: 10, fill: '#dc3545' }}
                                        />
                                        <ReferenceLine
                                            x={75}
                                            stroke="#ffc107"
                                            strokeDasharray="4 4"
                                            label={{ value: 'Порог 75', position: 'top', fontSize: 10, fill: '#ffc107' }}
                                        />
                                        <Bar dataKey="average" radius={[0, 4, 4, 0]} maxBarSize={22} animationDuration={800}>
                                            {problemsData.map((entry, index) => (
                                                <Cell key={index} fill={getScoreColor(entry.average)} />
                                            ))}
                                            <LabelList dataKey="average" position="right" style={{ fontSize: 12, fontWeight: 500, fill: '#495057' }} />
                                        </Bar>
                                    </BarChart>
                                </ResponsiveContainer>

                                <div className="d-flex flex-wrap gap-3 mt-3 small text-muted">
                                    <span><span className="d-inline-block rounded-circle me-1" style={{width: 10, height: 10, background: '#198754'}}></span>Отлично (91-100)</span>
                                    <span><span className="d-inline-block rounded-circle me-1" style={{width: 10, height: 10, background: '#0d6efd'}}></span>Хорошо (76-90)</span>
                                    <span><span className="d-inline-block rounded-circle me-1" style={{width: 10, height: 10, background: '#ffc107'}}></span>Удовл. (61-75)</span>
                                    <span><span className="d-inline-block rounded-circle me-1" style={{width: 10, height: 10, background: '#dc3545'}}></span>Неуд. (0-60)</span>
                                </div>
                            </>
                        ) : (
                            <div className="text-center text-muted py-5">
                                <p className="mb-0">Нет проблемных предметов — все средние баллы выше 75!</p>
                            </div>
                        )}
                    </div>
                </div>
            )}

            {/* Динамика */}
            <div className="card">
                <div className="card-header bg-white">
                    <h6 className="mb-0">Динамика успеваемости</h6>
                </div>
                <div className="card-body">
                    <div className="row g-2 mb-3">
                        <div className="col-md-3">
                            <select className="form-select form-select-sm" value={p1} onChange={e => setP1(e.target.value)}>
                                <option value="2025-осень">2025-осень</option>
                                <option value="2026-весна">2026-весна</option>
                            </select>
                        </div>
                        <div className="col-md-3">
                            <select className="form-select form-select-sm" value={p2} onChange={e => setP2(e.target.value)}>
                                <option value="2025-осень">2025-осень</option>
                                <option value="2026-весна">2026-весна</option>
                            </select>
                        </div>
                        <div className="col-md-3">
                            <button className="btn btn-sm btn-outline-secondary" onClick={loadDynamics}>Сравнить</button>
                        </div>
                    </div>
                    {dynamics && (
                        <div className="row">
                            <div className="col-md-6">
                                <p className="small mb-1">
                                    <strong>Абсолютный:</strong> {dynamics.absolute.average1} → {dynamics.absolute.average2}
                                    {' '}({dynamics.absolute.delta > 0 ? '+' : ''}{dynamics.absolute.delta})
                                </p>
                            </div>
                            <div className="col-md-6">
                                <p className="small mb-1">
                                    <strong>Взвешенный:</strong> {dynamics.weighted.average1} → {dynamics.weighted.average2}
                                    {' '}({dynamics.weighted.delta > 0 ? '+' : ''}{dynamics.weighted.delta})
                                </p>
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}