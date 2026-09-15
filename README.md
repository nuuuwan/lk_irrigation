# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_17:09:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,735 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 17:09:42 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | -0.009 |  |
| 2026-09-15 17:08:15 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-09-15 17:07:19 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-15 17:07:06 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-09-15 17:07:03 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-09-15 17:06:59 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.032 |  |
| 2026-09-15 17:06:47 | Magura (Kalu Ganga) | 4.36 | 🟡 Alert | -0.113 |  |
| 2026-09-15 17:06:33 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | -0.019 |  |
| 2026-09-15 17:06:04 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-15 17:05:14 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-15 17:05:04 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-09-15 17:04:51 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-15 17:04:43 | Baddegama (Gin Ganga) | 3.42 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-15 17:04:29 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.032 |  |
| 2026-09-15 17:04:24 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:03:49 | Hanwella (Kelani Ganga) | 2.38 | 🟢 Normal | -0.109 |  |
| 2026-09-15 17:03:41 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:03:40 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:03:38 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | -0.080 |  |
| 2026-09-15 17:03:33 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-09-15 17:03:28 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-09-15 17:02:45 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:02:39 | Putupaula (Kalu Ganga) | 1.49 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-15 17:02:26 | Panadugama (Nilwala Ganga) | 3.60 | 🟢 Normal | -0.131 |  |
| 2026-09-15 17:02:18 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-09-15 17:02:17 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-09-15 17:02:12 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.87 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:02:06 | Glencourse (Kelani Ganga) | 9.92 | 🟢 Normal | -0.141 |  |
| 2026-09-15 17:02:00 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:01:54 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:01:49 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:01:21 | Thanthirimale (Malwathu Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-09-15 17:01:14 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:01:09 | Manampitiya (Mahaweli Ganga) | -0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 17:00:09 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 17:06:47 | Magura (Kalu Ganga) | 4.36 | 🟡 Alert | -0.113 |  |
| 2026-09-15 17:07:03 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-09-15 17:02:17 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-09-15 17:06:04 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-15 17:07:06 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-09-15 17:04:51 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-15 17:02:39 | Putupaula (Kalu Ganga) | 1.49 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-15 17:05:14 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-15 17:04:43 | Baddegama (Gin Ganga) | 3.42 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-15 17:07:19 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-15 17:01:09 | Manampitiya (Mahaweli Ganga) | -0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 17:01:14 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:04:24 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:02:45 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:02:00 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:01:49 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:03:40 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:00:09 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:03:41 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-15 16:16:35 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:01:54 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:02:12 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.87 | 🟢 Normal | 0.000 |  |
| 2026-09-15 17:09:42 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | -0.009 |  |
| 2026-09-15 17:05:04 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-09-15 17:02:18 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-09-15 17:03:33 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-09-15 17:01:21 | Thanthirimale (Malwathu Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-09-15 17:06:33 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | -0.019 |  |
| 2026-09-15 17:08:15 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-09-15 17:03:28 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-09-15 17:06:59 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.032 |  |
| 2026-09-15 17:04:29 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.032 |  |
| 2026-09-15 17:03:38 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | -0.080 |  |
| 2026-09-15 17:03:49 | Hanwella (Kelani Ganga) | 2.38 | 🟢 Normal | -0.109 |  |
| 2026-09-15 16:05:07 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.113 |  |
| 2026-09-15 17:02:26 | Panadugama (Nilwala Ganga) | 3.60 | 🟢 Normal | -0.131 |  |
| 2026-09-15 17:02:06 | Glencourse (Kelani Ganga) | 9.92 | 🟢 Normal | -0.141 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)