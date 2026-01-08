# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--08_10:17:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,876 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 10:17:43 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-08 10:16:43 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.014 |  |
| 2026-01-08 10:15:03 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-08 10:11:03 | Panadugama (Nilwala Ganga) | 3.73 | 🟢 Normal | -0.037 |  |
| 2026-01-08 10:10:05 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-01-08 10:09:40 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 10:08:44 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-08 10:08:34 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-08 10:08:20 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-01-08 10:07:40 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-01-08 10:07:04 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-01-08 10:07:02 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-01-08 10:06:49 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-01-08 10:05:55 | Kithulgala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.039 |  |
| 2026-01-08 10:05:34 | Siyambalanduwa (Heda Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-01-08 10:05:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.067 |  |
| 2026-01-08 10:05:05 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.080 |  |
| 2026-01-08 10:04:33 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-01-08 10:04:06 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.041 |  |
| 2026-01-08 10:03:55 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-01-08 10:03:44 | Padiyathalawa (Maduru Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-08 10:03:43 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-01-08 10:03:40 | Weraganthota (Mahaweli Ganga) | -1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-08 10:03:30 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-01-08 10:03:29 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 10:03:23 | Katharagama (Menik Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-01-08 10:02:39 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-01-08 10:02:21 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.102 |  |
| 2026-01-08 10:01:54 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-08 10:01:54 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.121 |  |
| 2026-01-08 10:01:50 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-08 10:01:49 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-08 10:01:43 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 10:01:38 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 10:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-08 10:00:53 | Manampitiya (Mahaweli Ganga) | 2.31 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 10:07:04 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-01-08 10:15:03 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-01-08 10:01:54 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-08 09:10:12 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-08 10:08:44 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-08 10:00:53 | Manampitiya (Mahaweli Ganga) | 2.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-08 10:09:40 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 10:03:40 | Weraganthota (Mahaweli Ganga) | -1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-08 10:01:50 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-08 10:01:43 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 10:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-08 09:05:14 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-08 10:03:29 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 10:17:43 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-08 10:08:34 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-08 10:04:33 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-01-08 10:03:44 | Padiyathalawa (Maduru Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-08 10:01:49 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-08 10:01:38 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 10:06:49 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-01-08 08:06:00 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.009 |  |
| 2026-01-08 10:07:02 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-01-08 10:07:40 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-01-08 10:05:34 | Siyambalanduwa (Heda Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-01-08 10:08:20 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-01-08 10:02:39 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-01-08 10:03:23 | Katharagama (Menik Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-01-08 10:03:30 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-01-08 10:03:43 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-01-08 10:16:43 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.014 |  |
| 2026-01-08 10:10:05 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-01-08 10:03:55 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-01-08 10:11:03 | Panadugama (Nilwala Ganga) | 3.73 | 🟢 Normal | -0.037 |  |
| 2026-01-08 10:05:55 | Kithulgala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.039 |  |
| 2026-01-08 10:04:06 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.041 |  |
| 2026-01-08 10:05:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.067 |  |
| 2026-01-08 10:05:05 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.080 |  |
| 2026-01-08 10:02:21 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.102 |  |
| 2026-01-08 10:01:54 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)