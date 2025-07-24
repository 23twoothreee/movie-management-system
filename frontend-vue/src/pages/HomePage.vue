<template>
  <div class="movie-list">
    <MovieCard
      v-for="movie in movies"
      :key="movie.id"
      :title="movie.title"
      :date-added="movie.dateAdded"
      :poster-url="movie.posterUrl"
    />
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'

export default {
  name: 'MovieList',
  components: {
    MovieCard
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

  .movie-list {
    @include flex-wrap();
    gap: 20px;
    padding: 20px;
    height: 100vh;
    background-color: var(--page-background);
  }
</style>
