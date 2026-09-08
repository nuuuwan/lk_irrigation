# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--08_16:16:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **255,404 measurements** from **39** stations.
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
| 2026-09-08 16:16:32 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:12:06 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-08 16:10:18 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:08:59 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-08 16:08:53 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:07:13 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:07:02 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 16:06:02 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-08 16:05:31 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.047 |  |
| 2026-09-08 16:05:25 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:05:12 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-09-08 16:05:02 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:04:51 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | -0.030 |  |
| 2026-09-08 16:04:27 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:04:06 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:04:04 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:03:45 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:03:40 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-09-08 16:03:30 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 16:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 16:02:52 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:02:48 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:02:45 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.061 |  |
| 2026-09-08 16:02:36 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-08 16:02:28 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:02:25 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-09-08 16:02:25 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.040 |  |
| 2026-09-08 16:02:19 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:02:09 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:02:01 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.062 |  |
| 2026-09-08 16:01:57 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-09-08 16:01:54 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 16:01:49 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:01:35 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:01:20 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:01:14 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.022 |  |
| 2026-09-08 16:00:43 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:00:14 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:00:12 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.095 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-08 16:08:59 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-08 16:12:06 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-08 16:06:02 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-08 16:02:36 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-08 16:03:30 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 16:01:54 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 16:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 16:07:02 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 16:02:52 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:07:13 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:01:20 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:05:02 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:04:04 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:00:43 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:02:25 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:08:53 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:10:18 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:04:27 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:02:28 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:02:48 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:04:06 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:00:14 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:03:45 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:02:09 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:05:25 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:01:35 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:16:32 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:01:49 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-08 16:05:12 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-09-08 16:01:57 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-09-08 16:02:25 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-09-08 16:01:14 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.022 |  |
| 2026-09-08 16:04:51 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | -0.030 |  |
| 2026-09-08 16:03:40 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-09-08 16:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.040 |  |
| 2026-09-08 16:05:31 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.047 |  |
| 2026-09-08 16:02:45 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.061 |  |
| 2026-09-08 16:02:01 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.062 |  |
| 2026-09-08 16:00:12 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)