# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--19_07:27:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **319,850 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 07:27:52 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:21:02 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:20:13 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:12:52 | Panadugama (Nilwala Ganga) | 3.41 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:11:13 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:09:37 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:08:17 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.246 |  |
| 2026-11-19 07:07:09 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:07:02 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | -0.057 |  |
| 2026-11-19 07:05:43 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.059 |  |
| 2026-11-19 07:05:39 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:05:33 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-19 07:05:24 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:04:57 | Moraketiya (Walawe Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:04:54 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:04:36 | Glencourse (Kelani Ganga) | 9.77 | 🟢 Normal | -0.048 |  |
| 2026-11-19 07:04:36 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-19 07:04:29 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:03:45 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-19 07:03:35 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:03:27 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-11-19 07:03:24 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:03:17 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-19 07:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-19 07:03:11 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-11-19 07:03:05 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:03:01 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-19 07:02:55 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:02:37 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-19 07:02:24 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-11-19 07:02:23 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:02:19 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:01:56 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:01:50 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:01:28 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-19 07:01:11 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:00:30 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:00:20 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.056 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 07:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-19 07:03:17 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-19 07:03:45 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-19 07:03:01 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-19 07:05:33 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-19 07:02:23 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:01:50 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:20:13 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:00:30 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:02:55 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:01:11 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:05:39 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:11:13 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:00:19 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:03:24 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:03:35 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:04:29 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:12:52 | Panadugama (Nilwala Ganga) | 3.41 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:03:05 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:05:24 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:04:57 | Moraketiya (Walawe Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:01:56 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:04:54 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:21:02 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:02:19 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:09:37 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:27:52 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:07:09 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-19 07:04:36 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-19 07:02:37 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-11-19 07:01:28 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-19 07:02:24 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-11-19 07:03:11 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-11-19 07:03:27 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-11-19 07:04:36 | Glencourse (Kelani Ganga) | 9.77 | 🟢 Normal | -0.048 |  |
| 2026-11-19 07:00:20 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.056 |  |
| 2026-11-19 07:07:02 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | -0.057 |  |
| 2026-11-19 07:05:43 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.059 |  |
| 2026-11-19 07:08:17 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.246 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)