# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--08_16:09:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,110 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 16:09:48 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-01-08 16:08:42 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 16:07:53 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:07:41 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:07:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-08 16:06:50 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-08 16:06:46 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:06:22 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-01-08 16:06:11 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:05:57 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-08 16:05:37 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:05:36 | Thaldena (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 16:05:33 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | -0.077 |  |
| 2026-01-08 16:04:09 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:03:55 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:03:45 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-08 16:03:38 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:03:29 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 16:03:21 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -1.125 |  |
| 2026-01-08 16:02:58 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | -0.010 |  |
| 2026-01-08 16:02:49 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -1.125 |  |
| 2026-01-08 16:02:40 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.108 |  |
| 2026-01-08 16:02:31 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-01-08 16:02:21 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-01-08 16:02:03 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-01-08 16:01:45 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-01-08 16:01:17 | Weraganthota (Mahaweli Ganga) | -1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 16:01:11 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-01-08 16:00:45 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-01-08 16:00:41 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-08 16:00:40 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.076 |  |
| 2026-01-08 16:00:14 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-08 16:00:10 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:29:36 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-01-08 15:29:35 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-01-08 15:19:04 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 16:06:22 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-01-08 16:02:03 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-01-08 16:02:31 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-01-08 16:06:50 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-08 16:07:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-08 16:00:14 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-08 16:00:41 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-08 16:03:29 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 16:01:17 | Weraganthota (Mahaweli Ganga) | -1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 16:05:36 | Thaldena (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 16:08:42 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 16:05:57 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-08 16:00:10 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:06:46 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:07:53 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:04:34 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:03:55 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:04:09 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:03:38 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:07:41 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:05:37 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:06:11 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:19:04 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:09:48 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-01-08 16:03:45 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-08 16:01:11 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-01-08 16:01:45 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-01-08 16:02:58 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | -0.010 |  |
| 2026-01-08 15:01:31 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-08 16:00:45 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-01-08 15:02:25 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-01-08 16:02:21 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-01-08 15:06:25 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-01-08 15:04:02 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | -0.024 |  |
| 2026-01-08 15:07:07 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.031 |  |
| 2026-01-08 16:00:40 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.076 |  |
| 2026-01-08 16:05:33 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | -0.077 |  |
| 2026-01-08 16:02:40 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.108 |  |
| 2026-01-08 16:03:21 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -1.125 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)