# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_16:13:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,771 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 16:13:34 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:12:56 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:11:53 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.026 |  |
| 2026-05-23 16:10:03 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:09:50 | Baddegama (Gin Ganga) | 2.39 | 🟢 Normal | -0.028 |  |
| 2026-05-23 16:09:44 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-05-23 16:08:54 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.009 |  |
| 2026-05-23 16:07:40 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:07:36 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:07:36 | Peradeniya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-05-23 16:07:24 | Rathnapura (Kalu Ganga) | 5.76 | 🟡 Alert | -0.058 |  |
| 2026-05-23 16:07:01 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.020 |  |
| 2026-05-23 16:06:54 | Dunamale (Aththanagalu Oya) | 4.98 | 🟠 Minor Flood | -0.039 |  |
| 2026-05-23 16:05:27 | Magura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.047 |  |
| 2026-05-23 16:05:25 | Glencourse (Kelani Ganga) | 11.69 | 🟢 Normal | -0.112 |  |
| 2026-05-23 16:05:15 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:05:05 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 16:05:03 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:04:36 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | -0.021 |  |
| 2026-05-23 16:04:32 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | -0.019 |  |
| 2026-05-23 16:04:18 | Nagalagam Street (Kelani Ganga) | 1.23 | 🟡 Alert | -0.016 |  |
| 2026-05-23 16:03:38 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.021 |  |
| 2026-05-23 16:03:31 | Putupaula (Kalu Ganga) | 3.14 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-05-23 16:03:24 | Hanwella (Kelani Ganga) | 6.30 | 🟢 Normal | -0.100 |  |
| 2026-05-23 16:03:20 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:03:14 | Deraniyagala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.068 |  |
| 2026-05-23 16:02:54 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:02:47 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-05-23 16:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.63 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-23 16:02:06 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:01:56 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:01:41 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-05-23 16:01:39 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-05-23 16:01:38 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-05-23 16:01:35 | Ellagawa (Kalu Ganga) | 10.27 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-23 16:01:32 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:01:26 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 16:01:26 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-05-23 16:01:25 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:01:22 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:01:12 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-05-23 16:01:04 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 16:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.63 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-23 16:06:54 | Dunamale (Aththanagalu Oya) | 4.98 | 🟠 Minor Flood | -0.039 |  |
| 2026-05-23 16:03:31 | Putupaula (Kalu Ganga) | 3.14 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-05-23 16:01:35 | Ellagawa (Kalu Ganga) | 10.27 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-23 16:04:18 | Nagalagam Street (Kelani Ganga) | 1.23 | 🟡 Alert | -0.016 |  |
| 2026-05-23 16:07:24 | Rathnapura (Kalu Ganga) | 5.76 | 🟡 Alert | -0.058 |  |
| 2026-05-23 16:01:41 | Manampitiya (Mahaweli Ganga) | 0.09 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-05-23 16:05:05 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 16:01:26 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 16:01:04 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 16:05:03 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:01:56 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:13:34 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:01:25 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:01:22 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:02:06 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:07:40 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:05:15 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:03:20 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:01:32 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:12:56 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:10:03 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:07:36 | Peradeniya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-05-23 16:08:54 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.009 |  |
| 2026-05-23 16:01:12 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-05-23 16:01:26 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-05-23 16:01:38 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-05-23 16:09:44 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-05-23 16:04:32 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | -0.019 |  |
| 2026-05-23 16:07:01 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.020 |  |
| 2026-05-23 16:02:47 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-05-23 16:04:36 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | -0.021 |  |
| 2026-05-23 16:03:38 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.021 |  |
| 2026-05-23 16:11:53 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.026 |  |
| 2026-05-23 16:09:50 | Baddegama (Gin Ganga) | 2.39 | 🟢 Normal | -0.028 |  |
| 2026-05-23 16:05:27 | Magura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.047 |  |
| 2026-05-23 16:03:14 | Deraniyagala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.068 |  |
| 2026-05-23 16:03:24 | Hanwella (Kelani Ganga) | 6.30 | 🟢 Normal | -0.100 |  |
| 2026-05-23 16:05:25 | Glencourse (Kelani Ganga) | 11.69 | 🟢 Normal | -0.112 |  |

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)