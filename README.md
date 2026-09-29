# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_15:09:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **274,261 measurements** from **39** stations.
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
| 2026-09-29 15:09:04 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-09-29 15:08:45 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:08:25 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.043 |  |
| 2026-09-29 15:08:09 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-09-29 15:07:27 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:07:25 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:07:04 | Baddegama (Gin Ganga) | 3.02 | 🟢 Normal | -0.032 |  |
| 2026-09-29 15:06:26 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:05:38 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:05:17 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:04:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | -0.052 |  |
| 2026-09-29 15:04:55 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:04:53 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-09-29 15:04:45 | Glencourse (Kelani Ganga) | 10.71 | 🟢 Normal | -0.041 |  |
| 2026-09-29 15:04:37 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:04:06 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:04:00 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 15:03:45 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | -0.038 |  |
| 2026-09-29 15:03:30 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.020 |  |
| 2026-09-29 15:03:24 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-09-29 15:03:23 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-09-29 15:03:11 | Hanwella (Kelani Ganga) | 2.70 | 🟢 Normal | -0.040 |  |
| 2026-09-29 15:03:01 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.054 |  |
| 2026-09-29 15:02:56 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:02:56 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:02:49 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:02:47 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:02:35 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-09-29 15:02:28 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-09-29 15:02:12 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | -0.010 |  |
| 2026-09-29 15:02:07 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:01:40 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.085 |  |
| 2026-09-29 15:01:31 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:01:26 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-29 15:00:38 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-09-29 15:00:36 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | -0.011 |  |
| 2026-09-29 15:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-09-29 15:00:29 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:00:18 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-29 15:00:16 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 15:03:24 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-09-29 15:04:53 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-09-29 15:08:09 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-09-29 15:01:26 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-29 15:00:18 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-29 15:04:00 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 15:02:49 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:02:07 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:05:17 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:07:27 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:04:06 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:05:38 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:02:56 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:07:25 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:02:56 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:04:55 | Badalgama (Maha Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:01:31 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:08:45 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:04:37 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:00:29 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:02:47 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-09-29 15:09:04 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-09-29 15:03:23 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-09-29 15:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-09-29 15:02:12 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | -0.010 |  |
| 2026-09-29 15:00:36 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | -0.011 |  |
| 2026-09-29 15:02:28 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-09-29 15:00:38 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-09-29 15:02:35 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-09-29 15:03:30 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.020 |  |
| 2026-09-29 15:00:16 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.020 |  |
| 2026-09-29 15:07:04 | Baddegama (Gin Ganga) | 3.02 | 🟢 Normal | -0.032 |  |
| 2026-09-29 15:03:45 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | -0.038 |  |
| 2026-09-29 15:03:11 | Hanwella (Kelani Ganga) | 2.70 | 🟢 Normal | -0.040 |  |
| 2026-09-29 15:04:45 | Glencourse (Kelani Ganga) | 10.71 | 🟢 Normal | -0.041 |  |
| 2026-09-29 15:08:25 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.043 |  |
| 2026-09-29 15:04:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | -0.052 |  |
| 2026-09-29 15:03:01 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.054 |  |
| 2026-09-29 15:01:40 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)