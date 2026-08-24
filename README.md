# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_17:19:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **242,365 measurements** from **39** stations.
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
| 2026-08-24 17:19:29 | Manampitiya (Mahaweli Ganga) | -0.31 | 🟢 Normal | -0.009 |  |
| 2026-08-24 17:19:11 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.056 |  |
| 2026-08-24 17:12:59 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 17:11:23 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:11:03 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:09:41 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:09:29 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:07:03 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:06:59 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 17:06:16 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-24 17:05:36 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-24 17:05:28 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.053 |  |
| 2026-08-24 17:05:02 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-24 17:04:58 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:04:35 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:04:30 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-24 17:04:23 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-24 17:04:09 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-24 17:03:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.020 |  |
| 2026-08-24 17:03:31 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:03:28 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:03:26 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:03:24 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:03:14 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-08-24 17:03:05 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 17:03:01 | Hanwella (Kelani Ganga) | 1.09 | 🟢 Normal | -0.021 |  |
| 2026-08-24 17:02:42 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:02:39 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:02:39 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 17:02:25 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-08-24 17:02:16 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:02:05 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:01:45 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.063 |  |
| 2026-08-24 17:01:42 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:01:17 | Thanthirimale (Malwathu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:01:12 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:00:37 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:00:35 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | -0.169 |  |
| 2026-08-24 17:00:11 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-24 17:04:23 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-24 17:06:16 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-24 17:05:36 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-24 17:04:09 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-24 17:04:30 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-24 17:05:02 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-24 17:02:39 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 17:06:59 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 17:03:05 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 17:12:59 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 17:02:39 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:00:37 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:02:05 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:03:28 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:04:35 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:01:12 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:03:26 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:02:42 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:00:11 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:04:58 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:11:23 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:03:31 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:11:03 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:07:03 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:09:29 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:01:17 | Thanthirimale (Malwathu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:02:16 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:09:41 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:01:42 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-24 17:19:29 | Manampitiya (Mahaweli Ganga) | -0.31 | 🟢 Normal | -0.009 |  |
| 2026-08-24 17:03:14 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-08-24 16:00:39 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-08-24 17:02:25 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-08-24 17:03:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.020 |  |
| 2026-08-24 17:03:01 | Hanwella (Kelani Ganga) | 1.09 | 🟢 Normal | -0.021 |  |
| 2026-08-24 17:05:28 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.053 |  |
| 2026-08-24 17:19:11 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.056 |  |
| 2026-08-24 17:01:45 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.063 |  |
| 2026-08-24 17:00:35 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | -0.169 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)