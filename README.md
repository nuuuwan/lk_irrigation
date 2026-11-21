# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_00:03:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,232 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 00:03:15 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-22 00:02:55 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-22 00:02:47 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -108.000 |  |
| 2026-11-22 00:02:46 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -108.000 |  |
| 2026-11-22 00:02:46 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-22 00:02:28 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-22 00:02:24 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-22 00:02:24 | Dunamale (Aththanagalu Oya) | 1.41 | 🟢 Normal | -0.011 |  |
| 2026-11-22 00:02:22 | Moraketiya (Walawe Ganga) | 2.96 | 🟢 Normal | -0.010 |  |
| 2026-11-22 00:02:15 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-11-22 00:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.38 | 🟢 Normal | -0.032 |  |
| 2026-11-22 00:02:01 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | -0.064 |  |
| 2026-11-22 00:02:00 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | -0.039 |  |
| 2026-11-22 00:01:45 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.041 |  |
| 2026-11-22 00:01:34 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 00:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-22 00:01:13 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | 0.320 | 🔺 Rising |
| 2026-11-22 00:00:33 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 23:47:56 | Panadugama (Nilwala Ganga) | 4.51 | 🟢 Normal | -0.011 |  |
| 2026-11-21 23:23:42 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.320 | 🔺 Rising |
| 2026-11-21 23:23:33 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-21 23:23:12 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 23:02:17 | Badalgama (Maha Oya) | 3.65 | 🟢 Normal | 0.898 | 🔺 Rising |
| 2026-11-21 23:02:08 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | 0.383 | 🔺 Rising |
| 2026-11-22 00:01:13 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | 0.320 | 🔺 Rising |
| 2026-11-22 00:03:15 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-21 23:02:28 | Glencourse (Kelani Ganga) | 9.49 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-21 23:05:16 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-21 23:05:45 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-21 23:11:19 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-21 23:15:53 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-11-22 00:00:33 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 18:00:46 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-21 23:01:32 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-22 00:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-22 00:01:34 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:00:19 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-11-22 00:02:15 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-22 00:02:28 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-21 22:02:55 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-22 00:02:55 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:02:22 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-22 00:02:46 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-21 23:06:24 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-21 23:05:23 | Thanamalwila (Kirindi Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-11-22 00:02:22 | Moraketiya (Walawe Ganga) | 2.96 | 🟢 Normal | -0.010 |  |
| 2026-11-22 00:02:24 | Dunamale (Aththanagalu Oya) | 1.41 | 🟢 Normal | -0.011 |  |
| 2026-11-21 23:47:56 | Panadugama (Nilwala Ganga) | 4.51 | 🟢 Normal | -0.011 |  |
| 2026-11-21 23:16:56 | Urawa (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.022 |  |
| 2026-11-21 23:23:12 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.023 |  |
| 2026-11-21 23:07:07 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.028 |  |
| 2026-11-21 23:06:37 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | -0.029 |  |
| 2026-11-21 23:02:08 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | -0.030 |  |
| 2026-11-22 00:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.38 | 🟢 Normal | -0.032 |  |
| 2026-11-22 00:02:00 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | -0.039 |  |
| 2026-11-22 00:01:45 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.041 |  |
| 2026-11-21 23:04:51 | Hanwella (Kelani Ganga) | 1.51 | 🟢 Normal | -0.060 |  |
| 2026-11-22 00:02:01 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | -0.064 |  |
| 2026-11-21 23:03:03 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.070 |  |
| 2026-11-22 00:02:47 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)