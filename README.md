# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_07:12:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **264,029 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 07:12:38 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-18 07:09:29 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-09-18 07:08:52 | Baddegama (Gin Ganga) | 3.35 | 🟢 Normal | -0.028 |  |
| 2026-09-18 07:07:55 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.019 |  |
| 2026-09-18 07:07:51 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:06:51 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 07:05:53 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:05:33 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | -0.010 |  |
| 2026-09-18 07:05:33 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:05:28 | Glencourse (Kelani Ganga) | 9.49 | 🟢 Normal | -0.029 |  |
| 2026-09-18 07:05:24 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.081 |  |
| 2026-09-18 07:05:21 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-09-18 07:05:07 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:04:46 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-09-18 07:04:46 | Magura (Kalu Ganga) | 4.42 | 🟡 Alert | -0.116 |  |
| 2026-09-18 07:04:34 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.019 |  |
| 2026-09-18 07:04:02 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-09-18 07:04:01 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-09-18 07:03:55 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-09-18 07:03:51 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-09-18 07:03:27 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:03:15 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:03:13 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:03:07 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.044 |  |
| 2026-09-18 07:02:48 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-09-18 07:02:43 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:02:40 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:01:59 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.039 |  |
| 2026-09-18 07:01:57 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:01:47 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.033 |  |
| 2026-09-18 07:01:44 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | -0.021 |  |
| 2026-09-18 07:01:37 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | -0.002 |  |
| 2026-09-18 07:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:01:18 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.038 |  |
| 2026-09-18 07:01:09 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.041 |  |
| 2026-09-18 07:01:04 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 07:00:48 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 07:04:46 | Magura (Kalu Ganga) | 4.42 | 🟡 Alert | -0.116 |  |
| 2026-09-18 07:04:02 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-09-18 07:01:04 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 07:06:51 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 07:12:38 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-18 07:02:40 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:00:48 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:03:13 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:03:15 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:07:51 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:05:53 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:05:33 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:05:07 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:03:27 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:01:57 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:02:43 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2026-09-18 07:01:37 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | -0.002 |  |
| 2026-09-18 07:05:21 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-09-18 07:09:29 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-09-18 07:03:51 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-09-18 07:05:33 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | -0.010 |  |
| 2026-09-18 07:04:46 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-09-18 07:07:55 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.019 |  |
| 2026-09-18 07:03:55 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-09-18 07:04:34 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.019 |  |
| 2026-09-18 07:02:48 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-09-18 07:04:01 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-09-18 07:01:44 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | -0.021 |  |
| 2026-09-18 07:08:52 | Baddegama (Gin Ganga) | 3.35 | 🟢 Normal | -0.028 |  |
| 2026-09-18 07:05:28 | Glencourse (Kelani Ganga) | 9.49 | 🟢 Normal | -0.029 |  |
| 2026-09-18 07:01:47 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.033 |  |
| 2026-09-18 07:01:18 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.038 |  |
| 2026-09-18 07:01:59 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.039 |  |
| 2026-09-18 07:01:09 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.041 |  |
| 2026-09-18 07:03:07 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.044 |  |
| 2026-09-18 06:07:44 | Panadugama (Nilwala Ganga) | 4.36 | 🟢 Normal | -0.057 |  |
| 2026-09-18 07:05:24 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)