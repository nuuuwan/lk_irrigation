# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_20:26:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,040 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 20:26:06 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:18:01 | Panadugama (Nilwala Ganga) | 3.23 | 🟢 Normal | -0.010 |  |
| 2026-05-22 20:08:45 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-05-22 20:08:11 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:08:07 | Nagalagam Street (Kelani Ganga) | 1.49 | 🟡 Alert | 0.000 |  |
| 2026-05-22 20:07:54 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:06:46 | Giriulla (Maha Oya) | 2.01 | 🟢 Normal | -0.029 |  |
| 2026-05-22 20:05:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.04 | 🟡 Alert | 0.089 | 🔺 Rising |
| 2026-05-22 20:05:22 | Glencourse (Kelani Ganga) | 14.80 | 🟢 Normal | -0.131 |  |
| 2026-05-22 20:05:10 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-05-22 20:05:05 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.039 |  |
| 2026-05-22 20:04:51 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-05-22 20:04:40 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-22 20:04:35 | Magura (Kalu Ganga) | 4.32 | 🟡 Alert | -0.030 |  |
| 2026-05-22 20:04:19 | Dunamale (Aththanagalu Oya) | 5.15 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-22 20:03:54 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-05-22 20:03:30 | Hanwella (Kelani Ganga) | 8.07 | 🟠 Minor Flood | -0.022 |  |
| 2026-05-22 20:02:53 | Deraniyagala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.060 |  |
| 2026-05-22 20:02:49 | Rathnapura (Kalu Ganga) | 7.31 | 🟡 Alert | -0.092 |  |
| 2026-05-22 20:02:48 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:02:45 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:02:41 | Badalgama (Maha Oya) | 3.81 | 🟢 Normal | -0.022 |  |
| 2026-05-22 20:02:41 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:02:41 | Ellagawa (Kalu Ganga) | 9.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-22 20:02:30 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:02:06 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-22 20:02:05 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:01:58 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-22 20:01:51 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:01:50 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 20:01:25 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:01:24 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.022 |  |
| 2026-05-22 20:01:24 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:00:56 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:00:31 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | 0.054 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 20:04:19 | Dunamale (Aththanagalu Oya) | 5.15 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-22 20:03:30 | Hanwella (Kelani Ganga) | 8.07 | 🟠 Minor Flood | -0.022 |  |
| 2026-05-22 20:05:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.04 | 🟡 Alert | 0.089 | 🔺 Rising |
| 2026-05-22 20:08:07 | Nagalagam Street (Kelani Ganga) | 1.49 | 🟡 Alert | 0.000 |  |
| 2026-05-22 20:04:35 | Magura (Kalu Ganga) | 4.32 | 🟡 Alert | -0.030 |  |
| 2026-05-22 20:02:49 | Rathnapura (Kalu Ganga) | 7.31 | 🟡 Alert | -0.092 |  |
| 2026-05-22 20:03:54 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-05-22 20:01:58 | Baddegama (Gin Ganga) | 2.55 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-22 20:04:40 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-22 20:00:31 | Thawalama (Gin Ganga) | 2.65 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-22 20:02:41 | Ellagawa (Kalu Ganga) | 9.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-22 20:02:06 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-22 20:01:50 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 20:26:06 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:01:25 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:02:45 | Moragaswewa (Deduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:02:41 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-22 18:03:13 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:08:11 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:01:51 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:00:56 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:07:54 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:02:30 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:02:48 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:02:05 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:01:24 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-22 20:08:45 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-05-22 20:18:01 | Panadugama (Nilwala Ganga) | 3.23 | 🟢 Normal | -0.010 |  |
| 2026-05-22 18:00:49 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-05-22 20:04:51 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-05-22 20:05:10 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-05-22 20:01:24 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.022 |  |
| 2026-05-22 20:02:41 | Badalgama (Maha Oya) | 3.81 | 🟢 Normal | -0.022 |  |
| 2026-05-22 20:06:46 | Giriulla (Maha Oya) | 2.01 | 🟢 Normal | -0.029 |  |
| 2026-05-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.030 |  |
| 2026-05-22 20:05:05 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.039 |  |
| 2026-05-22 20:02:53 | Deraniyagala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.060 |  |
| 2026-05-22 20:05:22 | Glencourse (Kelani Ganga) | 14.80 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)