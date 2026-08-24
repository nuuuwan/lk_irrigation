# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_04:30:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **242,734 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 04:30:25 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:26:28 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-25 04:23:54 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:22:06 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-25 04:17:11 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:15:54 | Glencourse (Kelani Ganga) | 9.66 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-25 04:12:08 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-25 04:10:50 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:10:26 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:07:53 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:05:30 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-25 04:05:24 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:05:18 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.021 |  |
| 2026-08-25 04:05:15 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:05:01 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-08-25 04:04:32 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:03:46 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:03:35 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-08-25 04:03:32 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 04:03:19 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:03:14 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:03:03 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:02:45 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 04:02:20 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.071 |  |
| 2026-08-25 04:02:15 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | -0.021 |  |
| 2026-08-25 04:02:08 | Hanwella (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:01:48 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | -0.005 |  |
| 2026-08-25 04:01:44 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-25 04:01:36 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-25 04:01:22 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-25 04:01:22 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:01:19 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:00:45 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:00:24 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 04:03:35 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-08-25 04:15:54 | Glencourse (Kelani Ganga) | 9.66 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-25 04:01:44 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-25 04:01:22 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-25 04:22:06 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-25 04:05:30 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-25 04:12:08 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-25 04:26:28 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-25 00:18:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-25 04:03:32 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 04:02:45 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 04:00:24 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:30:25 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:04:32 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:05:15 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 18:02:21 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:03:46 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:03:19 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:10:50 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:02:08 | Hanwella (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:07:53 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:05:24 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:23:54 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-08-25 00:00:24 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 00:16:29 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:00:45 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:01:22 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:03:14 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:03:03 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:17:11 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:01:19 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:01:48 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | -0.005 |  |
| 2026-08-24 18:01:27 | Thanthirimale (Malwathu Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-08-25 04:05:01 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-08-25 04:02:15 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | -0.021 |  |
| 2026-08-25 04:05:18 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.021 |  |
| 2026-08-25 00:03:25 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.031 |  |
| 2026-08-25 04:02:20 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.071 |  |
| 2026-08-24 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)