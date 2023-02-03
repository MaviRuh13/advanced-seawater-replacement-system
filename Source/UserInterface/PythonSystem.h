// Search:
			bool			bShowSalesText;

// Add:
#ifdef MAVIRUH_WATER_SYSTEM
			int				bMaviRuhSuDegistir;
#endif

// Search:
		void							SetShowSalesTextFlag(int iFlag);

// Add:
#ifdef MAVIRUH_WATER_SYSTEM
		void							SetMaviRuhSuDegistir(unsigned int level);
		int								GetMaviRuhSuDegistir();
#endif