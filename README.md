# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_15:12:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,148 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 15:12:15 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:09:59 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:09:56 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:09:33 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-12 15:08:09 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.037 |  |
| 2026-04-12 15:07:16 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-04-12 15:07:02 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:06:36 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:05:49 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | -0.009 |  |
| 2026-04-12 15:05:15 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-12 15:05:09 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.025 |  |
| 2026-04-12 15:05:06 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:04:54 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-04-12 15:04:51 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:04:42 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:04:19 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 15:03:58 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:03:47 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-12 15:03:44 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-04-12 15:03:18 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:03:14 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:03:07 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:02:59 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-04-12 15:02:58 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-12 15:02:56 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:02:47 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:02:45 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:02:44 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.030 |  |
| 2026-04-12 15:02:24 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:02:24 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:02:17 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:02:04 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:01:52 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 15:01:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.040 |  |
| 2026-04-12 15:01:43 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:01:26 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:01:14 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:01:12 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.020 |  |
| 2026-04-12 15:01:10 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.034 |  |
| 2026-04-12 15:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-12 15:01:03 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | -0.178 |  |
| 2026-04-12 15:00:30 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 15:09:33 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-12 15:03:47 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-12 15:02:58 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-12 15:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-12 15:01:52 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 15:04:19 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 15:05:15 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-12 15:02:04 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:03:14 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:02:47 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:01:43 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:02:56 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:01:14 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:06:36 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:09:59 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:04:42 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:12:15 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:03:58 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:00:30 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:02:24 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:04:51 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:02:17 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:02:24 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:03:07 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:02:45 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:07:02 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:09:56 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-12 15:05:49 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | -0.009 |  |
| 2026-04-12 15:03:44 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-04-12 15:04:54 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-04-12 15:02:59 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-04-12 15:01:12 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.020 |  |
| 2026-04-12 15:05:09 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.025 |  |
| 2026-04-12 15:02:44 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.030 |  |
| 2026-04-12 15:07:16 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-04-12 15:01:10 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.034 |  |
| 2026-04-12 15:08:09 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.037 |  |
| 2026-04-12 15:01:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.040 |  |
| 2026-04-12 15:01:03 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | -0.178 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)