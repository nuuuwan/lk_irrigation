# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--06_05:12:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **226,185 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 05:12:42 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:11:56 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.018 |  |
| 2026-08-06 05:08:51 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.037 |  |
| 2026-08-06 05:07:58 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.019 |  |
| 2026-08-06 05:07:38 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:07:09 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:07:00 | Glencourse (Kelani Ganga) | 11.41 | 🟢 Normal | -0.029 |  |
| 2026-08-06 05:05:37 | Rathnapura (Kalu Ganga) | 2.71 | 🟢 Normal | -0.112 |  |
| 2026-08-06 05:05:31 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:05:30 | Peradeniya (Mahaweli Ganga) | 4.20 | 🟢 Normal | -0.062 |  |
| 2026-08-06 05:05:02 | Putupaula (Kalu Ganga) | 1.93 | 🟢 Normal | -0.005 |  |
| 2026-08-06 05:04:33 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-08-06 05:04:32 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:04:23 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-08-06 05:04:13 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:03:58 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:03:49 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:03:48 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:03:44 | Kithulgala (Kelani Ganga) | 2.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-06 05:03:35 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:03:35 | Nawalapitiya (Mahaweli Ganga) | 2.24 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-06 05:03:28 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-08-06 05:03:17 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-06 05:03:17 | Ellagawa (Kalu Ganga) | 7.98 | 🟢 Normal | -36.000 |  |
| 2026-08-06 05:03:15 | Ellagawa (Kalu Ganga) | 8.00 | 🟢 Normal | -36.000 |  |
| 2026-08-06 05:03:04 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:02:57 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-08-06 05:02:54 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:02:46 | Hanwella (Kelani Ganga) | 3.35 | 🟢 Normal | -0.071 |  |
| 2026-08-06 05:02:18 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-06 05:02:05 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:02:04 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:01:48 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:01:10 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:45:13 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:26:10 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.051 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 05:03:35 | Nawalapitiya (Mahaweli Ganga) | 2.24 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-06 05:03:17 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-06 05:02:18 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-06 05:03:44 | Kithulgala (Kelani Ganga) | 2.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-06 05:05:31 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:04:13 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:03:49 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:12:42 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:03:35 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:11:01 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:02:05 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:07:09 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:03:48 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:02:54 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:01:48 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:03:04 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:04:32 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:07:38 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:09:25 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:03:58 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-06 04:02:48 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:01:10 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:02:04 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 05:05:02 | Putupaula (Kalu Ganga) | 1.93 | 🟢 Normal | -0.005 |  |
| 2026-08-05 18:01:36 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | -0.010 |  |
| 2026-08-06 05:04:23 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-08-06 05:04:33 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-08-06 05:03:28 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-08-06 05:02:57 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-08-06 05:11:56 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.018 |  |
| 2026-08-06 05:07:58 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.019 |  |
| 2026-08-06 04:12:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | -0.026 |  |
| 2026-08-06 05:07:00 | Glencourse (Kelani Ganga) | 11.41 | 🟢 Normal | -0.029 |  |
| 2026-08-06 05:08:51 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.037 |  |
| 2026-08-06 04:26:10 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.051 |  |
| 2026-08-06 05:05:30 | Peradeniya (Mahaweli Ganga) | 4.20 | 🟢 Normal | -0.062 |  |
| 2026-08-06 05:02:46 | Hanwella (Kelani Ganga) | 3.35 | 🟢 Normal | -0.071 |  |
| 2026-08-06 05:05:37 | Rathnapura (Kalu Ganga) | 2.71 | 🟢 Normal | -0.112 |  |
| 2026-08-06 05:03:17 | Ellagawa (Kalu Ganga) | 7.98 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)