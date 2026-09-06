# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--07_02:02:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **253,932 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-07 02:02:50 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-09-07 02:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-07 02:02:39 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | -0.010 |  |
| 2026-09-07 02:02:37 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-07 02:02:26 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 02:02:11 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-07 02:01:58 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-09-07 02:01:55 | Moraketiya (Walawe Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-07 02:01:50 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.173 |  |
| 2026-09-07 02:01:35 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.063 |  |
| 2026-09-07 02:01:19 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-07 02:01:09 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-07 02:01:00 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-07 02:00:51 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-07 02:00:44 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 02:00:40 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-09-07 02:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-07 01:41:03 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.173 |  |
| 2026-09-07 01:22:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-07 02:02:50 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-09-07 02:00:51 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-07 02:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-07 02:01:09 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-07 01:06:39 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-07 01:04:32 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 02:00:44 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 01:06:57 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-07 02:01:19 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-07 02:02:26 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 02:01:00 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-07 02:00:33 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-07 00:04:12 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-07 02:02:11 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-07 01:00:48 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-06 18:06:01 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-07 02:02:37 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-07 02:01:58 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-09-07 02:01:55 | Moraketiya (Walawe Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-07 01:02:25 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-07 01:08:28 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-07 01:02:06 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-07 00:01:59 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-06 18:01:51 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-07 02:00:40 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-09-07 01:01:40 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-07 01:02:52 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-07 02:02:39 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | -0.010 |  |
| 2026-09-07 00:02:54 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-09-07 00:01:10 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-09-07 01:01:45 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-09-07 01:01:23 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-09-07 01:10:36 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | -0.018 |  |
| 2026-09-07 01:09:06 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.029 |  |
| 2026-09-07 01:11:18 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2026-09-07 02:01:35 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.063 |  |
| 2026-09-07 00:03:53 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.104 |  |
| 2026-09-06 18:00:09 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.114 |  |
| 2026-09-07 02:01:50 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.173 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)