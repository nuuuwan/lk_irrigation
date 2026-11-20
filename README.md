# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--20_10:15:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **320,845 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 10:15:14 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:12:20 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:10:06 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 10:09:47 | Kithulgala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.209 |  |
| 2026-11-20 10:09:20 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-20 10:08:42 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:08:31 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:07:33 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | -0.019 |  |
| 2026-11-20 10:07:28 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.009 |  |
| 2026-11-20 10:07:26 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:07:03 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:06:35 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.019 |  |
| 2026-11-20 10:06:15 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-11-20 10:05:18 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:04:54 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:04:54 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:04:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-20 10:04:07 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:03:43 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:03:38 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 10:03:17 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:03:07 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:03:06 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-20 10:03:03 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:03:03 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-11-20 10:03:01 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 4.909 | 🔺 Rising |
| 2026-11-20 10:02:53 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-20 10:02:43 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-11-20 10:02:43 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:02:39 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 4.909 | 🔺 Rising |
| 2026-11-20 10:02:30 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:02:18 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.011 |  |
| 2026-11-20 10:01:55 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.021 |  |
| 2026-11-20 10:01:49 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:01:27 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:01:24 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-11-20 10:01:20 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:00:54 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-11-20 10:00:53 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 10:03:01 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 4.909 | 🔺 Rising |
| 2026-11-20 10:04:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-20 10:02:53 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-20 10:03:06 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-20 10:09:20 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-20 10:06:15 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-11-20 10:03:38 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 10:10:06 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 10:00:53 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:01:20 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:04:07 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:04:54 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:01:27 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:08:42 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:08:31 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:03:17 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:02:30 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:04:54 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:02:43 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:07:26 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:03:07 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:05:18 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:01:49 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:03:43 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:07:03 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:12:20 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:03:03 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:15:14 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:07:28 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | -0.009 |  |
| 2026-11-20 10:01:24 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-11-20 10:03:03 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-11-20 10:02:43 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-11-20 10:02:18 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.011 |  |
| 2026-11-20 10:06:35 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.019 |  |
| 2026-11-20 10:07:33 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | -0.019 |  |
| 2026-11-20 10:00:54 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-11-20 10:01:55 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.021 |  |
| 2026-11-20 10:09:47 | Kithulgala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.209 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)