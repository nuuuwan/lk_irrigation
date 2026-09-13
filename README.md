# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_13:32:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **259,776 measurements** from **39** stations.
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
| 2026-09-13 13:32:09 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-13 13:25:39 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.008 |  |
| 2026-09-13 13:20:23 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.424 |  |
| 2026-09-13 13:17:49 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.011 |  |
| 2026-09-13 13:17:33 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.424 |  |
| 2026-09-13 13:16:31 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:10:59 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-13 13:09:20 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:08:30 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:08:05 | Magura (Kalu Ganga) | 3.28 | 🟢 Normal | -0.112 |  |
| 2026-09-13 13:07:52 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.084 |  |
| 2026-09-13 13:06:55 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:05:47 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:05:32 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:05:26 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-13 13:04:42 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | -0.086 |  |
| 2026-09-13 13:04:42 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-13 13:04:29 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:04:01 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:03:38 | Hanwella (Kelani Ganga) | 1.65 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-13 13:03:34 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:03:12 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:02:56 | Moragaswewa (Deduru Oya) | -0.31 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:02:53 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.170 |  |
| 2026-09-13 13:02:46 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:02:21 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-09-13 13:02:19 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | -0.021 |  |
| 2026-09-13 13:02:09 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.060 |  |
| 2026-09-13 13:02:04 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:02:03 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:02:01 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-13 13:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:01:33 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-13 13:01:24 | Weraganthota (Mahaweli Ganga) | -3.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:01:11 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-09-13 13:00:55 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:00:52 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:00:43 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-09-13 13:00:34 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 13:01:11 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-09-13 13:02:21 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-09-13 13:02:01 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-13 13:01:33 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-13 13:04:42 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-13 13:03:38 | Hanwella (Kelani Ganga) | 1.65 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-13 13:10:59 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-13 13:32:09 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-13 13:05:26 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-13 13:05:47 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:01:24 | Weraganthota (Mahaweli Ganga) | -3.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:03:12 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:00:52 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:02:56 | Moragaswewa (Deduru Oya) | -0.31 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:02:04 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:02:03 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:16:31 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:06:55 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:02:46 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:09:20 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:00:34 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:04:29 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:03:34 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:05:32 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:00:55 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:04:01 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:08:30 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-09-13 13:25:39 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.008 |  |
| 2026-09-13 13:00:43 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-09-13 13:17:49 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.011 |  |
| 2026-09-13 13:02:19 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | -0.021 |  |
| 2026-09-13 13:02:09 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.060 |  |
| 2026-09-13 13:07:52 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.084 |  |
| 2026-09-13 13:04:42 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | -0.086 |  |
| 2026-09-13 13:08:05 | Magura (Kalu Ganga) | 3.28 | 🟢 Normal | -0.112 |  |
| 2026-09-13 13:02:53 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.170 |  |
| 2026-09-13 13:20:23 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.424 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)