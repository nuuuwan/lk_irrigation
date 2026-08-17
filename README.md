# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_20:09:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **236,202 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-17 20:09:30 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 20:09:20 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-17 20:08:10 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-17 20:08:01 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:07:33 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.021 |  |
| 2026-08-17 20:07:23 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.067 |  |
| 2026-08-17 20:06:35 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-08-17 20:06:28 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-08-17 20:06:15 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:06:14 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:05:45 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.119 |  |
| 2026-08-17 20:05:21 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:04:59 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 20:04:43 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 20:03:57 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-17 20:03:53 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-17 20:03:44 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 20:03:36 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:03:32 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-08-17 20:02:35 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-08-17 20:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-17 20:02:12 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:01:55 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:01:36 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:01:32 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:01:11 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-08-17 20:00:55 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 20:00:44 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:00:13 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-17 20:02:35 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-08-17 19:24:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.58 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-08-17 20:06:28 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-08-17 20:06:35 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-08-17 20:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-17 20:03:57 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-17 20:00:55 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 19:04:58 | Ellagawa (Kalu Ganga) | 5.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-17 20:08:10 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-17 20:03:53 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-17 20:04:43 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 20:09:30 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 20:04:59 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 20:03:44 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 20:09:20 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-17 18:01:09 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | 0.000 |  |
| 2026-08-17 19:02:26 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:00:44 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:06:14 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 19:03:51 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:01:55 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:04:13 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:08:01 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:02:12 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-17 19:09:44 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-08-17 19:00:21 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:06:15 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:00:13 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:01:32 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:01:36 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:05:21 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:00:44 | Thanthirimale (Malwathu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:03:36 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-17 20:03:32 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-08-17 20:01:11 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-08-17 20:07:33 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.021 |  |
| 2026-08-17 20:07:23 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.067 |  |
| 2026-08-17 20:05:45 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)