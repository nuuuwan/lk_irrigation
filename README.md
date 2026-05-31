# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_21:09:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **166,937 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 21:09:08 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.028 |  |
| 2026-05-31 21:09:01 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.047 |  |
| 2026-05-31 21:08:12 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:07:02 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:06:25 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-31 21:06:24 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:06:23 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:06:21 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:06:20 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-05-31 21:05:20 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.030 |  |
| 2026-05-31 21:05:11 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-31 21:05:06 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:04:57 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-05-31 21:04:45 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:04:23 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:04:06 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 21:04:05 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:04:01 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:03:53 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 21:03:48 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:03:26 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:03:17 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:03:07 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:03:04 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | -0.100 |  |
| 2026-05-31 21:03:01 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:02:57 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-31 21:02:40 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:02:25 | Dunamale (Aththanagalu Oya) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-05-31 21:02:23 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-05-31 21:02:01 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:01:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.34 | 🟢 Normal | -0.030 |  |
| 2026-05-31 21:01:47 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:01:46 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:01:37 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 21:01:07 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:52:07 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 21:06:25 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-31 21:05:11 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-31 21:04:06 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 21:01:37 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 21:03:53 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:04:05 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-31 20:01:59 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:01:46 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:03:48 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:01:47 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 18:06:10 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:01:07 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:04:45 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:03:07 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:03:17 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:08:12 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:03:26 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:04:23 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:06:21 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:07:02 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:05:06 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:02:40 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:06:23 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:03:01 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:02:01 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:04:01 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-31 21:02:57 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-31 21:04:57 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-05-31 21:06:20 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-05-31 21:02:23 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-05-31 21:02:25 | Dunamale (Aththanagalu Oya) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-05-31 21:09:08 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.028 |  |
| 2026-05-31 21:05:20 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.030 |  |
| 2026-05-31 21:01:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.34 | 🟢 Normal | -0.030 |  |
| 2026-05-31 20:52:07 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.030 |  |
| 2026-05-31 21:09:01 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.047 |  |
| 2026-05-31 21:03:04 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)