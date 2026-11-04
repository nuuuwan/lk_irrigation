# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_16:17:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,759 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 16:17:44 | Magura (Kalu Ganga) | 2.47 | 🟢 Normal | -0.059 |  |
| 2026-11-04 16:15:16 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.045 |  |
| 2026-11-04 16:12:25 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | -0.035 |  |
| 2026-11-04 16:09:57 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.018 |  |
| 2026-11-04 16:09:42 | Panadugama (Nilwala Ganga) | 4.27 | 🟢 Normal | -4.500 |  |
| 2026-11-04 16:09:18 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | -4.500 |  |
| 2026-11-04 16:08:41 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-04 16:08:37 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | -0.028 |  |
| 2026-11-04 16:08:13 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-11-04 16:07:57 | Rathnapura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.055 |  |
| 2026-11-04 16:07:55 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-04 16:07:55 | Moragaswewa (Deduru Oya) | 4.34 | 🟢 Normal | -0.018 |  |
| 2026-11-04 16:07:20 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.059 |  |
| 2026-11-04 16:07:17 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | -0.029 |  |
| 2026-11-04 16:06:36 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.019 |  |
| 2026-11-04 16:06:35 | Peradeniya (Mahaweli Ganga) | 2.89 | 🟢 Normal | -0.009 |  |
| 2026-11-04 16:05:24 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-04 16:04:56 | Ellagawa (Kalu Ganga) | 6.71 | 🟢 Normal | -0.019 |  |
| 2026-11-04 16:04:44 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-11-04 16:04:38 | Badalgama (Maha Oya) | 3.69 | 🟢 Normal | -0.068 |  |
| 2026-11-04 16:04:01 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-04 16:03:50 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | -0.057 |  |
| 2026-11-04 16:03:49 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-04 16:03:30 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-04 16:03:28 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-11-04 16:03:13 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-11-04 16:03:08 | Pitabeddara (Nilwala Ganga) | 1.75 | 🟢 Normal | -0.032 |  |
| 2026-11-04 16:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.02 | 🟡 Alert | -0.010 |  |
| 2026-11-04 16:02:48 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | -0.061 |  |
| 2026-11-04 16:02:34 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-11-04 16:02:15 | Giriulla (Maha Oya) | 2.48 | 🟢 Normal | -0.100 |  |
| 2026-11-04 16:02:11 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | -0.011 |  |
| 2026-11-04 16:02:08 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | -0.005 |  |
| 2026-11-04 16:01:48 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | -0.011 |  |
| 2026-11-04 16:01:11 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-04 16:01:09 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-11-04 16:00:57 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-04 16:00:55 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | -0.020 |  |
| 2026-11-04 16:00:46 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 16:00:15 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 16:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.02 | 🟡 Alert | -0.010 |  |
| 2026-11-04 16:03:28 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-11-04 16:08:13 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-11-04 16:05:24 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-04 16:08:41 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-04 16:04:01 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-04 16:00:57 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-04 16:00:15 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 16:03:30 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-04 16:00:46 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 16:01:11 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-04 16:07:55 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-04 16:03:49 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-04 16:02:08 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | -0.005 |  |
| 2026-11-04 16:06:35 | Peradeniya (Mahaweli Ganga) | 2.89 | 🟢 Normal | -0.009 |  |
| 2026-11-04 16:04:44 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-11-04 16:02:34 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-11-04 16:01:09 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-11-04 16:01:48 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | -0.011 |  |
| 2026-11-04 16:02:11 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | -0.011 |  |
| 2026-11-04 16:09:57 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.018 |  |
| 2026-11-04 16:07:55 | Moragaswewa (Deduru Oya) | 4.34 | 🟢 Normal | -0.018 |  |
| 2026-11-04 16:06:36 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.019 |  |
| 2026-11-04 16:04:56 | Ellagawa (Kalu Ganga) | 6.71 | 🟢 Normal | -0.019 |  |
| 2026-11-04 16:00:55 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | -0.020 |  |
| 2026-11-04 16:03:13 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-11-04 16:08:37 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | -0.028 |  |
| 2026-11-04 16:07:17 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | -0.029 |  |
| 2026-11-04 16:03:08 | Pitabeddara (Nilwala Ganga) | 1.75 | 🟢 Normal | -0.032 |  |
| 2026-11-04 16:12:25 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | -0.035 |  |
| 2026-11-04 16:15:16 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.045 |  |
| 2026-11-04 16:07:57 | Rathnapura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.055 |  |
| 2026-11-04 16:03:50 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | -0.057 |  |
| 2026-11-04 16:07:20 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.059 |  |
| 2026-11-04 16:17:44 | Magura (Kalu Ganga) | 2.47 | 🟢 Normal | -0.059 |  |
| 2026-11-04 16:02:48 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | -0.061 |  |
| 2026-11-04 16:04:38 | Badalgama (Maha Oya) | 3.69 | 🟢 Normal | -0.068 |  |
| 2026-11-04 16:02:15 | Giriulla (Maha Oya) | 2.48 | 🟢 Normal | -0.100 |  |
| 2026-11-04 16:09:42 | Panadugama (Nilwala Ganga) | 4.27 | 🟢 Normal | -4.500 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)