# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_01:11:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,153 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 01:11:36 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-01-12 01:09:56 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:08:10 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-12 01:07:43 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 1.044 | 🔺 Rising |
| 2026-01-12 01:06:03 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:05:56 | Manampitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-12 01:05:22 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | -0.041 |  |
| 2026-01-12 01:05:21 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-12 01:05:21 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:04:55 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:04:12 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 01:03:45 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-01-12 01:03:26 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-01-12 01:02:58 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-12 01:02:49 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:02:38 | Siyambalanduwa (Heda Oya) | 1.20 | 🟢 Normal | -0.050 |  |
| 2026-01-12 01:02:22 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.040 |  |
| 2026-01-12 01:02:17 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:02:17 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:01:54 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.219 |  |
| 2026-01-12 01:01:37 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:01:27 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-12 01:01:23 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.044 |  |
| 2026-01-12 01:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:01:07 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 01:00:57 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-01-12 01:00:39 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:00:39 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:00:07 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 01:07:43 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 1.044 | 🔺 Rising |
| 2026-01-12 00:06:33 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | 0.502 | 🔺 Rising |
| 2026-01-12 01:03:26 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-01-12 00:11:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-11 18:00:33 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-12 01:05:56 | Manampitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-12 00:02:07 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 01:01:07 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 01:04:12 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 01:05:21 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-12 01:08:10 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-12 01:02:58 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-11 18:01:30 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:00:39 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:01:37 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:19 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:06:03 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:00:39 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:03:29 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:02:17 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:09:56 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:05:21 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:02:49 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:03:08 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:04:55 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:11:36 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-01-12 01:01:27 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-12 01:00:57 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-01-12 01:00:07 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | -0.011 |  |
| 2026-01-12 01:03:45 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-01-12 00:04:19 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-01-12 00:00:08 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-01-12 01:02:22 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.040 |  |
| 2026-01-12 01:05:22 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | -0.041 |  |
| 2026-01-12 01:01:23 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.044 |  |
| 2026-01-12 01:02:38 | Siyambalanduwa (Heda Oya) | 1.20 | 🟢 Normal | -0.050 |  |
| 2026-01-12 00:05:51 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.111 |  |
| 2026-01-12 01:01:54 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.219 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)