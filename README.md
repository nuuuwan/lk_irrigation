# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--08_01:31:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **254,829 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-08 01:31:53 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.008 |  |
| 2026-09-08 01:12:58 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:08:43 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-08 01:08:37 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | -0.010 |  |
| 2026-09-08 01:07:58 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:06:57 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:05:48 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-08 01:05:35 | Thanamalwila (Kirindi Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:05:34 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-09-08 01:05:30 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:04:53 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:04:43 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:04:32 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-08 01:03:47 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:03:19 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.040 |  |
| 2026-09-08 01:03:17 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:03:10 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | -0.222 |  |
| 2026-09-08 01:02:31 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:02:31 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.012 |  |
| 2026-09-08 01:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-09-08 01:02:21 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:01:53 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 01:01:51 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:01:42 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:01:24 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:01:14 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:01:06 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:00:59 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:00:44 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:00:36 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-08 00:03:07 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-09-08 01:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-09-08 01:05:48 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-08 00:07:37 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-08 00:00:56 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-08 01:08:43 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-08 01:04:32 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-07 18:10:27 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-08 00:04:55 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 01:01:53 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 01:01:14 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:00:59 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:04:53 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:07:58 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:01:51 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:02:31 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:00:36 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-07 18:04:43 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:00:44 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-08 00:05:31 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:01:42 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-08 00:08:21 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-09-08 00:14:06 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:01:24 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:12:58 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:02:21 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:01:06 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:05:30 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:03:47 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:03:17 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:06:57 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:05:35 | Thanamalwila (Kirindi Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-08 01:31:53 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.008 |  |
| 2026-09-08 01:08:37 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | -0.010 |  |
| 2026-09-08 01:02:31 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.012 |  |
| 2026-09-08 01:05:34 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-09-08 01:03:19 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.040 |  |
| 2026-09-07 18:02:01 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.050 |  |
| 2026-09-08 01:03:10 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | -0.222 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)