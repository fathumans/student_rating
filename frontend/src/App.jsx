import { useState } from 'react';
import StudentManager from './components/StudentManager';
import SubjectManager from './components/SubjectManager';
import GradeManager from './components/GradeManager';
import RatingView from './components/RatingView';
import StudentDetail from './components/StudentDetail';
import AnalyticsView from './components/AnalyticsView';

const TABS = [
    { id: 'rating', label: '⭐ Рейтинг' },
    { id: 'students', label: '👥 Студенты' },
    { id: 'subjects', label: '📚 Предметы' },
    { id: 'grades', label: '📝 Оценки' },
    { id: 'detail', label: '🔍 Детализация' },
    { id: 'analytics', label: '📊 Аналитика' },
];

export default function App() {
    const [activeTab, setActiveTab] = useState('rating');

    return (
        <div className="app">
            <header>
                <h1>Рейтинговая система студентов</h1>
                <p className="subtitle">ВВГУ · БИН-24-1 · Система баллов 100-point</p>
                <nav className="tabs">
                    {TABS.map(tab => (
                        <button key={tab.id} className={activeTab === tab.id ? 'active' : ''} onClick={() => setActiveTab(tab.id)}>
                            {tab.label}
                        </button>
                    ))}
                </nav>
            </header>
            <main>
                {activeTab === 'students' && <StudentManager />}
                {activeTab === 'subjects' && <SubjectManager />}
                {activeTab === 'grades' && <GradeManager />}
                {activeTab === 'rating' && <RatingView />}
                {activeTab === 'detail' && <StudentDetail />}
                {activeTab === 'analytics' && <AnalyticsView />}
            </main>
        </div>
    );
}