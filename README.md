# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_15:11:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,729 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 15:11:45 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:07:31 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:07:10 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-05-23 15:06:47 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:06:44 | Glencourse (Kelani Ganga) | 11.80 | 🟢 Normal | -0.119 |  |
| 2026-05-23 15:06:33 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-05-23 15:06:14 | Nagalagam Street (Kelani Ganga) | 1.25 | 🟡 Alert | -0.033 |  |
| 2026-05-23 15:06:05 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | -0.020 |  |
| 2026-05-23 15:06:04 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | -0.030 |  |
| 2026-05-23 15:06:01 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-05-23 15:05:46 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.030 |  |
| 2026-05-23 15:05:41 | Baddegama (Gin Ganga) | 2.42 | 🟢 Normal | -0.032 |  |
| 2026-05-23 15:05:37 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:05:24 | Rathnapura (Kalu Ganga) | 5.82 | 🟡 Alert | -0.039 |  |
| 2026-05-23 15:05:02 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:04:51 | Dunamale (Aththanagalu Oya) | 5.02 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-23 15:03:38 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:03:28 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:03:19 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-05-23 15:03:08 | Hanwella (Kelani Ganga) | 6.40 | 🟢 Normal | -0.094 |  |
| 2026-05-23 15:03:01 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:02:57 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-05-23 15:02:53 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:02:43 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.63 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-23 15:01:57 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.035 |  |
| 2026-05-23 15:01:36 | Putupaula (Kalu Ganga) | 3.12 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-05-23 15:01:22 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:01:21 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:01:20 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:01:11 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:01:10 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:01:10 | Deraniyagala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-23 15:01:09 | Ellagawa (Kalu Ganga) | 10.26 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-23 15:01:05 | Magura (Kalu Ganga) | 3.55 | 🟢 Normal | -0.050 |  |
| 2026-05-23 15:00:33 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:00:15 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 15:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.63 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-23 15:04:51 | Dunamale (Aththanagalu Oya) | 5.02 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-23 15:01:36 | Putupaula (Kalu Ganga) | 3.12 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-05-23 15:01:09 | Ellagawa (Kalu Ganga) | 10.26 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-23 15:06:14 | Nagalagam Street (Kelani Ganga) | 1.25 | 🟡 Alert | -0.033 |  |
| 2026-05-23 15:05:24 | Rathnapura (Kalu Ganga) | 5.82 | 🟡 Alert | -0.039 |  |
| 2026-05-23 15:06:33 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-05-23 15:01:10 | Deraniyagala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-23 15:00:15 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-23 15:02:43 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:01:22 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:02:53 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:01:21 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:03:01 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:03:28 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:01:20 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-23 13:01:26 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:01:11 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:05:02 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:07:31 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-23 14:02:26 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:00:33 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:06:47 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:01:10 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:11:45 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:03:38 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:05:37 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 15:07:10 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-05-23 15:06:01 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-05-23 15:02:57 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-05-23 15:06:05 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | -0.020 |  |
| 2026-05-23 15:03:19 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-05-23 15:05:46 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.030 |  |
| 2026-05-23 15:06:04 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | -0.030 |  |
| 2026-05-23 15:05:41 | Baddegama (Gin Ganga) | 2.42 | 🟢 Normal | -0.032 |  |
| 2026-05-23 15:01:57 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.035 |  |
| 2026-05-23 15:01:05 | Magura (Kalu Ganga) | 3.55 | 🟢 Normal | -0.050 |  |
| 2026-05-23 15:03:08 | Hanwella (Kelani Ganga) | 6.40 | 🟢 Normal | -0.094 |  |
| 2026-05-23 15:06:44 | Glencourse (Kelani Ganga) | 11.80 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)