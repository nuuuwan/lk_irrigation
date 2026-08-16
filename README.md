# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_10:16:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **234,934 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-16 10:16:18 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.032 |  |
| 2026-08-16 10:15:29 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-16 10:12:16 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-08-16 10:11:06 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:10:55 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.018 |  |
| 2026-08-16 10:10:32 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-16 10:09:59 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.029 |  |
| 2026-08-16 10:09:41 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:07:19 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | -0.089 |  |
| 2026-08-16 10:06:56 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | -0.045 |  |
| 2026-08-16 10:06:53 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:06:38 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:06:14 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:06:00 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:05:51 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.005 |  |
| 2026-08-16 10:05:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | -0.030 |  |
| 2026-08-16 10:05:16 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.132 |  |
| 2026-08-16 10:05:09 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:05:04 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:04:59 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | -0.011 |  |
| 2026-08-16 10:04:09 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.140 |  |
| 2026-08-16 10:03:47 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:03:39 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.061 |  |
| 2026-08-16 10:03:36 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-08-16 10:03:32 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-08-16 10:03:31 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:03:30 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.020 |  |
| 2026-08-16 10:03:18 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:02:58 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:02:35 | Glencourse (Kelani Ganga) | 9.89 | 🟢 Normal | -0.010 |  |
| 2026-08-16 10:02:32 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-08-16 10:02:16 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:01:46 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:01:32 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-16 10:01:17 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:01:15 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.061 |  |
| 2026-08-16 10:01:11 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:00:55 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:00:20 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-16 10:03:32 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-08-16 10:10:32 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-16 10:15:29 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-16 10:01:32 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-16 10:00:20 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:06:53 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:06:14 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:05:04 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:03:47 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:02:58 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:00:55 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:06:38 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:02:16 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:03:18 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:03:31 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:01:11 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:05:09 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:06:00 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-08-16 09:00:21 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:11:06 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:01:17 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:01:46 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-16 10:05:51 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.005 |  |
| 2026-08-16 10:12:16 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-08-16 10:02:35 | Glencourse (Kelani Ganga) | 9.89 | 🟢 Normal | -0.010 |  |
| 2026-08-16 10:04:59 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | -0.011 |  |
| 2026-08-16 10:10:55 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.018 |  |
| 2026-08-16 10:03:30 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.020 |  |
| 2026-08-16 10:03:36 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-08-16 10:02:32 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-08-16 10:09:59 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.029 |  |
| 2026-08-16 10:05:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | -0.030 |  |
| 2026-08-16 10:16:18 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.032 |  |
| 2026-08-16 10:06:56 | Ellagawa (Kalu Ganga) | 5.29 | 🟢 Normal | -0.045 |  |
| 2026-08-16 10:01:15 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.061 |  |
| 2026-08-16 10:03:39 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.061 |  |
| 2026-08-16 10:07:19 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | -0.089 |  |
| 2026-08-16 10:05:16 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.132 |  |
| 2026-08-16 10:04:09 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)