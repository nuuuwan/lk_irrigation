# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--19_17:24:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **320,242 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 17:24:53 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:19:33 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:11:14 | Ellagawa (Kalu Ganga) | 4.82 | 🟢 Normal | -0.009 |  |
| 2026-11-19 17:10:30 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:09:15 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-19 17:07:42 | Glencourse (Kelani Ganga) | 9.49 | 🟢 Normal | -0.060 |  |
| 2026-11-19 17:07:04 | Moraketiya (Walawe Ganga) | 1.87 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-19 17:06:50 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-11-19 17:06:16 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:06:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.99 | 🟢 Normal | -0.028 |  |
| 2026-11-19 17:05:52 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-11-19 17:05:28 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:05:24 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.021 |  |
| 2026-11-19 17:05:02 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:04:42 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | -0.010 |  |
| 2026-11-19 17:04:29 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:04:22 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:04:18 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-11-19 17:03:57 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:03:48 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:03:47 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:03:46 | Hanwella (Kelani Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-11-19 17:03:38 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:03:38 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:03:17 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:03:13 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:03:12 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-11-19 17:03:11 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-19 17:03:00 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-19 17:02:52 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-19 17:02:47 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:02:38 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:02:31 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:02:29 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-19 17:02:01 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:01:39 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:01:23 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-19 17:01:23 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:01:06 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:01:05 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 17:09:15 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-19 17:02:29 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-19 17:07:04 | Moraketiya (Walawe Ganga) | 1.87 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-19 17:03:11 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-19 17:01:23 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-19 17:02:52 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-19 17:05:28 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:03:38 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:01:23 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:03:48 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:01:39 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:03:57 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:02:31 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:03:38 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:03:17 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:04:29 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:04:22 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:10:30 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:03:13 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:03:47 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:02:38 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:19:33 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:05:02 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:02:47 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:24:53 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:01:06 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:02:01 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-19 17:11:14 | Ellagawa (Kalu Ganga) | 4.82 | 🟢 Normal | -0.009 |  |
| 2026-11-19 17:05:52 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-11-19 17:04:18 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-11-19 17:03:12 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-11-19 17:03:00 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-19 17:03:46 | Hanwella (Kelani Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-11-19 17:04:42 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | -0.010 |  |
| 2026-11-19 17:06:50 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-11-19 17:05:24 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.021 |  |
| 2026-11-19 17:06:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.99 | 🟢 Normal | -0.028 |  |
| 2026-11-19 17:07:42 | Glencourse (Kelani Ganga) | 9.49 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)