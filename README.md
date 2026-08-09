# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_21:09:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,088 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 21:09:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-09 21:09:26 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:09:16 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-09 21:09:05 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 21:08:30 | Glencourse (Kelani Ganga) | 10.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 21:05:39 | Deraniyagala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.090 |  |
| 2026-08-09 21:05:13 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:04:42 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:04:40 | Kithulgala (Kelani Ganga) | 2.38 | 🟢 Normal | 0.303 | 🔺 Rising |
| 2026-08-09 21:04:40 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.022 |  |
| 2026-08-09 21:04:07 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-08-09 21:03:29 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:03:19 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:03:09 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 21:03:07 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-08-09 21:03:05 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:03:01 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:02:51 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:02:39 | Ellagawa (Kalu Ganga) | 5.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-09 21:02:35 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:02:24 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | -0.011 |  |
| 2026-08-09 21:02:10 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-08-09 21:02:09 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:02:07 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:02:01 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:01:54 | Peradeniya (Mahaweli Ganga) | 3.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 21:01:48 | Hanwella (Kelani Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:01:45 | Nawalapitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | -0.059 |  |
| 2026-08-09 21:01:33 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-09 21:01:26 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:01:05 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:01:02 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:00:55 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:00:35 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:00:11 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 21:04:40 | Kithulgala (Kelani Ganga) | 2.38 | 🟢 Normal | 0.303 | 🔺 Rising |
| 2026-08-09 20:19:54 | Rathnapura (Kalu Ganga) | 3.25 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-08-09 21:09:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-09 21:03:07 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-08-09 21:01:33 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-09 21:02:39 | Ellagawa (Kalu Ganga) | 5.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-09 21:01:54 | Peradeniya (Mahaweli Ganga) | 3.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 21:09:16 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-09 21:03:09 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 18:01:36 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 21:08:30 | Glencourse (Kelani Ganga) | 10.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 21:09:05 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 21:00:35 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:02:07 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:02:01 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:02:51 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:00:55 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:03:43 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:01:48 | Hanwella (Kelani Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:09:26 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:03:01 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:03:29 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:01:05 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:04:42 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:02:09 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:01:02 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:05:13 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:01:26 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:03:05 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:02:35 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:00:11 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:03:19 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-09 21:02:10 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-08-09 21:04:07 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-08-09 21:02:24 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | -0.011 |  |
| 2026-08-09 21:04:40 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.022 |  |
| 2026-08-09 18:02:25 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.040 |  |
| 2026-08-09 21:01:45 | Nawalapitiya (Mahaweli Ganga) | 2.19 | 🟢 Normal | -0.059 |  |
| 2026-08-09 21:05:39 | Deraniyagala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)