# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_09:06:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **226,801 measurements** from **39** stations.
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
| 2026-08-07 09:06:33 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:05:59 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-07 09:05:46 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-07 09:05:14 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:05:01 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:04:47 | Peradeniya (Mahaweli Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:04:26 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:04:20 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 09:03:56 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:03:47 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | -0.070 |  |
| 2026-08-07 09:03:45 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 09:03:27 | Glencourse (Kelani Ganga) | 11.29 | 🟢 Normal | -0.084 |  |
| 2026-08-07 09:03:21 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-08-07 09:03:16 | Ellagawa (Kalu Ganga) | 5.93 | 🟢 Normal | -0.019 |  |
| 2026-08-07 09:03:09 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | -0.060 |  |
| 2026-08-07 09:02:54 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | -0.032 |  |
| 2026-08-07 09:02:51 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:02:50 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:02:47 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 09:02:35 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 09:02:11 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:02:08 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.061 |  |
| 2026-08-07 09:01:55 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:01:54 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:01:53 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-07 09:01:46 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.029 |  |
| 2026-08-07 09:01:21 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-08-07 09:01:18 | Nawalapitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | -0.040 |  |
| 2026-08-07 09:01:10 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-08-07 09:00:58 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:00:26 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:00:11 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.010 |  |
| 2026-08-07 08:34:59 | Glencourse (Kelani Ganga) | 11.33 | 🟢 Normal | -0.084 |  |
| 2026-08-07 08:29:40 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-08-07 08:19:26 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-07 09:03:21 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-08-07 08:03:42 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-08-07 09:01:53 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-07 08:17:31 | Kithulgala (Kelani Ganga) | 2.53 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-07 09:05:46 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-07 09:05:59 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-07 08:02:27 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-07 09:04:20 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 09:02:47 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 09:02:35 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 09:03:45 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 09:03:09 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:01:54 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:03:56 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-07 08:17:29 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:02:51 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-08-07 08:19:26 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:05:14 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:02:11 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:01:55 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-07 08:02:49 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:02:50 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:05:01 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:00:58 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:04:47 | Peradeniya (Mahaweli Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:04:26 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-07 09:06:33 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-07 08:14:20 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.009 |  |
| 2026-08-07 09:00:11 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.010 |  |
| 2026-08-07 09:01:10 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-08-07 09:01:21 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-08-07 09:03:16 | Ellagawa (Kalu Ganga) | 5.93 | 🟢 Normal | -0.019 |  |
| 2026-08-07 09:01:46 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.029 |  |
| 2026-08-07 09:02:54 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | -0.032 |  |
| 2026-08-07 09:01:18 | Nawalapitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | -0.040 |  |
| 2026-08-07 09:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | -0.060 |  |
| 2026-08-07 09:02:08 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.061 |  |
| 2026-08-07 09:03:47 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | -0.070 |  |
| 2026-08-07 09:03:27 | Glencourse (Kelani Ganga) | 11.29 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)