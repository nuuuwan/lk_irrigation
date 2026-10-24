# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--24_13:07:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,681 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 13:07:10 | Glencourse (Kelani Ganga) | 11.02 | 🟢 Normal | -0.056 |  |
| 2026-10-24 13:05:57 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-10-24 13:05:52 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-24 13:05:41 | Rathnapura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.031 |  |
| 2026-10-24 13:05:38 | Panadugama (Nilwala Ganga) | 4.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 13:05:23 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.097 |  |
| 2026-10-24 13:04:18 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | -0.010 |  |
| 2026-10-24 13:03:59 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.022 |  |
| 2026-10-24 13:03:55 | Hanwella (Kelani Ganga) | 3.39 | 🟢 Normal | -0.050 |  |
| 2026-10-24 13:03:53 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-10-24 13:03:51 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-24 13:03:20 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-24 13:03:03 | Putupaula (Kalu Ganga) | 1.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-24 13:02:59 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-24 13:02:59 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-10-24 13:02:56 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 13:02:46 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-24 13:02:28 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-10-24 13:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | -0.041 |  |
| 2026-10-24 13:02:13 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-24 13:02:12 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-24 13:02:12 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-10-24 13:01:58 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-24 13:01:52 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-24 13:01:40 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-24 13:01:39 | Moragaswewa (Deduru Oya) | 2.32 | 🟢 Normal | -0.339 |  |
| 2026-10-24 13:01:25 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-24 13:00:58 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | -0.022 |  |
| 2026-10-24 13:00:56 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.251 |  |
| 2026-10-24 13:00:53 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 13:00:21 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-24 13:00:09 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.154 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 12:04:14 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-10-24 13:02:13 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-24 13:05:52 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-24 13:03:03 | Putupaula (Kalu Ganga) | 1.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-24 13:03:51 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-24 13:05:38 | Panadugama (Nilwala Ganga) | 4.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 13:02:56 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 13:00:53 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 13:01:58 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-24 13:02:12 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:06:13 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 13:01:25 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:04:41 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-24 13:03:20 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:04:27 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-24 13:02:46 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-24 12:06:49 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-24 11:06:27 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-10-24 13:04:18 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | -0.010 |  |
| 2026-10-24 13:03:53 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-10-24 13:05:57 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-10-24 13:02:59 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-24 13:02:28 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-10-24 13:01:52 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-24 13:00:21 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-24 13:02:59 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-10-24 12:12:29 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.018 |  |
| 2026-10-24 13:02:12 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-10-24 13:03:59 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.022 |  |
| 2026-10-24 13:00:58 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | -0.022 |  |
| 2026-10-24 13:05:41 | Rathnapura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.031 |  |
| 2026-10-24 12:02:18 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.031 |  |
| 2026-10-24 13:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | -0.041 |  |
| 2026-10-24 13:03:55 | Hanwella (Kelani Ganga) | 3.39 | 🟢 Normal | -0.050 |  |
| 2026-10-24 13:07:10 | Glencourse (Kelani Ganga) | 11.02 | 🟢 Normal | -0.056 |  |
| 2026-10-24 13:05:23 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.097 |  |
| 2026-10-24 13:00:09 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.154 |  |
| 2026-10-24 13:00:56 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.251 |  |
| 2026-10-24 13:01:39 | Moragaswewa (Deduru Oya) | 2.32 | 🟢 Normal | -0.339 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)