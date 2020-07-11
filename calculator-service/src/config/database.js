module.exports = {
  dialect: 'postgres',
  host: 'postgres_db',
  username: 'docker',
  password: 'docker',
  database: 'varejo',
  port:"5432",
  define: {
    timestamps: true,
    underscored: true,
  },
};