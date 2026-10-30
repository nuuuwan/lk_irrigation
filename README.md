# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--30_18:10:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,303 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Putupaula — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 18:10:24 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.290 | 🔺 Rising |
| 2026-10-30 18:09:38 | Nagalagam Street (Kelani Ganga) | 0.53 | 🟢 Normal | -0.055 |  |
| 2026-10-30 18:09:23 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:08:13 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:07:19 | Ellagawa (Kalu Ganga) | 8.42 | 🟢 Normal | -0.075 |  |
| 2026-10-30 18:06:51 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:05:29 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.747 | 🔺 Rising |
| 2026-10-30 18:05:10 | Baddegama (Gin Ganga) | 3.17 | 🟢 Normal | -0.041 |  |
| 2026-10-30 18:04:56 | Rathnapura (Kalu Ganga) | 2.67 | 🟢 Normal | -0.029 |  |
| 2026-10-30 18:04:50 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:04:18 | Panadugama (Nilwala Ganga) | 5.18 | 🟡 Alert | 0.000 |  |
| 2026-10-30 18:04:17 | Panadugama (Nilwala Ganga) | 5.18 | 🟡 Alert | 0.000 |  |
| 2026-10-30 18:04:06 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:03:52 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-30 18:03:49 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 18:03:42 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 18:03:30 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 18:02:48 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:02:42 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 18:02:37 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:02:36 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:02:34 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-30 18:02:18 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:02:16 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-10-30 18:02:12 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:02:05 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.021 |  |
| 2026-10-30 18:02:00 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.019 |  |
| 2026-10-30 18:01:53 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:01:43 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-30 18:01:35 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.010 |  |
| 2026-10-30 18:01:27 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | -0.021 |  |
| 2026-10-30 18:01:24 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.011 |  |
| 2026-10-30 18:01:17 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:01:08 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.102 |  |
| 2026-10-30 18:01:07 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:00:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.30 | 🟡 Alert | -0.121 |  |
| 2026-10-30 18:00:47 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.012 |  |
| 2026-10-30 18:00:43 | Putupaula (Kalu Ganga) | 3.19 | 🟡 Alert | -0.032 |  |
| 2026-10-30 18:00:42 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-10-30 18:00:33 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:00:09 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 18:03:30 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 18:04:18 | Panadugama (Nilwala Ganga) | 5.18 | 🟡 Alert | 0.000 |  |
| 2026-10-30 18:00:43 | Putupaula (Kalu Ganga) | 3.19 | 🟡 Alert | -0.032 |  |
| 2026-10-30 18:00:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.30 | 🟡 Alert | -0.121 |  |
| 2026-10-30 18:05:29 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.747 | 🔺 Rising |
| 2026-10-30 18:10:24 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.290 | 🔺 Rising |
| 2026-10-30 18:02:34 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-30 18:01:43 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-30 18:02:16 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-10-30 18:03:52 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-30 18:02:42 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 18:03:42 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 18:03:49 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 18:02:36 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:01:17 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:01:53 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:06:51 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:01:07 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:09:23 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:04:06 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:02:37 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:02:18 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:08:13 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:04:50 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:02:48 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:02:12 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-30 18:01:35 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.010 |  |
| 2026-10-30 18:01:24 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.011 |  |
| 2026-10-30 18:00:47 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.012 |  |
| 2026-10-30 18:02:00 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.019 |  |
| 2026-10-30 18:00:09 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.021 |  |
| 2026-10-30 18:02:05 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.021 |  |
| 2026-10-30 18:01:27 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | -0.021 |  |
| 2026-10-30 18:00:42 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-10-30 18:04:56 | Rathnapura (Kalu Ganga) | 2.67 | 🟢 Normal | -0.029 |  |
| 2026-10-30 18:05:10 | Baddegama (Gin Ganga) | 3.17 | 🟢 Normal | -0.041 |  |
| 2026-10-30 18:09:38 | Nagalagam Street (Kelani Ganga) | 0.53 | 🟢 Normal | -0.055 |  |
| 2026-10-30 18:07:19 | Ellagawa (Kalu Ganga) | 8.42 | 🟢 Normal | -0.075 |  |
| 2026-10-30 18:01:08 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)