# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--30_18:08:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **247,374 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-30 18:08:17 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.025 |  |
| 2026-08-30 18:07:34 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:06:08 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:05:25 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:05:06 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:04:47 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:04:24 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:04:23 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-30 18:04:05 | Hanwella (Kelani Ganga) | 1.39 | 🟢 Normal | -0.039 |  |
| 2026-08-30 18:04:01 | Weraganthota (Mahaweli Ganga) | -3.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-30 18:03:53 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.092 |  |
| 2026-08-30 18:03:18 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:03:17 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:03:01 | Ellagawa (Kalu Ganga) | 4.96 | 🟢 Normal | -0.020 |  |
| 2026-08-30 18:02:55 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:02:51 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-30 18:02:28 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:02:21 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | -0.012 |  |
| 2026-08-30 18:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:02:14 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:02:13 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-30 18:01:59 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:01:58 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:01:57 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-08-30 18:01:38 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:01:33 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.071 |  |
| 2026-08-30 18:01:26 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.053 |  |
| 2026-08-30 18:01:24 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | -0.070 |  |
| 2026-08-30 18:00:54 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:00:40 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-30 18:00:36 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:00:25 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:00:24 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:00:13 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:00:10 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-30 17:47:38 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-30 17:46:55 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-30 17:23:23 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-30 17:20:48 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-30 17:19:59 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.025 |  |
| 2026-08-30 17:19:28 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-30 18:01:57 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-08-30 18:04:23 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-30 18:00:40 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-30 18:02:51 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-30 18:02:13 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-30 18:04:01 | Weraganthota (Mahaweli Ganga) | -3.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-30 18:00:10 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:00:54 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:01:38 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:01:58 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:01:59 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:00:13 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-30 17:19:28 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:05:25 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:07:34 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:02:55 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:00:24 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:05:06 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:02:28 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:03:17 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:02:14 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:04:47 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:06:08 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:03:18 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:00:36 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-30 17:10:58 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:00:25 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:04:24 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-08-30 17:00:51 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-08-30 18:02:21 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | -0.012 |  |
| 2026-08-30 18:03:01 | Ellagawa (Kalu Ganga) | 4.96 | 🟢 Normal | -0.020 |  |
| 2026-08-30 18:08:17 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.025 |  |
| 2026-08-30 17:03:20 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | -0.035 |  |
| 2026-08-30 18:04:05 | Hanwella (Kelani Ganga) | 1.39 | 🟢 Normal | -0.039 |  |
| 2026-08-30 18:01:26 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.053 |  |
| 2026-08-30 18:01:24 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | -0.070 |  |
| 2026-08-30 18:01:33 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.071 |  |
| 2026-08-30 18:03:53 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)