# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_16:24:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **110,699 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 16:24:23 | Magura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:21:04 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:12:40 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:10:46 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.036 |  |
| 2026-03-29 16:10:01 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-03-29 16:09:31 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:09:18 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:09:02 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:08:14 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:07:16 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-03-29 16:07:11 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:07:07 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.018 |  |
| 2026-03-29 16:06:23 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 378.000 | 🔺 Rising |
| 2026-03-29 16:06:21 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 378.000 | 🔺 Rising |
| 2026-03-29 16:05:46 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:04:21 | Ellagawa (Kalu Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:04:05 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:04:02 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:03:44 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:03:44 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | -0.020 |  |
| 2026-03-29 16:03:14 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:03:11 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:03:08 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:02:58 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:02:44 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:02:33 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:02:32 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-03-29 16:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-03-29 16:01:37 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:01:34 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:01:28 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-03-29 16:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:01:17 | Rathnapura (Kalu Ganga) | 0.38 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-29 16:01:15 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:01:15 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:01:01 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | -0.034 |  |
| 2026-03-29 16:00:37 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:00:23 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.110 |  |
| 2026-03-29 16:00:15 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-29 16:00:11 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 16:06:23 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 378.000 | 🔺 Rising |
| 2026-03-29 16:02:32 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-03-29 16:01:17 | Rathnapura (Kalu Ganga) | 0.38 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-29 16:00:15 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-29 16:10:01 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-03-29 16:01:34 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:02:58 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:09:18 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:12:40 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:09:31 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:01:15 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:01:37 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:24:23 | Magura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:03:11 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:03:08 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:04:21 | Ellagawa (Kalu Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:05:46 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:09:02 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:02:33 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:07:11 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:00:11 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:08:14 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:03:14 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:03:44 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:04:02 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:04:05 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:00:37 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:02:44 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:01:15 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:21:04 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-29 16:01:28 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-03-29 16:07:07 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.018 |  |
| 2026-03-29 16:03:44 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | -0.020 |  |
| 2026-03-29 16:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-03-29 16:07:16 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-03-29 16:01:01 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | -0.034 |  |
| 2026-03-29 16:10:46 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.036 |  |
| 2026-03-29 16:00:23 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)