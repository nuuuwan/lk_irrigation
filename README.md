# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--16_17:20:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **317,575 measurements** from **39** stations.
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
| 2026-11-16 17:20:40 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | -0.011 |  |
| 2026-11-16 17:13:20 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.021 |  |
| 2026-11-16 17:13:01 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | -0.009 |  |
| 2026-11-16 17:12:19 | Urawa (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:10:14 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | -0.030 |  |
| 2026-11-16 17:07:48 | Thalgahagoda (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:07:35 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:06:43 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 17:06:07 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:05:55 | Panadugama (Nilwala Ganga) | 4.36 | 🟢 Normal | -0.011 |  |
| 2026-11-16 17:05:52 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-16 17:05:30 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-11-16 17:05:29 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:04:40 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:04:12 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:04:08 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-16 17:04:05 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-11-16 17:03:51 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:03:43 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:03:29 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:03:11 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:03:08 | Rathnapura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-16 17:03:04 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-16 17:02:47 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:02:47 | Hanwella (Kelani Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:02:45 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:02:36 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | -0.020 |  |
| 2026-11-16 17:02:34 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-11-16 17:02:25 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.157 |  |
| 2026-11-16 17:02:24 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-11-16 17:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | -0.040 |  |
| 2026-11-16 17:02:09 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-16 17:02:01 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:01:44 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:01:35 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:01:24 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:01:02 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:01:02 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | -0.022 |  |
| 2026-11-16 17:00:10 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 17:04:08 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-16 17:03:04 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-16 17:03:08 | Rathnapura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-16 17:05:52 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-16 17:02:09 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-16 17:06:43 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 17:03:11 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:04:12 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:02:47 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:01:02 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:07:35 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:05:29 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:01:44 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:02:01 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:02:47 | Hanwella (Kelani Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:02:45 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:06:07 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:03:51 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:00:10 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:04:40 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:03:29 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:03:43 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:01:24 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:12:19 | Urawa (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:07:48 | Thalgahagoda (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:01:35 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-16 17:13:01 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | -0.009 |  |
| 2026-11-16 17:05:30 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-11-16 17:04:05 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-11-16 17:02:34 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-11-16 17:02:24 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-11-16 17:20:40 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | -0.011 |  |
| 2026-11-16 17:05:55 | Panadugama (Nilwala Ganga) | 4.36 | 🟢 Normal | -0.011 |  |
| 2026-11-16 17:02:36 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | -0.020 |  |
| 2026-11-16 17:13:20 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.021 |  |
| 2026-11-16 17:01:02 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | -0.022 |  |
| 2026-11-16 17:10:14 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | -0.030 |  |
| 2026-11-16 17:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | -0.040 |  |
| 2026-11-16 17:02:25 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.157 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)