import { useState } from 'react';
import { api } from '../api/client';

export default function AnalyticsView() {
    const [problems, setProblems] = useState([]);
    const [statistics, setStatistics] = useState([]);
    const [dynamics, setDynamics] = useState(null);
    const [p1, setP1] = useState('2023-осень');
    const [p2, setP2] = useState('2024-весна');

    const loadProblems = async () => setProblems(await api.getProblems(0.20));
    const loadStatistics = async () => setStatistics(await api.getStatistics());
    const loadDynamics = async () => setDynamics(await api.getDynamics(p1, p2));

    const getScoreColor = (score) => {
        if (score >= 91) return '#16a34a';
        if (score >= 76) return '#2563eb';
        if (score >= 61) return '#ca8a04';
        return '#dc2626';
    };

    return (
        <div>
            <h2>Аналитика</h2>

            <section>
                <h3>Статистика по предметам</h3>
                <button onClick={loadStatistics}>Обновить</button>
                {statistics.length > 0 && (
                    <table className="data-table">
                        <thead>
                        <tr><th>Предмет</th><th>Средний</th><th>Медиана</th><th>Стд. откл.</th><th>Min</th><th>Max</th></tr>
                        </thead>
                        <tbody>
                        {statistics.map(s => (
                            <tr key={s.subject_id}>
                                <td>{s.subject_name}</td>
                                <td style={{color: getScoreColor(s.average)}}>{s.average}</td>
                                <td>{s.median}</td>
                                <td>{s.std_dev}</td>
                                <td style={{color: getScoreColor(s.min)}}>{s.min}</td>
                                <td style={{color: getScoreColor(s.max)}}>{s.max}</td>
                            </tr>
                        ))}
                        </tbody>
                    </table>
                )}
            </section>

            <section>
                <h3>Проблемные предметы</h3>
                <button onClick={loadProblems}>Обновить</button>
                {problems.length === 0 ? <p>Нет проблемных предметов</p> : (
                    <table className="data-table">
                        <thead>
                        <tr><th>Предмет</th><th>Доля неудов</th><th>Средний балл</th><th>Min</th><th>Max</th><th>Студентов</th></tr>
                        </thead>
                        <tbody>
                        {problems.map(p => (
                            <tr key={p.subject_id}>
                                <td>{p.subject_name}</td>
                                <td>{(p.bad_rate * 100).toFixed(0)}%</td>
                                <td style={{color: getScoreColor(p.average_score)}}>{p.average_score}</td>
                                <td style={{color: getScoreColor(p.min_score)}}>{p.min_score}</td>
                                <td style={{color: getScoreColor(p.max_score)}}>{p.max_score}</td>
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
                    <div className="dynamics-grid">
                        <div className="card">
                            <h4>Абсолютный рейтинг</h4>
                            <p><strong>{dynamics.period1}</strong> → <strong>{dynamics.period2}</strong></p>
                            <p>Средний балл: {dynamics.absolute.average1} → {dynamics.absolute.average2}</p>
                            <p>Изменение: <span className={`trend-${dynamics.absolute.trend}`}>{dynamics.absolute.delta > 0 ? '+' : ''}{dynamics.absolute.delta}</span></p>
                            <p>Тренд: <span className={`trend-${dynamics.absolute.trend}`}>{dynamics.absolute.trend}</span></p>
                        </div>
                        <div className="card">
                            <h4>Взвешенный рейтинг</h4>
                            <p><strong>{dynamics.period1}</strong> → <strong>{dynamics.period2}</strong></p>
                            <p>Средний балл: {dynamics.weighted.average1} → {dynamics.weighted.average2}</p>
                            <p>Изменение: <span className={`trend-${dynamics.weighted.trend}`}>{dynamics.weighted.delta > 0 ? '+' : ''}{dynamics.weighted.delta}</span></p>
                            <p>Тренд: <span className={`trend-${dynamics.weighted.trend}`}>{dynamics.weighted.trend}</span></p>
                        </div>
                    </div>
                )}
            </section>
        </div>
    );
}