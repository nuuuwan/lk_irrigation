# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_13:08:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **129,302 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 13:08:15 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-19 13:08:06 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-19 13:07:35 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.009 |  |
| 2026-04-19 13:06:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.028 |  |
| 2026-04-19 13:06:13 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:05:34 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:05:29 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-04-19 13:05:24 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:05:13 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:04:44 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-19 13:04:28 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:04:05 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:03:45 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:03:25 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:03:18 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:03:10 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:02:56 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | -0.049 |  |
| 2026-04-19 13:02:56 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:02:55 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:02:35 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:02:31 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:02:21 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 13:02:14 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:02:13 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-19 13:02:11 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:02:07 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:02:02 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.059 |  |
| 2026-04-19 13:01:45 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | -0.010 |  |
| 2026-04-19 13:01:27 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-04-19 13:01:27 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:01:10 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:01:06 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:00:34 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.046 |  |
| 2026-04-19 13:00:24 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | -0.189 |  |
| 2026-04-19 12:21:30 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.046 |  |
| 2026-04-19 12:17:19 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 13:05:29 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-04-19 13:08:06 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-19 13:04:44 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-19 13:08:15 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-19 13:02:21 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 13:02:07 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:01:27 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:01:40 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:03:26 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:03:10 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:06:29 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:02:56 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:02:14 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:03:45 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-04-19 12:09:24 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:05:24 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:03:25 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:03:18 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:02:55 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:05:13 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:06:13 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:04:05 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:01:06 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:02:31 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:04:28 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:05:34 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:01:10 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:02:11 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-19 13:07:35 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.009 |  |
| 2026-04-19 12:04:40 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-19 13:02:13 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-19 13:01:27 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-04-19 13:01:45 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | -0.010 |  |
| 2026-04-19 13:06:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.028 |  |
| 2026-04-19 13:00:34 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.046 |  |
| 2026-04-19 13:02:56 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | -0.049 |  |
| 2026-04-19 13:02:02 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.059 |  |
| 2026-04-19 06:01:33 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.086 |  |
| 2026-04-19 13:00:24 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | -0.189 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)