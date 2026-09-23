# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_16:24:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **268,904 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Magura — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 16:24:57 | Thalgahagoda (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.025 |  |
| 2026-09-23 16:13:15 | Baddegama (Gin Ganga) | 3.70 | 🟡 Alert | -0.019 |  |
| 2026-09-23 16:11:54 | Glencourse (Kelani Ganga) | 12.63 | 🟢 Normal | -0.046 |  |
| 2026-09-23 16:10:13 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:09:55 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-23 16:09:25 | Nawalapitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-09-23 16:09:14 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:07:23 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-09-23 16:07:12 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:06:54 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-09-23 16:06:30 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:06:16 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:05:57 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:05:50 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-09-23 16:05:21 | Ellagawa (Kalu Ganga) | 7.93 | 🟢 Normal | -0.034 |  |
| 2026-09-23 16:04:52 | Magura (Kalu Ganga) | 4.02 | 🟡 Alert | 0.000 |  |
| 2026-09-23 16:04:35 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:04:29 | Rathnapura (Kalu Ganga) | 3.73 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:04:28 | Kuda Oya (Kirindi Oya) | 0.10 | 🟢 Normal | 367.200 | 🔺 Rising |
| 2026-09-23 16:04:27 | Kuda Oya (Kirindi Oya) | 0.00 | 🟢 Normal | 367.200 | 🔺 Rising |
| 2026-09-23 16:04:25 | Hanwella (Kelani Ganga) | 4.75 | 🟢 Normal | -0.029 |  |
| 2026-09-23 16:04:16 | Putupaula (Kalu Ganga) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:03:41 | Deraniyagala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-09-23 16:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.93 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-23 16:03:19 | Thawalama (Gin Ganga) | 2.71 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-09-23 16:03:06 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:02:45 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-09-23 16:02:45 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:02:41 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:02:31 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-09-23 16:01:35 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-23 16:01:35 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:01:31 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-23 16:01:22 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:01:17 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-23 16:01:11 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.016 |  |
| 2026-09-23 16:00:59 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | -0.021 |  |
| 2026-09-23 16:00:48 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:00:27 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 16:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.93 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-23 16:04:52 | Magura (Kalu Ganga) | 4.02 | 🟡 Alert | 0.000 |  |
| 2026-09-23 16:13:15 | Baddegama (Gin Ganga) | 3.70 | 🟡 Alert | -0.019 |  |
| 2026-09-23 16:04:28 | Kuda Oya (Kirindi Oya) | 0.10 | 🟢 Normal | 367.200 | 🔺 Rising |
| 2026-09-23 16:03:41 | Deraniyagala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-09-23 16:07:23 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-09-23 16:01:35 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-23 16:03:19 | Thawalama (Gin Ganga) | 2.71 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-09-23 16:01:31 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-23 16:09:25 | Nawalapitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-09-23 16:01:17 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-23 16:09:55 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-23 16:05:57 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:01:22 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:01:35 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:00:48 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:03:06 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:09:14 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:10:13 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:02:41 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:06:30 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:04:16 | Putupaula (Kalu Ganga) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:06:16 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:07:12 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:04:29 | Rathnapura (Kalu Ganga) | 3.73 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:04:35 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:02:45 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-23 16:05:50 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-09-23 16:02:31 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-09-23 16:01:11 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.016 |  |
| 2026-09-23 16:02:45 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-09-23 16:06:54 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-09-23 16:00:59 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | -0.021 |  |
| 2026-09-23 16:00:27 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.022 |  |
| 2026-09-23 16:24:57 | Thalgahagoda (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.025 |  |
| 2026-09-23 15:16:00 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | -0.026 |  |
| 2026-09-23 16:04:25 | Hanwella (Kelani Ganga) | 4.75 | 🟢 Normal | -0.029 |  |
| 2026-09-23 16:05:21 | Ellagawa (Kalu Ganga) | 7.93 | 🟢 Normal | -0.034 |  |
| 2026-09-23 16:11:54 | Glencourse (Kelani Ganga) | 12.63 | 🟢 Normal | -0.046 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)