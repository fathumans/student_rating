import { useState } from 'react';
import { api } from '../api/client';

export default function AnalyticsView() {
    const [problems, setProblems] = useState([]);
    const [dynamics, setDynamics] = useState(null);
    const [p1, setP1] = useState('2024-весна');
    const [p2, setP2] = useState('2024-осень');

    const loadProblems = async () => setProblems(await api.getProblems(0.15));
    const loadDynamics = async () => setDynamics(await api.getDynamics(p1, p2));

    return (
        <div>
            <h2>Аналитика</h2>

            <section>
                <h3>Проблемные предметы</h3>
                <button onClick={loadProblems}>Обновить</button>
                {problems.length === 0 ? <p>Нет проблемных предметов</p> : (
                    <table className="data-table">
                        <thead><tr><th>Предмет</th><th>Доля неудов</th><th>Средний балл</th><th>Студентов</th></tr></thead>
                        <tbody>
                        {problems.map(p => (
                            <tr key={p.subject_id}>
                                <td>{p.subject_name}</td>
                                <td>{(p.bad_rate * 100).toFixed(0)}%</td>
                                <td>{p.average}</td>
                                <td>{p.total_students}</td>
                            </tr>
                        ))}
                        </tbody>
                    </table>
                )}
            </section>

            <section style={{marginTop: 24}}>
                <h3>Динамика успеваемости</h3>
                <div className="form-row">
                    <input placeholder="Период 1" value={p1} onChange={e => setP1(e.target.value)} />
                    <input placeholder="Период 2" value={p2} onChange={e => setP2(e.target.value)} />
                    <button onClick={loadDynamics}>Сравнить</button>
                </div>
                {dynamics && (
                    <div className="card">
                        <p><strong>{dynamics.period1}</strong> → <strong>{dynamics.period2}</strong></p>
                        <p>Средний балл: {dynamics.average1} → {dynamics.average2}</p>
                        <p>Изменение: {dynamics.delta > 0 ? '+' : ''}{dynamics.delta}</p>
                        <p>Тренд: <span className={`trend-${dynamics.trend}`}>{dynamics.trend}</span></p>
                    </div>
                )}
            </section>
        </div>
    );
}