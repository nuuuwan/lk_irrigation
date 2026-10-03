# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_14:10:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **277,818 measurements** from **39** stations.
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
| 2026-10-03 14:10:24 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.056 |  |
| 2026-10-03 14:07:56 | Baddegama (Gin Ganga) | 2.42 | 🟢 Normal | -0.011 |  |
| 2026-10-03 14:06:07 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:05:45 | Rathnapura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.147 |  |
| 2026-10-03 14:05:04 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-10-03 14:04:48 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | -0.084 |  |
| 2026-10-03 14:04:42 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | -0.009 |  |
| 2026-10-03 14:04:41 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-03 14:04:06 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:04:06 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:03:56 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-10-03 14:03:56 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:03:45 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:03:36 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-03 14:03:27 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.246 |  |
| 2026-10-03 14:03:24 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:03:21 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.034 |  |
| 2026-10-03 14:03:15 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | -0.061 |  |
| 2026-10-03 14:03:14 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | -0.050 |  |
| 2026-10-03 14:03:08 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-10-03 14:02:46 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-10-03 14:02:44 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-10-03 14:02:44 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-03 14:02:18 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:02:11 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-10-03 14:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.042 |  |
| 2026-10-03 14:02:01 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:01:57 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:01:45 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:01:44 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:01:43 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:01:42 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-03 14:01:38 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:01:32 | Weraganthota (Mahaweli Ganga) | -3.51 | 🟢 Normal | -0.010 |  |
| 2026-10-03 14:01:16 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-10-03 14:01:08 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-03 14:01:04 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:00:51 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:00:50 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:00:14 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 14:02:46 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-10-03 14:01:08 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-03 14:03:36 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-03 14:02:44 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-03 14:04:41 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-03 14:00:51 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:01:38 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:01:43 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:02:01 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:02:18 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:04:06 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:20:58 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:01:57 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:03:56 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:01:44 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:03:24 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:03:45 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:00:50 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:01:04 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:06:07 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:01:45 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-03 14:04:42 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | -0.009 |  |
| 2026-10-03 14:03:56 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-10-03 14:01:32 | Weraganthota (Mahaweli Ganga) | -3.51 | 🟢 Normal | -0.010 |  |
| 2026-10-03 14:01:16 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-10-03 14:01:42 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-03 14:05:04 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-10-03 14:02:11 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-10-03 14:02:44 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-10-03 14:03:08 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-10-03 14:07:56 | Baddegama (Gin Ganga) | 2.42 | 🟢 Normal | -0.011 |  |
| 2026-10-03 14:03:21 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.034 |  |
| 2026-10-03 14:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.042 |  |
| 2026-10-03 14:03:14 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | -0.050 |  |
| 2026-10-03 14:10:24 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.056 |  |
| 2026-10-03 14:03:15 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | -0.061 |  |
| 2026-10-03 14:04:48 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | -0.084 |  |
| 2026-10-03 14:05:45 | Rathnapura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.147 |  |
| 2026-10-03 14:03:27 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.246 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)