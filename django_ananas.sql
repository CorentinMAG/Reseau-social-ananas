-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Client :  localhost:3306
-- Généré le :  Mer 10 Juin 2020 à 07:07
-- Version du serveur :  5.7.30-0ubuntu0.18.04.1
-- Version de PHP :  7.2.24-0ubuntu0.18.04.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `django_ananas`
--

-- --------------------------------------------------------

--
-- Structure de la table `authtoken_token`
--

CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` varchar(254) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `authtoken_token`
--

INSERT INTO `authtoken_token` (`key`, `created`, `user_id`) VALUES
('2f7a93af5b55e77f10fe3655be586faae3cc8292', '2020-06-07 19:30:06.794453', 'corentin.magyar@epfedu.fr'),
('31670c1388e6feba4208ba4fb6c9a796a40b8a23', '2020-06-07 20:42:10.370254', 'fabien.solde@epfedu.fr'),
('4bfba23b49abca75d73f69d558907d5920094f13', '2020-06-07 19:35:48.216978', 'margot.jourdan@epfedu.fr'),
('632089d65212688506b77f6fde8d7ef23ec3011d', '2020-06-07 20:35:57.788934', 'paul.deboissel@epfedu.fr'),
('6998c6de49c99b1975948edf14cd87ad33dfb45c', '2020-06-07 20:10:56.350624', 'pierre.francois@epfedu.fr'),
('f3d5c41b4cf795459ac71eb15c5695d84ef2bea7', '2020-06-07 19:21:22.652699', 'ananas.tropical@epfedu.fr');

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can view permission', 1, 'view_permission'),
(5, 'Can add group', 2, 'add_group'),
(6, 'Can change group', 2, 'change_group'),
(7, 'Can delete group', 2, 'delete_group'),
(8, 'Can view group', 2, 'view_group'),
(9, 'Can add content type', 3, 'add_contenttype'),
(10, 'Can change content type', 3, 'change_contenttype'),
(11, 'Can delete content type', 3, 'delete_contenttype'),
(12, 'Can view content type', 3, 'view_contenttype'),
(13, 'Can add campus', 4, 'add_campus'),
(14, 'Can change campus', 4, 'change_campus'),
(15, 'Can delete campus', 4, 'delete_campus'),
(16, 'Can view campus', 4, 'view_campus'),
(17, 'Can add majeure', 5, 'add_majeure'),
(18, 'Can change majeure', 5, 'change_majeure'),
(19, 'Can delete majeure', 5, 'delete_majeure'),
(20, 'Can view majeure', 5, 'view_majeure'),
(21, 'Can add user', 6, 'add_customuser'),
(22, 'Can change user', 6, 'change_customuser'),
(23, 'Can delete user', 6, 'delete_customuser'),
(24, 'Can view user', 6, 'view_customuser'),
(25, 'Can add etudiant', 7, 'add_etudiant'),
(26, 'Can change etudiant', 7, 'change_etudiant'),
(27, 'Can delete etudiant', 7, 'delete_etudiant'),
(28, 'Can view etudiant', 7, 'view_etudiant'),
(29, 'Can add administration', 8, 'add_administration'),
(30, 'Can change administration', 8, 'change_administration'),
(31, 'Can delete administration', 8, 'delete_administration'),
(32, 'Can view administration', 8, 'view_administration'),
(33, 'Can add message', 9, 'add_message'),
(34, 'Can change message', 9, 'change_message'),
(35, 'Can delete message', 9, 'delete_message'),
(36, 'Can view message', 9, 'view_message'),
(37, 'Can add tagged messages', 10, 'add_taggedmessages'),
(38, 'Can change tagged messages', 10, 'change_taggedmessages'),
(39, 'Can delete tagged messages', 10, 'delete_taggedmessages'),
(40, 'Can view tagged messages', 10, 'view_taggedmessages'),
(41, 'Can add chat', 11, 'add_chat'),
(42, 'Can change chat', 11, 'change_chat'),
(43, 'Can delete chat', 11, 'delete_chat'),
(44, 'Can view chat', 11, 'view_chat'),
(45, 'Can add Tag', 12, 'add_tags'),
(46, 'Can change Tag', 12, 'change_tags'),
(47, 'Can delete Tag', 12, 'delete_tags'),
(48, 'Can view Tag', 12, 'view_tags'),
(49, 'Can add Article', 13, 'add_article'),
(50, 'Can change Article', 13, 'change_article'),
(51, 'Can delete Article', 13, 'delete_article'),
(52, 'Can view Article', 13, 'view_article'),
(53, 'Can add tags_article', 14, 'add_tags_article'),
(54, 'Can change tags_article', 14, 'change_tags_article'),
(55, 'Can delete tags_article', 14, 'delete_tags_article'),
(56, 'Can view tags_article', 14, 'view_tags_article'),
(57, 'Can add pieces_jointes_post', 15, 'add_pieces_jointes_post'),
(58, 'Can change pieces_jointes_post', 15, 'change_pieces_jointes_post'),
(59, 'Can delete pieces_jointes_post', 15, 'delete_pieces_jointes_post'),
(60, 'Can view pieces_jointes_post', 15, 'view_pieces_jointes_post'),
(61, 'Can add Commentaire', 16, 'add_commentaires'),
(62, 'Can change Commentaire', 16, 'change_commentaires'),
(63, 'Can delete Commentaire', 16, 'delete_commentaires'),
(64, 'Can view Commentaire', 16, 'view_commentaires'),
(65, 'Can add Like', 17, 'add_likes'),
(66, 'Can change Like', 17, 'change_likes'),
(67, 'Can delete Like', 17, 'delete_likes'),
(68, 'Can view Like', 17, 'view_likes'),
(69, 'Can add pieces_jointes_comm', 18, 'add_pieces_jointes_comm'),
(70, 'Can change pieces_jointes_comm', 18, 'change_pieces_jointes_comm'),
(71, 'Can delete pieces_jointes_comm', 18, 'delete_pieces_jointes_comm'),
(72, 'Can view pieces_jointes_comm', 18, 'view_pieces_jointes_comm'),
(73, 'Can add log entry', 19, 'add_logentry'),
(74, 'Can change log entry', 19, 'change_logentry'),
(75, 'Can delete log entry', 19, 'delete_logentry'),
(76, 'Can view log entry', 19, 'view_logentry'),
(77, 'Can add session', 20, 'add_session'),
(78, 'Can change session', 20, 'change_session'),
(79, 'Can delete session', 20, 'delete_session'),
(80, 'Can view session', 20, 'view_session'),
(81, 'Can add Token', 21, 'add_token'),
(82, 'Can change Token', 21, 'change_token'),
(83, 'Can delete Token', 21, 'delete_token'),
(84, 'Can view Token', 21, 'view_token');

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` varchar(254) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2020-06-07 19:19:22.959469', '1', 'Tous les tags', 1, '[{\"added\": {}}]', 12, 'ananas.tropical@epfedu.fr'),
(2, '2020-06-07 19:32:49.797274', 'corentin.magyar@epfedu.fr', 'corentin.magyar@epfedu.fr', 2, '[{\"changed\": {\"fields\": [\"User permissions\"]}}]', 6, 'ananas.tropical@epfedu.fr'),
(3, '2020-06-07 20:40:08.698402', 'corentin.magyar@epfedu.fr', 'corentin.magyar@epfedu.fr', 2, '[{\"changed\": {\"fields\": [\"Superuser status\"]}}]', 6, 'ananas.tropical@epfedu.fr'),
(4, '2020-06-08 09:49:36.194097', '16', 'Aide covid-19 jeunes :', 2, '[{\"changed\": {\"fields\": [\"Contenu post\"]}}]', 13, 'fabien.solde@epfedu.fr'),
(5, '2020-06-08 09:50:13.773875', '16', 'Aide covid-19 jeunes :', 2, '[{\"changed\": {\"fields\": [\"Contenu post\"]}}]', 13, 'fabien.solde@epfedu.fr'),
(6, '2020-06-08 10:07:57.009056', '18', 'Chiffrement des données: Ercom', 2, '[{\"changed\": {\"fields\": [\"Contenu post\"]}}]', 13, 'fabien.solde@epfedu.fr'),
(7, '2020-06-08 10:11:18.461062', '16', 'Aide covid-19 jeunes :', 2, '[{\"changed\": {\"fields\": [\"Contenu post\"]}}]', 13, 'fabien.solde@epfedu.fr'),
(8, '2020-06-08 10:11:33.665788', '16', 'Aide covid-19 jeunes :', 2, '[{\"changed\": {\"fields\": [\"Contenu post\"]}}]', 13, 'fabien.solde@epfedu.fr'),
(9, '2020-06-08 10:12:24.765961', '19', 'Présentation de la Junior Entreprise EPF Projets', 2, '[{\"changed\": {\"fields\": [\"Contenu post\"]}}]', 13, 'fabien.solde@epfedu.fr'),
(10, '2020-06-08 10:12:37.343540', '19', 'Présentation de la Junior Entreprise EPF Projets', 2, '[{\"changed\": {\"fields\": [\"Contenu post\"]}}]', 13, 'fabien.solde@epfedu.fr'),
(11, '2020-06-08 10:12:58.004336', '18', 'Chiffrement des données: Ercom', 2, '[{\"changed\": {\"fields\": [\"Contenu post\"]}}]', 13, 'fabien.solde@epfedu.fr'),
(12, '2020-06-08 10:14:04.265755', '18', 'Chiffrement des données: Ercom', 2, '[{\"changed\": {\"fields\": [\"Contenu post\"]}}]', 13, 'fabien.solde@epfedu.fr'),
(13, '2020-06-08 10:16:05.234987', '20', 'toto', 3, '', 13, 'fabien.solde@epfedu.fr'),
(14, '2020-06-08 10:28:05.644219', '8', 'Expo photo', 3, '', 12, 'margot.jourdan@epfedu.fr'),
(15, '2020-06-08 18:25:28.361164', 'corentin.magyar@epfedu.fr', 'corentin.magyar@epfedu.fr', 2, '[{\"changed\": {\"fields\": [\"Staff status\"]}}]', 6, 'ananas.tropical@epfedu.fr');

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(19, 'admin', 'logentry'),
(2, 'auth', 'group'),
(1, 'auth', 'permission'),
(21, 'authtoken', 'token'),
(3, 'contenttypes', 'contenttype'),
(8, 'login', 'administration'),
(4, 'login', 'campus'),
(6, 'login', 'customuser'),
(7, 'login', 'etudiant'),
(5, 'login', 'majeure'),
(11, 'messenger', 'chat'),
(9, 'messenger', 'message'),
(10, 'messenger', 'taggedmessages'),
(20, 'sessions', 'session'),
(13, 'timeline', 'article'),
(16, 'timeline', 'commentaires'),
(17, 'timeline', 'likes'),
(18, 'timeline', 'pieces_jointes_comm'),
(15, 'timeline', 'pieces_jointes_post'),
(12, 'timeline', 'tags'),
(14, 'timeline', 'tags_article');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-06-07 19:13:38.752390'),
(2, 'contenttypes', '0002_remove_content_type_name', '2020-06-07 19:13:38.789932'),
(3, 'auth', '0001_initial', '2020-06-07 19:13:38.822399'),
(4, 'auth', '0002_alter_permission_name_max_length', '2020-06-07 19:13:38.868157'),
(5, 'auth', '0003_alter_user_email_max_length', '2020-06-07 19:13:38.874109'),
(6, 'auth', '0004_alter_user_username_opts', '2020-06-07 19:13:38.880577'),
(7, 'auth', '0005_alter_user_last_login_null', '2020-06-07 19:13:38.887019'),
(8, 'auth', '0006_require_contenttypes_0002', '2020-06-07 19:13:38.888319'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2020-06-07 19:13:38.894417'),
(10, 'auth', '0008_alter_user_username_max_length', '2020-06-07 19:13:38.901084'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2020-06-07 19:13:38.907830'),
(12, 'auth', '0010_alter_group_name_max_length', '2020-06-07 19:13:38.915763'),
(13, 'auth', '0011_update_proxy_permissions', '2020-06-07 19:13:38.932583'),
(14, 'admin', '0001_initial', '2020-06-07 19:13:47.423705'),
(15, 'admin', '0002_logentry_remove_auto_add', '2020-06-07 19:13:47.452740'),
(16, 'admin', '0003_logentry_add_action_flag_choices', '2020-06-07 19:13:47.460249'),
(17, 'authtoken', '0001_initial', '2020-06-07 19:13:47.475524'),
(18, 'authtoken', '0002_auto_20160226_1747', '2020-06-07 19:13:47.519315'),
(19, 'sessions', '0001_initial', '2020-06-07 19:13:47.529222');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('1fpju4qs52pb8md0a8b2azr455v1xvaa', 'N2ExNDMxMjBhYTE1NDQxY2JiYWJlMDEzM2E2ZWIzZTZlZGFmN2M0ODp7InRva2VuIjoiZjNkNWM0MWI0Y2Y3OTU0NTlhYzcxZWIxNWM1Njk1ZDg0ZWYyYmVhNyIsIl9hdXRoX3VzZXJfaWQiOiJhbmFuYXMudHJvcGljYWxAZXBmZWR1LmZyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyZWFjMjdiNTg1NmIxYWJjZDIyNmY5ZGY0NjU0NzRhMmYxZTdkNDI1In0=', '2020-06-22 10:38:19.645304'),
('3nynd71tkfway38txh24qhacrtekdmi6', 'NzFhOTQyODlkOGI3YjIxMGQzYzhkMWYxYTljNDg1NmIwZmYwYWZiMDp7InRva2VuIjoiMmY3YTkzYWY1YjU1ZTc3ZjEwZmUzNjU1YmU1ODZmYWFlM2NjODI5MiIsIl9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9pZCI6ImNvcmVudGluLm1hZ3lhckBlcGZlZHUuZnIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjNjNTAxNDZmNWMxMTIwNmY4MmE1Njg5YTBjNGI3YTM2M2NhODBlMzMifQ==', '2020-06-22 06:28:01.360732'),
('7wyu8tssxgz1v7eu9yw9fh9wjhjb0ghm', 'NzFhOTQyODlkOGI3YjIxMGQzYzhkMWYxYTljNDg1NmIwZmYwYWZiMDp7InRva2VuIjoiMmY3YTkzYWY1YjU1ZTc3ZjEwZmUzNjU1YmU1ODZmYWFlM2NjODI5MiIsIl9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9pZCI6ImNvcmVudGluLm1hZ3lhckBlcGZlZHUuZnIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjNjNTAxNDZmNWMxMTIwNmY4MmE1Njg5YTBjNGI3YTM2M2NhODBlMzMifQ==', '2020-06-22 11:44:36.276184'),
('8cdqwmyhny20fi2i9l1mvkg9bt32b2ip', 'ZTAyNjAzYWMwYjk3NjY2ZmMzMmZmOWM5YzUxZjM3YmM2MjBiOTEyYzp7InRva2VuIjoiNjMyMDg5ZDY1MjEyNjg4NTA2Yjc3ZjZmZGU4ZDdlZjIzZWMzMDExZCIsIl9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9pZCI6InBhdWwuZGVib2lzc2VsQGVwZmVkdS5mciIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZjVlMDA3ZWE1YzhhMTM3MDI5N2Y0NGVkZDhkNmU1NGRmZDFkMDJhZiJ9', '2020-06-21 20:45:11.530249'),
('9rvrblqpva28z2khi1inkf3i8iwlfv3b', 'NzFhOTQyODlkOGI3YjIxMGQzYzhkMWYxYTljNDg1NmIwZmYwYWZiMDp7InRva2VuIjoiMmY3YTkzYWY1YjU1ZTc3ZjEwZmUzNjU1YmU1ODZmYWFlM2NjODI5MiIsIl9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9pZCI6ImNvcmVudGluLm1hZ3lhckBlcGZlZHUuZnIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjNjNTAxNDZmNWMxMTIwNmY4MmE1Njg5YTBjNGI3YTM2M2NhODBlMzMifQ==', '2020-06-22 06:52:24.709941'),
('bxn9z7e8ncm7jg45l6zrlwisfrhx0zr2', 'OWRjMzIyZDhiNGQ3NTJiOTZmMDQyOTQ2ZGE5OTFkZmRkMDM1MDNkNTp7InRva2VuIjoiZjNkNWM0MWI0Y2Y3OTU0NTlhYzcxZWIxNWM1Njk1ZDg0ZWYyYmVhNyIsIl9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9pZCI6ImFuYW5hcy50cm9waWNhbEBlcGZlZHUuZnIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjJlYWMyN2I1ODU2YjFhYmNkMjI2ZjlkZjQ2NTQ3NGEyZjFlN2Q0MjUifQ==', '2020-06-21 20:39:52.337302'),
('cefnrg2c3722xtr2um5m8gpbgus847ru', 'OTdjYTMyNjFiNzNjYzI4NThhMjNhMDA2Nzc1MjczODJlNDFmMmUyMzp7InRva2VuIjoiMzE2NzBjMTM4OGU2ZmViYTQyMDhiYTRmYjZjOWE3OTZhNDBiOGEyMyIsIl9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9pZCI6ImZhYmllbi5zb2xkZUBlcGZlZHUuZnIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjgyYjhkZGE0NTE5YzgxZDllYThjODhmY2I5MjViZTkwZDVkZTI0NmMifQ==', '2020-06-21 20:49:29.535618'),
('cjlx8r1smdx6lkhdzb7txxen91te1b29', 'ZTAyNjAzYWMwYjk3NjY2ZmMzMmZmOWM5YzUxZjM3YmM2MjBiOTEyYzp7InRva2VuIjoiNjMyMDg5ZDY1MjEyNjg4NTA2Yjc3ZjZmZGU4ZDdlZjIzZWMzMDExZCIsIl9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9pZCI6InBhdWwuZGVib2lzc2VsQGVwZmVkdS5mciIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZjVlMDA3ZWE1YzhhMTM3MDI5N2Y0NGVkZDhkNmU1NGRmZDFkMDJhZiJ9', '2020-06-21 20:47:06.240361'),
('dpadaig0o8u70a3buki2vx3jyp3vs0h2', 'OTdjYTMyNjFiNzNjYzI4NThhMjNhMDA2Nzc1MjczODJlNDFmMmUyMzp7InRva2VuIjoiMzE2NzBjMTM4OGU2ZmViYTQyMDhiYTRmYjZjOWE3OTZhNDBiOGEyMyIsIl9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9pZCI6ImZhYmllbi5zb2xkZUBlcGZlZHUuZnIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjgyYjhkZGE0NTE5YzgxZDllYThjODhmY2I5MjViZTkwZDVkZTI0NmMifQ==', '2020-06-22 10:16:53.171541'),
('g6ru383wgxlmynl4d02smut3fvoweshf', 'NzFhOTQyODlkOGI3YjIxMGQzYzhkMWYxYTljNDg1NmIwZmYwYWZiMDp7InRva2VuIjoiMmY3YTkzYWY1YjU1ZTc3ZjEwZmUzNjU1YmU1ODZmYWFlM2NjODI5MiIsIl9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9pZCI6ImNvcmVudGluLm1hZ3lhckBlcGZlZHUuZnIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjNjNTAxNDZmNWMxMTIwNmY4MmE1Njg5YTBjNGI3YTM2M2NhODBlMzMifQ==', '2020-06-22 09:26:16.328959'),
('hc6wswm29087pjht9nplwfgsu8m5lby7', 'MTY0N2ViMTI1OWMyYjc3YmQzYTQ5MGRmOTE2NzgxM2MyZDJjY2UxZTp7InRva2VuIjoiNGJmYmEyM2I0OWFiY2E3NWQ3M2Y2OWQ1NTg5MDdkNTkyMDA5NGYxMyIsIl9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9pZCI6Im1hcmdvdC5qb3VyZGFuQGVwZmVkdS5mciIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiM2JmZGFmZDA3ZWY2N2VlODk4YWUxNTgwMjZiZTYyZDVmZmQ0NzZmOSJ9', '2020-06-21 20:44:18.042463'),
('hsjm37e7j4hokbsrewu3amom0pf8dk89', 'MTY0N2ViMTI1OWMyYjc3YmQzYTQ5MGRmOTE2NzgxM2MyZDJjY2UxZTp7InRva2VuIjoiNGJmYmEyM2I0OWFiY2E3NWQ3M2Y2OWQ1NTg5MDdkNTkyMDA5NGYxMyIsIl9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9pZCI6Im1hcmdvdC5qb3VyZGFuQGVwZmVkdS5mciIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiM2JmZGFmZDA3ZWY2N2VlODk4YWUxNTgwMjZiZTYyZDVmZmQ0NzZmOSJ9', '2020-06-22 12:38:55.139703'),
('ibnyedv34jnz1n7pedyqgciuep5aame2', 'OTdjYTMyNjFiNzNjYzI4NThhMjNhMDA2Nzc1MjczODJlNDFmMmUyMzp7InRva2VuIjoiMzE2NzBjMTM4OGU2ZmViYTQyMDhiYTRmYjZjOWE3OTZhNDBiOGEyMyIsIl9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9pZCI6ImZhYmllbi5zb2xkZUBlcGZlZHUuZnIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjgyYjhkZGE0NTE5YzgxZDllYThjODhmY2I5MjViZTkwZDVkZTI0NmMifQ==', '2020-06-21 20:45:27.100948'),
('jjwzz4rtq0vyowkaykf50t12vjyajhb0', 'NzFhOTQyODlkOGI3YjIxMGQzYzhkMWYxYTljNDg1NmIwZmYwYWZiMDp7InRva2VuIjoiMmY3YTkzYWY1YjU1ZTc3ZjEwZmUzNjU1YmU1ODZmYWFlM2NjODI5MiIsIl9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9pZCI6ImNvcmVudGluLm1hZ3lhckBlcGZlZHUuZnIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjNjNTAxNDZmNWMxMTIwNmY4MmE1Njg5YTBjNGI3YTM2M2NhODBlMzMifQ==', '2020-06-21 21:13:20.564710'),
('k9t5fkntl13favop2xzzd3vkeev9wehb', 'OTdjYTMyNjFiNzNjYzI4NThhMjNhMDA2Nzc1MjczODJlNDFmMmUyMzp7InRva2VuIjoiMzE2NzBjMTM4OGU2ZmViYTQyMDhiYTRmYjZjOWE3OTZhNDBiOGEyMyIsIl9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9pZCI6ImZhYmllbi5zb2xkZUBlcGZlZHUuZnIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjgyYjhkZGE0NTE5YzgxZDllYThjODhmY2I5MjViZTkwZDVkZTI0NmMifQ==', '2020-06-21 20:44:45.184669'),
('l63v0h1mcx5cnmp0xgnt4r4uhraigjus', 'OTdjYTMyNjFiNzNjYzI4NThhMjNhMDA2Nzc1MjczODJlNDFmMmUyMzp7InRva2VuIjoiMzE2NzBjMTM4OGU2ZmViYTQyMDhiYTRmYjZjOWE3OTZhNDBiOGEyMyIsIl9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9pZCI6ImZhYmllbi5zb2xkZUBlcGZlZHUuZnIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjgyYjhkZGE0NTE5YzgxZDllYThjODhmY2I5MjViZTkwZDVkZTI0NmMifQ==', '2020-06-22 09:12:45.259142'),
('mbvxbi35kj0hejcf0x829w8m1mf7di2y', 'NzFhOTQyODlkOGI3YjIxMGQzYzhkMWYxYTljNDg1NmIwZmYwYWZiMDp7InRva2VuIjoiMmY3YTkzYWY1YjU1ZTc3ZjEwZmUzNjU1YmU1ODZmYWFlM2NjODI5MiIsIl9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9pZCI6ImNvcmVudGluLm1hZ3lhckBlcGZlZHUuZnIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjNjNTAxNDZmNWMxMTIwNmY4MmE1Njg5YTBjNGI3YTM2M2NhODBlMzMifQ==', '2020-06-21 19:30:06.803085'),
('njxk1q080luov98omtjpyg8kyxx9ybza', 'YWZiYjQ1ODJmOTU3YWY5ZmNhMzQ1ODFlYzlkNjE2YzE2YjQ4MTBiMDp7InRva2VuIjoiNjk5OGM2ZGU0OWM5OWIxOTc1OTQ4ZWRmMTRjZDg3YWQzM2RmYjQ1YyIsIl9hdXRoX3VzZXJfaWQiOiJwaWVycmUuZnJhbmNvaXNAZXBmZWR1LmZyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwMTEwNmNmYjE3ZTdjNDUyNGRhNzAyYTM5YTlkNmVlYzg2YTkxMjM5In0=', '2020-06-21 20:10:56.357770'),
('r5tcjm42e145rxi46d9g2vm7mpfpx44q', 'NzFhOTQyODlkOGI3YjIxMGQzYzhkMWYxYTljNDg1NmIwZmYwYWZiMDp7InRva2VuIjoiMmY3YTkzYWY1YjU1ZTc3ZjEwZmUzNjU1YmU1ODZmYWFlM2NjODI5MiIsIl9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9pZCI6ImNvcmVudGluLm1hZ3lhckBlcGZlZHUuZnIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjNjNTAxNDZmNWMxMTIwNmY4MmE1Njg5YTBjNGI3YTM2M2NhODBlMzMifQ==', '2020-06-21 20:53:28.967738'),
('rhmru42xdwrrqw6lgsw3rolbdtoqh6u2', 'OWRjMzIyZDhiNGQ3NTJiOTZmMDQyOTQ2ZGE5OTFkZmRkMDM1MDNkNTp7InRva2VuIjoiZjNkNWM0MWI0Y2Y3OTU0NTlhYzcxZWIxNWM1Njk1ZDg0ZWYyYmVhNyIsIl9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9pZCI6ImFuYW5hcy50cm9waWNhbEBlcGZlZHUuZnIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjJlYWMyN2I1ODU2YjFhYmNkMjI2ZjlkZjQ2NTQ3NGEyZjFlN2Q0MjUifQ==', '2020-06-21 19:30:49.742404'),
('rzmvqm7sihks1p3sjcvly42oop8ikov1', 'OTdjYTMyNjFiNzNjYzI4NThhMjNhMDA2Nzc1MjczODJlNDFmMmUyMzp7InRva2VuIjoiMzE2NzBjMTM4OGU2ZmViYTQyMDhiYTRmYjZjOWE3OTZhNDBiOGEyMyIsIl9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9pZCI6ImZhYmllbi5zb2xkZUBlcGZlZHUuZnIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjgyYjhkZGE0NTE5YzgxZDllYThjODhmY2I5MjViZTkwZDVkZTI0NmMifQ==', '2020-06-23 11:45:45.615289'),
('t2ug3khcdj48rrgu7nhukf67g4dxpesh', 'ZTAyNjAzYWMwYjk3NjY2ZmMzMmZmOWM5YzUxZjM3YmM2MjBiOTEyYzp7InRva2VuIjoiNjMyMDg5ZDY1MjEyNjg4NTA2Yjc3ZjZmZGU4ZDdlZjIzZWMzMDExZCIsIl9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9pZCI6InBhdWwuZGVib2lzc2VsQGVwZmVkdS5mciIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZjVlMDA3ZWE1YzhhMTM3MDI5N2Y0NGVkZDhkNmU1NGRmZDFkMDJhZiJ9', '2020-06-21 20:35:57.796412'),
('x3ujbqisxqf7mxxx00dmgeeqrupaf3fd', 'NzFhOTQyODlkOGI3YjIxMGQzYzhkMWYxYTljNDg1NmIwZmYwYWZiMDp7InRva2VuIjoiMmY3YTkzYWY1YjU1ZTc3ZjEwZmUzNjU1YmU1ODZmYWFlM2NjODI5MiIsIl9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9pZCI6ImNvcmVudGluLm1hZ3lhckBlcGZlZHUuZnIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjNjNTAxNDZmNWMxMTIwNmY4MmE1Njg5YTBjNGI3YTM2M2NhODBlMzMifQ==', '2020-06-22 06:35:02.376328');

-- --------------------------------------------------------

--
-- Structure de la table `login_administration`
--

CREATE TABLE `login_administration` (
  `id` int(11) NOT NULL,
  `user_id` varchar(254) NOT NULL,
  `poste` varchar(255) DEFAULT NULL,
  `phone` varchar(128) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `login_campus`
--

CREATE TABLE `login_campus` (
  `id` int(11) NOT NULL,
  `nom` varchar(30) NOT NULL,
  `adresse` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `login_campus`
--

INSERT INTO `login_campus` (`id`, `nom`, `adresse`) VALUES
(1, 'Sceaux', '3 bis Rue Lakanal, 92330 Sceaux'),
(2, 'Troyes', ' 2 Rue F Sastre, 10430 Rosières-prés-Troyes'),
(3, 'Montpellier', '21 Boulevard Berthelot, 34000 Montpellier');

-- --------------------------------------------------------

--
-- Structure de la table `login_customuser`
--

CREATE TABLE `login_customuser` (
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `email` varchar(254) NOT NULL,
  `avatar` varchar(200) NOT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `is_etudiant` tinyint(1) NOT NULL,
  `is_autre` tinyint(1) NOT NULL,
  `genre` varchar(5) DEFAULT NULL,
  `campus_id` int(11) DEFAULT NULL,
  `Birthdate` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `login_customuser`
--

INSERT INTO `login_customuser` (`password`, `last_login`, `is_superuser`, `is_staff`, `is_active`, `date_joined`, `email`, `avatar`, `photo`, `first_name`, `last_name`, `is_etudiant`, `is_autre`, `genre`, `campus_id`, `Birthdate`) VALUES
('pbkdf2_sha256$180000$UV5apqBYOVLF$gPk1png3ECuf4/pU/+q0ylILErCch57gO/U21qDGDDc=', '2020-06-08 18:25:17.808241', 1, 1, 1, '2020-06-07 19:14:56.417584', 'ananas.tropical@epfedu.fr', 'https://www.gravatar.com/avatar/b42663f505c8ce45f975724f23aed635?d=identicon', '', 'Ananas', 'Tropical', 1, 0, NULL, NULL, NULL),
('pbkdf2_sha256$180000$W4YNloauwIgm$LGdhLZ48KJNauGHDnhtv3SqwFhRUsBizk4laV6do13c=', '2020-06-08 18:25:01.000000', 1, 1, 1, '2020-06-07 19:29:26.000000', 'corentin.magyar@epfedu.fr', 'https://www.gravatar.com/avatar/e43919f8f4b148bc894718faffbfc32d?d=identicon', 'photoProfile/11780032_881761691916324_564830540575674464_o.jpg', 'Corentin', 'Magyar', 1, 0, NULL, 1, '10/10/1997'),
('pbkdf2_sha256$180000$9A3mYBCqq9Of$Iy1MqO5dB83nHL+HMWu9EzV0xt+GcjBVrOxY6pcfUsA=', '2020-06-09 11:45:45.607464', 1, 1, 1, '2020-06-07 20:40:56.995059', 'fabien.solde@epfedu.fr', 'https://www.gravatar.com/avatar/9885078707ed8afac18370dc2bfeff75?d=identicon', 'photoProfile/Sylabus_EPF_4e8tbYa.jpg', 'Fabien', 'SOLDE', 1, 0, NULL, 1, NULL),
('pbkdf2_sha256$180000$taFzMwZcBiw1$/kndBGjpjqcnlUQrOHK4Pr+4q8a/ZC3kNu/uamr34Ck=', '2020-06-08 12:38:55.133614', 1, 1, 1, '2020-06-07 19:35:23.349513', 'margot.jourdan@epfedu.fr', 'https://www.gravatar.com/avatar/56594cb238facbcd22bbb2fb41c8a891?d=identicon', 'photoProfile/download20200302161015.png', 'Margot', 'Jourdan', 1, 0, NULL, 1, '01/02/1998'),
('pbkdf2_sha256$180000$zFyQnWCgN2vH$lNF6ks93dJ21kceCQZcPqHYW0itTL7VyiGEd8Q1wk4Q=', '2020-06-07 20:47:06.237570', 1, 1, 1, '2020-06-07 20:35:03.862705', 'paul.deboissel@epfedu.fr', 'https://www.gravatar.com/avatar/93f901f31f7404c1fe4b39842d18ffc2?d=identicon', 'photoProfile/Snapchat-738128810.jpg', 'Paul', 'de Boissel', 1, 0, NULL, 1, '23/08/1996'),
('pbkdf2_sha256$180000$UckCGqv5ZrE5$yt2dZMNOHPHnPTAd5N0jQ7QxCJHVuJ1F4HeIAIYiZOc=', '2020-06-07 20:10:56.355301', 1, 1, 1, '2020-06-07 20:10:37.453929', 'pierre.francois@epfedu.fr', 'https://www.gravatar.com/avatar/10b599bae14ab7eb6bcc069b7a6949ce?d=identicon', '', 'Pierre', 'FRANCOIS', 1, 0, NULL, 1, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `login_customuser_groups`
--

CREATE TABLE `login_customuser_groups` (
  `id` int(11) NOT NULL,
  `customuser_id` varchar(254) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `login_customuser_user_permissions`
--

CREATE TABLE `login_customuser_user_permissions` (
  `id` int(11) NOT NULL,
  `customuser_id` varchar(254) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `login_customuser_user_permissions`
--

INSERT INTO `login_customuser_user_permissions` (`id`, `customuser_id`, `permission_id`) VALUES
(3, 'corentin.magyar@epfedu.fr', 45),
(1, 'corentin.magyar@epfedu.fr', 49),
(2, 'corentin.magyar@epfedu.fr', 53);

-- --------------------------------------------------------

--
-- Structure de la table `login_etudiant`
--

CREATE TABLE `login_etudiant` (
  `id` int(11) NOT NULL,
  `user_id` varchar(254) NOT NULL,
  `majeure_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `login_etudiant`
--

INSERT INTO `login_etudiant` (`id`, `user_id`, `majeure_id`) VALUES
(1, 'corentin.magyar@epfedu.fr', 1),
(2, 'margot.jourdan@epfedu.fr', 1),
(3, 'pierre.francois@epfedu.fr', 1),
(4, 'paul.deboissel@epfedu.fr', 1),
(5, 'fabien.solde@epfedu.fr', 1);

-- --------------------------------------------------------

--
-- Structure de la table `login_majeure`
--

CREATE TABLE `login_majeure` (
  `id` int(11) NOT NULL,
  `nom` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `login_majeure`
--

INSERT INTO `login_majeure` (`id`, `nom`) VALUES
(10, 'Ancien'),
(12, 'Apprentissage'),
(11, 'Bachelor'),
(9, 'Cycle généraliste'),
(2, 'Majeure Aéronautique & Espace'),
(8, 'Majeure Data Engineering'),
(4, 'Majeure Energie & Environnement'),
(5, 'Majeure Engineering & Management'),
(3, 'Majeure Ingénierie & Architecture Durable'),
(1, 'Majeure Ingénierie & Numérique'),
(6, 'Majeure Ingénierie & Santé'),
(7, 'Majeure Structure & Matériaux'),
(13, 'Master of Science ICE'),
(14, 'Passerelle SIGMA');

-- --------------------------------------------------------

--
-- Structure de la table `messenger_chat`
--

CREATE TABLE `messenger_chat` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `status` varchar(7) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `messenger_chat`
--

INSERT INTO `messenger_chat` (`id`, `name`, `timestamp`, `status`) VALUES
(1, 'HELLO', '2020-06-07 20:13:42.106013', 'Public'),
(2, 'Projet Ananas', '2020-06-08 09:57:36.279581', 'Private'),
(3, 'Public prés', '2020-06-08 12:41:45.570237', 'Public');

-- --------------------------------------------------------

--
-- Structure de la table `messenger_chat_admin`
--

CREATE TABLE `messenger_chat_admin` (
  `id` int(11) NOT NULL,
  `chat_id` int(11) NOT NULL,
  `customuser_id` varchar(254) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `messenger_chat_admin`
--

INSERT INTO `messenger_chat_admin` (`id`, `chat_id`, `customuser_id`) VALUES
(1, 1, 'corentin.magyar@epfedu.fr'),
(2, 2, 'paul.deboissel@epfedu.fr'),
(4, 3, 'fabien.solde@epfedu.fr'),
(3, 3, 'margot.jourdan@epfedu.fr');

-- --------------------------------------------------------

--
-- Structure de la table `messenger_chat_messages`
--

CREATE TABLE `messenger_chat_messages` (
  `id` int(11) NOT NULL,
  `chat_id` int(11) NOT NULL,
  `message_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `messenger_chat_messages`
--

INSERT INTO `messenger_chat_messages` (`id`, `chat_id`, `message_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4),
(5, 1, 5),
(6, 1, 6),
(7, 3, 7),
(8, 3, 8);

-- --------------------------------------------------------

--
-- Structure de la table `messenger_chat_participants`
--

CREATE TABLE `messenger_chat_participants` (
  `id` int(11) NOT NULL,
  `chat_id` int(11) NOT NULL,
  `customuser_id` varchar(254) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `messenger_chat_participants`
--

INSERT INTO `messenger_chat_participants` (`id`, `chat_id`, `customuser_id`) VALUES
(1, 1, 'ananas.tropical@epfedu.fr'),
(2, 1, 'corentin.magyar@epfedu.fr'),
(8, 1, 'fabien.solde@epfedu.fr'),
(3, 1, 'margot.jourdan@epfedu.fr'),
(9, 1, 'paul.deboissel@epfedu.fr'),
(77, 1, 'pierre.francois@epfedu.fr'),
(43, 2, 'corentin.magyar@epfedu.fr'),
(46, 2, 'fabien.solde@epfedu.fr'),
(45, 2, 'margot.jourdan@epfedu.fr'),
(47, 2, 'paul.deboissel@epfedu.fr'),
(44, 2, 'pierre.francois@epfedu.fr'),
(62, 3, 'ananas.tropical@epfedu.fr'),
(63, 3, 'corentin.magyar@epfedu.fr'),
(64, 3, 'fabien.solde@epfedu.fr'),
(65, 3, 'margot.jourdan@epfedu.fr'),
(66, 3, 'paul.deboissel@epfedu.fr'),
(67, 3, 'pierre.francois@epfedu.fr');

-- --------------------------------------------------------

--
-- Structure de la table `messenger_chat_tag`
--

CREATE TABLE `messenger_chat_tag` (
  `id` int(11) NOT NULL,
  `chat_id` int(11) NOT NULL,
  `taggedmessages_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `messenger_chat_tag`
--

INSERT INTO `messenger_chat_tag` (`id`, `chat_id`, `taggedmessages_id`) VALUES
(2, 3, 2);

-- --------------------------------------------------------

--
-- Structure de la table `messenger_message`
--

CREATE TABLE `messenger_message` (
  `id` int(11) NOT NULL,
  `contact_id` varchar(254) NOT NULL,
  `content` longtext NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `is_admin` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `messenger_message`
--

INSERT INTO `messenger_message` (`id`, `contact_id`, `content`, `timestamp`, `is_admin`) VALUES
(1, 'corentin.magyar@epfedu.fr', 'bonjour à tous :)', '2020-06-07 20:14:20.580423', 1),
(2, 'margot.jourdan@epfedu.fr', 'bonsoir :)', '2020-06-07 20:20:24.874306', 0),
(3, 'corentin.magyar@epfedu.fr', 'hello', '2020-06-07 21:13:48.216058', 1),
(4, 'fabien.solde@epfedu.fr', 'Bonjour, bonne chance pour la présentation de cette aprem !', '2020-06-08 07:57:02.043659', 0),
(5, 'paul.deboissel@epfedu.fr', 'Bonjour, bonjour !', '2020-06-08 09:20:47.890940', 0),
(6, 'fabien.solde@epfedu.fr', 'On est là !', '2020-06-08 12:41:45.378002', 0),
(7, 'fabien.solde@epfedu.fr', 'Bonjour', '2020-06-08 12:41:53.817085', 0),
(8, 'paul.deboissel@epfedu.fr', 'Salut Fabien !', '2020-06-08 12:42:26.383511', 0);

-- --------------------------------------------------------

--
-- Structure de la table `messenger_taggedmessages`
--

CREATE TABLE `messenger_taggedmessages` (
  `id` int(11) NOT NULL,
  `content_id` int(11) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `author_id` varchar(254) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `messenger_taggedmessages`
--

INSERT INTO `messenger_taggedmessages` (`id`, `content_id`, `timestamp`, `author_id`) VALUES
(1, 1, '2020-06-07 20:52:08.032352', 'corentin.magyar@epfedu.fr'),
(2, 7, '2020-06-08 12:42:30.983922', 'margot.jourdan@epfedu.fr');

-- --------------------------------------------------------

--
-- Structure de la table `timeline_article`
--

CREATE TABLE `timeline_article` (
  `id` int(11) NOT NULL,
  `date` datetime(6) NOT NULL,
  `titre` varchar(100) NOT NULL,
  `auteur_id` varchar(254) NOT NULL,
  `contenu_post` longtext NOT NULL,
  `slug` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `timeline_article`
--

INSERT INTO `timeline_article` (`id`, `date`, `titre`, `auteur_id`, `contenu_post`, `slug`, `photo`) VALUES
(3, '2020-06-07 19:39:46.781419', 'TEST', 'corentin.magyar@epfedu.fr', '---\r\n**Advertisement :)**\r\n\r\n- **[pica](https://nodeca.github.io/pica/demo/)** - high quality and fast image\r\n  resize in browser.\r\n- **[babelfish](https://github.com/nodeca/babelfish/)** - developer friendly\r\n  i18n with plurals support and easy syntax.\r\n\r\nYou will like those projects!\r\n\r\n---\r\n\r\n# h1 Heading 8-)\r\n## h2 Heading\r\n### h3 Heading\r\n#### h4 Heading\r\n##### h5 Heading\r\n###### h6 Heading\r\n\r\n\r\n## Horizontal Rules\r\n\r\n___\r\n\r\n---\r\n\r\n***\r\n\r\n\r\n## Typographic replacements\r\n\r\nEnable typographer option to see result.\r\n\r\n(c) (C) (r) (R) (tm) (TM) (p) (P) +-\r\n\r\ntest.. test... test..... test?..... test!....\r\n\r\n!!!!!! ???? ,,  -- ---\r\n\r\n\"Smartypants, double quotes\" and \'single quotes\'\r\n\r\n\r\n## Emphasis\r\n\r\n**This is bold text**\r\n\r\n*This is italic text*\r\n\r\n~~Strikethrough~~\r\n\r\n\r\n## Blockquotes\r\n\r\n\r\n> Blockquotes can also be nested...\r\n>> ...by using additional greater-than signs right next to each other...\r\n> > > ...or with spaces between arrows.\r\n\r\n\r\n## Lists\r\n\r\nUnordered\r\n\r\n+ Create a list by starting a line with `+`, `-`, or `*`\r\n+ Sub-lists are made by indenting 2 spaces:\r\n  - Marker character change forces new list start:\r\n    * Ac tristique libero volutpat at\r\n    + Facilisis in pretium nisl aliquet\r\n    - Nulla volutpat aliquam velit\r\n+ Very easy!\r\n\r\nOrdered\r\n\r\n1. Lorem ipsum dolor sit amet\r\n2. Consectetur adipiscing elit\r\n3. Integer molestie lorem at massa\r\n\r\n\r\n1. You can use sequential numbers...\r\n1. ...or keep all the numbers as `1.`\r\n\r\nStart numbering with offset:\r\n\r\n57. foo\r\n1. bar\r\n\r\n\r\n## Code\r\n\r\nInline `code`\r\n\r\nIndented code\r\n\r\n    // Some comments\r\n    line 1 of code\r\n    line 2 of code\r\n    line 3 of code\r\n\r\n\r\nBlock code \"fences\"\r\n\r\n```\r\nSample text here...\r\n```\r\n\r\nSyntax highlighting\r\n\r\n``` js\r\nvar foo = function (bar) {\r\n  return bar++;\r\n};\r\n\r\nconsole.log(foo(5));\r\n```\r\n\r\n## Tables\r\n\r\n| Option | Description |\r\n| ------ | ----------- |\r\n| data   | path to data files to supply the data that will be passed into templates. |\r\n| engine | engine to be used for processing templates. Handlebars is the default. |\r\n| ext    | extension to be used for dest files. |\r\n\r\nRight aligned columns\r\n\r\n| Option | Description |\r\n| ------:| -----------:|\r\n| data   | path to data files to supply the data that will be passed into templates. |\r\n| engine | engine to be used for processing templates. Handlebars is the default. |\r\n| ext    | extension to be used for dest files. |\r\n\r\n\r\n## Links\r\n\r\n[link text](http://dev.nodeca.com)\r\n\r\n[link with title](http://nodeca.github.io/pica/demo/ \"title text!\")\r\n\r\nAutoconverted link https://github.com/nodeca/pica (enable linkify to see)\r\n\r\n\r\n## Images\r\n\r\n![Minion](https://octodex.github.com/images/minion.png)\r\n![Stormtroopocat](https://octodex.github.com/images/stormtroopocat.jpg \"The Stormtroopocat\")\r\n\r\nLike links, Images also have a footnote style syntax\r\n\r\n![Alt text][id]\r\n\r\nWith a reference later in the document defining the URL location:\r\n\r\n[id]: https://octodex.github.com/images/dojocat.jpg  \"The Dojocat\"\r\n\r\n\r\n## Plugins\r\n\r\nThe killer feature of `markdown-it` is very effective support of\r\n[syntax plugins](https://www.npmjs.org/browse/keyword/markdown-it-plugin).\r\n\r\n\r\n### [Emojies](https://github.com/markdown-it/markdown-it-emoji)\r\n\r\n> Classic markup: :wink: :crush: :cry: :tear: :laughing: :yum:\r\n>\r\n> Shortcuts (emoticons): :-) :-( 8-) ;)\r\n\r\nsee [how to change output](https://github.com/markdown-it/markdown-it-emoji#change-output) with twemoji.\r\n\r\n\r\n### [Subscript](https://github.com/markdown-it/markdown-it-sub) / [Superscript](https://github.com/markdown-it/markdown-it-sup)\r\n\r\n- 19^th^\r\n- H~2~O\r\n\r\n\r\n### [\\<ins>](https://github.com/markdown-it/markdown-it-ins)\r\n\r\n++Inserted text++\r\n\r\n\r\n### [\\<mark>](https://github.com/markdown-it/markdown-it-mark)\r\n\r\n==Marked text==\r\n\r\n\r\n### [Footnotes](https://github.com/markdown-it/markdown-it-footnote)\r\n\r\nFootnote 1 link[^first].\r\n\r\nFootnote 2 link[^second].\r\n\r\nInline footnote^[Text of inline footnote] definition.\r\n\r\nDuplicated footnote reference[^second].\r\n\r\n[^first]: Footnote **can have markup**\r\n\r\n    and multiple paragraphs.\r\n\r\n[^second]: Footnote text.\r\n\r\n\r\n### [Definition lists](https://github.com/markdown-it/markdown-it-deflist)\r\n\r\nTerm 1\r\n\r\n:   Definition 1\r\nwith lazy continuation.\r\n\r\nTerm 2 with *inline markup*\r\n\r\n:   Definition 2\r\n\r\n        { some code, part of Definition 2 }\r\n\r\n    Third paragraph of definition 2.\r\n\r\n_Compact style:_\r\n\r\nTerm 1\r\n  ~ Definition 1\r\n\r\nTerm 2\r\n  ~ Definition 2a\r\n  ~ Definition 2b\r\n\r\n\r\n### [Abbreviations](https://github.com/markdown-it/markdown-it-abbr)\r\n\r\nThis is HTML abbreviation example.\r\n\r\nIt converts \"HTML\", but keep intact partial entries like \"xxxHTMLyyy\" and so on.\r\n\r\n*[HTML]: Hyper Text Markup Language\r\n\r\n### [Custom containers](https://github.com/markdown-it/markdown-it-container)\r\n\r\n::: warning\r\n*here be dragons*\r\n:::', 'test', 'photos/EPF-copie.jpg'),
(4, '2020-06-07 19:45:54.218137', 'Coronavirus - Fermeture de l\'école', 'margot.jourdan@epfedu.fr', '**Coronavirus - Covid-19 : informations, consignes et foire aux questions**\r\n\r\nEn raison de la situation sanitaire actuelle, l\'EPF école d\'ingénieur.e.s met en place cette page d\'informations. \r\n\r\nVous y trouverez une Foire Aux Questions en bas de page ainsi que les informations mises à jour plusieurs fois par semaine. \r\nMise à jour du 2 juin 2020 - Communiqué de presse du ministère de l\'intérieur\r\n\r\nSur les déplacements et restrictions : téléchargez le document \r\nMise à jour du 13 mai 2020 - sur l\'accompagnement des élèves en situation difficile\r\nBesoin de soutien en cette période ? Voici quelques numéros / contacts utiles pour vous accompagner en situation difficile.\r\n\r\nMme NDONGMEZA Edith, assistante sociale du CROUS à Antony avec qui nous travaillons. En revanche, je ne sais pas si elle a poursuivi son activité en télétravail avec le confinement. edith.ndongmeza@crous-versailles.fr / ndongmeza.edith@u-psud.fr\r\n\r\nLa plateforme d\'écoute Nightline Paris est joignable par téléphone à toute heure il me semble, les bénévoles pourront lui donner les coordonnées de professionnels de santé. Leur site https://www.soutien-etudiant.info/ recense également toutes les structures de soutien psychologique pour chaque académie, il liste les services d’écoute disponibles dans toute la France par thème.\r\n\r\nMme Laure AIOTTI, naturopathe & sophrologue à Montpellier qui est disponible pour l\'ensemble des étudiants EPF qui ressentent le besoin d\'être accompagnés.\r\n\r\nhttp://www.laureariotti-naturopathe.fr - la.naturoandco@gmail.com\r\n\r\nSachez aussi que le directeur général de la Santé a annoncé la création d\'une cellule d\'aide psychologique via le numéro vert 0800.130.000, afin d\'aider les Français désemparés face à la menace épidémique du nouveau coronavirus et aux mesures drastiques du confinement.\r\n\r\nCe site web répertorie toutes les possibilités de soutien psy. https://www.soutien-etudiant.info/\r\n\r\nN\'hésitez pas à consulter :  http://www.apsytude.com/fr/apsytude/nos-actions/happsy-line/\r\n\r\nEt FIL SANTÉ JEUNES - 0 800 235 236 (gratuit depuis un poste fixe) 01 44 93 30 74 (depuis un portable)\r\nNous vous rappelons aussi l’existence de l’adresse HelpCovid19@epf.fr sur laquelle vous pouvez signaler toute difficulté personnelle (isolement, maladie etc.) ou matérielle (pb de matériel, réseau, financière etc).\"\r\n\r\nMise à jour du 28 avril 2020 - sur la validation des stages effectués en télétravail \r\n\r\nSauf avis contraire du gouvernement dans les semaines à venir, l’école autorise exceptionnellement pour l’année scolaire 2019-2020, tous les étudiants à réaliser leur stage en télétravail. Cette dérogation ne prévaut que dans le contexte actuel de confinement car elle n’est d’ordinaire pas autorisée (L. 124-1 du Code de l’éducation).\r\n\r\nEn conséquence, si vous venez de trouver votre stage en France ou à l\'international ; au regard de la situation sanitaire actuelle et de l’incertitude portant sur la date de levée des confinements, tous les stages sont concernés, quelles que soient les dates de début et de fin de stage, le pays concerné (France ou international) et l\'objet des missions réalisées.\r\n\r\n \r\nMise à jour du 28 avril 2020 - sur les stages de bachelors \r\n\r\nCompte-tenu des circonstances sanitaires nous précisons et adaptons les règles concernant les stages. Nous avons conscience des difficultés que chacun peut rencontrer mais il est essentiel de préserver autant que possible les compétences et la qualité de notre formation.\r\nEnsemble, nous relèverons ce challenge et accompagnerons et étudierons la situation de chacun avec objectivité et bienveillance.\r\nVeuillez trouver ci-joint les adaptations possibles selon votre année de formation.\r\nNous vous faisons confiance.', 'coronavirus-fermeture-de-lecole', 'photos/chla-what-you-should-know-covid-19-1200x628-01-1400x675-c-center.jpg'),
(12, '2020-06-07 20:19:30.195126', 'Réinscriptions ouvertes', 'margot.jourdan@epfedu.fr', '### Modalités de réinscription 2020/2021\r\n\r\nLes réinscriptions en ligne seront ouvertes  **du 25 mai au 21 juin 2020**.  \r\n\r\nPour toutes questions concernant le règlement des frais de scolarité ou le contrat, contacter : [reinscription@epf.fr](mailto:reinscription@epf.fr)\r\n\r\nCette procédure concerne tous les élèves sauf :\r\n\r\n* les apprentis et les contrats de professionnalisation (ayant déjà signé un contrat de travail avec leur entreprise d\'accueil)  \r\n_si votre contrat est en cours de signature, merci de procéder à la réinscription standard en choisissant le mode de règlement \"prélèvements en 10 fois\"_ -  _merci de nous contacter une fois le contrat signé afin de supprimer l\'échéancier de règlement_\r\n\r\n* les bachelors  \r\n\r\nÉTAPE 1 : Vous devez impérativement vous acquitter auprès du  **CROUS**  de la cotisation annuelle de Contribution Vie Etudiante et de Campus (**CVEC**) en application de la loi relative à l\'orientation et à la réussite des étudiants du 8 mars 2018.  Plus d’information sur : [http://cvec-info.nuonet.fr/la-cvec.html](http://cvec-info.nuonet.fr/la-cvec.html)| [**Obtenir mon attestation**](https://cvec.etudiant.gouv.fr/)\r\n\r\nLe numéro CVEC ainsi que l\'attestation vous seront demandés dans les étapes ultérieures de la réinscription.\r\n\r\nÉTAPE 2 : dans My epf rubrique \"**[Modifier mes informations personnelles et réinscription](https://my.epf.fr/_layouts/crypt/generer_cle.aspx?service=fiche_etudiant)**\" (ouverture le Lundi 25 Mai 18h)\r\n\r\nCliquez sur \"Modifier vos données\", vérifiez et modifiez si besoin vos informations personnelles, saisissez votre numéro de CVEC, choisissez le mode de règlement des frais de scolarité et cliquez sur \"Valider les modifications\".\r\n\r\n> Montant des frais de scolarité 2020-2021 :\r\n> \r\n> Formation Généraliste : 8360 €\r\n> \r\n> Formation Technologique : 6200€\r\n> \r\n> Autres formations : tarifs spécifiques\r\n> \r\n> 2 modes de règlement possibles:\r\n> \r\n> - paiement au comptant par prélèvement au 3 Août 2020 de la  **totalité**  de la scolarité\r\n> \r\n> - paiement échelonné en 10 prélèvements de 10 Septembre 2020 au 10 Juin 2021\r\n\r\nETAPE 3 : dans My epf rubrique \"[**Télécharger mes documents administratifs**](https://my.epf.fr/_layouts/crypt/generer_cle.aspx?service=edition)\" (ouverture le Lundi 25 Mai 18h)\r\n\r\nCliquez sur Télécharger à côté du contrat d\'études. Vérifiez le contenu du contrat puis cliquez sur Démarrer pour amorcer la procédure de signature électronique. Un premier mail est envoyé à l\'élève sur son adresse epfedu. L\'élève doit consulter sa messagerie epfedu et suivre les instructions données dans le message \"EPF via Docusign\". Une fois que l\'élève a signé, un mail est automatiquement envoyé au référent financier qui doit à son tour suivre les instructions données dans le message \"Epf via Docusign\". Une fois que les deux ont signé, un mail final est envoyé aux deux signataires et l\'EPF récupère automatiquement le document signé.\r\n\r\nETAPE 4 : dans My epf rubrique \"**[Déposer des documents administratifs](https://my.epf.fr/_layouts/crypt/generer_cle.aspx?service=load-my-documents)\"**\r\n\r\nDéposez les documents pdf pour compléter votre dossier (Attestation CVEC, RIB si changement de coordonnées bancaires et paiement par prélèvement, attestation bourse si boursier et Carte Nationale d\'Identité si nécessaire)\r\n\r\n**Dans tous les cas, vous recevrez un mail de confirmation de la bonne réception de votre dossier de réinscription dès qu\'il sera traité par nos services.**', 'reinscriptions-ouvertes', 'photos/reinscriptions_DhD31kP.png'),
(14, '2020-06-07 20:31:28.950827', 'Le déménagement au campus de Cachan décalé à 2022', 'margot.jourdan@epfedu.fr', 'En raison de l\'arrêt des travaux lors de la période de confinement due au covid-19, le chantier du Campus de Cachan à pris du retard. \r\nAinsi, celui-ci ne pourra pas être complété pour la rentrée de septembre 2021.\r\nOn espère son ouverture au deuxième semestre 2022.', 'le-demenagement-au-campus-de-cachan-decale-a-2022', 'photos/ens-cachan-retouche.jpg'),
(15, '2020-06-08 09:17:02.795139', 'L\'implication des étudiants dans le cadre de la gestion du Covid-19', 'paul.deboissel@epfedu.fr', '**Comment les étudiants, et plus particulièrement les étudiants ingénieurs peuvent-ils s’impliquer dans la gestion de la crise du Covid-19 ?**\r\n\r\n\r\nCela fait maintenant sept semaines que les étudiants de la France entière sont en confinement. En effet, le 12 mars 2020, le président Emmanuel Macron a annoncé la fermeture des écoles, lycées et universités.\r\n\r\n**Comment les étudiants peuvent-ils alors aider et se rendre utiles pendant cette crise du Covid-19 ?**\r\n\r\nDès les premiers jours, un hashtag #JeVeuxAider est apparu sur les réseaux sociaux. Bien que confinés chez eux, les étudiants ont manifesté leur désir de se rendre utile pendant cette crise sanitaire majeure au travers de cet hashtag. Rapidement, le gouvernement a pu répondre à cette volonté de milliers d’étudiants en explicitant sur le site [etudiant.gouv.fr][1] les actions qu’ils pourraient mener.\r\n\r\nVoici les 4 actions prioritaires citées par le gouvernement :\r\n\r\n·       L’aide alimentaire et d\'urgence.\r\n\r\n·       La garde exceptionnelle d\'enfants.\r\n\r\n·       Le lien avec les personnes fragiles isolées.\r\n\r\n·       La solidarité de proximité.\r\n\r\nAinsi, les étudiants souhaitant participer à l’une de ces actions ont pu s’inscrire simplement sur le site jeveuxaider.gouv.fr, mis en place par le gouvernement.\r\n\r\nComment les étudiants ingénieurs peuvent-ils mettre en application les connaissances apprises lors de leur cursus afin de venir en aide ?\r\n\r\n**L’AUF (Agence Universitaire de la Francophonie)** a lancé un appel à projets international afin de soutenir les étudiants, élèves-ingénieurs ou jeunes chercheurs ayant une initiative de projets avec un impact technologique, économique ou social à court terme, lié à la pandémie.\r\nEn effet, pendant cette période inhabituelle, les étudiants sont particulièrement réactifs, ingénieux et créatifs.\r\nL’objectif de cet appel à projets est de mettre en valeur l’apport des étudiants dans la gestion de la crise sanitaire et de pouvoir aider à surmonter les difficultés provoquées par celle-ci, notamment dans le système de santé.\r\n\r\nVoici quelques exemples :\r\n\r\n **- Communication et sensibilisation à la prévention des risques\r\n   sanitaires. \r\n - Prévention des impacts psychologiques ou\r\n   socio-économiques de la crise sanitaire.\r\n - Production de matériel\r\n   indispensable aux soins, à la protection ou à la prévention des\r\n   risques sanitaires (masques, gants, désinfectants, respirateurs…).\r\n - Développement d’applications et d’outils d’aide à la décision.**\r\n \r\nL’une des problématiques de cette crise sanitaire est la logistique et notamment la gestion des stocks de gants, de masques et de blouses dans les milieux hospitaliers. Certains étudiants ingénieurs sont ainsi allés soutenir les hôpitaux dans leur organisation.  Il s’agit de les accompagner dans la gestion du personnel en réalisant notamment des plannings. Les étudiants peuvent également aider à gérer des stocks en créant des outils de logistique efficaces. Ceux-ci permettent de donner un accès simplifié à l’état des réserves en temps et en heure, la possibilité de l’actualiser et donc de faciliter la gestion des stocks.\r\n\r\nCes actions permettent de soulager le personnel hospitalier dans leurs tâches quotidiennes, qui demandent beaucoup de temps et d’efforts. Les soignants peuvent ainsi pleinement se consacrer aux patients malades. Cette aide logistique peut s’étendre à tous les milieux médicaux ainsi qu’aux entreprises de production, notamment celles spécialisées en matériels sanitaires.\r\nEn dehors du milieu médical, les étudiants ingénieurs peuvent aider à la mise en place de solutions numériques telles que des applications mobiles ou des sites internet.\r\nCette crise a fait naître une nouvelle ère digitale, où le numérique est au cœur des nouvelles stratégies des entreprises et des commerçants.\r\n\r\n \r\n\r\nAinsi, l’AUF met à disposition un fonds de 500 000 euros pour cet appel à projets.\r\nCelui-ci ? ouvert jusqu’au 3 mai 2020, concerne des projets de moins de 10 000 euros à 50 000 euros.\r\n\r\n \r\n\r\nDe nombreuses plateformes ont été créées afin de pouvoir impliquer le plus grand monde dans la recherche de solutions face à la crise.\r\n\r\nC’est notamment le cas du site [www.covid3d.org][2], une plateforme interne d\'impression haut-débit mise en place par l’APHP, permettant de répondre aux besoins sanitaires urgents des soignants. Ce site fait office de fédération des initiatives de conceptions et d’impressions 3D pour lutter contre le Covid-19 en Île-de-France.\r\n\r\nCette plateforme fait appel aux compétences des fabricants et des ingénieurs. Ceux-ci peuvent notamment :\r\n\r\n\r\n·       Participer à la recherche et au développement via JOGL (Just One Giant Lab), un partenaire de la plateforme qui est le premier laboratoire de recherche et d’innovation. Celui-ci fonctionne comme une plateforme de mobilisation massive.\r\nCette initiative vise à créer les solutions indispensables et à développer la recherche afin de faire face à la pandémie et de ralentir sa propagation. Ces actions se concentrent sur la détection, la prévention et le traitement du virus.\r\n\r\n·       Participer à la conception et à la diffusion de matériel médical par les soignants grâce au partenaire Emergency.IO. Il peut s’agir de matériel de protection et de confort ou d’équipements médicaux. Les modèles sont réalisés grâce à des procédés de fabrication innovants tels que la conception et l’impression 3D.\r\n\r\nCette plateforme est divisée en deux parties : la première est à destination des soignants afin d’enregistrer leurs besoins et la seconde est à destination des ingénieurs et des fabricants, afin qu’ils puissent prendre connaissance des demandes et besoins du personnel médical.\r\n\r\nMargaux PAULIAC, élève en 3ème année à l’EPF a d’ailleurs utilisé son imprimante 3D pour fabriquer des visières de protection antiprojection afin de se rendre utile et de contribuer à l’élan de solidarité.\r\n\r\n![Figure 1. Photo du catalogue de projets de la plateforme 3D COVID][3]\r\n\r\nFace à cette situation, **EPF Projets Sceaux** peut aider les entreprises à trouver des solutions logistiques mais également digitales pour contribuer à la gestion de la crise.\r\n\r\nNos compétences variées, notamment dans les domaines de l’IT et du Digital, comprenant la réalisation de sites internet, de logiciels, d’applications web et mobiles, la gestion de bases de données et la conception assistée par ordinateur, nous permettent de répondre de façon adaptée aux différents besoins de nos clients.\r\n\r\n\r\nCapucine BUARD\r\n\r\n\r\n  [1]: http://etudiant.gouv.fr\r\n  [2]: https://www.covid3d.org/\r\n  [3]: https://www.epfprojets-sceaux.com/Web/img/Covid%2019%20et%20%C3%A9tudiants_files/image002.jpg', 'limplication-des-etudiants-dans-le-cadre-de-la-gestion-du-covid-19', 'photos/img_article.png'),
(16, '2020-06-08 09:47:51.328307', 'Aide covid-19 jeunes :', 'fabien.solde@epfedu.fr', '###Aide covid-19 jeunes : aide de 200 euros versée aux étudiants et aux jeunes précaires\r\n\r\n\r\nÉdouard Philippe a annoncé le 4 mai devant le Sénat le versement d\'une aide de 200 € dès le mois de juin pour soutenir les étudiants et les jeunes précaires de moins de 25 ans en grande difficulté face à la crise sanitaire liée à l\'épidémie du Coronavirus. En raison du confinement, certains jeunes se trouvent dans une situation financière critique. Cette aide ponctuelle sera versée en une fois et devrait concerner environ 800 000 jeunes.\r\n\r\n![enter image description here][1]\r\n\r\n###Qui est concerné ?\r\nEn raison du confinement instauré pour lutter contre la propagation de l\'épidémie du Coronavirus, de nombreux étudiants et jeunes gens font face à de grandes difficultés financières du fait de la perte de leur emploi et de la fermeture des restaurants universitaires.\r\n\r\nUne aide de 200 € sera versée dès le début du mois de juin aux étudiants, boursiers ou non boursiers, ayant perdu leur travail (à partir de 32h par mois, soit 8h par semaine) ou leur stage gratifié ainsi qu\'aux étudiants originaires d\'outre-mer isolés en métropole et qui n\'ont pu rentrer chez eux en raison de la crise sanitaire.\r\n\r\n###### Les apprentis et les étudiants en chômage partiel ne sont donc pas concernés.\r\n\r\nCette aide de 200 € sera versée mi-juin aux jeunes de moins de 25 ans dans une situation « précaire » ou « modeste » bénéficiaires des allocations personnalisées au logement (APL).\r\n\r\n#####Modalités d\'attribution aux étudiants\r\nLes étudiants devront remplir un formulaire disponible dès le 12 mai sur le site etudiants.gouv.fr . Les instructions pour remplir les dossiers seront simplifiées et le versement de l\'aide exceptionnelle interviendra dans les semaines qui suivront afin que les étudiants puissent en bénéficier dès le début du mois de juin.\r\n\r\n**Cette aide exceptionnelle viendra en complément :**\r\n\r\n - Des bourses sur critères sociaux ;\r\n - Des aides d\'urgence ;\r\n - Des aides spécifiques mises en place par les établissements (bons d\'achat alimentaire ou de matériel informatique et de téléphonie).\r\n\r\nVoir l\'article original sur : [https://www.service-public.fr/particuliers/actualites/A14039][2]\r\n\r\n\r\n  [1]: /media/pagedown-uploads/bourse.jpg\r\n\r\n  [2]: https://www.service-public.fr/particuliers/actualites/A14039', 'aide-covid-19-jeunes', 'photos/Souuus.jpeg'),
(17, '2020-06-08 09:48:30.098541', 'La recherche au cœur de la formation EPF', 'paul.deboissel@epfedu.fr', 'La recherche est située au cœur de l’économie de la connaissance et de l’innovation. Ainsi, l’EPF estime que la confrontation de ses élèves à la recherche peut développer leurs qualités de créativité, de curiosité, de rigueur, de prise de risque et d’autonomie. **Ces qualités sont au centre du processus de l’innovation.**\r\n\r\nCette confrontation ouvre aux élèves-ingénieurs [de nouvelles perspectives professionnelles dans les centres de R&D et les start-ups.][1]\r\n\r\nL’EPF a placé la recherche au cœur de son processus de formation. L’exposition des élèves à la recherche s’effectue grâce :\r\n\r\n - Aux **enseignants-chercheurs** et aux **intervenants extérieurs** (CNRS, R&D industrielles…) qui leur transfèrent leurs connaissances et leurs méthodologies ;\r\n - A un **parcours pédagogique** qui les confrontent à des expériences recherche ;\r\n - Aux opportunités offertes par certains stages de 4ème année en laboratoire de recherche (25 % des élèves EPF), avec prise de brevets et/ou la rédaction de publications scientifiques.\r\n\r\nEn dernière année d’études, l’EPF offre la possibilité de préparer un Master 2 Recherche, qui peut déboucher sur une Thèse (3% des élèves EPF diplômés).\r\n\r\n**LIENS INDUSTRIELS**\r\n\r\nGrâce aux liens privilégiés tissés avec des entreprises partenaires, l’EPF a mis en place 4 chaires d\'entreprises depuis 2012:\r\n\r\n - **Thales** dans le domaine de la cybersécurité ;\r\n - **Dassault Systèmes** dans le domaine de l\'ingénierie systèmes ;\r\n - **Global Concept** dans le domaine des télécommunications ;\r\n - **Odysée Environnement** dans le domaine du traitement des eaux.\r\n\r\nLes partenaires de l\'EPF sont ainsi impliqués dans la formation des élèves ingénieurs, dans le développement de la recherche et dans l\'ingénierie pédagogique.\r\n\r\n**LES TECHLABS**\r\n\r\nL’EPF a créé des **TechLab** sur chacun de ses trois campus de Sceaux, Troyes et Montpellier, pour offrir aux élèves des **moyens de conception et de prototypage** dans le cadre de leurs projets, et favoriser le démarrage de leurs **activités entrepreneuriales**, en lien avec les plateformes de recherche et d’innovation.\r\n\r\n**Campus de Sceaux**\r\n\r\n**TechLab Fabrication additive**\r\n\r\nLe TechLab travaille avec le club Robotic, dirigé et animé par les élèves de Sceaux, dont les activités principales sont la réalisation de mini robots et la participation dans des challenges comme E=M6. En phase de démarrage, le but essentiel est d’intéresser un maximum d’élèves et les initier aux différentes machines du Tech’Lab. Les premières utilisations sont : le projet mécatronique et le projet innovation de 2A, le challenge 4I et les projets scientifiques (serre connectée, tunnel intelligent, bracelet aveugle...) des élèves de la formation par Apprentissage.\r\n**En savoir + :** Khaled SAHLI - [khaled.sahli@epf.fr][2]\r\n\r\n![Figure 1 : Exemple TechLab][3]\r\n\r\n**TechLab Chimie**\r\n\r\nLe TechLab Chimie est localisé provisoirement sur le campus de l’ESTP à Cachan (94). Il permet aux élèves de l’EPF d’effectuer leurs TP de Chimie, et d’avoir accès à des moyens en chimie environnementale : **Spectroscopie infra-rouge** (Perkin Elmer Frontier) et **UV-visible** (Dr Lange-Xion 500), **Boucle de traitement de l’eau** : simule les étapes de coagulation et floculation.\r\n\r\n**En savoir + :** Tony LOURTEAU - [tony.lourteau@epf.fr][4]\r\n\r\n![Figure 2 : Exemple TechLab Chimie][5]\r\n\r\n**Campus de Troyes**\r\n\r\n**TechLab Fabrication Additive**\r\n\r\nLe TechLab **Fabrication Additive** de Troyes travaille sur des projets novateurs comme les matériaux intelligents, les traitements de surfaces de pièces métalliques, les orthèses personnalisées obtenues par impression 3D et d’autres projets de recherche. Il comporte :\r\n\r\n - 8 imprimantes (dont une imprimante couleur) ;\r\n - 1 imprimante 3D métallique (projet) ;\r\n - 2 scanners 3D et des moyens logiciel associés.\r\n\r\n**En savoir + :** Julien GARDAN - [julien.gardan@epf.fr][6]\r\n\r\n![Figure 3 : Exemple TechLab Fabrication Additive][7]\r\n\r\n**TechLab Transition Énergétique et Environnementale**\r\n\r\nLe TechLab de Montpellier élabore des projets innovants en lien avec les énergies, l’environnement et les chaines de mesures à travers des pôles thématiques autour du prototypage mécatronique : réalisation et programmation de cartes électroniques, machines de fabrication à commande numérique, kits pédagogiques.\r\n\r\nIl constitue un soutien à la formation pédagogique (bancs de TP, projets étudiants), aux ambitions entrepreneuriales étudiantes (objets connectés) et aux activités de recherche.\r\n**En savoir + :** Antoine Gademer - [antoine.gademer@epf.fr][8]\r\n\r\n![Figure 4 : Exemple TechLab Transition Énergétique et Environnementale][9]\r\n\r\n\r\n  [1]: https://www.abg.asso.fr/fr/\r\n  [2]: http://khaled.sahli@epf.fr\r\n  [3]: https://www.epf.fr/sites/default/files/media/rte/techlab_fabadd_sceaux.png\r\n  [4]: http://tony.lourteau@epf.fr\r\n  [5]: https://www.epf.fr/sites/default/files/media/rte/techlab_chimie_sceaux.png\r\n  [6]: http://julien.gardan@epf.fr\r\n  [7]: https://www.epf.fr/sites/default/files/media/rte/techlab_fabadd_troyes.jpg\r\n  [8]: http://antoine.gademer@epf.fr\r\n  [9]: https://www.epf.fr/sites/default/files/media/rte/techlab_tee_troyes.jpg', 'la-recherche-au-cur-de-la-formation-epf', 'photos/imgarti.PNG'),
(18, '2020-06-08 10:05:58.670974', 'Chiffrement des données: Ercom', 'fabien.solde@epfedu.fr', '####Chiffrement des données: Ercom, la pépite française qui cartonne à l\'Elysée et dans les entreprises du CAC 40\r\n\r\n######Le spécialiste du chiffrement, acquis par Thales en 2019, connaît depuis plusieurs années une croissance à deux chiffres portée par la totale confiance dont il bénéficie au sein de l\'État et par un partenariat clé avec Samsung.\r\n![Le logiciel de sécurité Cryptosmart lancé par Ercom est notamment utilisé à l\'Élysée.][1]\r\n\r\nCe n\'est pas le stand le plus tonitruant mais sa fréquentation, discrète et régulière, indique bien que la société a le vent en poupe. Même le ministre de l\'Intérieur, Christophe Castaner, est venu passer une tête durant les deux heures qu\'aura duré sa visite au Forum international de la cybersécurité (FIC), [grand-messe qui réunit tous les ans à Lille le gratin mondial de la cyber.][2] Et pour cause, le patron de Beauvau fait partie des quelque 45.000 personnes qui utilisent Cryptosmart, l\'application phare développée par la pépite française Ercom (rachetée par [Thales][3] en 2019). Lancée en partenariat avec Samsung, celle-ci permet de chiffrer de bout en bout les SMS, les appels et le contenu des smartphones. \"Nous proposons un niveau de sécurité militaire sur des terminaux grand public, précise-t-on chez Ercom. Nos grands clients sont au nombre d\'une quinzaine.\"\r\n\r\n###Application utilisée par Macron\r\nParmi eux: des groupes du CAC 40, [les ministères des Armées][4] et des Affaires étrangères ou encore l\'Élysée. Adepte de l\'application, Emmanuel Macron est ainsi particulièrement mis en avant par les commerciaux d’Ercom. Le chef de l\'État possède un Samsung Galaxy S7 à écran tactile, muni d\'une puce protégeant son contenu et d’une clé inviolable. Une véritable forteresse 2.0 qui s\'appuie aussi sur la [technologie développée par Orange Cyberdefense][5] -l\'ensemble des données sont notamment hébergées dans les datacenters Orange en France- et prévoit la destruction immédiate des données en cas de perte ou de vol de l\'objet.\r\n\r\n###Symbole de la confiance que voue l\'État aux produits d\'Ercom: \r\nCryptosmart est la seule application sécurisée certifiée au niveau \"Diffusion Restreinte\" (DR) par le gendarme français de la cybersécurité (ANSSI). \"C\'est vrai que nous avons bâti une relation de confiance très forte avec l\'État, mais aussi avec l’OTAN ou l’UE. Toutefois, nos produits s\'adressent également spécifiquement au Comex d\'un grand groupe qui discute d\'une fusion par exemple ou au commercial qui se trouve en Russie, en Chine ou en Israël et qui veut communiquer avec son entreprise.\" Dans ce cas, Ercom offre deux possibilités à ses clients: un chiffrement de A à Z de la communication ou alors un chiffrement plus light, du pays d\'où est passé l\'appel jusqu\'à la société concernée. \r\n\r\n###Samsung séduit par la PME tricolore\r\nFondée en 1986, Ercom s\'est spécialisée depuis 2007 dans l’édition de solutions de sécurisation des communications par chiffrement de bout en bout. La PME, qui comprend 200 salariés et réalisait en 2018 un chiffre d\'affaires (CA) de 50 millions d\'euros, a [été acquise par Thales en janvier 2019][6] -cette dernière ne communique pas sur le CA de ses filiales. \"Le rachat par Thales ouvre de nouvelles perspectives avec notamment des capacités de développement conséquentes\", plaide-t-on côté Ercom. Ces dernières années, la société a connu une croissance annuelle de l\'ordre de 20%.\r\n\r\nClé de voûte de l\'application Cryptosmart, le partenariat avec le géant coréen, leader mondial des smartphones, pourrait aussi se renforcer à l\'avenir. \"Le degré de collaboration que nous avons avec Samsung est à la fois excellent et rare dans ce secteur, poursuit-on chez Ercom. Afin que nous puissions sécuriser le téléphone, les fabricants doivent faire preuve de transparence. C\'est totalement le cas avec Samsung alors que Apple, par exemple, est moins disposé à le faire.\" Ce rapprochement entre les deux sociétés remonte à 2015 quand le responsable de la R&D mondiale des smartphones Samsung, découvre que le locataire de l\'Élysée utilise un téléphone fabriqué par son groupe, hautement sécurisé par une technologie développée par la PME française. Quelques semaines plus tard, le partenariat sera conclu et donnera lieu à trois ans de recherche intensive pour mettre sur le marché la successful application Cryptosmart.\r\n\r\n\r\n  [1]: /media/pagedown-uploads/ercrom.jpg\r\n  [2]: https://www.challenges.fr/societe/le-piege-des-objets-connectes_695984\r\n  [3]: https://www.challenges.fr/tag_marque/thales_3042/\r\n  [4]: https://www.challenges.fr/high-tech/internet/ercom-assurera-la-cybersecurite-du-ministere-de-la-defense_42468\r\n  [5]: https://www.orange-business.com/fr/presse/avec-l-offre-mobile-security-intense-orange-cyberdefense-democratise-la-securisation-des\r\n  [6]: https://capitalfinance.lesechos.fr/deals/sortie/thales-a-bien-rachete-le-specialiste-des-interceptions-et-de-la-securite-informatique-ercom-994845', 'chiffrement-des-donnees-ercom', 'photos/ercom.png'),
(19, '2020-06-08 10:08:18.002793', 'Présentation de la Junior Entreprise EPF Projets', 'paul.deboissel@epfedu.fr', '#####EPF Projets Sceaux fait partie depuis mars 2015 des \"30 meilleures Junior-Entreprises\" de France ! Félicitations !\r\n\r\n**QUI SOMMES-NOUS ?**\r\nEPF Projets est une **Junior-Entreprise**, à savoir une association loi 1901 à vocation économique mais à but non-lucratif qui est implantée au sein d\'une École ou Université. Elle permet à ses membres et consultants, tous étudiants, d\'appliquer pour le compte de professionnels les compétences et savoir-faire acquis lors de leur formation.\r\n\r\n**EPF Projets Sceaux est la Junior-Entreprise de l\'EPF**. Implantées dans les établissements d\'enseignements supérieurs, les Junior-Entreprises (JE) sont des associations fonctionnant sur le modèle de cabinets de conseils. Constitué de 40 membres actifs du cycle ingénieur et de consultants rémunérés, EPF Projets offre une **expérience enrichissante**, au contact de l\'entreprise. De par son professionnalisme et sa qualité de service, EPF Projets Sceaux est pour la cinquième année consécutive dans la liste des **30 meilleures Junior-Entreprises de France parmi plus de 200 Juniors**.\r\n\r\nNous ne sommes pas seuls à exercer cette activité ! Il y a 200 Juniors en France (issues d’écoles d’ingénieurs, de commerce ou d’universités) qui sont associées au sein de la Confédération Nationale des Junior-Entreprises. Cette structure délivre les certifications, mène les audits annuels de tous ses membres et est notre porte-parole auprès des professionnels et des instances administratives.\r\n\r\n**QUE FAISONS-NOUS ?**\r\nLe rôle d’EPF Projets est semblable à celui d’une **entreprise de conseil** : nous nous chargeons de trouver des professionnels qui ont du travail à sous-traiter et nous embauchons des peufiens en tant que consultants pour le réaliser et être payés.\r\n\r\nNous proposons des solutions innovantes, concurrentielles mais surtout de qualité dans nos différents domaines de compétence :\r\n\r\n - **Informatique** (sites Internet, applications mobile, sécurisation, logiciels...)\r\n - **Traduction** (documents techniques, sites Internet, contrats...)\r\n - **Conseil** (étude de marché, business plan, audit...)\r\n - **Génie Industriel** (bilan thermique, bilan carbone...)\r\n\r\nNos engagements permanents sur les études qui nous sont fournies sont la réactivité, la qualité et le professionnalisme. Au fait des nouveautés et des tendances émergentes, nous mettons un point d’honneur à garder une culture de l’innovation dans notre travail et à adopter une organisation interne au plus près des dernières avancées : approche par processus, transition énergétique, management de la qualité…\r\n\r\nEPF Projets est gérée comme une entreprise et de fait notre gouvernance s’articule autour d’un Conseil d’Administration élu tous les ans et de différents pôles spécialisés : commercial et prospection, qualité, communication, RH, SI et trésorerie.\r\n\r\nEn 2013, nous avons réalisé 18 études pour plus de **50 000€ de chiffre d’affaires** auprès de grands groupes comme de startups et certaines entreprises de référence nous font régulièrement confiance, comme par exemple Dassault Systèmes, GDF SUEZ, Vinci, ou encore AXA et Manhattan Associates.\r\n\r\nEn 2016, EPF Projets Sceaux était parmi les 3 finalistes du [prix de l\'engagement][1].\r\n\r\n**ENVIE D’EN SAVOIR PLUS ?**\r\nPour plus d’informations ou pour rester au courant de nos activités, n’hésitez pas à utiliser tous les medias que nous mettons à votre disposition :\r\n\r\nNotre site internet : [www.epfprojets-sceaux.com/][2]\r\n\r\n\r\n  [1]: https://www.epf.fr/actualite/epf-projets-sceaux-une-junior-entreprise-engagee\r\n  [2]: http://www.epfprojets-sceaux.com/', 'presentation-de-la-junior-entreprise-epf-projets', 'photos/Capture.JPG');

-- --------------------------------------------------------

--
-- Structure de la table `timeline_article_tags`
--

CREATE TABLE `timeline_article_tags` (
  `id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL,
  `tags_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `timeline_article_tags`
--

INSERT INTO `timeline_article_tags` (`id`, `article_id`, `tags_id`) VALUES
(3, 3, 2),
(4, 4, 3),
(5, 4, 4),
(6, 4, 5),
(7, 4, 6),
(18, 12, 3),
(19, 12, 6),
(21, 14, 4),
(22, 15, 5),
(23, 15, 7),
(24, 16, 5),
(25, 17, 4),
(26, 17, 9),
(27, 18, 9),
(28, 18, 10),
(29, 19, 7);

-- --------------------------------------------------------

--
-- Structure de la table `timeline_commentaires`
--

CREATE TABLE `timeline_commentaires` (
  `id_comm` int(11) NOT NULL,
  `contenu_comm` varchar(500) NOT NULL,
  `id_post_id` int(11) DEFAULT NULL,
  `id_user_id` varchar(254) NOT NULL,
  `date_comm` datetime(6) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `timeline_commentaires`
--

INSERT INTO `timeline_commentaires` (`id_comm`, `contenu_comm`, `id_post_id`, `id_user_id`, `date_comm`, `parent_id`) VALUES
(1, 'Notre moteur de markdown semble ne pas prendre en compte toutes les balises :(', 3, 'corentin.magyar@epfedu.fr', '2020-06-07 20:15:26.188704', NULL),
(3, 'c\'est un peu triste mais en même temps c\'est cool que ça marche !!', 3, 'corentin.magyar@epfedu.fr', '2020-06-07 20:25:08.781292', 1),
(5, 'Quel dommage, j\'aurais aimé y passer une année !', 14, 'paul.deboissel@epfedu.fr', '2020-06-08 09:22:32.387230', NULL),
(6, 'N\'oubliez pas que les plus démunis sont les premiers touchés ! Si vous voullez donner de votre temps : https://www.restosducoeur.org/benevolat-spontane/', 15, 'fabien.solde@epfedu.fr', '2020-06-08 09:37:44.392466', NULL),
(7, 'Merci pour cet article, j\'ai appris beaucoup de choses !', 18, 'paul.deboissel@epfedu.fr', '2020-06-08 10:11:19.433177', NULL);

-- --------------------------------------------------------

--
-- Structure de la table `timeline_likes`
--

CREATE TABLE `timeline_likes` (
  `id_like` int(11) NOT NULL,
  `id_post_id` int(11) NOT NULL,
  `date_like` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `timeline_pieces_jointes_comm`
--

CREATE TABLE `timeline_pieces_jointes_comm` (
  `id_pj` int(11) NOT NULL,
  `id_comm_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `timeline_pieces_jointes_post`
--

CREATE TABLE `timeline_pieces_jointes_post` (
  `id_pj` int(11) NOT NULL,
  `lien_pj` varchar(200) NOT NULL,
  `id_post_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `timeline_tags`
--

CREATE TABLE `timeline_tags` (
  `id_tag` int(11) NOT NULL,
  `text_tag` varchar(100) NOT NULL,
  `type_tag` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `timeline_tags`
--

INSERT INTO `timeline_tags` (`id_tag`, `text_tag`, `type_tag`) VALUES
(1, 'Tous les tags', 'invisible'),
(2, 'test', 'test'),
(3, 'Important', 'Ecole'),
(4, 'Actualité EPF', 'Ecole'),
(5, 'Coronavirus', 'Santé'),
(6, 'Administration', 'Ecole'),
(7, 'EPF Projets', 'Associations'),
(9, 'Tech Trend', 'Recherche & Industrie'),
(10, 'MIN', 'Recherche & Industrie');

-- --------------------------------------------------------

--
-- Structure de la table `timeline_tags_article`
--

CREATE TABLE `timeline_tags_article` (
  `id_tag_article` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Index pour les tables exportées
--

--
-- Index pour la table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD PRIMARY KEY (`key`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Index pour la table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Index pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Index pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Index pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_login_customuser_email` (`user_id`);

--
-- Index pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Index pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Index pour la table `login_administration`
--
ALTER TABLE `login_administration`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Index pour la table `login_campus`
--
ALTER TABLE `login_campus`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nom` (`nom`);

--
-- Index pour la table `login_customuser`
--
ALTER TABLE `login_customuser`
  ADD PRIMARY KEY (`email`),
  ADD KEY `login_customuser_campus_id_32552061_fk_login_campus_id` (`campus_id`);

--
-- Index pour la table `login_customuser_groups`
--
ALTER TABLE `login_customuser_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `login_customuser_groups_customuser_id_group_id_280bd5c2_uniq` (`customuser_id`,`group_id`),
  ADD KEY `login_customuser_groups_group_id_639d055d_fk_auth_group_id` (`group_id`);

--
-- Index pour la table `login_customuser_user_permissions`
--
ALTER TABLE `login_customuser_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `login_customuser_user_pe_customuser_id_permission_afb8143d_uniq` (`customuser_id`,`permission_id`),
  ADD KEY `login_customuser_use_permission_id_2b8ae21e_fk_auth_perm` (`permission_id`);

--
-- Index pour la table `login_etudiant`
--
ALTER TABLE `login_etudiant`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD KEY `login_etudiant_majeure_id_74904257_fk_login_majeure_id` (`majeure_id`);

--
-- Index pour la table `login_majeure`
--
ALTER TABLE `login_majeure`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nom` (`nom`);

--
-- Index pour la table `messenger_chat`
--
ALTER TABLE `messenger_chat`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `messenger_chat_admin`
--
ALTER TABLE `messenger_chat_admin`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `messenger_chat_admin_chat_id_customuser_id_eacfa7e2_uniq` (`chat_id`,`customuser_id`),
  ADD KEY `messenger_chat_admin_customuser_id_6e957aca_fk_login_cus` (`customuser_id`);

--
-- Index pour la table `messenger_chat_messages`
--
ALTER TABLE `messenger_chat_messages`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `messenger_chat_messages_chat_id_message_id_bca784e9_uniq` (`chat_id`,`message_id`),
  ADD KEY `messenger_chat_messa_message_id_9e7b02bd_fk_messenger` (`message_id`);

--
-- Index pour la table `messenger_chat_participants`
--
ALTER TABLE `messenger_chat_participants`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `messenger_chat_participants_chat_id_customuser_id_ad071b07_uniq` (`chat_id`,`customuser_id`),
  ADD KEY `messenger_chat_parti_customuser_id_cf11d27b_fk_login_cus` (`customuser_id`);

--
-- Index pour la table `messenger_chat_tag`
--
ALTER TABLE `messenger_chat_tag`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `messenger_chat_tag_chat_id_taggedmessages_id_ac72fa7d_uniq` (`chat_id`,`taggedmessages_id`),
  ADD KEY `messenger_chat_tag_taggedmessages_id_dcc92f3a_fk_messenger` (`taggedmessages_id`);

--
-- Index pour la table `messenger_message`
--
ALTER TABLE `messenger_message`
  ADD PRIMARY KEY (`id`),
  ADD KEY `messenger_message_contact_id_e044bdeb_fk_login_customuser_email` (`contact_id`);

--
-- Index pour la table `messenger_taggedmessages`
--
ALTER TABLE `messenger_taggedmessages`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `content_id` (`content_id`),
  ADD KEY `messenger_taggedmess_author_id_3dc8a359_fk_login_cus` (`author_id`);

--
-- Index pour la table `timeline_article`
--
ALTER TABLE `timeline_article`
  ADD PRIMARY KEY (`id`),
  ADD KEY `timeline_article_auteur_id_b6a3caa8_fk_login_customuser_email` (`auteur_id`),
  ADD KEY `timeline_article_slug_b2c4f697` (`slug`);

--
-- Index pour la table `timeline_article_tags`
--
ALTER TABLE `timeline_article_tags`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `timeline_article_tags_article_id_tags_id_7c5320c7_uniq` (`article_id`,`tags_id`),
  ADD KEY `timeline_article_tags_tags_id_ca29f58a_fk_timeline_tags_id_tag` (`tags_id`);

--
-- Index pour la table `timeline_commentaires`
--
ALTER TABLE `timeline_commentaires`
  ADD PRIMARY KEY (`id_comm`),
  ADD KEY `timeline_commentaires_id_post_id_367fd43f_fk_timeline_article_id` (`id_post_id`),
  ADD KEY `timeline_commentaire_id_user_id_c9ee7c4a_fk_login_cus` (`id_user_id`),
  ADD KEY `timeline_commentaire_parent_id_912f1086_fk_timeline_` (`parent_id`);

--
-- Index pour la table `timeline_likes`
--
ALTER TABLE `timeline_likes`
  ADD PRIMARY KEY (`id_like`),
  ADD KEY `timeline_likes_id_post_id_ee21b547_fk_timeline_article_id` (`id_post_id`);

--
-- Index pour la table `timeline_pieces_jointes_comm`
--
ALTER TABLE `timeline_pieces_jointes_comm`
  ADD PRIMARY KEY (`id_pj`),
  ADD KEY `timeline_pieces_join_id_comm_id_43d4fc88_fk_timeline_` (`id_comm_id`);

--
-- Index pour la table `timeline_pieces_jointes_post`
--
ALTER TABLE `timeline_pieces_jointes_post`
  ADD PRIMARY KEY (`id_pj`),
  ADD KEY `timeline_pieces_join_id_post_id_d0f8f744_fk_timeline_` (`id_post_id`);

--
-- Index pour la table `timeline_tags`
--
ALTER TABLE `timeline_tags`
  ADD PRIMARY KEY (`id_tag`);

--
-- Index pour la table `timeline_tags_article`
--
ALTER TABLE `timeline_tags_article`
  ADD PRIMARY KEY (`id_tag_article`),
  ADD KEY `timeline_tags_article_tag_id_1bb2e1ae_fk_timeline_tags_id_tag` (`tag_id`),
  ADD KEY `timeline_tags_article_article_id_ad615eb4_fk_timeline_article_id` (`article_id`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=85;
--
-- AUTO_INCREMENT pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
--
-- AUTO_INCREMENT pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
--
-- AUTO_INCREMENT pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
--
-- AUTO_INCREMENT pour la table `login_administration`
--
ALTER TABLE `login_administration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `login_campus`
--
ALTER TABLE `login_campus`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT pour la table `login_customuser_groups`
--
ALTER TABLE `login_customuser_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `login_customuser_user_permissions`
--
ALTER TABLE `login_customuser_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT pour la table `login_etudiant`
--
ALTER TABLE `login_etudiant`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT pour la table `login_majeure`
--
ALTER TABLE `login_majeure`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- AUTO_INCREMENT pour la table `messenger_chat`
--
ALTER TABLE `messenger_chat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT pour la table `messenger_chat_admin`
--
ALTER TABLE `messenger_chat_admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT pour la table `messenger_chat_messages`
--
ALTER TABLE `messenger_chat_messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT pour la table `messenger_chat_participants`
--
ALTER TABLE `messenger_chat_participants`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=86;
--
-- AUTO_INCREMENT pour la table `messenger_chat_tag`
--
ALTER TABLE `messenger_chat_tag`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT pour la table `messenger_message`
--
ALTER TABLE `messenger_message`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT pour la table `messenger_taggedmessages`
--
ALTER TABLE `messenger_taggedmessages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT pour la table `timeline_article`
--
ALTER TABLE `timeline_article`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
--
-- AUTO_INCREMENT pour la table `timeline_article_tags`
--
ALTER TABLE `timeline_article_tags`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;
--
-- AUTO_INCREMENT pour la table `timeline_commentaires`
--
ALTER TABLE `timeline_commentaires`
  MODIFY `id_comm` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT pour la table `timeline_likes`
--
ALTER TABLE `timeline_likes`
  MODIFY `id_like` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `timeline_pieces_jointes_comm`
--
ALTER TABLE `timeline_pieces_jointes_comm`
  MODIFY `id_pj` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `timeline_pieces_jointes_post`
--
ALTER TABLE `timeline_pieces_jointes_post`
  MODIFY `id_pj` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `timeline_tags`
--
ALTER TABLE `timeline_tags`
  MODIFY `id_tag` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT pour la table `timeline_tags_article`
--
ALTER TABLE `timeline_tags_article`
  MODIFY `id_tag_article` int(11) NOT NULL AUTO_INCREMENT;
--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD CONSTRAINT `authtoken_token_user_id_35299eff_fk_login_customuser_email` FOREIGN KEY (`user_id`) REFERENCES `login_customuser` (`email`);

--
-- Contraintes pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Contraintes pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Contraintes pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_login_customuser_email` FOREIGN KEY (`user_id`) REFERENCES `login_customuser` (`email`);

--
-- Contraintes pour la table `login_administration`
--
ALTER TABLE `login_administration`
  ADD CONSTRAINT `login_administration_user_id_c42f5db1_fk_login_customuser_email` FOREIGN KEY (`user_id`) REFERENCES `login_customuser` (`email`);

--
-- Contraintes pour la table `login_customuser`
--
ALTER TABLE `login_customuser`
  ADD CONSTRAINT `login_customuser_campus_id_32552061_fk_login_campus_id` FOREIGN KEY (`campus_id`) REFERENCES `login_campus` (`id`);

--
-- Contraintes pour la table `login_customuser_groups`
--
ALTER TABLE `login_customuser_groups`
  ADD CONSTRAINT `login_customuser_gro_customuser_id_50381d88_fk_login_cus` FOREIGN KEY (`customuser_id`) REFERENCES `login_customuser` (`email`),
  ADD CONSTRAINT `login_customuser_groups_group_id_639d055d_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Contraintes pour la table `login_customuser_user_permissions`
--
ALTER TABLE `login_customuser_user_permissions`
  ADD CONSTRAINT `login_customuser_use_customuser_id_c6f5792f_fk_login_cus` FOREIGN KEY (`customuser_id`) REFERENCES `login_customuser` (`email`),
  ADD CONSTRAINT `login_customuser_use_permission_id_2b8ae21e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Contraintes pour la table `login_etudiant`
--
ALTER TABLE `login_etudiant`
  ADD CONSTRAINT `login_etudiant_majeure_id_74904257_fk_login_majeure_id` FOREIGN KEY (`majeure_id`) REFERENCES `login_majeure` (`id`),
  ADD CONSTRAINT `login_etudiant_user_id_f6cf0a43_fk_login_customuser_email` FOREIGN KEY (`user_id`) REFERENCES `login_customuser` (`email`);

--
-- Contraintes pour la table `messenger_chat_admin`
--
ALTER TABLE `messenger_chat_admin`
  ADD CONSTRAINT `messenger_chat_admin_chat_id_dc5a0032_fk_messenger_chat_id` FOREIGN KEY (`chat_id`) REFERENCES `messenger_chat` (`id`),
  ADD CONSTRAINT `messenger_chat_admin_customuser_id_6e957aca_fk_login_cus` FOREIGN KEY (`customuser_id`) REFERENCES `login_customuser` (`email`);

--
-- Contraintes pour la table `messenger_chat_messages`
--
ALTER TABLE `messenger_chat_messages`
  ADD CONSTRAINT `messenger_chat_messa_message_id_9e7b02bd_fk_messenger` FOREIGN KEY (`message_id`) REFERENCES `messenger_message` (`id`),
  ADD CONSTRAINT `messenger_chat_messages_chat_id_c7ddff3d_fk_messenger_chat_id` FOREIGN KEY (`chat_id`) REFERENCES `messenger_chat` (`id`);

--
-- Contraintes pour la table `messenger_chat_participants`
--
ALTER TABLE `messenger_chat_participants`
  ADD CONSTRAINT `messenger_chat_parti_chat_id_a0ceeca9_fk_messenger` FOREIGN KEY (`chat_id`) REFERENCES `messenger_chat` (`id`),
  ADD CONSTRAINT `messenger_chat_parti_customuser_id_cf11d27b_fk_login_cus` FOREIGN KEY (`customuser_id`) REFERENCES `login_customuser` (`email`);

--
-- Contraintes pour la table `messenger_chat_tag`
--
ALTER TABLE `messenger_chat_tag`
  ADD CONSTRAINT `messenger_chat_tag_chat_id_1fc46777_fk_messenger_chat_id` FOREIGN KEY (`chat_id`) REFERENCES `messenger_chat` (`id`),
  ADD CONSTRAINT `messenger_chat_tag_taggedmessages_id_dcc92f3a_fk_messenger` FOREIGN KEY (`taggedmessages_id`) REFERENCES `messenger_taggedmessages` (`id`);

--
-- Contraintes pour la table `messenger_message`
--
ALTER TABLE `messenger_message`
  ADD CONSTRAINT `messenger_message_contact_id_e044bdeb_fk_login_customuser_email` FOREIGN KEY (`contact_id`) REFERENCES `login_customuser` (`email`);

--
-- Contraintes pour la table `messenger_taggedmessages`
--
ALTER TABLE `messenger_taggedmessages`
  ADD CONSTRAINT `messenger_taggedmess_author_id_3dc8a359_fk_login_cus` FOREIGN KEY (`author_id`) REFERENCES `login_customuser` (`email`),
  ADD CONSTRAINT `messenger_taggedmess_content_id_9ee7d07f_fk_messenger` FOREIGN KEY (`content_id`) REFERENCES `messenger_message` (`id`);

--
-- Contraintes pour la table `timeline_article`
--
ALTER TABLE `timeline_article`
  ADD CONSTRAINT `timeline_article_auteur_id_b6a3caa8_fk_login_customuser_email` FOREIGN KEY (`auteur_id`) REFERENCES `login_customuser` (`email`);

--
-- Contraintes pour la table `timeline_article_tags`
--
ALTER TABLE `timeline_article_tags`
  ADD CONSTRAINT `timeline_article_tags_article_id_8722f73c_fk_timeline_article_id` FOREIGN KEY (`article_id`) REFERENCES `timeline_article` (`id`),
  ADD CONSTRAINT `timeline_article_tags_tags_id_ca29f58a_fk_timeline_tags_id_tag` FOREIGN KEY (`tags_id`) REFERENCES `timeline_tags` (`id_tag`);

--
-- Contraintes pour la table `timeline_commentaires`
--
ALTER TABLE `timeline_commentaires`
  ADD CONSTRAINT `timeline_commentaire_id_user_id_c9ee7c4a_fk_login_cus` FOREIGN KEY (`id_user_id`) REFERENCES `login_customuser` (`email`),
  ADD CONSTRAINT `timeline_commentaire_parent_id_912f1086_fk_timeline_` FOREIGN KEY (`parent_id`) REFERENCES `timeline_commentaires` (`id_comm`),
  ADD CONSTRAINT `timeline_commentaires_id_post_id_367fd43f_fk_timeline_article_id` FOREIGN KEY (`id_post_id`) REFERENCES `timeline_article` (`id`);

--
-- Contraintes pour la table `timeline_likes`
--
ALTER TABLE `timeline_likes`
  ADD CONSTRAINT `timeline_likes_id_post_id_ee21b547_fk_timeline_article_id` FOREIGN KEY (`id_post_id`) REFERENCES `timeline_article` (`id`);

--
-- Contraintes pour la table `timeline_pieces_jointes_comm`
--
ALTER TABLE `timeline_pieces_jointes_comm`
  ADD CONSTRAINT `timeline_pieces_join_id_comm_id_43d4fc88_fk_timeline_` FOREIGN KEY (`id_comm_id`) REFERENCES `timeline_commentaires` (`id_comm`);

--
-- Contraintes pour la table `timeline_pieces_jointes_post`
--
ALTER TABLE `timeline_pieces_jointes_post`
  ADD CONSTRAINT `timeline_pieces_join_id_post_id_d0f8f744_fk_timeline_` FOREIGN KEY (`id_post_id`) REFERENCES `timeline_article` (`id`);

--
-- Contraintes pour la table `timeline_tags_article`
--
ALTER TABLE `timeline_tags_article`
  ADD CONSTRAINT `timeline_tags_article_article_id_ad615eb4_fk_timeline_article_id` FOREIGN KEY (`article_id`) REFERENCES `timeline_article` (`id`),
  ADD CONSTRAINT `timeline_tags_article_tag_id_1bb2e1ae_fk_timeline_tags_id_tag` FOREIGN KEY (`tag_id`) REFERENCES `timeline_tags` (`id_tag`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
