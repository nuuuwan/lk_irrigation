# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--19_22:29:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **265,509 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 22:29:04 | Magura (Kalu Ganga) | 3.66 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-19 22:14:54 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-19 22:13:01 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:08:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-19 22:08:35 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:08:21 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.074 |  |
| 2026-09-19 22:07:33 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:06:28 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-09-19 22:06:16 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:05:25 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-09-19 22:05:20 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:05:02 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:04:20 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:04:18 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:04:07 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-09-19 22:04:05 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-09-19 22:03:50 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | -0.022 |  |
| 2026-09-19 22:03:48 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-09-19 22:03:47 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-09-19 22:03:25 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-19 22:03:10 | Panadugama (Nilwala Ganga) | 2.94 | 🟢 Normal | -0.011 |  |
| 2026-09-19 22:03:09 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 22:03:04 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-09-19 22:03:02 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-19 22:02:59 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:02:52 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:02:30 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:02:28 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:02:23 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:02:19 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-09-19 22:02:10 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:01:43 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:01:42 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:01:33 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:01:15 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-19 22:00:46 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:00:25 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 22:03:48 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-09-19 22:03:25 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-19 22:29:04 | Magura (Kalu Ganga) | 3.66 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-19 22:01:15 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-19 22:03:02 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-19 22:00:25 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 22:03:09 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 22:14:54 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-19 22:08:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-19 22:01:43 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:02:23 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:00:46 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:01:42 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:06:16 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:07:33 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-19 18:01:55 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:02:30 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:02:59 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:04:20 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:05:02 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:02:52 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:04:18 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:01:33 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-19 18:01:39 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:13:01 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:08:35 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:05:20 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-19 22:02:10 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-19 18:01:44 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.010 |  |
| 2026-09-19 22:04:07 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-09-19 22:04:05 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-09-19 22:03:04 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-09-19 22:03:10 | Panadugama (Nilwala Ganga) | 2.94 | 🟢 Normal | -0.011 |  |
| 2026-09-19 22:03:47 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-09-19 22:02:19 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-09-19 22:06:28 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-09-19 22:03:50 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | -0.022 |  |
| 2026-09-19 22:05:25 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-09-19 22:08:21 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)