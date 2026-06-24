import { useState, useEffect } from 'react';
import { api } from '../api/client';

export default function RatingView() {
    const [combined, setCombined] = useState([]);
    const [mode, setMode] = useState('combined'); // combined | absolute | weighted

    const load = async () => {
        try {
            const data = await api.getRatingCombined();
            setCombined(data);
        } catch (err) {
            console.error('Ошибка загрузки рейтинга:', err);
        }
    };

    useEffect(() => { load(); }, []);

    const getRatingColor = (rating) => {
        if (rating >= 91) return '#16a34a';
        if (rating >= 76) return '#2563eb';
        if (rating >= 61) return '#ca8a04';
        return '#dc2626';
    };

    const getDiffBadge = (diff) => {
        if (diff > 0) return <span className="badge-up">↗ +{diff}</span>;
        if (diff < 0) return <span className="badge-down">↘ {diff}</span>;
        return <span className="badge-same">→ 0</span>;
    };

    const sorted = [...combined].sort((a, b) => {
        if (mode === 'absolute') return a.absolute_rank - b.absolute_rank;
        if (mode === 'weighted') return a.weighted_rank - b.weighted_rank;
        return a.absolute_rank - b.absolute_rank;
    });

    return (
        <div>
            <h2>Рейтинг группы БИН-24-1</h2>
            <div className="rating-controls">
                <button className={mode === 'combined' ? 'active' : ''} onClick={() => setMode('combined')}>Объединённый</button>
                <button className={mode === 'absolute' ? 'active' : ''} onClick={() => setMode('absolute')}>Абсолютный</button>
                <button className={mode === 'weighted' ? 'active' : ''} onClick={() => setMode('weighted')}>Взвешенный</button>
                <button onClick={() => api.exportCSV()} style={{marginLeft: 'auto'}}>📥 Экспорт CSV</button>
            </div>

            <table className="data-table rating-table">
                <thead>
                <tr>
                    <th>Место</th>
                    <th>ФИО</th>
                    {mode === 'combined' && <th>Абс. место</th>}
                    {mode === 'combined' && <th>Взв. место</th>}
                    <th>Абс. балл</th>
                    <th>Взв. балл</th>
                    {mode === 'combined' && <th>Разница</th>}
                    <th>Отличных</th>
                </tr>
                </thead>
                <tbody>
                {sorted.map((s, idx) => (
                    <tr key={s.id} className={idx < 3 ? `top-${idx + 1}` : ''}>
                        <td className="rank-cell">{mode === 'combined' ? idx + 1 : (mode === 'absolute' ? s.absolute_rank : s.weighted_rank)}</td>
                        <td className="name-cell">{s.name}</td>
                        {mode === 'combined' && <td>{s.absolute_rank}</td>}
                        {mode === 'combined' && <td>{s.weighted_rank}</td>}
                        <td className="score-cell" style={{color: getRatingColor(s.absolute_rating)}}>
                            {s.absolute_rating}
                        </td>
                        <td className="score-cell" style={{color: getRatingColor(s.weighted_rating)}}>
                            {s.weighted_rating}
                        </td>
                        {mode === 'combined' && <td>{getDiffBadge(s.rating_diff)}</td>}
                        <td>{s.excellent_count}</td>
                    </tr>
                ))}
                </tbody>
            </table>
        </div>
    );
}