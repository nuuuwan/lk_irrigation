# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--23_03:27:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,233 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 03:27:42 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-11-23 03:27:26 | Panadugama (Nilwala Ganga) | 4.20 | 🟢 Normal | -0.084 |  |
| 2026-11-23 03:24:44 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:24:04 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-23 03:12:28 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.093 |  |
| 2026-11-23 03:12:16 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:09:38 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:08:23 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-23 03:07:54 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2026-11-23 03:07:37 | Moraketiya (Walawe Ganga) | 2.65 | 🟢 Normal | -0.032 |  |
| 2026-11-23 03:06:35 | Rathnapura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.106 |  |
| 2026-11-23 03:06:22 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.032 |  |
| 2026-11-23 03:06:14 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:05:22 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:05:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-23 03:04:15 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:03:50 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:03:46 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:03:39 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-11-23 03:03:39 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-11-23 03:02:59 | Thawalama (Gin Ganga) | 2.87 | 🟢 Normal | -0.082 |  |
| 2026-11-23 03:02:54 | Glencourse (Kelani Ganga) | 9.59 | 🟢 Normal | -0.010 |  |
| 2026-11-23 03:02:49 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.175 |  |
| 2026-11-23 03:02:39 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 03:02:24 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:02:13 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-23 03:01:54 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:01:44 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 03:01:33 | Moragaswewa (Deduru Oya) | 2.15 | 🟢 Normal | -0.061 |  |
| 2026-11-23 03:01:28 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:01:13 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-23 03:00:21 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-11-23 02:55:15 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.106 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 03:07:54 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2026-11-23 03:01:13 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-23 03:05:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-23 02:28:32 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-23 03:08:23 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-22 18:00:53 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-23 03:01:44 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 03:02:39 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 03:24:04 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-23 03:09:38 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:01:28 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:01:54 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:24:44 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:00:10 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:12:16 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:03:46 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:02:24 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 01:02:26 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:03:50 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:04:15 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-22 18:02:00 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:05:22 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:06:14 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-23 03:27:42 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-11-23 03:02:54 | Glencourse (Kelani Ganga) | 9.59 | 🟢 Normal | -0.010 |  |
| 2026-11-23 03:03:39 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-11-23 03:02:13 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-23 03:03:39 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-11-23 03:00:21 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-23 03:07:37 | Moraketiya (Walawe Ganga) | 2.65 | 🟢 Normal | -0.032 |  |
| 2026-11-23 03:06:22 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.032 |  |
| 2026-11-23 03:01:33 | Moragaswewa (Deduru Oya) | 2.15 | 🟢 Normal | -0.061 |  |
| 2026-11-23 03:02:59 | Thawalama (Gin Ganga) | 2.87 | 🟢 Normal | -0.082 |  |
| 2026-11-23 03:27:26 | Panadugama (Nilwala Ganga) | 4.20 | 🟢 Normal | -0.084 |  |
| 2026-11-23 02:02:03 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.087 |  |
| 2026-11-23 03:12:28 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.093 |  |
| 2026-11-23 03:06:35 | Rathnapura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.106 |  |
| 2026-11-23 03:02:49 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.175 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)