# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--19_17:19:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **265,317 measurements** from **39** stations.
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
| 2026-09-19 17:19:54 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.008 |  |
| 2026-09-19 17:10:23 | Magura (Kalu Ganga) | 3.44 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-19 17:08:45 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:08:10 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:07:44 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-09-19 17:07:14 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:06:41 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-19 17:05:39 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-09-19 17:05:36 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 17:05:31 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:04:51 | Baddegama (Gin Ganga) | 2.42 | 🟢 Normal | -0.032 |  |
| 2026-09-19 17:04:46 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:04:42 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-19 17:04:29 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:03:55 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2026-09-19 17:03:48 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | -0.030 |  |
| 2026-09-19 17:03:44 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.064 |  |
| 2026-09-19 17:03:43 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:03:18 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:03:17 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:03:12 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:02:36 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-09-19 17:02:33 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:02:28 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:02:05 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | -0.080 |  |
| 2026-09-19 17:02:01 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:01:56 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:01:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:01:32 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-09-19 17:01:24 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.010 |  |
| 2026-09-19 17:01:19 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.056 |  |
| 2026-09-19 17:01:19 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-19 17:01:13 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-09-19 17:01:03 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-19 17:00:39 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 17:03:55 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2026-09-19 17:01:13 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-09-19 17:06:41 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-19 17:10:23 | Magura (Kalu Ganga) | 3.44 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-19 17:05:39 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-09-19 17:01:19 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-19 17:04:42 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-19 17:01:03 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-19 17:05:36 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 17:03:17 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:03:18 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:08:10 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:01:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:00:39 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:04:29 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:03:12 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:08:45 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:03:43 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-19 16:05:30 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:02:33 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:07:14 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:04:46 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:05:31 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:02:01 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:01:56 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 17:19:54 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.008 |  |
| 2026-09-19 17:07:44 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-09-19 17:02:36 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-09-19 17:01:24 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.010 |  |
| 2026-09-19 17:01:32 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-09-19 16:37:58 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.012 |  |
| 2026-09-19 17:03:48 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | -0.030 |  |
| 2026-09-19 17:04:51 | Baddegama (Gin Ganga) | 2.42 | 🟢 Normal | -0.032 |  |
| 2026-09-19 13:07:37 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | -0.037 |  |
| 2026-09-19 17:01:19 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.056 |  |
| 2026-09-19 17:03:44 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.064 |  |
| 2026-09-19 17:02:05 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)