# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--28_13:25:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **218,534 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-28 13:25:23 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.016 |  |
| 2026-07-28 13:20:01 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:18:50 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:15:07 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-28 13:13:36 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-07-28 13:09:43 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-28 13:08:46 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.089 |  |
| 2026-07-28 13:08:09 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-07-28 13:07:08 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:07:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.019 |  |
| 2026-07-28 13:07:01 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:06:20 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.041 |  |
| 2026-07-28 13:06:10 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:05:57 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-28 13:05:55 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-28 13:05:46 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-28 13:05:41 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.029 |  |
| 2026-07-28 13:04:44 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-28 13:04:43 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:04:25 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:04:19 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:04:12 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-28 13:04:01 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-28 13:03:54 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:03:43 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:03:41 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-07-28 13:03:17 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-07-28 13:02:59 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:02:44 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-28 13:02:25 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:01:54 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:01:41 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:01:34 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:01:34 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:01:17 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:01:06 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:00:59 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-28 13:00:58 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-28 13:03:41 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-07-28 13:08:09 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-07-28 13:13:36 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-07-28 13:04:01 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-28 13:04:12 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-07-28 13:04:44 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-28 13:05:55 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-28 13:05:57 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-28 13:05:46 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-28 13:00:59 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-28 13:02:44 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-28 13:15:07 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-28 13:09:43 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-28 13:02:25 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:01:06 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:06:10 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:01:41 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:01:34 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:02:59 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:01:54 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:04:19 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:03:54 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:04:25 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:01:17 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:01:34 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:18:50 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:03:43 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:04:43 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-28 12:02:34 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:00:58 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:07:01 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:20:01 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:07:08 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-28 13:03:17 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-07-28 13:25:23 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.016 |  |
| 2026-07-28 13:07:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.019 |  |
| 2026-07-28 13:05:41 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.029 |  |
| 2026-07-28 13:06:20 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.041 |  |
| 2026-07-28 13:08:46 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)