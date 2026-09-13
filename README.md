# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_17:12:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **259,936 measurements** from **39** stations.
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
| 2026-09-13 17:12:25 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-13 17:12:10 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 17:08:58 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.011 |  |
| 2026-09-13 17:07:36 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.022 |  |
| 2026-09-13 17:07:21 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-09-13 17:07:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 17:06:37 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.029 |  |
| 2026-09-13 17:06:33 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-09-13 17:05:59 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:05:53 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:05:49 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:05:29 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-09-13 17:05:17 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:05:07 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-09-13 17:04:45 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | -0.012 |  |
| 2026-09-13 17:04:20 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-13 17:04:01 | Manampitiya (Mahaweli Ganga) | -0.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-13 17:03:48 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-09-13 17:03:38 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 17:03:27 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:03:18 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:03:03 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.090 |  |
| 2026-09-13 17:02:54 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:02:53 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:02:45 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-13 17:02:43 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 17:02:35 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-13 17:02:25 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:02:15 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-09-13 17:01:48 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:01:31 | Weraganthota (Mahaweli Ganga) | -3.60 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-13 17:01:24 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:01:09 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 17:01:08 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.030 |  |
| 2026-09-13 17:01:04 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:00:52 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:00:51 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:00:14 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:00:10 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-09-13 16:59:52 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 17:05:07 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-09-13 17:00:10 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-09-13 17:12:25 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-13 17:04:20 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-13 17:02:35 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-13 17:01:31 | Weraganthota (Mahaweli Ganga) | -3.60 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-13 17:02:45 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-13 17:04:01 | Manampitiya (Mahaweli Ganga) | -0.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-13 17:01:09 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 17:02:43 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 17:07:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 17:03:38 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 17:12:10 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 17:01:48 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:00:14 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:03:18 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:05:53 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:01:04 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:00:52 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:03:27 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:01:24 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:05:59 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:02:25 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:02:53 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:05:17 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:00:51 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:02:54 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:05:49 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-13 17:05:29 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-09-13 17:07:21 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-09-13 17:03:48 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-09-13 17:08:58 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.011 |  |
| 2026-09-13 17:04:45 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | -0.012 |  |
| 2026-09-13 17:06:33 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-09-13 17:02:15 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-09-13 17:07:36 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.022 |  |
| 2026-09-13 17:06:37 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.029 |  |
| 2026-09-13 17:01:08 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.030 |  |
| 2026-09-13 17:03:03 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)