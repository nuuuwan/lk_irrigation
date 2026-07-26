# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--26_12:23:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **216,721 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-26 12:23:30 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:15:50 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:15:06 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-07-26 12:10:44 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:08:19 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-07-26 12:07:46 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-07-26 12:07:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-07-26 12:06:31 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-07-26 12:06:31 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:06:16 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:05:53 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:05:45 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:05:36 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.015 |  |
| 2026-07-26 12:04:46 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-07-26 12:04:36 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:04:09 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:04:05 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-07-26 12:04:04 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-07-26 12:03:55 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:03:44 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-07-26 12:03:43 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-07-26 12:03:19 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:03:10 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-07-26 12:02:59 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:02:51 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-26 12:02:46 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:02:34 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:02:25 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:02:24 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:02:18 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:02:18 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -0.010 |  |
| 2026-07-26 12:02:12 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:02:07 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:01:54 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:01:44 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.190 |  |
| 2026-07-26 12:01:36 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:01:25 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:01:22 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:01:21 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-07-26 12:00:10 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-26 12:03:44 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-07-26 12:01:21 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-07-26 12:04:46 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-07-26 12:04:05 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-07-26 12:08:19 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-07-26 12:07:46 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-07-26 12:00:10 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-26 12:15:06 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-07-26 12:02:07 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:02:18 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:15:50 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:01:25 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:23:30 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-26 11:00:21 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:03:55 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:02:46 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:04:09 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:02:25 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:05:45 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:04:36 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:01:22 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:02:34 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:01:54 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:02:12 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:03:19 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:10:44 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:06:16 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:01:36 | Thanthirimale (Malwathu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:02:59 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:05:53 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:02:24 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-26 12:04:04 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-07-26 12:03:10 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-07-26 12:02:51 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-26 12:02:18 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -0.010 |  |
| 2026-07-26 12:06:31 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-07-26 12:05:36 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.015 |  |
| 2026-07-26 12:07:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-07-26 12:01:44 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.190 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)