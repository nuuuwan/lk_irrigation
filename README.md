# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--23_10:04:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,480 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 10:04:50 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 10:03:54 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-11-23 10:03:44 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | -0.040 |  |
| 2026-11-23 10:03:43 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.053 |  |
| 2026-11-23 10:03:36 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-11-23 10:03:31 | Hanwella (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-23 10:03:10 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-23 10:02:58 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.049 |  |
| 2026-11-23 10:02:57 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 10:02:54 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-23 10:02:44 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-23 10:02:44 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.061 |  |
| 2026-11-23 10:02:37 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-11-23 10:02:30 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.032 |  |
| 2026-11-23 10:02:24 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-23 10:02:15 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-11-23 10:02:12 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 10:02:12 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 10:02:11 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.041 |  |
| 2026-11-23 10:02:05 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-23 10:01:59 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-23 10:01:42 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 10:01:37 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | -0.022 |  |
| 2026-11-23 10:01:35 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-23 10:01:31 | Moragaswewa (Deduru Oya) | 1.27 | 🟢 Normal | -0.030 |  |
| 2026-11-23 10:01:28 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 10:00:56 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-11-23 10:00:52 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-23 10:00:21 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-23 09:24:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.52 | 🟢 Normal | 0.034 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 09:05:11 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-11-23 10:02:44 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-23 10:01:59 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-23 09:24:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.52 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-23 09:03:39 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-23 10:02:05 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-23 10:02:54 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-23 10:02:57 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 10:01:28 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 10:00:21 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-23 10:00:52 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-23 10:01:42 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 10:03:10 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-23 10:02:12 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 10:02:24 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-23 09:02:50 | Pitabeddara (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 10:03:31 | Hanwella (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-23 10:01:35 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-23 10:04:50 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 10:02:12 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 09:06:32 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-23 09:04:30 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 10:03:36 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-11-23 10:02:15 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-11-23 10:03:54 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-11-23 10:02:37 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-11-23 10:00:56 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-23 10:01:37 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | -0.022 |  |
| 2026-11-23 09:07:32 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.028 |  |
| 2026-11-23 10:01:31 | Moragaswewa (Deduru Oya) | 1.27 | 🟢 Normal | -0.030 |  |
| 2026-11-23 10:02:30 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.032 |  |
| 2026-11-23 10:03:44 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | -0.040 |  |
| 2026-11-23 10:02:11 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.041 |  |
| 2026-11-23 10:02:58 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.049 |  |
| 2026-11-23 10:03:43 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.053 |  |
| 2026-11-23 09:06:02 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.056 |  |
| 2026-11-23 10:02:44 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.061 |  |
| 2026-11-23 09:05:38 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)