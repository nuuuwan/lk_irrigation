# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_14:15:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,642 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 14:15:06 | Horowpothana (Yan Oya) | 2.56 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-01-12 14:14:52 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:14:50 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.065 |  |
| 2026-01-12 14:13:24 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:10:32 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-01-12 14:09:10 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.092 |  |
| 2026-01-12 14:08:11 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:07:25 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:07:16 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-01-12 14:07:00 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.218 |  |
| 2026-01-12 14:06:45 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:06:33 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:05:36 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-12 14:05:26 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-12 14:05:08 | Yaka Wewa (Ma Oya) | 3.25 | 🟢 Normal | 0.454 | 🔺 Rising |
| 2026-01-12 14:04:39 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:04:27 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-12 14:04:23 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-01-12 14:03:24 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:03:22 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.031 |  |
| 2026-01-12 14:03:21 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.011 |  |
| 2026-01-12 14:03:09 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-01-12 14:03:03 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | -0.091 |  |
| 2026-01-12 14:02:37 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-12 14:02:34 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.051 |  |
| 2026-01-12 14:02:33 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:02:32 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:02:21 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 14:02:08 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:01:53 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-01-12 14:01:42 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:01:20 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:01:20 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-01-12 14:01:17 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:00:47 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:00:37 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:00:13 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-01-12 14:00:09 | Weraganthota (Mahaweli Ganga) | -1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 13:56:47 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 14:05:08 | Yaka Wewa (Ma Oya) | 3.25 | 🟢 Normal | 0.454 | 🔺 Rising |
| 2026-01-12 14:01:20 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-01-12 14:15:06 | Horowpothana (Yan Oya) | 2.56 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-01-12 14:04:27 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-12 14:02:37 | Badalgama (Maha Oya) | 2.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-12 14:05:36 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-12 14:00:09 | Weraganthota (Mahaweli Ganga) | -1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 14:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 14:02:21 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:01:17 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:00:37 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:04:39 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:02:08 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:02:33 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:14:52 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:13:24 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:07:25 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:01:42 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:00:47 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:06:45 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:08:11 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:01:20 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:02:32 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:03:24 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:05:26 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-12 14:10:32 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-01-12 14:00:13 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-01-12 14:03:21 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.011 |  |
| 2026-01-12 14:04:23 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-01-12 14:07:16 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-01-12 13:56:47 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.012 |  |
| 2026-01-12 14:03:09 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-01-12 14:03:22 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.031 |  |
| 2026-01-12 14:01:53 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-01-12 14:02:34 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.051 |  |
| 2026-01-12 14:14:50 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.065 |  |
| 2026-01-12 14:03:03 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | -0.091 |  |
| 2026-01-12 14:09:10 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.092 |  |
| 2026-01-12 14:07:00 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.218 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)