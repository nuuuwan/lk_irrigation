# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--17_21:11:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **318,608 measurements** from **39** stations.
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
| 2026-11-17 21:11:42 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:10:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.49 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-17 21:08:11 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 21:07:54 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-17 21:07:33 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-11-17 21:07:28 | Panadugama (Nilwala Ganga) | 3.71 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:07:16 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:06:38 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-17 21:05:48 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:05:29 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.022 |  |
| 2026-11-17 21:05:21 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:04:33 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:04:25 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:04:11 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-11-17 21:03:51 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:03:47 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-11-17 21:03:41 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.032 |  |
| 2026-11-17 21:03:20 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:02:43 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:02:42 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-17 21:02:40 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:02:38 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.020 |  |
| 2026-11-17 21:02:21 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-17 21:02:20 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:02:04 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:01:38 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-17 21:01:36 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 21:01:33 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.012 |  |
| 2026-11-17 21:01:30 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:01:28 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:01:23 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:01:20 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-11-17 21:01:15 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:00:10 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 21:02:42 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-17 21:02:21 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-17 21:07:54 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-17 21:01:38 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-17 21:00:10 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-17 21:01:36 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 21:08:11 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 21:06:38 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-17 21:10:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.49 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-17 18:03:49 | Weraganthota (Mahaweli Ganga) | -2.19 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:01:28 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:02:20 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:04:25 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:02:43 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:03:41 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:05:21 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:02:04 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:07:16 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:07:28 | Panadugama (Nilwala Ganga) | 3.71 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:11:42 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:01:30 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:01:23 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:03:51 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:03:20 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:02:40 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:01:44 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:01:15 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:05:48 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:04:33 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-17 21:07:33 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-11-17 20:10:08 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-11-17 21:04:11 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-11-17 21:03:47 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-11-17 21:01:20 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-11-17 20:15:39 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-11-17 21:01:33 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.012 |  |
| 2026-11-17 21:02:38 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.020 |  |
| 2026-11-17 21:05:29 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.022 |  |
| 2026-11-17 21:03:41 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.032 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)