import { useState, useEffect } from 'react';
import { api } from '../api/client';

export default function RatingView() {
    const [rating, setRating] = useState([]);

    const load = async () => setRating(await api.getRating());
    useEffect(() => { load(); }, []);

    return (
        <div>
            <h2>Рейтинг</h2>
            <button onClick={() => api.exportCSV()} style={{marginBottom: 12}}>📥 Экспорт CSV</button>
            <table className="data-table">
                <thead><tr><th>Место</th><th>ФИО</th><th>Группа</th><th>Рейтинг</th><th>Пятёрок</th></tr></thead>
                <tbody>
                {rating.map(r => (
                    <tr key={r.id} className={r.rank <= 3 ? `top-${r.rank}` : ''}>
                        <td>{r.rank}</td>
                        <td>{r.name}</td>
                        <td>{r.group}</td>
                        <td>{r.rating}</td>
                        <td>{r.fives_count}</td>
                    </tr>
                ))}
                </tbody>
            </table>
        </div>
    );
}