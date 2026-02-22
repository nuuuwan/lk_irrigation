# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_12:12:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,962 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 12:12:40 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-22 12:09:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.04 | 🟡 Alert | 0.063 | 🔺 Rising |
| 2026-02-22 12:06:45 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-22 12:06:10 | Magura (Kalu Ganga) | 3.19 | 🟢 Normal | -1.902 |  |
| 2026-02-22 12:06:07 | Badalgama (Maha Oya) | 3.21 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-22 12:05:18 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-22 12:05:11 | Rathnapura (Kalu Ganga) | 3.77 | 🟢 Normal | -0.176 |  |
| 2026-02-22 12:05:07 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-22 12:04:58 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.042 |  |
| 2026-02-22 12:04:54 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 12:04:51 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | -0.136 |  |
| 2026-02-22 12:04:45 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | -0.059 |  |
| 2026-02-22 12:04:37 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.043 |  |
| 2026-02-22 12:04:36 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-22 12:04:17 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-02-22 12:03:55 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.043 |  |
| 2026-02-22 12:03:26 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | -0.191 |  |
| 2026-02-22 12:03:21 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | -0.298 |  |
| 2026-02-22 12:03:18 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.128 |  |
| 2026-02-22 12:03:03 | Thanamalwila (Kirindi Oya) | 1.64 | 🟢 Normal | -0.043 |  |
| 2026-02-22 12:02:53 | Hanwella (Kelani Ganga) | 2.57 | 🟢 Normal | -0.112 |  |
| 2026-02-22 12:02:49 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-22 12:02:34 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.040 |  |
| 2026-02-22 12:02:31 | Weraganthota (Mahaweli Ganga) | -1.26 | 🟢 Normal | -0.232 |  |
| 2026-02-22 12:02:24 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -0.145 |  |
| 2026-02-22 12:02:19 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-22 12:02:12 | Putupaula (Kalu Ganga) | 1.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-22 12:02:09 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 12:09:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.04 | 🟡 Alert | 0.063 | 🔺 Rising |
| 2026-02-22 12:00:47 | Manampitiya (Mahaweli Ganga) | 4.25 | 🟡 Alert | -0.060 |  |
| 2026-02-22 12:06:07 | Badalgama (Maha Oya) | 3.21 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-22 12:05:18 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-22 12:02:19 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-22 12:02:49 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-22 12:01:50 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-22 12:05:07 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-22 12:02:12 | Putupaula (Kalu Ganga) | 1.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-22 12:02:09 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-22 12:12:40 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-22 12:04:54 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 12:04:36 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-22 12:06:45 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-22 12:01:37 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-22 12:01:09 | Ellagawa (Kalu Ganga) | 7.74 | 🟢 Normal | -0.010 |  |
| 2026-02-22 12:04:17 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-02-22 12:00:06 | Nakkala (Kumbukkan Oya) | 1.41 | 🟢 Normal | -0.021 |  |
| 2026-02-22 12:01:20 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.021 |  |
| 2026-02-22 12:00:19 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-02-22 11:07:23 | Thalgahagoda (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.036 |  |
| 2026-02-22 12:02:34 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.040 |  |
| 2026-02-22 12:01:39 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.040 |  |
| 2026-02-22 12:04:58 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.042 |  |
| 2026-02-22 12:01:23 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.043 |  |
| 2026-02-22 12:03:03 | Thanamalwila (Kirindi Oya) | 1.64 | 🟢 Normal | -0.043 |  |
| 2026-02-22 12:04:37 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.043 |  |
| 2026-02-22 12:03:55 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.043 |  |
| 2026-02-22 12:04:45 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | -0.059 |  |
| 2026-02-22 12:02:53 | Hanwella (Kelani Ganga) | 2.57 | 🟢 Normal | -0.112 |  |
| 2026-02-22 11:04:18 | Kuda Oya (Kirindi Oya) | 2.15 | 🟢 Normal | -0.127 |  |
| 2026-02-22 12:03:18 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.128 |  |
| 2026-02-22 12:04:51 | Glencourse (Kelani Ganga) | 10.20 | 🟢 Normal | -0.136 |  |
| 2026-02-22 12:02:24 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -0.145 |  |
| 2026-02-22 12:05:11 | Rathnapura (Kalu Ganga) | 3.77 | 🟢 Normal | -0.176 |  |
| 2026-02-22 12:03:26 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | -0.191 |  |
| 2026-02-22 12:02:31 | Weraganthota (Mahaweli Ganga) | -1.26 | 🟢 Normal | -0.232 |  |
| 2026-02-22 12:03:21 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | -0.298 |  |
| 2026-02-22 12:06:10 | Magura (Kalu Ganga) | 3.19 | 🟢 Normal | -1.902 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)