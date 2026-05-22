# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--22_07:33:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **158,533 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 07:33:58 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:13:21 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-22 07:12:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.25 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-05-22 07:12:10 | Putupaula (Kalu Ganga) | 1.34 | 🟢 Normal | 0.458 | 🔺 Rising |
| 2026-05-22 07:10:26 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-22 07:09:26 | Badalgama (Maha Oya) | 4.19 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-22 07:08:26 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:08:19 | Galgamuwa (Mee Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:08:01 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:07:41 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-05-22 07:07:30 | Ellagawa (Kalu Ganga) | 8.08 | 🟢 Normal | 0.560 | 🔺 Rising |
| 2026-05-22 07:07:23 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.218 |  |
| 2026-05-22 07:07:07 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-22 07:06:59 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:06:37 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-22 07:06:03 | Hanwella (Kelani Ganga) | 6.24 | 🟢 Normal | 0.855 | 🔺 Rising |
| 2026-05-22 07:05:56 | Magura (Kalu Ganga) | 3.34 | 🟢 Normal | 0.846 | 🔺 Rising |
| 2026-05-22 07:05:48 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-05-22 07:05:05 | Dunamale (Aththanagalu Oya) | 4.50 | 🟠 Minor Flood | 0.253 | 🔺 Rising |
| 2026-05-22 07:04:48 | Deraniyagala (Kelani Ganga) | 4.26 | 🟢 Normal | -0.101 |  |
| 2026-05-22 07:04:46 | Glencourse (Kelani Ganga) | 14.60 | 🟢 Normal | 0.520 | 🔺 Rising |
| 2026-05-22 07:04:34 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:04:16 | Moragaswewa (Deduru Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:04:03 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 07:03:44 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:03:38 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-05-22 07:03:21 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:02:31 | Rathnapura (Kalu Ganga) | 7.42 | 🟡 Alert | 0.415 | 🔺 Rising |
| 2026-05-22 07:02:27 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 07:02:13 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:02:06 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-05-22 07:01:13 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.031 |  |
| 2026-05-22 07:01:10 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 07:00:55 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-22 07:00:48 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.006 |  |
| 2026-05-22 07:00:16 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.080 |  |
| 2026-05-22 07:00:10 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-22 07:00:10 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-22 07:05:05 | Dunamale (Aththanagalu Oya) | 4.50 | 🟠 Minor Flood | 0.253 | 🔺 Rising |
| 2026-05-22 07:02:31 | Rathnapura (Kalu Ganga) | 7.42 | 🟡 Alert | 0.415 | 🔺 Rising |
| 2026-05-22 07:06:03 | Hanwella (Kelani Ganga) | 6.24 | 🟢 Normal | 0.855 | 🔺 Rising |
| 2026-05-22 07:05:56 | Magura (Kalu Ganga) | 3.34 | 🟢 Normal | 0.846 | 🔺 Rising |
| 2026-05-22 07:07:30 | Ellagawa (Kalu Ganga) | 8.08 | 🟢 Normal | 0.560 | 🔺 Rising |
| 2026-05-22 07:04:46 | Glencourse (Kelani Ganga) | 14.60 | 🟢 Normal | 0.520 | 🔺 Rising |
| 2026-05-22 07:12:10 | Putupaula (Kalu Ganga) | 1.34 | 🟢 Normal | 0.458 | 🔺 Rising |
| 2026-05-22 07:12:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.25 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-05-22 07:07:41 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-05-22 07:07:07 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-22 07:09:26 | Badalgama (Maha Oya) | 4.19 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-22 07:06:37 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-22 07:13:21 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-22 07:00:55 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-22 07:10:26 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-22 07:00:10 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-22 07:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 07:04:03 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 07:02:27 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-22 07:08:01 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:03:44 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:02:13 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:04:16 | Moragaswewa (Deduru Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:08:26 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:08:19 | Galgamuwa (Mee Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:33:58 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:03:21 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:06:59 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:00:10 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:04:34 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:01:10 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-22 07:00:48 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.006 |  |
| 2026-05-22 07:02:06 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-05-22 07:03:38 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-05-22 07:05:48 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-05-22 07:01:13 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.031 |  |
| 2026-05-22 07:00:16 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.080 |  |
| 2026-05-22 07:04:48 | Deraniyagala (Kelani Ganga) | 4.26 | 🟢 Normal | -0.101 |  |
| 2026-05-22 07:07:23 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.218 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)