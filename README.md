# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--01_14:07:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **248,990 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-01 14:07:29 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-01 14:06:31 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:05:23 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 14:05:22 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-09-01 14:05:09 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.034 |  |
| 2026-09-01 14:04:58 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-01 14:04:48 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-01 14:04:46 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:04:45 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:04:38 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-01 14:04:18 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.020 |  |
| 2026-09-01 14:04:17 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:03:48 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:03:25 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.021 |  |
| 2026-09-01 14:03:06 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-09-01 14:03:05 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-01 14:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.13 | 🟢 Normal | -0.069 |  |
| 2026-09-01 14:02:55 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:02:48 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:02:47 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:02:43 | Manampitiya (Mahaweli Ganga) | -0.62 | 🟢 Normal | -0.010 |  |
| 2026-09-01 14:02:41 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:02:34 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-01 14:02:32 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:02:29 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:02:14 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:02:08 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-09-01 14:01:58 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-09-01 14:01:57 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:01:43 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:01:40 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:01:40 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:01:21 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.020 |  |
| 2026-09-01 14:01:11 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:01:07 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:01:03 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:00:50 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:00:48 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-01 14:01:58 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-09-01 14:04:38 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-01 14:03:05 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-01 14:04:58 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-01 14:04:48 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-01 14:07:29 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-01 14:05:23 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 14:01:07 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:01:40 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:00:48 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:04:46 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:02:41 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:01:40 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:04:17 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:01:03 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:02:14 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:02:55 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:02:32 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-01 11:02:11 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:02:48 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:01:11 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:01:43 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:01:57 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:02:47 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:03:48 | Rathnapura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:00:50 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:04:45 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:06:31 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:02:29 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-01 14:05:22 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-09-01 14:02:08 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-09-01 14:02:43 | Manampitiya (Mahaweli Ganga) | -0.62 | 🟢 Normal | -0.010 |  |
| 2026-09-01 14:03:06 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-09-01 14:02:34 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-01 14:04:18 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.020 |  |
| 2026-09-01 14:01:21 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.020 |  |
| 2026-09-01 14:03:25 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.021 |  |
| 2026-09-01 14:05:09 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.034 |  |
| 2026-09-01 14:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.13 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)