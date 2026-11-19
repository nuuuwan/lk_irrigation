# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--19_16:03:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **320,185 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 16:03:16 | Hanwella (Kelani Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-11-19 16:03:14 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-19 16:03:06 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:02:52 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:02:47 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:02:41 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.082 |  |
| 2026-11-19 16:01:59 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-11-19 16:01:58 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.380 | 🔺 Rising |
| 2026-11-19 16:01:38 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:01:36 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-11-19 16:01:35 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.030 |  |
| 2026-11-19 16:01:32 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-19 16:01:25 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | -0.020 |  |
| 2026-11-19 16:01:19 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:01:11 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-11-19 16:01:03 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:00:55 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:00:39 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-11-19 16:00:31 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:00:07 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 15:06:10 | Panadugama (Nilwala Ganga) | 3.76 | 🟢 Normal | 0.468 | 🔺 Rising |
| 2026-11-19 16:01:58 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.380 | 🔺 Rising |
| 2026-11-19 15:05:14 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-11-19 16:03:14 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-19 15:14:26 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-19 16:01:32 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-19 16:00:31 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:01:38 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-19 15:03:20 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:01:03 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:03:06 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:00:07 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:00:55 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-19 15:01:21 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-19 15:06:20 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:02:52 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:02:47 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 15:03:10 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-11-19 15:02:06 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:02:41 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-19 16:01:19 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-19 15:05:25 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | -0.009 |  |
| 2026-11-19 15:06:24 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-11-19 15:09:58 | Moraketiya (Walawe Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-19 16:03:16 | Hanwella (Kelani Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-11-19 15:01:18 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-11-19 16:01:59 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-11-19 16:00:39 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-11-19 16:01:11 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-11-19 15:06:18 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-11-19 15:02:00 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.015 |  |
| 2026-11-19 16:01:36 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-11-19 16:01:25 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | -0.020 |  |
| 2026-11-19 15:16:33 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.025 |  |
| 2026-11-19 16:01:35 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.030 |  |
| 2026-11-19 15:05:20 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | -0.030 |  |
| 2026-11-19 15:03:36 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.032 |  |
| 2026-11-19 16:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)