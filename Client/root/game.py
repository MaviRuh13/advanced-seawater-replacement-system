# Search: def Open(self):
		self.currentCubeNPC = 0

# Add:
		if app.MAVIRUH_WATER_SYSTEM:
			if systemSetting.GetMaviRuhSuDegistir() == 0:
				systemSetting.SetMaviRuhSuDegistir(0)
				background.SuDegistir("d:/ymir Work/special/water")
			elif systemSetting.GetMaviRuhSuDegistir() == 1:
				systemSetting.SetMaviRuhSuDegistir(1)
				background.SuDegistir2("d:/ymir Work/special/eski_saltanat_suyu")
			elif systemSetting.GetMaviRuhSuDegistir() == 2:
				systemSetting.SetMaviRuhSuDegistir(2)
				background.SuDegistir3("d:/ymir Work/special/saltanat_suyu")
			elif systemSetting.GetMaviRuhSuDegistir() == 3:
				systemSetting.SetMaviRuhSuDegistir(3)
				background.SuDegistir4("d:/ymir Work/special/deniz_suyu")
			elif systemSetting.GetMaviRuhSuDegistir() == 4:
				systemSetting.SetMaviRuhSuDegistir(4)
				background.SuDegistir5("d:/ymir Work/special/maviruh_deniz_suyu")
			elif systemSetting.GetMaviRuhSuDegistir() == 5:
				systemSetting.SetMaviRuhSuDegistir(5)
				background.SuDegistir6("d:/ymir Work/special/comedy_water")
			elif systemSetting.GetMaviRuhSuDegistir() == 6:
				systemSetting.SetMaviRuhSuDegistir(6)
				background.SuDegistir7("d:/ymir Work/special/new_water")
			elif systemSetting.GetMaviRuhSuDegistir() == 7:
				systemSetting.SetMaviRuhSuDegistir(7)
				background.SuDegistir8("d:/ymir Work/special/lava")
			else:
				systemSetting.SetMaviRuhSuDegistir(0)
				background.SuDegistir("d:/ymir Work/special/water")

# Search:
	def __IsShowNameItem(self):
		if systemSetting.IsAlwaysShowName() == 1:
			return True

		return False

# Add:
	if app.MAVIRUH_WATER_SYSTEM:
		def __GetMaviRuhSuDegistir(self):
			if systemSetting.GetMaviRuhSuDegistir() == 0:
				return True
			return False
		def __GetMaviRuhSuDegistir2(self):
			if systemSetting.GetMaviRuhSuDegistir() == 1:
				return True
			return False
		def __GetMaviRuhSuDegistir3(self):
			if systemSetting.GetMaviRuhSuDegistir() == 2:
				return True
			return False
		def __GetMaviRuhSuDegistir4(self):
			if systemSetting.GetMaviRuhSuDegistir() == 3:
				return True
			return False
		def __GetMaviRuhSuDegistir5(self):
			if systemSetting.GetMaviRuhSuDegistir() == 5:
				return True
			return False
		def __GetMaviRuhSuDegistir6(self):
			if systemSetting.GetMaviRuhSuDegistir() == 6:
				return True
			return False
		def __GetMaviRuhSuDegistir7(self):
			if systemSetting.GetMaviRuhSuDegistir() == 7:
				return True
			return False