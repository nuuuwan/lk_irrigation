# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--09_08:16:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **255,996 measurements** from **39** stations.
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
| 2026-09-09 08:16:57 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:12:09 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:10:49 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-09 08:10:06 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:08:23 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:08:07 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:07:38 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-09-09 08:06:23 | Rathnapura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-09-09 08:06:21 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:06:12 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:05:28 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:05:00 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 08:04:46 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.044 |  |
| 2026-09-09 08:04:27 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-09 08:04:23 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:04:01 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:03:42 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:03:37 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.024 |  |
| 2026-09-09 08:03:30 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:03:22 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:03:21 | Hanwella (Kelani Ganga) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 08:03:16 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:03:14 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | -0.040 |  |
| 2026-09-09 08:03:13 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-09 08:03:01 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-09-09 08:02:57 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:02:56 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:02:54 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-09-09 08:02:19 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:02:04 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:01:35 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:01:22 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.101 |  |
| 2026-09-09 08:01:19 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.052 |  |
| 2026-09-09 08:01:17 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:00:47 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-09 08:00:36 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:00:36 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:00:23 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 07:59:48 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-09 08:03:01 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-09-09 08:02:54 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-09-09 08:07:38 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-09-09 08:00:47 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-09 08:03:13 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-09 08:10:49 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-09 08:04:27 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-09 08:03:21 | Hanwella (Kelani Ganga) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 08:05:00 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 08:03:42 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:00:36 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:03:16 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:00:23 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:02:19 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:10:06 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:03:22 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:03:30 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-09 07:01:06 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:01:17 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:04:01 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:02:57 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:12:09 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:04:23 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:16:57 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:02:04 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:02:56 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:05:28 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:06:12 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:08:07 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:01:35 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:08:23 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:00:36 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:06:23 | Rathnapura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-09-09 08:03:37 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.024 |  |
| 2026-09-09 08:03:14 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | -0.040 |  |
| 2026-09-09 08:04:46 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.044 |  |
| 2026-09-09 08:01:19 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.052 |  |
| 2026-09-09 08:01:22 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)