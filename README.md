# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--31_07:14:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **247,833 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 07:14:23 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:12:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.82 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-31 07:11:56 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:10:58 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:10:28 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | -0.009 |  |
| 2026-08-31 07:10:13 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.067 |  |
| 2026-08-31 07:09:32 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.018 |  |
| 2026-08-31 07:08:22 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-08-31 07:08:17 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:07:07 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-08-31 07:07:06 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-08-31 07:07:04 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:05:39 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:05:39 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:05:29 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.148 |  |
| 2026-08-31 07:05:13 | Ellagawa (Kalu Ganga) | 4.82 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:04:58 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-31 07:04:45 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.038 |  |
| 2026-08-31 07:04:40 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:04:36 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:04:28 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.001 |  |
| 2026-08-31 07:04:18 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:04:14 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:03:46 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:03:45 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:03:39 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:03:25 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:02:51 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | -0.030 |  |
| 2026-08-31 07:02:45 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:02:32 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-08-31 07:02:26 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:02:16 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:01:55 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 07:01:51 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:01:45 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:01:41 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:01:39 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:01:24 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-08-31 07:00:52 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-08-31 07:00:50 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.052 |  |
| 2026-08-31 07:00:21 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.036 |  |
| 2026-08-31 07:00:16 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 07:07:07 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-08-31 07:00:52 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-08-31 07:08:22 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-08-31 07:12:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.82 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-31 07:04:58 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-31 07:00:16 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 07:01:55 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 07:04:28 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.001 |  |
| 2026-08-31 07:01:51 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:11:56 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:04:18 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:03:25 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:03:46 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:03:45 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:10:58 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:02:26 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:03:39 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:05:13 | Ellagawa (Kalu Ganga) | 4.82 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:05:39 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:01:45 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:14:23 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:01:41 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:04:40 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:04:36 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:04:14 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:02:16 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:05:39 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:08:17 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:02:45 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 07:10:28 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | -0.009 |  |
| 2026-08-31 07:02:32 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-08-31 07:09:32 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.018 |  |
| 2026-08-31 07:02:51 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | -0.030 |  |
| 2026-08-31 07:00:21 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.036 |  |
| 2026-08-31 07:04:45 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.038 |  |
| 2026-08-31 07:01:24 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-08-31 07:00:50 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.052 |  |
| 2026-08-31 07:10:13 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.067 |  |
| 2026-08-31 07:05:29 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.148 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)