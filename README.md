# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_00:04:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **259,275 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 00:04:50 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:04:35 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:04:25 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:04:16 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-13 00:03:49 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:03:20 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.063 |  |
| 2026-09-13 00:03:12 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-13 00:02:52 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:02:40 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.058 |  |
| 2026-09-13 00:02:37 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 00:02:29 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.011 |  |
| 2026-09-13 00:02:28 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:02:25 | Manampitiya (Mahaweli Ganga) | -0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:02:16 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-09-13 00:02:12 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:02:09 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.042 |  |
| 2026-09-13 00:01:58 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:01:52 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.011 |  |
| 2026-09-13 00:01:49 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:01:44 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.025 |  |
| 2026-09-13 00:01:39 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:01:32 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:01:08 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:00:57 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-12 23:32:36 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 23:24:10 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-12 23:07:11 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-09-12 21:58:58 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-13 00:03:12 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-12 23:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-13 00:04:16 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-12 23:07:09 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-13 00:02:37 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-12 23:11:10 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-12 18:00:50 | Weraganthota (Mahaweli Ganga) | -3.57 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:01:08 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:03:49 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:04:35 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 23:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:01:39 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:02:12 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:01:58 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-12 18:03:01 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:04:50 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:03:09 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:01:32 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | 0.000 |  |
| 2026-09-12 23:06:17 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:02:28 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:04:25 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:00:57 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-12 23:03:11 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:02:52 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 23:24:10 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:02:25 | Manampitiya (Mahaweli Ganga) | -0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-12 23:04:02 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-12 18:00:45 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:01:49 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:02:16 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-09-13 00:02:29 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.011 |  |
| 2026-09-13 00:01:52 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.011 |  |
| 2026-09-12 23:05:24 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-09-13 00:01:44 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.025 |  |
| 2026-09-13 00:02:09 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.042 |  |
| 2026-09-13 00:02:40 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.058 |  |
| 2026-09-13 00:03:20 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)