# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_04:50:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **235,596 measurements** from **39** stations.
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
| 2026-08-17 04:50:04 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:23:33 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:13:25 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:12:47 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-17 04:10:10 | Glencourse (Kelani Ganga) | 9.82 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:09:11 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-17 04:08:08 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-08-17 04:07:59 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-08-17 04:07:46 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-08-17 04:07:23 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.012 |  |
| 2026-08-17 04:07:02 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:06:37 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:05:36 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-08-17 04:05:25 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:05:21 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 04:05:01 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:05:01 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:04:53 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:04:45 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-17 04:02:59 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:02:59 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:02:58 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-08-17 04:02:55 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 04:02:44 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:02:40 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 04:02:25 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:02:19 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:01:54 | Peradeniya (Mahaweli Ganga) | 2.71 | 🟢 Normal | -0.140 |  |
| 2026-08-17 04:01:39 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:01:36 | Ellagawa (Kalu Ganga) | 5.04 | 🟢 Normal | -0.010 |  |
| 2026-08-17 04:01:22 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:01:14 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:00:42 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:00:42 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-17 04:07:46 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-08-17 04:07:59 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-08-17 04:04:45 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-17 04:12:47 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-17 04:02:55 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 04:02:40 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 03:01:23 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-17 04:05:21 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 04:09:11 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-17 04:01:39 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:01:14 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:23:33 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:00:42 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-17 02:01:46 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:02:44 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:05:25 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:02:57 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:02:59 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:50:04 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:05:01 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:13:25 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:01:22 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:10:10 | Glencourse (Kelani Ganga) | 9.82 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:07:02 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:02:59 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:04:53 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:02:25 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:10:59 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:05:01 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:02:19 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:06:37 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-17 04:01:36 | Ellagawa (Kalu Ganga) | 5.04 | 🟢 Normal | -0.010 |  |
| 2026-08-17 04:05:36 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-08-16 18:03:12 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.010 |  |
| 2026-08-17 03:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | -0.011 |  |
| 2026-08-17 04:07:23 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.012 |  |
| 2026-08-17 04:08:08 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-08-17 04:02:58 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-08-17 04:01:54 | Peradeniya (Mahaweli Ganga) | 2.71 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)