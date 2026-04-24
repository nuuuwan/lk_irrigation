# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_15:16:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,862 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 15:16:05 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | -0.052 |  |
| 2026-04-24 15:11:09 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-24 15:08:33 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.037 |  |
| 2026-04-24 15:08:10 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:08:07 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-24 15:07:55 | Panadugama (Nilwala Ganga) | 2.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-24 15:07:01 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-04-24 15:06:54 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-04-24 15:05:59 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.027 |  |
| 2026-04-24 15:05:21 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:05:07 | Galgamuwa (Mee Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:04:04 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | -0.031 |  |
| 2026-04-24 15:04:03 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:03:49 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-04-24 15:03:34 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-04-24 15:03:01 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-04-24 15:02:51 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-04-24 15:02:47 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:02:46 | Thanamalwila (Kirindi Oya) | 1.55 | 🟢 Normal | -0.030 |  |
| 2026-04-24 15:02:42 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.040 |  |
| 2026-04-24 15:02:41 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 15:02:37 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-04-24 15:02:32 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.021 |  |
| 2026-04-24 15:02:31 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:02:13 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.051 |  |
| 2026-04-24 15:02:07 | Katharagama (Menik Ganga) | 1.96 | 🟢 Normal | -0.020 |  |
| 2026-04-24 15:02:03 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-24 15:02:02 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-24 15:01:33 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:01:30 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.020 |  |
| 2026-04-24 15:01:15 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:01:13 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-24 15:01:11 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-04-24 15:01:08 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:00:47 | Kuda Oya (Kirindi Oya) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-04-24 15:00:36 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-24 15:00:15 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:00:01 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-24 14:29:57 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.052 |  |
| 2026-04-24 14:28:40 | Galgamuwa (Mee Oya) | 0.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 15:03:34 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-04-24 15:00:36 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-24 15:02:03 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-24 15:02:02 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-24 15:01:13 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-24 15:07:55 | Panadugama (Nilwala Ganga) | 2.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-24 15:11:09 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-24 15:02:41 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 15:08:07 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-24 15:08:10 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:02:31 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:01:33 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:01:15 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:00:01 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:05:07 | Galgamuwa (Mee Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:02:47 | Hanwella (Kelani Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:01:08 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:00:15 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:02:13 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:04:03 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:05:21 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-24 15:03:49 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-04-24 15:02:37 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-04-24 15:07:01 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-04-24 15:06:54 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-04-24 15:03:01 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-04-24 15:01:30 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.020 |  |
| 2026-04-24 15:00:47 | Kuda Oya (Kirindi Oya) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-04-24 15:01:11 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-04-24 15:02:07 | Katharagama (Menik Ganga) | 1.96 | 🟢 Normal | -0.020 |  |
| 2026-04-24 15:02:51 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-04-24 15:02:32 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.021 |  |
| 2026-04-24 15:05:59 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.027 |  |
| 2026-04-24 15:02:46 | Thanamalwila (Kirindi Oya) | 1.55 | 🟢 Normal | -0.030 |  |
| 2026-04-24 15:04:04 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | -0.031 |  |
| 2026-04-24 15:08:33 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.037 |  |
| 2026-04-24 15:02:42 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.040 |  |
| 2026-04-24 15:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.051 |  |
| 2026-04-24 15:16:05 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | -0.052 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)