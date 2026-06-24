import { useState, useEffect } from 'react';
import StudentManager from './components/StudentManager';
import SubjectManager from './components/SubjectManager';
import GradeManager from './components/GradeManager';
import RatingView from './components/RatingView';
import AnalyticsView from './components/AnalyticsView';

const TABS = [
    { id: 'rating', label: 'Рейтинг' },
    { id: 'students', label: 'Студенты' },
    { id: 'subjects', label: 'Предметы' },
    { id: 'grades', label: 'Оценки' },
    { id: 'analytics', label: 'Аналитика' },
];

export default function App() {
    const [activeTab, setActiveTab] = useState('rating');
    const [selectedGroup, setSelectedGroup] = useState('');
    const [groups, setGroups] = useState([]);

    // Загружаем список групп один раз
    useEffect(() => {
        fetch('/api/students')
            .then(r => r.json())
            .then(students => {
                const grps = [...new Set(students.map(s => s.group))].sort();
                setGroups(grps);
                if (grps.length) setSelectedGroup(grps[0]);
            })
            .catch(() => setGroups(['БИН-24-1']));
    }, []);

    return (
        <div className="container py-4">
            <header className="mb-4 pb-3">
                <div className="d-flex justify-content-between align-items-start">
                    <div>
                        <h4 className="mb-1">Рейтинговая система студентов</h4>
                    </div>
                    <div className="d-flex align-items-center gap-2">
                        <label className="text-muted small mb-0">Группа:</label>
                        <select
                            className="form-select form-select-sm"
                            style={{ width: 140 }}
                            value={selectedGroup}
                            onChange={e => setSelectedGroup(e.target.value)}
                        >
                            {groups.map(g => <option key={g} value={g}>{g}</option>)}
                        </select>
                    </div>
                </div>
            </header>

            <ul className="nav nav-tabs d-flex justify-content-center mb-4">
                {TABS.map(tab => (
                    <li className="nav-item" key={tab.id}>
                        <button
                            className={`nav-link link-secondary ${activeTab === tab.id ? 'active' : ''}`}
                            onClick={() => setActiveTab(tab.id)}
                        >
                            {tab.label}
                        </button>
                    </li>
                ))}
            </ul>

            {activeTab === 'students' && <StudentManager group={selectedGroup} />}
            {activeTab === 'subjects' && <SubjectManager />}
            {activeTab === 'grades' && <GradeManager group={selectedGroup} />}
            {activeTab === 'rating' && <RatingView group={selectedGroup} />}
            {activeTab === 'analytics' && <AnalyticsView group={selectedGroup} />}
        </div>
    );
}