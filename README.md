# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_19:21:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **242,442 measurements** from **39** stations.
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
| 2026-08-24 19:21:18 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 1.857 | 🔺 Rising |
| 2026-08-24 19:19:25 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.024 |  |
| 2026-08-24 19:18:01 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.016 |  |
| 2026-08-24 19:12:45 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.025 |  |
| 2026-08-24 19:10:39 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | -0.009 |  |
| 2026-08-24 19:10:25 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-24 19:09:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-24 19:08:11 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.019 |  |
| 2026-08-24 19:07:42 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:07:23 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:04:23 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:04:03 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 19:04:02 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 19:04:01 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:03:46 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.236 | 🔺 Rising |
| 2026-08-24 19:03:46 | Glencourse (Kelani Ganga) | 9.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-24 19:03:44 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:03:40 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:03:28 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:02:59 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-08-24 19:02:37 | Hanwella (Kelani Ganga) | 1.04 | 🟢 Normal | -0.030 |  |
| 2026-08-24 19:02:24 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-08-24 19:02:24 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-08-24 19:02:16 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:02:16 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:02:16 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-24 19:02:00 | Moragaswewa (Deduru Oya) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 19:01:51 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:01:43 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:01:25 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.031 |  |
| 2026-08-24 19:01:12 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:01:12 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:01:11 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:01:10 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:01:09 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:00:49 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-08-24 19:00:45 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:00:35 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:00:11 | Horowpothana (Yan Oya) | 1.97 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-24 19:21:18 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 1.857 | 🔺 Rising |
| 2026-08-24 19:03:46 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | 0.236 | 🔺 Rising |
| 2026-08-24 19:02:24 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-08-24 19:00:11 | Horowpothana (Yan Oya) | 1.97 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-24 19:03:46 | Glencourse (Kelani Ganga) | 9.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-24 19:09:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-24 19:02:16 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-24 19:02:00 | Moragaswewa (Deduru Oya) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 19:04:02 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 19:04:03 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 19:10:25 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-24 19:03:28 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:01:51 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:01:43 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:03:40 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 18:02:21 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:07:42 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:00:35 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:04:23 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:02:16 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:02:16 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:07:23 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:00:45 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:03:44 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:04:01 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:01:12 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:01:12 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:10:39 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | -0.009 |  |
| 2026-08-24 18:01:27 | Thanthirimale (Malwathu Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-08-24 19:00:49 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-08-24 19:02:24 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-08-24 19:18:01 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.016 |  |
| 2026-08-24 19:08:11 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.019 |  |
| 2026-08-24 19:02:59 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-08-24 19:19:25 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.024 |  |
| 2026-08-24 19:12:45 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.025 |  |
| 2026-08-24 19:02:37 | Hanwella (Kelani Ganga) | 1.04 | 🟢 Normal | -0.030 |  |
| 2026-08-24 19:01:25 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.031 |  |
| 2026-08-24 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)