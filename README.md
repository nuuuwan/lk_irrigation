# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_12:20:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **240,374 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-22 12:20:28 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.033 |  |
| 2026-08-22 12:17:41 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:12:41 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-08-22 12:12:00 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:08:30 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-08-22 12:07:55 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.011 |  |
| 2026-08-22 12:06:30 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.021 |  |
| 2026-08-22 12:05:47 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | -0.020 |  |
| 2026-08-22 12:05:37 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:05:36 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-08-22 12:05:19 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:05:02 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:04:34 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.011 |  |
| 2026-08-22 12:04:31 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-08-22 12:04:07 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:04:06 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:04:05 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.015 |  |
| 2026-08-22 12:03:42 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:03:25 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:03:10 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:03:03 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:02:37 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-08-22 12:02:36 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.030 |  |
| 2026-08-22 12:02:35 | Galgamuwa (Mee Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:02:34 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.019 |  |
| 2026-08-22 12:02:31 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | -0.040 |  |
| 2026-08-22 12:02:19 | Ellagawa (Kalu Ganga) | 5.82 | 🟢 Normal | -0.030 |  |
| 2026-08-22 12:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | -0.020 |  |
| 2026-08-22 12:01:49 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:01:40 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:01:24 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:01:17 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.052 |  |
| 2026-08-22 12:01:13 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:01:08 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:01:06 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:01:04 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.030 |  |
| 2026-08-22 12:00:39 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-08-22 12:00:32 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:00:29 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:00:27 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.056 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-22 12:12:41 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-08-22 12:03:25 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:01:13 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:03:42 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:00:29 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:03:10 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:00:32 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:02:35 | Galgamuwa (Mee Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:04:06 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:05:02 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:05:37 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:01:08 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:01:06 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:01:24 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:01:40 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:05:19 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:03:03 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:17:41 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:01:49 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:12:00 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:04:07 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-22 12:02:37 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-08-22 12:05:36 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-08-22 12:04:31 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-08-22 12:00:39 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-08-22 12:07:55 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.011 |  |
| 2026-08-22 12:04:34 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.011 |  |
| 2026-08-22 12:04:05 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.015 |  |
| 2026-08-22 12:02:34 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.019 |  |
| 2026-08-22 12:05:47 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | -0.020 |  |
| 2026-08-22 12:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | -0.020 |  |
| 2026-08-22 12:06:30 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.021 |  |
| 2026-08-22 12:02:19 | Ellagawa (Kalu Ganga) | 5.82 | 🟢 Normal | -0.030 |  |
| 2026-08-22 12:02:36 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.030 |  |
| 2026-08-22 12:01:04 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.030 |  |
| 2026-08-22 12:20:28 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.033 |  |
| 2026-08-22 12:02:31 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | -0.040 |  |
| 2026-08-22 12:01:17 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.052 |  |
| 2026-08-22 12:00:27 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.056 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)