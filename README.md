# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_00:02:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,208 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 00:02:54 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-11-03 00:02:46 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-03 00:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | -0.020 |  |
| 2026-11-03 00:02:27 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 00:01:38 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-03 00:01:07 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.012 |  |
| 2026-11-03 00:01:05 | Thaldena (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.161 |  |
| 2026-11-03 00:00:13 | Horowpothana (Yan Oya) | 3.18 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-03 00:00:13 | Wellawaya (Kirindi Oya) | 2.85 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-02 23:21:44 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 23:07:08 | Holombuwa (Kelani Ganga) | 2.81 | 🟢 Normal | 1.432 | 🔺 Rising |
| 2026-11-02 23:07:54 | Peradeniya (Mahaweli Ganga) | 4.28 | 🟢 Normal | 0.396 | 🔺 Rising |
| 2026-11-02 23:07:50 | Magura (Kalu Ganga) | 2.12 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-11-02 23:03:27 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-11-02 23:01:31 | Padiyathalawa (Maduru Oya) | 1.92 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-11-02 23:04:49 | Rathnapura (Kalu Ganga) | 4.15 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-03 00:00:13 | Horowpothana (Yan Oya) | 3.18 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-02 18:02:49 | Galgamuwa (Mee Oya) | 0.91 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-03 00:00:13 | Wellawaya (Kirindi Oya) | 2.85 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-03 00:02:46 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-02 23:07:16 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-02 23:07:10 | Norwood (Kelani Ganga) | 1.27 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-02 23:16:21 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-02 23:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-02 22:27:41 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-11-03 00:01:38 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-02 23:02:40 | Moragaswewa (Deduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-03 00:02:27 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 23:03:27 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-02 22:04:08 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-02 23:03:59 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 23:21:44 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:01:45 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-02 23:15:02 | Ellagawa (Kalu Ganga) | 5.89 | 🟢 Normal | -0.008 |  |
| 2026-11-02 23:09:37 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-02 23:09:26 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-11-02 23:08:31 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-11-02 23:02:09 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-11-02 23:00:21 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | -0.011 |  |
| 2026-11-03 00:01:07 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.012 |  |
| 2026-11-03 00:02:54 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-11-03 00:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | -0.020 |  |
| 2026-11-02 23:03:08 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | -0.030 |  |
| 2026-11-02 18:00:17 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.030 |  |
| 2026-11-02 23:01:08 | Panadugama (Nilwala Ganga) | 4.32 | 🟢 Normal | -0.042 |  |
| 2026-11-02 23:08:04 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.074 |  |
| 2026-11-02 23:05:31 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | -0.148 |  |
| 2026-11-03 00:01:05 | Thaldena (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.161 |  |
| 2026-11-02 23:04:04 | Deraniyagala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.310 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)