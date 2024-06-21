class BaseModelLightcurve:
    def calc_peak_luminosity(self, **kwargs):
        """
        Calculate the peak luminosity of the lightcurve.
        """
        raise NotImplementedError

    def calc_peak_time(self, **kwargs):
        """
        Calculate the peak time of the lightcurve.
        """
        raise NotImplementedError
