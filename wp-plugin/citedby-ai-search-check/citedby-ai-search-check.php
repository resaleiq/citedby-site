<?php
/**
 * Plugin Name:       CitedBy AI-Search Check
 * Plugin URI:        https://citedby.eu
 * Description:       One click in wp-admin shows whether AI-search crawlers can read your site: robots.txt, llms.txt, sitemap and a free page check from citedby.eu.
 * Version:           0.1.0
 * Requires at least: 5.8
 * Requires PHP:      7.4
 * Author:            CitedBy
 * Author URI:        https://citedby.eu
 * License:           GPL v2 or later
 * License URI:       https://www.gnu.org/licenses/gpl-2.0.html
 * Text Domain:       citedby-ai-search-check
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'CITEDBY_ASC_VERSION', '0.1.0' );
define( 'CITEDBY_ASC_API', 'https://citedby.eu/api/check' );
define( 'CITEDBY_ASC_AUDIT', 'https://citedby.eu/ai-visibility-audit' );

require_once __DIR__ . '/includes/class-citedby-asc-local.php';
require_once __DIR__ . '/includes/class-citedby-asc-admin.php';

add_action( 'admin_menu', array( 'CitedBy_ASC_Admin', 'menu' ) );
add_filter( 'plugin_action_links_' . plugin_basename( __FILE__ ), array( 'CitedBy_ASC_Admin', 'action_links' ) );
