# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_18:20:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **277,978 measurements** from **39** stations.
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
| 2026-10-03 18:20:47 | Panadugama (Nilwala Ganga) | 4.08 | 🟢 Normal | -0.070 |  |
| 2026-10-03 18:07:58 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:07:51 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.056 |  |
| 2026-10-03 18:07:39 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.063 |  |
| 2026-10-03 18:06:06 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.025 |  |
| 2026-10-03 18:05:22 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | 0.512 | 🔺 Rising |
| 2026-10-03 18:05:21 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:05:15 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-03 18:04:39 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-10-03 18:04:21 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:04:04 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 18:03:55 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:03:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:03:25 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-03 18:03:11 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | -0.032 |  |
| 2026-10-03 18:03:10 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:02:57 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:02:47 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.051 |  |
| 2026-10-03 18:02:40 | Ellagawa (Kalu Ganga) | 5.93 | 🟢 Normal | -0.062 |  |
| 2026-10-03 18:02:38 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.013 |  |
| 2026-10-03 18:02:29 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:02:25 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-03 18:02:24 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-10-03 18:02:22 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | -0.060 |  |
| 2026-10-03 18:02:16 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.011 |  |
| 2026-10-03 18:02:14 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-10-03 18:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.16 | 🟢 Normal | -0.040 |  |
| 2026-10-03 18:01:53 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.011 |  |
| 2026-10-03 18:01:48 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | -0.010 |  |
| 2026-10-03 18:01:38 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:01:38 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.041 |  |
| 2026-10-03 18:01:21 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-10-03 18:01:21 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | -0.067 |  |
| 2026-10-03 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-03 18:00:47 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.032 |  |
| 2026-10-03 18:00:43 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:00:40 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:00:40 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-10-03 18:00:14 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 18:05:22 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | 0.512 | 🔺 Rising |
| 2026-10-03 18:04:39 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-10-03 18:03:25 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-03 18:02:25 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-03 18:05:15 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-03 18:04:04 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 18:00:14 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:01:38 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:00:43 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:00:40 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:04:21 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:03:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:07:58 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:03:55 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:03:10 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:02:29 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:02:57 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:05:21 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:01:48 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | -0.010 |  |
| 2026-10-03 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-03 18:02:14 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-10-03 18:02:16 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.011 |  |
| 2026-10-03 18:01:21 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-10-03 18:01:53 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.011 |  |
| 2026-10-03 18:02:38 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.013 |  |
| 2026-10-03 18:02:24 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-10-03 18:00:40 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-10-03 18:06:06 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.025 |  |
| 2026-10-03 18:00:47 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.032 |  |
| 2026-10-03 18:03:11 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | -0.032 |  |
| 2026-10-03 18:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.16 | 🟢 Normal | -0.040 |  |
| 2026-10-03 18:01:38 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.041 |  |
| 2026-10-03 18:02:47 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.051 |  |
| 2026-10-03 18:07:51 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.056 |  |
| 2026-10-03 18:02:22 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | -0.060 |  |
| 2026-10-03 18:02:40 | Ellagawa (Kalu Ganga) | 5.93 | 🟢 Normal | -0.062 |  |
| 2026-10-03 18:07:39 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.063 |  |
| 2026-10-03 18:01:21 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | -0.067 |  |
| 2026-10-03 18:20:47 | Panadugama (Nilwala Ganga) | 4.08 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)