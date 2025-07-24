<template>
    <div class="movie-card">
        <img
            :src="posterUrl"
            alt="Movie Poster"
            class="movie-poster"
        />
        <div class="movie-info">
            <h3 class="movie-title">{{ title }}</h3>
            <p class="movie-date">Added on {{ formattedDate() }}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'MovieCard',

    props: {
        title: {
            type: String,
            required: true
        },
        dateAdded: {
            type: String,
            required: true
        },
        posterUrl: {
            type: String,
            default: 'https://s.studiobinder.com/wp-content/uploads/2019/06/Movie-Poster-Template-Movie-Credits-StudioBinder.jpg'
        }
    },

    methods: {
        formattedDate() {
            const date = new Date(this.dateAdded)
            return date.toLocaleDateString(undefined, {
                year: 'numeric',
                month: 'short',
                day: 'numeric'
            })
        }
    }
};
</script>

<style lang='scss' scoped>
    @use '@/stylesheets/styles.scss';
    
    .movie-card {
        width: 200px;
        border-radius: 8px;
        overflow: hidden;
        background-color: var(--card-background);
        color: var(--white);
        transition: transform 0.3s ease;
        cursor: pointer;
    }

    .movie-card:hover {
        transform: scale(1.05);
    }

    .movie-poster {
        width: 100%;
        height: auto;
        display: block;
    }

    .movie-info {
        padding: 12px;
        background-color: var(--card-info-background);
    }

    .movie-title {
        font-size: 16px;
        margin: 0;
        font-weight: bold;
    }

    .movie-date {
        font-size: 14px;
        color: var(--secondary);
        margin-top: 4px;
    }
</style>
