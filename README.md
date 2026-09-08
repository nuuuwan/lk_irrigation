# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--08_19:15:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **255,522 measurements** from **39** stations.
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
| 2026-09-08 19:15:34 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.032 |  |
| 2026-09-08 19:13:20 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-09-08 19:11:58 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:10:26 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-08 19:09:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.054 |  |
| 2026-09-08 19:09:37 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:08:25 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.071 |  |
| 2026-09-08 19:07:16 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-09-08 19:05:49 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-08 19:05:33 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:05:17 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 19:04:52 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:04:29 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:04:28 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:04:25 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:03:58 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.030 |  |
| 2026-09-08 19:03:51 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-09-08 19:03:48 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | -0.021 |  |
| 2026-09-08 19:03:43 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.055 |  |
| 2026-09-08 19:02:55 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-09-08 19:02:50 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:02:49 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-08 19:02:43 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-08 19:02:42 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-08 19:02:41 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:02:37 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-09-08 19:02:34 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:02:17 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-09-08 19:01:59 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:01:41 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:01:32 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:01:23 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:01:07 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:01:00 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 19:00:59 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:00:48 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-08 19:07:16 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.203 | 🔺 Rising |
| 2026-09-08 19:02:55 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-09-08 19:02:37 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-09-08 19:13:20 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-09-08 19:02:49 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-08 19:02:42 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-08 19:02:43 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-08 19:05:49 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-08 19:01:00 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 19:05:17 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 19:10:26 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-08 19:00:59 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:01:07 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:01:59 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:02:41 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:02:34 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:00:48 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:05:02 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:09:37 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:01:41 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:04:28 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:04:29 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:02:50 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:04:52 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:04:25 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:05:33 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:00:29 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:11:58 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:01:23 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:01:32 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-08 19:03:51 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-09-08 19:02:17 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-09-08 19:03:48 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | -0.021 |  |
| 2026-09-08 19:03:58 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.030 |  |
| 2026-09-08 19:15:34 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.032 |  |
| 2026-09-08 18:00:11 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.034 |  |
| 2026-09-08 19:09:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.054 |  |
| 2026-09-08 19:03:43 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.055 |  |
| 2026-09-08 19:08:25 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)