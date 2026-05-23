# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_10:20:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,535 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 10:20:44 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.033 |  |
| 2026-05-23 10:16:15 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:14:39 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:12:27 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | -0.028 |  |
| 2026-05-23 10:08:01 | Nagalagam Street (Kelani Ganga) | 1.34 | 🟡 Alert | -0.029 |  |
| 2026-05-23 10:07:27 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-05-23 10:06:22 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-05-23 10:06:09 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.144 |  |
| 2026-05-23 10:05:59 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:05:34 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.029 |  |
| 2026-05-23 10:05:26 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:05:19 | Badalgama (Maha Oya) | 3.23 | 🟢 Normal | -0.030 |  |
| 2026-05-23 10:05:11 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-05-23 10:04:47 | Glencourse (Kelani Ganga) | 12.23 | 🟢 Normal | -0.075 |  |
| 2026-05-23 10:04:43 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 10:04:28 | Rathnapura (Kalu Ganga) | 6.14 | 🟡 Alert | -0.067 |  |
| 2026-05-23 10:04:01 | Deraniyagala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.067 |  |
| 2026-05-23 10:03:26 | Dunamale (Aththanagalu Oya) | 5.12 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-23 10:03:23 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:03:22 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:03:16 | Hanwella (Kelani Ganga) | 6.85 | 🟢 Normal | -0.091 |  |
| 2026-05-23 10:03:01 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.030 |  |
| 2026-05-23 10:03:00 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.041 |  |
| 2026-05-23 10:02:47 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:02:46 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:02:37 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.036 |  |
| 2026-05-23 10:02:31 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:02:26 | Putupaula (Kalu Ganga) | 3.02 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-05-23 10:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.56 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-05-23 10:02:13 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:02:03 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:01:23 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:01:21 | Ellagawa (Kalu Ganga) | 10.17 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-05-23 10:01:12 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:00:42 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-23 10:00:36 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:00:24 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.030 |  |
| 2026-05-23 10:00:17 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 10:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.56 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-05-23 10:03:26 | Dunamale (Aththanagalu Oya) | 5.12 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-23 10:01:21 | Ellagawa (Kalu Ganga) | 10.17 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-05-23 10:02:26 | Putupaula (Kalu Ganga) | 3.02 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-05-23 10:08:01 | Nagalagam Street (Kelani Ganga) | 1.34 | 🟡 Alert | -0.029 |  |
| 2026-05-23 10:04:28 | Rathnapura (Kalu Ganga) | 6.14 | 🟡 Alert | -0.067 |  |
| 2026-05-23 10:04:43 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 10:02:47 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:02:13 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:16:15 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:02:03 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:03:23 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:01:12 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:01:23 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:03:22 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:02:31 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:05:59 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:02:46 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:05:26 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:14:39 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:00:36 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-23 10:06:22 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-05-23 10:00:17 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-23 10:05:11 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-05-23 10:00:42 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-23 10:07:27 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-05-23 10:12:27 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | -0.028 |  |
| 2026-05-23 10:05:34 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.029 |  |
| 2026-05-23 10:00:24 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.030 |  |
| 2026-05-23 10:05:19 | Badalgama (Maha Oya) | 3.23 | 🟢 Normal | -0.030 |  |
| 2026-05-23 10:03:01 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.030 |  |
| 2026-05-23 10:20:44 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.033 |  |
| 2026-05-23 10:02:37 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.036 |  |
| 2026-05-23 10:03:00 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.041 |  |
| 2026-05-23 10:04:01 | Deraniyagala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.067 |  |
| 2026-05-23 09:04:47 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | -0.069 |  |
| 2026-05-23 10:04:47 | Glencourse (Kelani Ganga) | 12.23 | 🟢 Normal | -0.075 |  |
| 2026-05-23 10:03:16 | Hanwella (Kelani Ganga) | 6.85 | 🟢 Normal | -0.091 |  |
| 2026-05-23 10:06:09 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.144 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)