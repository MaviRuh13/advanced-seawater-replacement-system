// Add:
#include "../UserInterface/locale_inc.h"

// Search:
		void			RenderScreenFiltering();

// Add:
#ifdef MAVIRUH_WATER_SYSTEM
		void			SuDegistir(const char * c_szFileName);
		void			SuDegistir2(const char * c_szFileName);
		void			SuDegistir3(const char * c_szFileName);
		void			SuDegistir4(const char * c_szFileName);
		void			SuDegistir5(const char * c_szFileName);
		void			SuDegistir6(const char * c_szFileName);
		void			SuDegistir7(const char * c_szFileName);
		void			SuDegistir8(const char * c_szFileName);
#endif

// Search:
		void					UnloadWaterTexture();

// Add:
#ifdef MAVIRUH_WATER_SYSTEM
		void					LoadOzelSu(const char * szDosyaAdi);
		void					LoadOzelSu2(const char * szDosyaAdi2);
		void					LoadOzelSu3(const char * szDosyaAdi3);
		void					LoadOzelSu4(const char * szDosyaAdi4);
		void					LoadOzelSu5(const char * szDosyaAdi5);
		void					LoadOzelSu6(const char * szDosyaAdi6);
		void					LoadOzelSu7(const char * szDosyaAdi7);
		void					LoadOzelSu8(const char * szDosyaAdi8);
#endif