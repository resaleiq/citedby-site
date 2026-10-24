<?php
/**
 * wp-admin page: Tools > AI-Search Check.
 *
 * @package citedby-ai-search-check
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

class CitedBy_ASC_Admin {

	const SLUG = 'citedby-ai-search-check';

	public static function menu() {
		add_management_page(
			__( 'AI-Search Check', 'citedby-ai-search-check' ),
			__( 'AI-Search Check', 'citedby-ai-search-check' ),
			'manage_options',
			self::SLUG,
			array( __CLASS__, 'page' )
		);
	}

	public static function action_links( $links ) {
		$url = admin_url( 'tools.php?page=' . self::SLUG );
		array_unshift( $links, '<a href="' . esc_url( $url ) . '">' . esc_html__( 'Run check', 'citedby-ai-search-check' ) . '</a>' );
		return $links;
	}

	/** Link to the full audit, tagged so we can count plugin visits. */
	public static function audit_url() {
		return add_query_arg(
			array(
				'source'       => 'wp-plugin',
				'utm_source'   => 'wp-plugin',
				'utm_medium'   => 'plugin',
				'utm_campaign' => 'ai-search-check',
			),
			CITEDBY_ASC_AUDIT
		);
	}

	/**
	 * Ask citedby.eu to check the home page. Sends the site address and nothing else; only called after the button.
	 *
	 * @return array|WP_Error
	 */
	public static function remote_check() {
		$lang = substr( (string) determine_locale(), 0, 2 );
		$res  = wp_remote_post(
			CITEDBY_ASC_API,
			array(
				'timeout' => 30,
				'headers' => array( 'Content-Type' => 'application/json' ),
				'body'    => wp_json_encode(
					array(
						'url'    => home_url( '/' ),
						'lang'   => in_array( $lang, array( 'fr', 'nl' ), true ) ? $lang : 'en',
						'source' => 'wp-plugin',
					)
				),
			)
		);
		if ( is_wp_error( $res ) ) {
			return $res;
		}
		$code = (int) wp_remote_retrieve_response_code( $res );
		$data = json_decode( wp_remote_retrieve_body( $res ), true );
		if ( 200 !== $code || ! is_array( $data ) || empty( $data['ok'] ) ) {
			$reason = 'unavailable';
			if ( 429 === $code ) {
				$reason = 'rate_limited';
			} elseif ( is_array( $data ) && isset( $data['error'] ) && 'bad_url' === $data['error'] ) {
				$reason = 'bad_url';
			}
			return new WP_Error( 'citedby_asc_api', $reason );
		}
		return $data;
	}

	private static function remote_error_text( $reason ) {
		if ( 'rate_limited' === $reason ) {
			return __( 'citedby.eu allows a few checks an hour per site. Try again later.', 'citedby-ai-search-check' );
		}
		if ( 'bad_url' === $reason ) {
			return __( 'citedby.eu can only check a public address. This site is on a local or private address (localhost, a staging network or an IP), so the page check was skipped. The checks above still stand.', 'citedby-ai-search-check' );
		}
		return __( 'citedby.eu did not answer. The checks above still stand. Try again later.', 'citedby-ai-search-check' );
	}

	private static function status_label( $status ) {
		$map = array(
			'pass'    => array( '&#10003;', __( 'OK', 'citedby-ai-search-check' ), '#00a32a' ),
			'fail'    => array( '&#10007;', __( 'Needs a fix', 'citedby-ai-search-check' ), '#d63638' ),
			'warn'    => array( '!', __( 'Could be better', 'citedby-ai-search-check' ), '#dba617' ),
			'info'    => array( 'i', __( 'Optional', 'citedby-ai-search-check' ), '#787c82' ),
			'unknown' => array( '?', __( 'Not measured', 'citedby-ai-search-check' ), '#787c82' ),
		);
		return isset( $map[ $status ] ) ? $map[ $status ] : null;
	}

	private static function row( $status, $text ) {
		$s = self::status_label( $status );
		if ( ! $s ) {
			return;
		}
		echo '<tr><td style="width:9em;color:' . esc_attr( $s[2] ) . ';font-weight:600"><span aria-hidden="true">' . wp_kses( $s[0], array() ) . '</span> ' . esc_html( $s[1] ) . '</td><td>' . esc_html( $text ) . '</td></tr>';
	}

	private static function render_local( $l ) {
		echo '<h2>' . esc_html__( 'Checked from your site', 'citedby-ai-search-check' ) . '</h2><table class="widefat striped"><tbody>';
		self::row( $l['public'] ? 'pass' : 'fail', $l['public'] ? __( 'Search engines are allowed to index this site.', 'citedby-ai-search-check' ) : __( 'Settings > Reading has "Discourage search engines" ticked. Crawlers are asked to stay away.', 'citedby-ai-search-check' ) );
		self::row( $l['robots_found'] ? 'pass' : 'info', $l['robots_found'] ? __( 'robots.txt found.', 'citedby-ai-search-check' ) : __( 'No robots.txt found. Crawlers may read everything.', 'citedby-ai-search-check' ) );
		foreach ( $l['bots'] as $token => $b ) {
			/* translators: 1: crawler name, 2: what it feeds, e.g. "GPTBot (OpenAI training)" */
			$name = sprintf( __( '%1$s (%2$s)', 'citedby-ai-search-check' ), $token, $b['label'] );
			if ( $b['blocked'] && in_array( $token, CitedBy_ASC_Local::TRAINING, true ) ) {
				/* translators: %s: crawler */
				self::row( 'info', sprintf( __( '%s is blocked by robots.txt. That is a normal choice: it keeps your pages out of model training and does not remove you from AI search answers.', 'citedby-ai-search-check' ), $name ) );
				continue;
			}
			self::row( $b['blocked'] ? 'fail' : 'pass', $b['blocked'] ? sprintf( /* translators: %s: crawler */ __( '%s is blocked by robots.txt.', 'citedby-ai-search-check' ), $name ) : sprintf( /* translators: %s: crawler */ __( '%s is not blocked.', 'citedby-ai-search-check' ), $name ) );
		}
		self::row( $l['llms'] ? 'pass' : 'info', $l['llms'] ? __( 'llms.txt found.', 'citedby-ai-search-check' ) : __( 'No llms.txt. It is optional and no assistant has promised to read it.', 'citedby-ai-search-check' ) );
		self::row( '' !== $l['sitemap'] ? 'pass' : 'warn', '' !== $l['sitemap'] ? sprintf( /* translators: %s: sitemap URL */ __( 'Sitemap found: %s', 'citedby-ai-search-check' ), $l['sitemap'] ) : __( 'No sitemap found at the usual addresses.', 'citedby-ai-search-check' ) );
		echo '</tbody></table>';
		echo '<p class="description">' . esc_html__( 'A page-level block (noindex, a security plugin, a firewall or CDN bot rule) is not visible here. The page check below fetches your home page from outside.', 'citedby-ai-search-check' ) . '</p>';
	}

	private static function render_remote( $r ) {
		$texts = array(
			'crawlers'   => __( 'AI crawlers are not blocked in robots.txt (as seen from citedby.eu)', 'citedby-ai-search-check' ),
			'raw_text'   => __( 'Your home page text is in the HTML a crawler receives', 'citedby-ai-search-check' ),
			'org_schema' => __( 'Organization or business structured data (JSON-LD) on the home page', 'citedby-ai-search-check' ),
			'llms_txt'   => __( 'llms.txt present', 'citedby-ai-search-check' ),
		);
		echo '<h2>' . esc_html__( 'Checked from outside (citedby.eu)', 'citedby-ai-search-check' ) . '</h2>';
		if ( empty( $r['reachable'] ) ) {
			echo '<p>' . esc_html__( 'citedby.eu could not load your home page. If the site is on a private network or behind a login, this check cannot run.', 'citedby-ai-search-check' ) . '</p>';
			return;
		}
		echo '<table class="widefat striped"><tbody>';
		foreach ( (array) $r['checks'] as $c ) {
			if ( isset( $c['id'], $c['status'], $texts[ $c['id'] ] ) ) {
				self::row( $c['status'], $texts[ $c['id'] ] );
			}
		}
		echo '</tbody></table>';
	}

	public static function page() {
		if ( ! current_user_can( 'manage_options' ) ) {
			wp_die( esc_html__( 'You do not have permission to view this page.', 'citedby-ai-search-check' ) );
		}
		echo '<div class="wrap"><h1>' . esc_html__( 'CitedBy AI-Search Check', 'citedby-ai-search-check' ) . '</h1>';
		echo '<p>' . esc_html__( 'Find out whether AI-search crawlers can read this site. The first part runs on your server. The second sends your home page address to citedby.eu, which loads the page and reports back. Nothing is sent until you press the button.', 'citedby-ai-search-check' ) . '</p>';

		$run = isset( $_POST['citedby_asc_run'] ); // phpcs:ignore WordPress.Security.NonceVerification.Missing -- verified on the next line.
		if ( $run ) {
			check_admin_referer( 'citedby_asc_run' );
			self::render_local( CitedBy_ASC_Local::run() );
			$remote = self::remote_check();
			if ( is_wp_error( $remote ) ) {
				echo '<h2>' . esc_html__( 'Checked from outside (citedby.eu)', 'citedby-ai-search-check' ) . '</h2><p>' . esc_html( self::remote_error_text( $remote->get_error_message() ) ) . '</p>';
			} else {
				self::render_remote( $remote );
			}
			echo '<p style="margin-top:1.5em"><a class="button button-primary" target="_blank" rel="noopener" href="' . esc_url( self::audit_url() ) . '">' . esc_html__( 'Get the full audit with the exact fix', 'citedby-ai-search-check' ) . '</a></p>';
		}

		echo '<form method="post">';
		wp_nonce_field( 'citedby_asc_run' );
		echo '<p><button type="submit" name="citedby_asc_run" value="1" class="button ' . ( $run ? '' : 'button-primary' ) . '">' . esc_html( $run ? __( 'Run again', 'citedby-ai-search-check' ) : __( 'Run the check', 'citedby-ai-search-check' ) ) . '</button></p></form>';
		echo '</div>';
	}
}
