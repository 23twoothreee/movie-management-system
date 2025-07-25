<template>
  <div class="container">
    <div class="header">
      <h2 class="title">Movie List</h2>
      <BaseButton>Add a movie</BaseButton>
    </div>
    <div class="movie-list">
      <template v-if="movies.length > 0">
        <MovieCard
          v-for="movie in movies"
          :key="movie.id"
          :title="movie.title"
          :date-added="movie.dateAdded"
          :poster-url="movie.posterUrl"
        />
      </template>
      <div v-else class="empty-state">
        <i class="mdi mdi-movie-open-off-outline"></i>
        <p>No movies found.</p>
        <BaseButton>Add a movie</BaseButton>
      </div>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'
import BaseButton from '../components/BaseButton.vue';

export default {
  name: 'MovieList',

  components: {
    MovieCard,
    BaseButton
  },

  data() {
    return {
      movies: [
        {
          id: 1,
          title: 'Inception',
          dateAdded: '2021-07-16',
          posterUrl: 'https://m.media-amazon.com/images/I/81p+xe8cbnL._AC_SY679_.jpg'
        },
        {
          id: 1,
          title: 'Inception',
          dateAdded: '2021-07-16',
          posterUrl: 'https://m.media-amazon.com/images/I/81p+xe8cbnL._AC_SY679_.jpg'
        },
        {
          id: 1,
          title: 'Inception',
          dateAdded: '2021-07-16',
          posterUrl: 'https://m.media-amazon.com/images/I/81p+xe8cbnL._AC_SY679_.jpg'
        },
        {
          id: 1,
          title: 'Inception',
          dateAdded: '2021-07-16',
          posterUrl: 'https://m.media-amazon.com/images/I/81p+xe8cbnL._AC_SY679_.jpg'
        },
        {
          id: 1,
          title: 'Inception',
          dateAdded: '2021-07-16',
          posterUrl: 'https://m.media-amazon.com/images/I/81p+xe8cbnL._AC_SY679_.jpg'
        },
        {
          id: 1,
          title: 'Inception',
          dateAdded: '2021-07-16',
          posterUrl: 'https://m.media-amazon.com/images/I/81p+xe8cbnL._AC_SY679_.jpg'
        },
        {
          id: 1,
          title: 'Inception',
          dateAdded: '2021-07-16',
          posterUrl: 'https://m.media-amazon.com/images/I/81p+xe8cbnL._AC_SY679_.jpg'
        },
        {
          id: 1,
          title: 'Inception',
          dateAdded: '2021-07-16',
          posterUrl: 'https://m.media-amazon.com/images/I/81p+xe8cbnL._AC_SY679_.jpg'
        },
        {
          id: 1,
          title: 'Inception',
          dateAdded: '2021-07-16',
          posterUrl: 'https://m.media-amazon.com/images/I/81p+xe8cbnL._AC_SY679_.jpg'
        },
        {
          id: 2,
          title: 'The Matrix',
          dateAdded: '1999-03-31',
          posterUrl: 'https://m.media-amazon.com/images/I/51EG732BV3L.jpg'
        },
        {
          id: 3,
          title: 'Interstellar',
          dateAdded: '2014-11-07',
          posterUrl: 'https://m.media-amazon.com/images/I/91kFYg4fX3L._AC_SY679_.jpg'
        }
      ]
    }
  }
}
</script>

<style lang='scss' scoped>
  @use '@/stylesheets/styles.scss' as *;

  .container {
    padding: 0px 40px;
    background-color: var(--page-background);
    height: 100vh;
  }

  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    color: var(--white);
    height: 80px;
  }

  .movie-list {
    @include flex-wrap;
    background-color: var(--page-background);
    gap: 40px;
    justify-content: center;
  }

  .empty-state {
    @include flex-column;
    align-items: center;
    justify-content: center;
    height: 80vh;
    width: 100%;
    text-align: center;
    gap: 16px;
    color: var(--secondary);

    i {
      font-size: 80px;
      color: var(--secondary);
    }

    p {
      font-size: 18px;
      margin: 0;
    }
  }
</style>
