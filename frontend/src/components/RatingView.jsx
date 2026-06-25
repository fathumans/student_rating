import { useState, useEffect, useMemo } from 'react';
import { api } from '../api/client';

export default function RatingView({ group }) {
    const [combined, setCombined] = useState([]);
    const [sortField, setSortField] = useState('absolute_rank');
    const [sortDir, setSortDir] = useState('asc');

    useEffect(() => {
        api.getRatingCombined().then(setCombined).catch(console.error);
    }, []);

    const filteredCombined = useMemo(() => {
        if (!group) return combined;
        return combined.filter(s => s.group === group);
    }, [combined, group]);

    const handleSort = (field) => {
        if (sortField === field) {
            setSortDir(prev => prev === 'asc' ? 'desc' : 'asc');
        } else {
            setSortField(field);
            setSortDir('asc');
        }
    };

    const arrow = (field) => {
        if (sortField !== field) return '';
        return sortDir === 'asc' ? ' ↑' : ' ↓';
    };

    const sorted = [...filteredCombined].sort((a, b) => {
        let va = a[sortField], vb = b[sortField];
        if (typeof va === 'string') { va = va.toLowerCase(); vb = vb.toLowerCase(); }
        if (va < vb) return sortDir === 'asc' ? -1 : 1;
        if (va > vb) return sortDir === 'asc' ? 1 : -1;
        return 0;
    });

    return (
        <div>
            <div className="d-flex justify-content-between align-items-center mb-3">
                <h5 className="mb-0">Рейтинг — {group}</h5>
                <button className="btn btn-sm btn-outline-secondary" onClick={() => api.exportCSV(group)}>
                    Экспорт CSV
                </button>
            </div>

            <div className="table-responsive">
                <table className="table table-sm table-hover">
                    <thead>
                    <tr className="table-light">
                        <th onClick={() => handleSort('absolute_rank')} style={{cursor:'pointer'}}>Место{arrow('absolute_rank')}</th>
                        <th onClick={() => handleSort('weighted_rank')} style={{cursor:'pointer'}}>Место (взв){arrow('weighted_rank')}</th>
                        <th onClick={() => handleSort('name')} style={{cursor:'pointer'}}>ФИО{arrow('name')}</th>
                        <th onClick={() => handleSort('absolute_rating')} style={{cursor:'pointer'}} className="text-center">Абс. балл{arrow('absolute_rating')}</th>
                        <th onClick={() => handleSort('weighted_rating')} style={{cursor:'pointer'}} className="text-center">Взв. балл{arrow('weighted_rating')}</th>
                    </tr>
                    </thead>
                    <tbody>
                    {sorted.map(s => (
                        <tr key={s.id}>
                            <td>{s.absolute_rank}</td>
                            <td>{s.weighted_rank}</td>
                            <td>{s.name}</td>
                            <td className="text-center">{s.absolute_rating}</td>
                            <td className="text-center">{s.weighted_rating}</td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </div>

            {sorted.length === 0 && <p className="text-muted text-center py-4">Нет данных</p>}
        </div>
    );
}