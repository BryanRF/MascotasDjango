-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-10-2023 a las 01:04:51
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `mascotas_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_adopcion`
--

CREATE TABLE `api_adopcion` (
  `id` char(32) NOT NULL,
  `fecha_adopcion` date DEFAULT NULL,
  `comentarios` longtext NOT NULL,
  `estado_adopcion_id` char(32) NOT NULL,
  `mascota_id` char(32) NOT NULL,
  `usuario_adoptante_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `api_adopcion`
--

INSERT INTO `api_adopcion` (`id`, `fecha_adopcion`, `comentarios`, `estado_adopcion_id`, `mascota_id`, `usuario_adoptante_id`) VALUES
('f00cfaeea54347d1a91b5bba4c38e4f8', NULL, 'asdasdasd', '2314eb8fb6104a4e94ee31a22316428b', '366b286a6084469f9dccfa64d7790183', 'de466096e4154d4fa2048820a14f1177');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_comentario`
--

CREATE TABLE `api_comentario` (
  `id` char(32) NOT NULL,
  `contenido` longtext NOT NULL,
  `fecha_publicacion` datetime(6) NOT NULL,
  `autor_id` char(32) NOT NULL,
  `mascota_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_direccion`
--

CREATE TABLE `api_direccion` (
  `id` char(32) NOT NULL,
  `direccion` longtext NOT NULL,
  `persona_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_donacion`
--

CREATE TABLE `api_donacion` (
  `id` char(32) NOT NULL,
  `descripcion` longtext NOT NULL,
  `fecha_donacion` date NOT NULL,
  `persona_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_especie`
--

CREATE TABLE `api_especie` (
  `id` char(32) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `imagen` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `api_especie`
--

INSERT INTO `api_especie` (`id`, `nombre`, `imagen`) VALUES
('6dd1de56c4364e3da56ee1c64255aaba', 'Perros', 'imagenes_mascotas/6_CkTqyqC.png'),
('8f7485742bbe47d1a8ef00a41a38b8d5', 'Gatos', 'imagenes_mascotas/5_QpXTqK4.png'),
('d3dca5ed75da41e9bdbfa130aae8472c', 'Loros', 'imagenes_mascotas/7_ZNjJS3v.png'),
('e2414acc89884aeeac5c2155b19a6b8b', 'Conejos', 'imagenes_mascotas/4_6t08f3b.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_estadoadopcion`
--

CREATE TABLE `api_estadoadopcion` (
  `id` char(32) NOT NULL,
  `estado` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `api_estadoadopcion`
--

INSERT INTO `api_estadoadopcion` (`id`, `estado`) VALUES
('2314eb8fb6104a4e94ee31a22316428b', 'Pendiente'),
('339becb477d24cf3afcd12d1daf9d5e5', 'Rechazado'),
('87481b7e8fcd4b23bd90e6ba85542122', 'Anulado'),
('ddb52544584c4087a3bcf5eb554c1425', 'Aprobado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_etiqueta`
--

CREATE TABLE `api_etiqueta` (
  `id` char(32) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `api_etiqueta`
--

INSERT INTO `api_etiqueta` (`id`, `nombre`) VALUES
('8d05af3618b04a52bb7f4eb838ea72e2', 'Amigable'),
('8f99dbec861f4c7483562d53a11ee6ba', 'Jugueton'),
('9e426470e87d4aadbebd9045138bf05a', 'Inteligente'),
('dc32bdc74ee44ad5a4e8a020ef83f3fa', 'Dormilon'),
('ef85d6d413ee48cd9170ab6bdb422a9b', 'Parlanchin');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_evaluacionadopcion`
--

CREATE TABLE `api_evaluacionadopcion` (
  `id` char(32) NOT NULL,
  `calificacion` int(10) UNSIGNED NOT NULL CHECK (`calificacion` >= 0),
  `comentarios` longtext NOT NULL,
  `fecha_evaluacion` date NOT NULL,
  `adopcion_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_evento`
--

CREATE TABLE `api_evento` (
  `id` char(32) NOT NULL,
  `nombre` varchar(300) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin_participacion` date NOT NULL,
  `costo_participacion` decimal(10,2) NOT NULL,
  `recaudacion` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `api_evento`
--

INSERT INTO `api_evento` (`id`, `nombre`, `fecha_inicio`, `fecha_fin_participacion`, `costo_participacion`, `recaudacion`) VALUES
('0b1f8eefc0cc47d3a32e9f446037cf7c', 'Rifa', '2023-11-30', '2023-11-29', 5.00, 0.00),
('3d435746e6734f9a966f1ded4d13685f', 'Bingo', '2023-10-29', '2023-10-28', 5.00, 0.00),
('70c1376e94834b50b54af58167cdd7b0', 'Pollada Bailable', '2023-11-18', '2023-11-18', 10.00, 0.00),
('ac7ac2036fa94af994b881d5e83c0182', 'Bingo', '2023-12-22', '2023-12-21', 5.00, 0.00);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_eventoparticipante`
--

CREATE TABLE `api_eventoparticipante` (
  `id` char(32) NOT NULL,
  `evento_id` char(32) NOT NULL,
  `participante_id` char(32) NOT NULL,
  `ticket` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_ganador`
--

CREATE TABLE `api_ganador` (
  `id` bigint(20) NOT NULL,
  `evento_id` char(32) NOT NULL,
  `participante_id` char(32) NOT NULL,
  `premio_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_imagen`
--

CREATE TABLE `api_imagen` (
  `id` char(32) NOT NULL,
  `imagen` varchar(100) NOT NULL,
  `mascota_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `api_imagen`
--

INSERT INTO `api_imagen` (`id`, `imagen`, `mascota_id`) VALUES
('06ebdcb4a0f549aea50e4bb7028ad7e8', 'imagenes_mascotas/pexels-julissa-helmuth-3874435_x8wWqTJ.jpg', 'e2bb1ae995f345f4a42bbac31b924b91'),
('08859f118afd42ce86c8f6cc4fdb70b4', 'imagenes_mascotas/pexels-francesco-ungaro-96442_P5w395K.jpg', '2679bf4aa8c54ef1a6f84cb03af7b0f9'),
('1fc6b0ba630d4d5eb4e1fffc4744ac75', 'imagenes_mascotas/pexels-goochie-poochie-grooming-3361739_RhWdfRk.jpg', '4cf006a3fea14ab983ee19144d7b5782'),
('7c5c813cb9d54f35a8f40b77a9b98ab4', 'imagenes_mascotas/pexels-halil-ibrahim-çetin-1754986_kMQ9abE.jpg', 'ce298a350a4d4de4ab32a2c1cc06676f'),
('b4faf03722a64134a3c2c3eec23f6336', 'imagenes_mascotas/pexels-frank-cone-2285996_r1QKDYU.jpg', 'f5e6f146526c49439bac36f913136e5b'),
('c8004102ceb14dc3b1e5ce4b6a2f8ee2', 'imagenes_mascotas/pexels-hans-martha-1059823_OFapypG.jpg', 'deeb47783afa467f8ec230ae5e7569b8'),
('e5f3efabc72449cbb26a4b9eb0f208a4', 'imagenes_mascotas/pexels-fox-755834_jsxQj1q.jpg', '366b286a6084469f9dccfa64d7790183'),
('fb5dad29c8b641dda92baac2c2ccb1ed', 'imagenes_mascotas/pexels-evg-kowalievska-1170986_porYlij.jpg', '9339dc2ed4274121a3d8577bf5f5d8ea');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_mascota`
--

CREATE TABLE `api_mascota` (
  `id` char(32) NOT NULL,
  `codigo` varchar(10) DEFAULT NULL,
  `nombre` varchar(100) NOT NULL,
  `edad` int(11) NOT NULL,
  `descripcion` longtext NOT NULL,
  `disponible` tinyint(1) NOT NULL,
  `color` varchar(50) NOT NULL,
  `tamano` varchar(20) NOT NULL,
  `genero` varchar(10) NOT NULL,
  `likes` int(11) NOT NULL,
  `especie_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `api_mascota`
--

INSERT INTO `api_mascota` (`id`, `codigo`, `nombre`, `edad`, `descripcion`, `disponible`, `color`, `tamano`, `genero`, `likes`, `especie_id`) VALUES
('2679bf4aa8c54ef1a6f84cb03af7b0f9', '40591119', 'Joaquin', 3, 'Es muy dormilon', 1, 'Blanco con manchas', '20 cm', 'macho', 42, 'e2414acc89884aeeac5c2155b19a6b8b'),
('366b286a6084469f9dccfa64d7790183', 'DKO3K2023', 'Simon', 2, 'Un gato muy cariñoso', 1, 'Gris y blanco', '20 cm', 'macho', 43, '8f7485742bbe47d1a8ef00a41a38b8d5'),
('4cf006a3fea14ab983ee19144d7b5782', '40276982', 'Coquito', 3, 'Muy juegueton', 1, 'Blanco', '30cm', 'macho', 35, '6dd1de56c4364e3da56ee1c64255aaba'),
('9339dc2ed4274121a3d8577bf5f5d8ea', '12614592', 'Abocato', 2, 'Un gato muy serio pero fiel compañero', 1, 'Amarillo y con rayas blancas', '20 cm', 'macho', 42, '8f7485742bbe47d1a8ef00a41a38b8d5'),
('ce298a350a4d4de4ab32a2c1cc06676f', '13648103', 'Kuno', 2, 'Siempre en cama', 1, 'Amarillo y con rayas blancas', '21 cm', 'macho', 12, '8f7485742bbe47d1a8ef00a41a38b8d5'),
('deeb47783afa467f8ec230ae5e7569b8', '11534326', 'Loracio', 2, 'Es muy hablador', 1, 'arcoiris', '10 cm', 'macho', 12, 'd3dca5ed75da41e9bdbfa130aae8472c'),
('e2bb1ae995f345f4a42bbac31b924b91', '15677270', 'Princesa', 3, 'Muerde pero no ladra', 1, 'Negro con blanco con rayas', '60 cm', 'hembra', 13, '6dd1de56c4364e3da56ee1c64255aaba'),
('f5e6f146526c49439bac36f913136e5b', '97187168', 'Pana Rabit', 2, 'Muy rapido y jugueton', 1, 'gris', '20 cm', 'hembra', 3, 'e2414acc89884aeeac5c2155b19a6b8b');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_mascota_etiquetas`
--

CREATE TABLE `api_mascota_etiquetas` (
  `id` bigint(20) NOT NULL,
  `mascota_id` char(32) NOT NULL,
  `etiqueta_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `api_mascota_etiquetas`
--

INSERT INTO `api_mascota_etiquetas` (`id`, `mascota_id`, `etiqueta_id`) VALUES
(17, '2679bf4aa8c54ef1a6f84cb03af7b0f9', '8f99dbec861f4c7483562d53a11ee6ba'),
(18, '2679bf4aa8c54ef1a6f84cb03af7b0f9', '9e426470e87d4aadbebd9045138bf05a'),
(2, '366b286a6084469f9dccfa64d7790183', '8d05af3618b04a52bb7f4eb838ea72e2'),
(1, '366b286a6084469f9dccfa64d7790183', '8f99dbec861f4c7483562d53a11ee6ba'),
(4, '366b286a6084469f9dccfa64d7790183', '9e426470e87d4aadbebd9045138bf05a'),
(3, '366b286a6084469f9dccfa64d7790183', 'dc32bdc74ee44ad5a4e8a020ef83f3fa'),
(5, '4cf006a3fea14ab983ee19144d7b5782', '8d05af3618b04a52bb7f4eb838ea72e2'),
(8, '9339dc2ed4274121a3d8577bf5f5d8ea', '8d05af3618b04a52bb7f4eb838ea72e2'),
(9, '9339dc2ed4274121a3d8577bf5f5d8ea', '9e426470e87d4aadbebd9045138bf05a'),
(10, 'ce298a350a4d4de4ab32a2c1cc06676f', '8f99dbec861f4c7483562d53a11ee6ba'),
(11, 'ce298a350a4d4de4ab32a2c1cc06676f', 'dc32bdc74ee44ad5a4e8a020ef83f3fa'),
(12, 'deeb47783afa467f8ec230ae5e7569b8', '8f99dbec861f4c7483562d53a11ee6ba'),
(14, 'deeb47783afa467f8ec230ae5e7569b8', '9e426470e87d4aadbebd9045138bf05a'),
(13, 'deeb47783afa467f8ec230ae5e7569b8', 'ef85d6d413ee48cd9170ab6bdb422a9b'),
(7, 'e2bb1ae995f345f4a42bbac31b924b91', '8d05af3618b04a52bb7f4eb838ea72e2'),
(6, 'e2bb1ae995f345f4a42bbac31b924b91', '8f99dbec861f4c7483562d53a11ee6ba'),
(16, 'f5e6f146526c49439bac36f913136e5b', '8d05af3618b04a52bb7f4eb838ea72e2'),
(15, 'f5e6f146526c49439bac36f913136e5b', '8f99dbec861f4c7483562d53a11ee6ba');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_persona`
--

CREATE TABLE `api_persona` (
  `id` char(32) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `dni` varchar(15) NOT NULL,
  `email` varchar(254) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `api_persona`
--

INSERT INTO `api_persona` (`id`, `nombre`, `telefono`, `dni`, `email`, `fecha_nacimiento`, `user_id`) VALUES
('47f8861c78884621b2d4fdb813f0843d', 'Eduardo', '98761234', '12312342', 'review@culqi.com', '2023-10-26', 8),
('de466096e4154d4fa2048820a14f1177', 'Brayan Rojas Freyre', '998511222', '74473887', 'rfreyrebrayaned@gmail.com', '1999-12-26', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_premio`
--

CREATE TABLE `api_premio` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` longtext NOT NULL,
  `evento_id` char(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_vacuna`
--

CREATE TABLE `api_vacuna` (
  `id` char(32) NOT NULL,
  `nombre_vacuna` varchar(100) NOT NULL,
  `fecha_administracion` date NOT NULL,
  `proxima_fecha_vacunacion` date NOT NULL,
  `notas_adicionales` longtext NOT NULL,
  `mascota_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `api_vacuna`
--

INSERT INTO `api_vacuna` (`id`, `nombre_vacuna`, `fecha_administracion`, `proxima_fecha_vacunacion`, `notas_adicionales`, `mascota_id`) VALUES
('5467edc5eda14e63ab8870ad4370e9ce', 'Rabia', '2023-10-21', '2023-11-21', 'Este control culmino', '366b286a6084469f9dccfa64d7790183');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_visitaadopcion`
--

CREATE TABLE `api_visitaadopcion` (
  `id` char(32) NOT NULL,
  `fecha_visita` date NOT NULL,
  `adoptante_id` char(32) NOT NULL,
  `mascota_id` char(32) NOT NULL,
  `asistio` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `api_visitageneral`
--

CREATE TABLE `api_visitageneral` (
  `id` char(32) NOT NULL,
  `fecha_visita` date NOT NULL,
  `asistio` tinyint(1) DEFAULT NULL,
  `persona_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add adopcion', 7, 'add_adopcion'),
(26, 'Can change adopcion', 7, 'change_adopcion'),
(27, 'Can delete adopcion', 7, 'delete_adopcion'),
(28, 'Can view adopcion', 7, 'view_adopcion'),
(29, 'Can add especie', 8, 'add_especie'),
(30, 'Can change especie', 8, 'change_especie'),
(31, 'Can delete especie', 8, 'delete_especie'),
(32, 'Can view especie', 8, 'view_especie'),
(33, 'Can add estado adopcion', 9, 'add_estadoadopcion'),
(34, 'Can change estado adopcion', 9, 'change_estadoadopcion'),
(35, 'Can delete estado adopcion', 9, 'delete_estadoadopcion'),
(36, 'Can view estado adopcion', 9, 'view_estadoadopcion'),
(37, 'Can add etiqueta', 10, 'add_etiqueta'),
(38, 'Can change etiqueta', 10, 'change_etiqueta'),
(39, 'Can delete etiqueta', 10, 'delete_etiqueta'),
(40, 'Can view etiqueta', 10, 'view_etiqueta'),
(41, 'Can add mascota', 11, 'add_mascota'),
(42, 'Can change mascota', 11, 'change_mascota'),
(43, 'Can delete mascota', 11, 'delete_mascota'),
(44, 'Can view mascota', 11, 'view_mascota'),
(45, 'Can add persona', 12, 'add_persona'),
(46, 'Can change persona', 12, 'change_persona'),
(47, 'Can delete persona', 12, 'delete_persona'),
(48, 'Can view persona', 12, 'view_persona'),
(49, 'Can add vacuna', 13, 'add_vacuna'),
(50, 'Can change vacuna', 13, 'change_vacuna'),
(51, 'Can delete vacuna', 13, 'delete_vacuna'),
(52, 'Can view vacuna', 13, 'view_vacuna'),
(53, 'Can add imagen', 14, 'add_imagen'),
(54, 'Can change imagen', 14, 'change_imagen'),
(55, 'Can delete imagen', 14, 'delete_imagen'),
(56, 'Can view imagen', 14, 'view_imagen'),
(57, 'Can add evaluacion adopcion', 15, 'add_evaluacionadopcion'),
(58, 'Can change evaluacion adopcion', 15, 'change_evaluacionadopcion'),
(59, 'Can delete evaluacion adopcion', 15, 'delete_evaluacionadopcion'),
(60, 'Can view evaluacion adopcion', 15, 'view_evaluacionadopcion'),
(61, 'Can add direccion', 16, 'add_direccion'),
(62, 'Can change direccion', 16, 'change_direccion'),
(63, 'Can delete direccion', 16, 'delete_direccion'),
(64, 'Can view direccion', 16, 'view_direccion'),
(65, 'Can add comentario', 17, 'add_comentario'),
(66, 'Can change comentario', 17, 'change_comentario'),
(67, 'Can delete comentario', 17, 'delete_comentario'),
(68, 'Can view comentario', 17, 'view_comentario'),
(69, 'Can add visita adopcion', 18, 'add_visitaadopcion'),
(70, 'Can change visita adopcion', 18, 'change_visitaadopcion'),
(71, 'Can delete visita adopcion', 18, 'delete_visitaadopcion'),
(72, 'Can view visita adopcion', 18, 'view_visitaadopcion'),
(73, 'Can add evento', 19, 'add_evento'),
(74, 'Can change evento', 19, 'change_evento'),
(75, 'Can delete evento', 19, 'delete_evento'),
(76, 'Can view evento', 19, 'view_evento'),
(77, 'Can add visita general', 20, 'add_visitageneral'),
(78, 'Can change visita general', 20, 'change_visitageneral'),
(79, 'Can delete visita general', 20, 'delete_visitageneral'),
(80, 'Can view visita general', 20, 'view_visitageneral'),
(81, 'Can add evento participante', 21, 'add_eventoparticipante'),
(82, 'Can change evento participante', 21, 'change_eventoparticipante'),
(83, 'Can delete evento participante', 21, 'delete_eventoparticipante'),
(84, 'Can view evento participante', 21, 'view_eventoparticipante'),
(85, 'Can add donacion', 22, 'add_donacion'),
(86, 'Can change donacion', 22, 'change_donacion'),
(87, 'Can delete donacion', 22, 'delete_donacion'),
(88, 'Can view donacion', 22, 'view_donacion'),
(89, 'Can add premio', 23, 'add_premio'),
(90, 'Can change premio', 23, 'change_premio'),
(91, 'Can delete premio', 23, 'delete_premio'),
(92, 'Can view premio', 23, 'view_premio'),
(93, 'Can add ganador', 24, 'add_ganador'),
(94, 'Can change ganador', 24, 'change_ganador'),
(95, 'Can delete ganador', 24, 'delete_ganador'),
(96, 'Can view ganador', 24, 'view_ganador');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$GUWTfVTxeJhx94l7nr9SXp$YGvQPR5nYmTSckWGW9nOE/xE4eIF31n/k+jroSqMVhA=', '2023-10-26 19:28:13.923572', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2023-10-21 21:18:19.301536'),
(3, 'pbkdf2_sha256$600000$GUWTfVTxeJhx94l7nr9SXp$YGvQPR5nYmTSckWGW9nOE/xE4eIF31n/k+jroSqMVhA=', '2023-10-27 20:57:00.468349', 0, 'brayan123', '', '', 'rfreyrebrayaned@gmail.com', 0, 1, '2023-10-22 02:12:05.592334'),
(5, 'pbkdf2_sha256$600000$0Pp0N6gQnm40E7ZdHDAAdG$0oer4LL2n+f7t3aY75ptE2gq2PXh7crtl3s0h9Ll7HU=', NULL, 0, 'brayan1', '', '', '22', 0, 1, '2023-10-27 20:58:46.064094'),
(8, 'pbkdf2_sha256$600000$kE4QmiX6DTLgqSw7njGJGx$pv5aXNS4rha4mr3BJA7q9lWVnFL6Tl6D2mSLmZllRwQ=', '2023-10-27 23:03:26.861426', 0, 'brayan133', '', '', 'review@culqi.com', 0, 1, '2023-10-27 23:03:14.344851');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-10-21 21:48:30.376462', '8f748574-2bbe-47d1-a8ef-00a41a38b8d5', 'Gatos', 1, '[{\"added\": {}}]', 8, 1),
(2, '2023-10-21 21:48:33.583070', '6dd1de56-c436-4e3d-a56e-e1c64255aaba', 'Perros', 1, '[{\"added\": {}}]', 8, 1),
(3, '2023-10-21 21:48:41.032330', 'd3dca5ed-75da-41e9-bdbf-a130aae8472c', 'Loros', 1, '[{\"added\": {}}]', 8, 1),
(4, '2023-10-21 21:48:48.248199', 'e2414acc-8988-4aee-ac5c-2155b19a6b8b', 'Conejos', 1, '[{\"added\": {}}]', 8, 1),
(5, '2023-10-21 21:58:45.526794', '8f99dbec-861f-4c74-8356-2d53a11ee6ba', 'Jugueton', 1, '[{\"added\": {}}]', 10, 1),
(6, '2023-10-21 21:58:52.670704', 'dc32bdc7-4ee4-4ad5-a4e8-a020ef83f3fa', 'Dormilon', 1, '[{\"added\": {}}]', 10, 1),
(7, '2023-10-21 21:59:02.079719', '8d05af36-18b0-4a52-bb7f-4eb838ea72e2', 'Amigable', 1, '[{\"added\": {}}]', 10, 1),
(8, '2023-10-21 21:59:18.951377', '9e426470-e87d-4aad-bebd-9045138bf05a', 'Inteligente', 1, '[{\"added\": {}}]', 10, 1),
(9, '2023-10-21 22:02:14.676910', '366b286a-6084-469f-9dcc-fa64d7790183', 'Simon', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"vacuna\", \"object\": \"Vacuna de Rabia para Simon\"}}]', 11, 1),
(10, '2023-10-21 22:28:32.327139', '4cf006a3-fea1-4ab9-83ee-19144d7b5782', 'Coquito', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"imagen\", \"object\": \"Imagen de Coquito\"}}]', 11, 1),
(11, '2023-10-21 22:29:36.189964', 'e2bb1ae9-95f3-45f4-a42b-bac31b924b91', 'Princesa', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"imagen\", \"object\": \"Imagen de Princesa\"}}]', 11, 1),
(12, '2023-10-21 22:32:31.679132', '366b286a-6084-469f-9dcc-fa64d7790183', 'Simon', 2, '[{\"added\": {\"name\": \"imagen\", \"object\": \"Imagen de Simon\"}}]', 11, 1),
(13, '2023-10-22 00:55:08.027122', '9339dc2e-d427-4121-a3d8-577bf5f5d8ea', 'Abocato', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"imagen\", \"object\": \"Imagen de Abocato\"}}]', 11, 1),
(14, '2023-10-22 00:56:18.373980', 'ce298a35-0a4d-4de4-ab32-a2c1cc06676f', 'Kuno', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"imagen\", \"object\": \"Imagen de Kuno\"}}]', 11, 1),
(15, '2023-10-22 16:28:35.201849', 'ef85d6d4-13ee-48cd-9170-ab6bdb422a9b', 'Parlanchin', 1, '[{\"added\": {}}]', 10, 1),
(16, '2023-10-22 16:29:18.942273', 'deeb4778-3afa-467f-8ec2-30ae5e7569b8', 'Loracio', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"imagen\", \"object\": \"Imagen de Loracio\"}}]', 11, 1),
(17, '2023-10-26 04:23:57.956389', 'e2414acc-8988-4aee-ac5c-2155b19a6b8b', 'Conejos', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 8, 1),
(18, '2023-10-26 04:24:10.308616', 'd3dca5ed-75da-41e9-bdbf-a130aae8472c', 'Loros', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 8, 1),
(19, '2023-10-26 04:24:16.853069', '8f748574-2bbe-47d1-a8ef-00a41a38b8d5', 'Gatos', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 8, 1),
(20, '2023-10-26 04:24:23.574466', '6dd1de56-c436-4e3d-a56e-e1c64255aaba', 'Perros', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 8, 1),
(21, '2023-10-26 04:28:22.980921', 'f5e6f146-526c-4943-9bac-36f913136e5b', 'Pana Rabit', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"imagen\", \"object\": \"Imagen de Pana Rabit\"}}]', 11, 1),
(22, '2023-10-26 04:29:14.322504', '2679bf4a-a8c5-4ef1-a6f8-4cb03af7b0f9', 'Joaquin', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"imagen\", \"object\": \"Imagen de Joaquin\"}}]', 11, 1),
(23, '2023-10-26 04:31:28.459776', 'e2414acc-8988-4aee-ac5c-2155b19a6b8b', 'Conejos', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 8, 1),
(24, '2023-10-26 04:31:34.803090', 'd3dca5ed-75da-41e9-bdbf-a130aae8472c', 'Loros', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 8, 1),
(25, '2023-10-26 04:31:40.668158', '8f748574-2bbe-47d1-a8ef-00a41a38b8d5', 'Gatos', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 8, 1),
(26, '2023-10-26 04:31:46.332859', '6dd1de56-c436-4e3d-a56e-e1c64255aaba', 'Perros', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 8, 1),
(27, '2023-10-26 05:27:26.259287', '3d435746-e673-4f9a-966f-1ded4d13685f', 'Evento: Bingo el 2023-10-29.', 1, '[{\"added\": {}}]', 19, 1),
(28, '2023-10-26 05:27:51.638953', '0b1f8eef-c0cc-47d3-a32e-9f446037cf7c', 'Evento: Rifa el 2023-11-30.', 1, '[{\"added\": {}}]', 19, 1),
(29, '2023-10-26 05:28:20.510992', '70c1376e-9483-4b50-b54a-f58167cdd7b0', 'Evento: Pollada Bailable el 2023-10-12.', 1, '[{\"added\": {}}]', 19, 1),
(30, '2023-10-26 05:28:50.183028', 'ac7ac203-6fa9-4af9-94b8-81d5e83c0182', 'Evento: Bingo el 2023-12-22.', 1, '[{\"added\": {}}]', 19, 1),
(31, '2023-10-26 05:39:11.964712', '70c1376e-9483-4b50-b54a-f58167cdd7b0', 'Evento: Pollada Bailable el 2023-11-18.', 2, '[{\"changed\": {\"fields\": [\"Fecha inicio\", \"Fecha fin participacion\"]}}]', 19, 1),
(32, '2023-10-26 06:02:49.744513', '9339dc2e-d427-4121-a3d8-577bf5f5d8ea', 'Abocato', 2, '[{\"changed\": {\"name\": \"imagen\", \"object\": \"Imagen de Abocato\", \"fields\": [\"Imagen\"]}}]', 11, 1),
(33, '2023-10-26 06:03:08.352329', 'f5e6f146-526c-4943-9bac-36f913136e5b', 'Pana Rabit', 2, '[{\"changed\": {\"name\": \"imagen\", \"object\": \"Imagen de Pana Rabit\", \"fields\": [\"Imagen\"]}}]', 11, 1),
(34, '2023-10-26 06:03:19.846025', 'e2bb1ae9-95f3-45f4-a42b-bac31b924b91', 'Princesa', 2, '[{\"changed\": {\"name\": \"imagen\", \"object\": \"Imagen de Princesa\", \"fields\": [\"Imagen\"]}}]', 11, 1),
(35, '2023-10-26 06:03:32.842164', 'deeb4778-3afa-467f-8ec2-30ae5e7569b8', 'Loracio', 2, '[{\"changed\": {\"name\": \"imagen\", \"object\": \"Imagen de Loracio\", \"fields\": [\"Imagen\"]}}]', 11, 1),
(36, '2023-10-26 06:03:49.416957', 'ce298a35-0a4d-4de4-ab32-a2c1cc06676f', 'Kuno', 2, '[{\"changed\": {\"name\": \"imagen\", \"object\": \"Imagen de Kuno\", \"fields\": [\"Imagen\"]}}]', 11, 1),
(37, '2023-10-26 06:04:03.902205', '9339dc2e-d427-4121-a3d8-577bf5f5d8ea', 'Abocato', 2, '[{\"changed\": {\"name\": \"imagen\", \"object\": \"Imagen de Abocato\", \"fields\": [\"Imagen\"]}}]', 11, 1),
(38, '2023-10-26 06:04:16.197486', '4cf006a3-fea1-4ab9-83ee-19144d7b5782', 'Coquito', 2, '[{\"changed\": {\"name\": \"imagen\", \"object\": \"Imagen de Coquito\", \"fields\": [\"Imagen\"]}}]', 11, 1),
(39, '2023-10-26 06:04:38.064307', '366b286a-6084-469f-9dcc-fa64d7790183', 'Simon', 2, '[{\"changed\": {\"name\": \"imagen\", \"object\": \"Imagen de Simon\", \"fields\": [\"Imagen\"]}}]', 11, 1),
(40, '2023-10-26 06:04:52.408119', '2679bf4a-a8c5-4ef1-a6f8-4cb03af7b0f9', 'Joaquin', 2, '[{\"changed\": {\"name\": \"imagen\", \"object\": \"Imagen de Joaquin\", \"fields\": [\"Imagen\"]}}]', 11, 1),
(41, '2023-10-26 19:28:25.507253', '2314eb8f-b610-4a4e-94ee-31a22316428b', 'Pendiente', 1, '[{\"added\": {}}]', 9, 1),
(42, '2023-10-26 19:28:29.070723', 'ddb52544-584c-4087-a3bc-f5eb554c1425', 'Aprobado', 1, '[{\"added\": {}}]', 9, 1),
(43, '2023-10-26 19:28:34.161659', '339becb4-77d2-4cf3-afcd-12d1daf9d5e5', 'Rechazado', 1, '[{\"added\": {}}]', 9, 1),
(44, '2023-10-26 19:28:38.422853', '87481b7e-8fcd-4b23-bd90-e6ba85542122', 'Anulado', 1, '[{\"added\": {}}]', 9, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(7, 'api', 'adopcion'),
(17, 'api', 'comentario'),
(16, 'api', 'direccion'),
(22, 'api', 'donacion'),
(8, 'api', 'especie'),
(9, 'api', 'estadoadopcion'),
(10, 'api', 'etiqueta'),
(15, 'api', 'evaluacionadopcion'),
(19, 'api', 'evento'),
(21, 'api', 'eventoparticipante'),
(24, 'api', 'ganador'),
(14, 'api', 'imagen'),
(11, 'api', 'mascota'),
(12, 'api', 'persona'),
(23, 'api', 'premio'),
(13, 'api', 'vacuna'),
(18, 'api', 'visitaadopcion'),
(20, 'api', 'visitageneral'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-10-21 21:17:59.409304'),
(2, 'auth', '0001_initial', '2023-10-21 21:17:59.990787'),
(3, 'admin', '0001_initial', '2023-10-21 21:18:00.127704'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-10-21 21:18:00.140694'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-10-21 21:18:00.152689'),
(6, 'api', '0001_initial', '2023-10-21 21:18:01.278688'),
(7, 'contenttypes', '0002_remove_content_type_name', '2023-10-21 21:18:01.366727'),
(8, 'auth', '0002_alter_permission_name_max_length', '2023-10-21 21:18:01.445679'),
(9, 'auth', '0003_alter_user_email_max_length', '2023-10-21 21:18:01.470661'),
(10, 'auth', '0004_alter_user_username_opts', '2023-10-21 21:18:01.483654'),
(11, 'auth', '0005_alter_user_last_login_null', '2023-10-21 21:18:01.546617'),
(12, 'auth', '0006_require_contenttypes_0002', '2023-10-21 21:18:01.549613'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2023-10-21 21:18:01.561607'),
(14, 'auth', '0008_alter_user_username_max_length', '2023-10-21 21:18:01.585591'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2023-10-21 21:18:01.607576'),
(16, 'auth', '0010_alter_group_name_max_length', '2023-10-21 21:18:01.631584'),
(17, 'auth', '0011_update_proxy_permissions', '2023-10-21 21:18:01.651571'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2023-10-21 21:18:01.695543'),
(19, 'sessions', '0001_initial', '2023-10-21 21:18:01.741516'),
(20, 'api', '0002_remove_mascota_raza', '2023-10-21 21:58:01.686636'),
(21, 'api', '0003_alter_mascota_codigo', '2023-10-21 22:00:52.216359'),
(22, 'api', '0004_persona_user', '2023-10-22 02:11:28.256672'),
(23, 'api', '0005_visitaadopcion', '2023-10-22 03:35:02.598341'),
(24, 'api', '0006_visitaadopcion_asistio', '2023-10-22 03:37:23.968192'),
(25, 'api', '0007_remove_persona_genero', '2023-10-26 03:40:18.116199'),
(26, 'api', '0008_especie_imagen', '2023-10-26 04:22:34.814200'),
(27, 'api', '0009_evento_remove_adopcion_usuario_administrador_and_more', '2023-10-26 05:13:04.896908'),
(28, 'api', '0010_eventoparticipante_ticket_alter_evento_recaudacion_and_more', '2023-10-26 06:53:12.834930'),
(29, 'api', '0011_alter_adopcion_fecha_adopcion', '2023-10-26 19:51:25.263136'),
(30, 'api', '0012_alter_eventoparticipante_ticket', '2023-10-27 18:51:13.810329'),
(31, 'api', '0013_alter_eventoparticipante_ticket', '2023-10-27 18:51:13.874858');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0lidt7c4xorlubujdo1z18zfuhfedf2q', '.eJxVjEEOwiAQRe_C2hCoMFCX7nsGMsMwUjVtUtqV8e7apAvd_vfef6mE21rT1sqSRlYXdVan340wP8q0A77jdJt1nqd1GUnvij5o08PM5Xk93L-Diq1-a88QKKJxPWXxJkrfORsgQogWuhDACVuBDhwzGQuCYLCPvlChzCLq_QHIgjfv:1quOMe:ugB0u5jHpP539vXI6QO-n4B-spirHtbGuOQW82Ll2qc', '2023-11-05 02:38:52.274437'),
('2096h5sgvutmuxud01bb85j103yhwjz5', '.eJxVjDsOwyAQRO9CHSHMgr2kTO8zoOUXnEQgGbuKcvcYyUVSjTTvzbyZpX3Ldm9xtUtgVzawy2_nyD9j6SA8qNwr97Vs6-J4V_hJG59riK_b6f4dZGq5r9GnZCZSSY0IKoETSBq9HqQZo_ICIICWQiFMyUWHMtCRQh9YGJLs8wXi7Deq:1qubGl:BHJDEXcMZom80EpHZ92FjAwxf8eUC9sHbcGRHPDnjPk', '2023-11-05 16:25:39.143299'),
('9od5nh8zbhf5175zzlepd0wgskrloert', '.eJxVjDsOwyAQRO9CHSHMgr2kTO8zoOUXnEQgGbuKcvcYyUVSjTTvzbyZpX3Ldm9xtUtgVzawy2_nyD9j6SA8qNwr97Vs6-J4V_hJG59riK_b6f4dZGq5r9GnZCZSSY0IKoETSBq9HqQZo_ICIICWQiFMyUWHMtCRQh9YGJLs8wXi7Deq:1qvxNT:opoSvrHiCdBqZiR_X6vVS1oD5Ma2O1F40D01pFxzGvk', '2023-11-09 10:14:11.745480');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `api_adopcion`
--
ALTER TABLE `api_adopcion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_adopcion_estado_adopcion_id_618d1e39_fk_api_estad` (`estado_adopcion_id`),
  ADD KEY `api_adopcion_mascota_id_282a7709_fk_api_mascota_id` (`mascota_id`),
  ADD KEY `api_adopcion_usuario_adoptante_id_4a7353b3_fk_api_persona_id` (`usuario_adoptante_id`);

--
-- Indices de la tabla `api_comentario`
--
ALTER TABLE `api_comentario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_comentario_autor_id_33a450ab_fk_api_persona_id` (`autor_id`),
  ADD KEY `api_comentario_mascota_id_aa22ce1f_fk_api_mascota_id` (`mascota_id`);

--
-- Indices de la tabla `api_direccion`
--
ALTER TABLE `api_direccion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_direccion_persona_id_c8ee09a9_fk_api_persona_id` (`persona_id`);

--
-- Indices de la tabla `api_donacion`
--
ALTER TABLE `api_donacion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_donacion_persona_id_f772aad6_fk_api_persona_id` (`persona_id`);

--
-- Indices de la tabla `api_especie`
--
ALTER TABLE `api_especie`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_estadoadopcion`
--
ALTER TABLE `api_estadoadopcion`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_etiqueta`
--
ALTER TABLE `api_etiqueta`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_evaluacionadopcion`
--
ALTER TABLE `api_evaluacionadopcion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_evaluacionadopcion_adopcion_id_16e5d611_fk_api_adopcion_id` (`adopcion_id`);

--
-- Indices de la tabla `api_evento`
--
ALTER TABLE `api_evento`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `api_eventoparticipante`
--
ALTER TABLE `api_eventoparticipante`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ticket` (`ticket`),
  ADD KEY `api_eventoparticipante_evento_id_2506aa93_fk_api_evento_id` (`evento_id`),
  ADD KEY `api_eventoparticipan_participante_id_4e5c47ed_fk_api_perso` (`participante_id`);

--
-- Indices de la tabla `api_ganador`
--
ALTER TABLE `api_ganador`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_ganador_evento_id_a3b4408d_fk_api_evento_id` (`evento_id`),
  ADD KEY `api_ganador_participante_id_1f5b2b48_fk_api_event` (`participante_id`),
  ADD KEY `api_ganador_premio_id_e46d8c07_fk_api_premio_id` (`premio_id`);

--
-- Indices de la tabla `api_imagen`
--
ALTER TABLE `api_imagen`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_imagen_mascota_id_57e65203_fk_api_mascota_id` (`mascota_id`);

--
-- Indices de la tabla `api_mascota`
--
ALTER TABLE `api_mascota`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`),
  ADD KEY `api_mascota_especie_id_76ff385f_fk_api_especie_id` (`especie_id`);

--
-- Indices de la tabla `api_mascota_etiquetas`
--
ALTER TABLE `api_mascota_etiquetas`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_mascota_etiquetas_mascota_id_etiqueta_id_4dd60ad0_uniq` (`mascota_id`,`etiqueta_id`),
  ADD KEY `api_mascota_etiquetas_etiqueta_id_020ae7dd_fk_api_etiqueta_id` (`etiqueta_id`);

--
-- Indices de la tabla `api_persona`
--
ALTER TABLE `api_persona`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indices de la tabla `api_premio`
--
ALTER TABLE `api_premio`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_premio_evento_id_0b012334_fk_api_evento_id` (`evento_id`);

--
-- Indices de la tabla `api_vacuna`
--
ALTER TABLE `api_vacuna`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_vacuna_mascota_id_1134ab17_fk_api_mascota_id` (`mascota_id`);

--
-- Indices de la tabla `api_visitaadopcion`
--
ALTER TABLE `api_visitaadopcion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_visitaadopcion_adoptante_id_e2eb907e_fk_api_persona_id` (`adoptante_id`),
  ADD KEY `api_visitaadopcion_mascota_id_acfc79aa_fk_api_mascota_id` (`mascota_id`);

--
-- Indices de la tabla `api_visitageneral`
--
ALTER TABLE `api_visitageneral`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_visitageneral_persona_id_34aabd34_fk_api_persona_id` (`persona_id`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `api_ganador`
--
ALTER TABLE `api_ganador`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `api_mascota_etiquetas`
--
ALTER TABLE `api_mascota_etiquetas`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `api_premio`
--
ALTER TABLE `api_premio`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `api_adopcion`
--
ALTER TABLE `api_adopcion`
  ADD CONSTRAINT `api_adopcion_estado_adopcion_id_618d1e39_fk_api_estad` FOREIGN KEY (`estado_adopcion_id`) REFERENCES `api_estadoadopcion` (`id`),
  ADD CONSTRAINT `api_adopcion_mascota_id_282a7709_fk_api_mascota_id` FOREIGN KEY (`mascota_id`) REFERENCES `api_mascota` (`id`),
  ADD CONSTRAINT `api_adopcion_usuario_adoptante_id_4a7353b3_fk_api_persona_id` FOREIGN KEY (`usuario_adoptante_id`) REFERENCES `api_persona` (`id`);

--
-- Filtros para la tabla `api_comentario`
--
ALTER TABLE `api_comentario`
  ADD CONSTRAINT `api_comentario_autor_id_33a450ab_fk_api_persona_id` FOREIGN KEY (`autor_id`) REFERENCES `api_persona` (`id`),
  ADD CONSTRAINT `api_comentario_mascota_id_aa22ce1f_fk_api_mascota_id` FOREIGN KEY (`mascota_id`) REFERENCES `api_mascota` (`id`);

--
-- Filtros para la tabla `api_direccion`
--
ALTER TABLE `api_direccion`
  ADD CONSTRAINT `api_direccion_persona_id_c8ee09a9_fk_api_persona_id` FOREIGN KEY (`persona_id`) REFERENCES `api_persona` (`id`);

--
-- Filtros para la tabla `api_donacion`
--
ALTER TABLE `api_donacion`
  ADD CONSTRAINT `api_donacion_persona_id_f772aad6_fk_api_persona_id` FOREIGN KEY (`persona_id`) REFERENCES `api_persona` (`id`);

--
-- Filtros para la tabla `api_evaluacionadopcion`
--
ALTER TABLE `api_evaluacionadopcion`
  ADD CONSTRAINT `api_evaluacionadopcion_adopcion_id_16e5d611_fk_api_adopcion_id` FOREIGN KEY (`adopcion_id`) REFERENCES `api_adopcion` (`id`);

--
-- Filtros para la tabla `api_eventoparticipante`
--
ALTER TABLE `api_eventoparticipante`
  ADD CONSTRAINT `api_eventoparticipan_participante_id_4e5c47ed_fk_api_perso` FOREIGN KEY (`participante_id`) REFERENCES `api_persona` (`id`),
  ADD CONSTRAINT `api_eventoparticipante_evento_id_2506aa93_fk_api_evento_id` FOREIGN KEY (`evento_id`) REFERENCES `api_evento` (`id`);

--
-- Filtros para la tabla `api_ganador`
--
ALTER TABLE `api_ganador`
  ADD CONSTRAINT `api_ganador_evento_id_a3b4408d_fk_api_evento_id` FOREIGN KEY (`evento_id`) REFERENCES `api_evento` (`id`),
  ADD CONSTRAINT `api_ganador_participante_id_1f5b2b48_fk_api_event` FOREIGN KEY (`participante_id`) REFERENCES `api_eventoparticipante` (`id`),
  ADD CONSTRAINT `api_ganador_premio_id_e46d8c07_fk_api_premio_id` FOREIGN KEY (`premio_id`) REFERENCES `api_premio` (`id`);

--
-- Filtros para la tabla `api_imagen`
--
ALTER TABLE `api_imagen`
  ADD CONSTRAINT `api_imagen_mascota_id_57e65203_fk_api_mascota_id` FOREIGN KEY (`mascota_id`) REFERENCES `api_mascota` (`id`);

--
-- Filtros para la tabla `api_mascota`
--
ALTER TABLE `api_mascota`
  ADD CONSTRAINT `api_mascota_especie_id_76ff385f_fk_api_especie_id` FOREIGN KEY (`especie_id`) REFERENCES `api_especie` (`id`);

--
-- Filtros para la tabla `api_mascota_etiquetas`
--
ALTER TABLE `api_mascota_etiquetas`
  ADD CONSTRAINT `api_mascota_etiquetas_etiqueta_id_020ae7dd_fk_api_etiqueta_id` FOREIGN KEY (`etiqueta_id`) REFERENCES `api_etiqueta` (`id`),
  ADD CONSTRAINT `api_mascota_etiquetas_mascota_id_ed03182d_fk_api_mascota_id` FOREIGN KEY (`mascota_id`) REFERENCES `api_mascota` (`id`);

--
-- Filtros para la tabla `api_persona`
--
ALTER TABLE `api_persona`
  ADD CONSTRAINT `api_persona_user_id_456e1718_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `api_premio`
--
ALTER TABLE `api_premio`
  ADD CONSTRAINT `api_premio_evento_id_0b012334_fk_api_evento_id` FOREIGN KEY (`evento_id`) REFERENCES `api_evento` (`id`);

--
-- Filtros para la tabla `api_vacuna`
--
ALTER TABLE `api_vacuna`
  ADD CONSTRAINT `api_vacuna_mascota_id_1134ab17_fk_api_mascota_id` FOREIGN KEY (`mascota_id`) REFERENCES `api_mascota` (`id`);

--
-- Filtros para la tabla `api_visitaadopcion`
--
ALTER TABLE `api_visitaadopcion`
  ADD CONSTRAINT `api_visitaadopcion_adoptante_id_e2eb907e_fk_api_persona_id` FOREIGN KEY (`adoptante_id`) REFERENCES `api_persona` (`id`),
  ADD CONSTRAINT `api_visitaadopcion_mascota_id_acfc79aa_fk_api_mascota_id` FOREIGN KEY (`mascota_id`) REFERENCES `api_mascota` (`id`);

--
-- Filtros para la tabla `api_visitageneral`
--
ALTER TABLE `api_visitageneral`
  ADD CONSTRAINT `api_visitageneral_persona_id_34aabd34_fk_api_persona_id` FOREIGN KEY (`persona_id`) REFERENCES `api_persona` (`id`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
