import { useState } from 'react';
import { api } from '../api/client';

export default function StudentDetail() {
    const [studentId, setStudentId] = useState('');
    const [detail, setDetail] = useState(null);
    const [loading, setLoading] = useState(false);

    const loadDetail = async () => {
        if (!studentId) return;
        setLoading(true);
        try {
            const data = await api.getStudentDetail(Number(studentId));
            setDetail(data);
        } catch (err) {
            alert('Ошибка: ' + err.message);
        } finally {
            setLoading(false);
        }
    };

    const getScoreColor = (score) => {
        if (score >= 91) return '#16a34a';
        if (score >= 76) return '#2563eb';
        if (score >= 61) return '#ca8a04';
        return '#dc2626';
    };

    return (
        <div>
            <h2>Детализация студента</h2>
            <div className="form-row">
                <input
                    type="number"
                    placeholder="ID студента"
                    value={studentId}
                    onChange={e => setStudentId(e.target.value)}
                />
                <button onClick={loadDetail} disabled={loading}>
                    {loading ? 'Загрузка...' : 'Показать'}
                </button>
            </div>

            {detail && (
                <div className="student-detail">
                    <div className="detail-header">
                        <h3>{detail.student.name}</h3>
                        <p>Группа: {detail.student.group}</p>
                        <div className="detail-scores">
                            <div className="score-box">
                                <span className="score-label">Абсолютный рейтинг</span>
                                <span className="score-value" style={{color: getScoreColor(detail.absolute_rating)}}>
                  {detail.absolute_rating}
                </span>
                            </div>
                            <div className="score-box">
                                <span className="score-label">Взвешенный рейтинг</span>
                                <span className="score-value" style={{color: getScoreColor(detail.weighted_rating)}}>
                  {detail.weighted_rating}
                </span>
                            </div>
                        </div>
                    </div>

                    <table className="data-table">
                        <thead>
                        <tr>
                            <th>Предмет</th>
                            <th>Тип</th>
                            <th>Вес</th>
                            <th>Текущая</th>
                            <th>Промежуточная</th>
                            <th>Итог</th>
                            <th>Оценка</th>
                            <th>Статус</th>
                        </tr>
                        </thead>
                        <tbody>
                        {detail.subjects.map((subj, i) => (
                            <tr key={i}>
                                <td>{subj.subject_name}</td>
                                <td>{subj.type}</td>
                                <td>{subj.weight}</td>
                                <td>{subj.current}</td>
                                <td>{subj.final}</td>
                                <td style={{fontWeight: 'bold', color: getScoreColor(subj.total_score)}}>
                                    {subj.total_score}
                                </td>
                                <td>{subj.grade}</td>
                                <td>{subj.status}</td>
                            </tr>
                        ))}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
}