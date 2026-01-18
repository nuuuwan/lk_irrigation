# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--18_17:12:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **49,142 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 17:12:51 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:12:45 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:09:07 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:08:39 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-01-18 17:08:29 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:06:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:06:46 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:06:45 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:06:30 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-01-18 17:06:18 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:05:34 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-18 17:05:13 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-18 17:05:12 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.019 |  |
| 2026-01-18 17:04:47 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | -0.011 |  |
| 2026-01-18 17:04:39 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.080 |  |
| 2026-01-18 17:04:07 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:03:56 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:03:52 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:03:50 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:03:45 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:03:30 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:03:23 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:03:22 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:03:06 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-01-18 17:02:27 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-18 17:02:15 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:01:58 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.011 |  |
| 2026-01-18 17:01:44 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:01:21 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:01:18 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.127 |  |
| 2026-01-18 17:01:17 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:01:16 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:01:12 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:01:04 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-18 17:00:45 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-01-18 17:00:44 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.020 |  |
| 2026-01-18 17:00:42 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:00:27 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:46:27 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 17:05:13 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-18 17:02:27 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-18 17:01:04 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-18 17:05:34 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-18 17:01:21 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:00:27 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:09:07 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:00:42 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:12:51 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:03:45 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:06:46 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:03:56 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:01:12 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:03:30 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:06:18 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:06:49 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:06:45 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:46:27 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:01:16 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:02:15 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:08:29 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:03:50 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:03:23 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:01:44 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:12:45 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:01:17 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:03:52 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-18 17:06:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-01-18 16:15:20 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | -0.009 |  |
| 2026-01-18 17:08:39 | Padiyathalawa (Maduru Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-01-18 17:06:30 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-01-18 17:03:06 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-01-18 17:01:58 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.011 |  |
| 2026-01-18 17:00:45 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-01-18 17:04:47 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | -0.011 |  |
| 2026-01-18 17:05:12 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.019 |  |
| 2026-01-18 17:00:44 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.020 |  |
| 2026-01-18 17:04:39 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.080 |  |
| 2026-01-18 17:01:18 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)