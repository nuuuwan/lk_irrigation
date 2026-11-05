# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_19:20:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,769 measurements** from **39** stations.
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
| 2026-11-05 19:20:36 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-11-05 19:18:18 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.008 |  |
| 2026-11-05 19:15:36 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 12.000 | 🔺 Rising |
| 2026-11-05 19:15:33 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 12.000 | 🔺 Rising |
| 2026-11-05 19:10:54 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | -0.036 |  |
| 2026-11-05 19:09:42 | Hanwella (Kelani Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:09:40 | Hanwella (Kelani Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:09:03 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-11-05 19:09:01 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:08:55 | Rathnapura (Kalu Ganga) | 2.72 | 🟢 Normal | -0.085 |  |
| 2026-11-05 19:07:42 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-11-05 19:07:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.90 | 🟢 Normal | -0.019 |  |
| 2026-11-05 19:06:53 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:06:34 | Badalgama (Maha Oya) | 3.24 | 🟢 Normal | -0.028 |  |
| 2026-11-05 19:06:21 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:05:03 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:04:56 | Giriulla (Maha Oya) | 2.04 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-05 19:04:36 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 19:04:14 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-11-05 19:03:45 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-05 19:03:39 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-05 19:03:20 | Moraketiya (Walawe Ganga) | 1.76 | 🟢 Normal | -0.019 |  |
| 2026-11-05 19:03:05 | Panadugama (Nilwala Ganga) | 4.27 | 🟢 Normal | -0.013 |  |
| 2026-11-05 19:02:57 | Thawalama (Gin Ganga) | 2.13 | 🟢 Normal | -0.021 |  |
| 2026-11-05 19:02:18 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-11-05 19:02:18 | Dunamale (Aththanagalu Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:02:13 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:02:10 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 19:02:10 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:01:55 | Thanamalwila (Kirindi Oya) | 1.94 | 🟢 Normal | -0.021 |  |
| 2026-11-05 19:01:54 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-05 19:01:37 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-11-05 19:01:34 | Kuda Oya (Kirindi Oya) | 2.16 | 🟢 Normal | -0.011 |  |
| 2026-11-05 19:01:30 | Moragaswewa (Deduru Oya) | 3.29 | 🟢 Normal | -0.010 |  |
| 2026-11-05 19:01:20 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:01:03 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:00:41 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:59:38 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 19:15:36 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 12.000 | 🔺 Rising |
| 2026-11-05 19:09:03 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-11-05 19:20:36 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-11-05 19:03:39 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-05 19:04:56 | Giriulla (Maha Oya) | 2.04 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-05 19:03:45 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-05 19:01:54 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-05 19:04:36 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 19:02:10 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 19:00:41 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:06:53 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:01:03 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:03:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:09:42 | Hanwella (Kelani Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:02:13 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:06:21 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:09:01 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:02:10 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:02:18 | Dunamale (Aththanagalu Oya) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:05:03 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-05 19:18:18 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.008 |  |
| 2026-11-05 19:07:42 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-11-05 17:17:33 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-11-05 19:01:37 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-11-05 19:01:30 | Moragaswewa (Deduru Oya) | 3.29 | 🟢 Normal | -0.010 |  |
| 2026-11-05 19:01:34 | Kuda Oya (Kirindi Oya) | 2.16 | 🟢 Normal | -0.011 |  |
| 2026-11-05 18:01:46 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | -0.012 |  |
| 2026-11-05 19:03:05 | Panadugama (Nilwala Ganga) | 4.27 | 🟢 Normal | -0.013 |  |
| 2026-11-05 19:07:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.90 | 🟢 Normal | -0.019 |  |
| 2026-11-05 19:03:20 | Moraketiya (Walawe Ganga) | 1.76 | 🟢 Normal | -0.019 |  |
| 2026-11-05 19:02:18 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-11-05 19:04:14 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-11-05 19:02:57 | Thawalama (Gin Ganga) | 2.13 | 🟢 Normal | -0.021 |  |
| 2026-11-05 19:01:55 | Thanamalwila (Kirindi Oya) | 1.94 | 🟢 Normal | -0.021 |  |
| 2026-11-05 19:06:34 | Badalgama (Maha Oya) | 3.24 | 🟢 Normal | -0.028 |  |
| 2026-11-05 19:10:54 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | -0.036 |  |
| 2026-11-05 18:01:57 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.049 |  |
| 2026-11-05 19:08:55 | Rathnapura (Kalu Ganga) | 2.72 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)