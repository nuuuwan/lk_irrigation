# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--18_07:33:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **318,955 measurements** from **39** stations.
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
| 2026-11-18 07:33:10 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:15:42 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:08:48 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:08:14 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:07:54 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.018 |  |
| 2026-11-18 07:07:06 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:07:05 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:06:54 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.065 |  |
| 2026-11-18 07:06:49 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:06:36 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:06:31 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:06:12 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-11-18 07:06:08 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:05:52 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:05:35 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:05:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-18 07:05:16 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:04:38 | Hanwella (Kelani Ganga) | 1.92 | 🟢 Normal | -0.021 |  |
| 2026-11-18 07:04:33 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:04:22 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.001 |  |
| 2026-11-18 07:04:05 | Manampitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-11-18 07:03:35 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-18 07:03:33 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 07:03:20 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 07:02:56 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.051 |  |
| 2026-11-18 07:02:44 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.049 |  |
| 2026-11-18 07:02:43 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:02:27 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:02:19 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-11-18 07:02:11 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:02:07 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:01:51 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:01:49 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:01:44 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.032 |  |
| 2026-11-18 07:01:42 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:00:51 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:00:29 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 07:05:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-18 07:03:35 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-18 06:01:53 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 07:03:20 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 07:03:33 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 07:00:51 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:00:29 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:02:27 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:07:06 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:05:35 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:06:36 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:06:49 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:33:10 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:07:05 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:05:52 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:08:48 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:06:31 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:06:08 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:04:33 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:05:16 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:08:14 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:02:43 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-18 07:04:22 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.001 |  |
| 2026-11-18 07:06:12 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-11-18 07:01:42 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:02:07 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:01:51 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:01:49 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:15:42 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:02:11 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-11-18 07:02:19 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-11-18 07:07:54 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.018 |  |
| 2026-11-18 07:04:05 | Manampitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-11-18 07:04:38 | Hanwella (Kelani Ganga) | 1.92 | 🟢 Normal | -0.021 |  |
| 2026-11-18 07:01:44 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.032 |  |
| 2026-11-18 07:02:44 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | -0.049 |  |
| 2026-11-18 07:02:56 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.051 |  |
| 2026-11-18 07:06:54 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)