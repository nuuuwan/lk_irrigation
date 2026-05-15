# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_16:13:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,639 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 16:13:16 | Magura (Kalu Ganga) | 4.42 | 🟡 Alert | -0.076 |  |
| 2026-05-15 16:12:10 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.034 |  |
| 2026-05-15 16:11:58 | Dunamale (Aththanagalu Oya) | 4.74 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 16:09:30 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-05-15 16:08:35 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-15 16:08:19 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -0.028 |  |
| 2026-05-15 16:08:01 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-15 16:07:47 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-15 16:07:44 | Baddegama (Gin Ganga) | 3.32 | 🟢 Normal | -0.010 |  |
| 2026-05-15 16:07:30 | Ellagawa (Kalu Ganga) | 8.71 | 🟢 Normal | 0.000 |  |
| 2026-05-15 16:07:05 | Badalgama (Maha Oya) | 4.20 | 🟢 Normal | -0.039 |  |
| 2026-05-15 16:07:00 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-15 16:05:59 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | -0.114 |  |
| 2026-05-15 16:04:55 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-15 16:04:06 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-05-15 16:03:49 | Panadugama (Nilwala Ganga) | 4.20 | 🟢 Normal | -0.031 |  |
| 2026-05-15 16:03:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.01 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-15 16:03:35 | Moragaswewa (Deduru Oya) | 3.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 16:03:34 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 16:03:18 | Glencourse (Kelani Ganga) | 11.91 | 🟢 Normal | -0.180 |  |
| 2026-05-15 16:03:18 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-15 16:03:09 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 16:03:00 | Hanwella (Kelani Ganga) | 5.36 | 🟢 Normal | -0.130 |  |
| 2026-05-15 16:02:58 | Giriulla (Maha Oya) | 3.03 | 🟢 Normal | -0.059 |  |
| 2026-05-15 16:02:57 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-15 16:02:46 | Rathnapura (Kalu Ganga) | 4.36 | 🟢 Normal | -0.044 |  |
| 2026-05-15 16:02:12 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-15 16:02:11 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-15 16:01:52 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.040 |  |
| 2026-05-15 16:01:33 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.358 | 🔺 Rising |
| 2026-05-15 16:01:32 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-15 16:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-15 16:00:42 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-05-15 16:00:41 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-05-15 16:00:32 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-05-15 16:00:23 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.012 |  |
| 2026-05-15 16:00:20 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.013 |  |
| 2026-05-15 16:00:14 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.010 |  |
| 2026-05-15 16:00:09 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 16:03:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.01 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-15 16:11:58 | Dunamale (Aththanagalu Oya) | 4.74 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 16:13:16 | Magura (Kalu Ganga) | 4.42 | 🟡 Alert | -0.076 |  |
| 2026-05-15 16:01:33 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.358 | 🔺 Rising |
| 2026-05-15 16:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-15 16:03:35 | Moragaswewa (Deduru Oya) | 3.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 16:03:09 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 16:07:47 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-15 16:01:32 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-15 16:03:34 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 16:00:42 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-05-15 15:04:04 | Galgamuwa (Mee Oya) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-05-15 16:02:57 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-15 16:07:30 | Ellagawa (Kalu Ganga) | 8.71 | 🟢 Normal | 0.000 |  |
| 2026-05-15 16:04:55 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-15 16:08:35 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-15 16:03:18 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-15 16:00:41 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-05-15 16:08:01 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-15 16:00:09 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-15 16:02:12 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-15 16:09:30 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-05-15 16:07:00 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-15 16:07:44 | Baddegama (Gin Ganga) | 3.32 | 🟢 Normal | -0.010 |  |
| 2026-05-15 16:00:14 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.010 |  |
| 2026-05-15 16:00:32 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-05-15 16:04:06 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-05-15 16:00:23 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.012 |  |
| 2026-05-15 16:00:20 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.013 |  |
| 2026-05-15 16:08:19 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -0.028 |  |
| 2026-05-15 16:03:49 | Panadugama (Nilwala Ganga) | 4.20 | 🟢 Normal | -0.031 |  |
| 2026-05-15 16:12:10 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.034 |  |
| 2026-05-15 16:07:05 | Badalgama (Maha Oya) | 4.20 | 🟢 Normal | -0.039 |  |
| 2026-05-15 16:01:52 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.040 |  |
| 2026-05-15 16:02:46 | Rathnapura (Kalu Ganga) | 4.36 | 🟢 Normal | -0.044 |  |
| 2026-05-15 16:02:58 | Giriulla (Maha Oya) | 3.03 | 🟢 Normal | -0.059 |  |
| 2026-05-15 16:05:59 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | -0.114 |  |
| 2026-05-15 16:03:00 | Hanwella (Kelani Ganga) | 5.36 | 🟢 Normal | -0.130 |  |
| 2026-05-15 16:03:18 | Glencourse (Kelani Ganga) | 11.91 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)