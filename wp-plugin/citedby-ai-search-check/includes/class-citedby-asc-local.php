<?php
/**
 * Checks that run from this site itself (no call to citedby.eu): robots.txt, llms.txt, sitemap.
 *
 * @package citedby-ai-search-check
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

class CitedBy_ASC_Local {

	/** AI crawlers shown to the site owner: user-agent token => what it feeds. */
	const BOTS = array(
		'OAI-SearchBot'    => 'ChatGPT search',
		'GPTBot'           => 'OpenAI training',
		'ChatGPT-User'     => 'ChatGPT browsing',
		'PerplexityBot'    => 'Perplexity',
		'ClaudeBot'        => 'Claude',
		'Claude-SearchBot' => 'Claude search',
		'Google-Extended'  => 'Gemini training',
		'Applebot-Extended' => 'Apple Intelligence',
		'CCBot'            => 'Common Crawl',
		'Bingbot'          => 'Bing and Copilot',
	);

	/**
	 * Fetch one URL of this site and return status and body (max 200 KB).
	 *
	 * @param string $url Absolute URL.
	 * @return array{status:int,body:string}
	 */
	public static function fetch( $url ) {
		$res = wp_remote_get(
			$url,
			array(
				'timeout'     => 10,
				'redirection' => 3,
				'limit_response_size' => 204800,
				'sslverify'   => apply_filters( 'https_local_ssl_verify', false ),
			)
		);
		if ( is_wp_error( $res ) ) {
			return array( 'status' => 0, 'body' => '' );
		}
		return array(
			'status' => (int) wp_remote_retrieve_response_code( $res ),
			'body'   => (string) wp_remote_retrieve_body( $res ),
		);
	}

	/**
	 * Parse robots.txt text into groups: [ ['agents'=>[lowercase], 'rules'=>[[type,path],...]], ... ].
	 *
	 * @param string $text robots.txt body.
	 * @return array
	 */
	public static function parse_robots( $text ) {
		$groups  = array();
		$current = null;
		$in_rules = false;
		foreach ( preg_split( '/\r\n|\r|\n/', $text ) as $line ) {
			$line = trim( preg_replace( '/#.*$/', '', $line ) );
			if ( '' === $line || false === strpos( $line, ':' ) ) {
				continue;
			}
			list( $key, $val ) = array_map( 'trim', explode( ':', $line, 2 ) );
			$key = strtolower( $key );
			if ( 'user-agent' === $key ) {
				if ( null === $current || $in_rules ) {
					$groups[] = array( 'agents' => array(), 'rules' => array() );
					$current  = count( $groups ) - 1;
					$in_rules = false;
				}
				$groups[ $current ]['agents'][] = strtolower( $val );
			} elseif ( ( 'disallow' === $key || 'allow' === $key ) && null !== $current ) {
				$in_rules = true;
				$groups[ $current ]['rules'][] = array( $key, $val );
			}
		}
		return $groups;
	}

	/**
	 * Is the whole site closed to this crawler by robots.txt?
	 * The group naming the bot wins, else the "*" group. "Disallow: /" with no "Allow: /" closes it.
	 *
	 * @param array  $groups Output of parse_robots().
	 * @param string $bot    User-agent token.
	 * @return bool
	 */
	public static function bot_blocked( $groups, $bot ) {
		$bot   = strtolower( $bot );
		$match = null;
		foreach ( $groups as $g ) {
			if ( in_array( $bot, $g['agents'], true ) ) {
				$match = $g;
				break;
			}
		}
		if ( null === $match ) {
			foreach ( $groups as $g ) {
				if ( in_array( '*', $g['agents'], true ) ) {
					$match = $g;
					break;
				}
			}
		}
		if ( null === $match ) {
			return false;
		}
		$closed = false;
		$open   = false;
		foreach ( $match['rules'] as $r ) {
			if ( 'disallow' === $r[0] && '/' === $r[1] ) {
				$closed = true;
			}
			if ( 'allow' === $r[0] && '/' === $r[1] ) {
				$open = true;
			}
		}
		return $closed && ! $open;
	}

	/**
	 * Run the three local checks.
	 *
	 * @return array
	 */
	public static function run() {
		$out    = array();
		$robots = self::fetch( home_url( '/robots.txt' ) );
		$found  = 200 === $robots['status'] && false === stripos( substr( $robots['body'], 0, 500 ), '<html' );
		$groups = $found ? self::parse_robots( $robots['body'] ) : array();

		$out['public'] = (bool) get_option( 'blog_public' );
		$out['robots_found'] = $found;
		$out['bots'] = array();
		foreach ( self::BOTS as $token => $label ) {
			$out['bots'][ $token ] = array(
				'label'   => $label,
				'blocked' => self::bot_blocked( $groups, $token ),
			);
		}

		$llms = self::fetch( home_url( '/llms.txt' ) );
		$out['llms'] = 200 === $llms['status'] && strlen( $llms['body'] ) > 50 && false === stripos( substr( $llms['body'], 0, 500 ), '<html' );

		$candidates = array();
		if ( $found && preg_match_all( '/^\s*sitemap:\s*(\S+)/im', $robots['body'], $m ) ) {
			$candidates = $m[1];
		}
		$candidates[] = home_url( '/wp-sitemap.xml' );
		$candidates[] = home_url( '/sitemap.xml' );
		$out['sitemap'] = '';
		foreach ( array_slice( array_unique( $candidates ), 0, 4 ) as $url ) {
			$url = esc_url_raw( $url );
			if ( '' === $url ) {
				continue;
			}
			$r = self::fetch( $url );
			if ( 200 === $r['status'] && ( false !== strpos( $r['body'], '<urlset' ) || false !== strpos( $r['body'], '<sitemapindex' ) ) ) {
				$out['sitemap'] = $url;
				break;
			}
		}
		return $out;
	}
}
