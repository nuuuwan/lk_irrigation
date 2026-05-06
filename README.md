# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_04:03:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **144,945 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 04:03:27 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-07 04:03:13 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-05-07 04:03:07 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | 0.568 | 🔺 Rising |
| 2026-05-07 04:02:57 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-05-07 04:02:44 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.011 |  |
| 2026-05-07 04:02:44 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.085 |  |
| 2026-05-07 04:02:30 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | 0.326 | 🔺 Rising |
| 2026-05-07 04:02:15 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-07 04:02:09 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.146 |  |
| 2026-05-07 04:01:27 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.011 |  |
| 2026-05-07 04:01:25 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-07 04:01:23 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-05-07 04:01:17 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-07 04:01:11 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.003 |  |
| 2026-05-07 04:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-07 04:01:00 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-05-07 04:00:59 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-07 04:00:58 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-05-07 04:00:49 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 04:00:34 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.030 |  |
| 2026-05-07 03:14:59 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.114 |  |
| 2026-05-07 03:11:15 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.033 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 02:14:21 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | 576.000 | 🔺 Rising |
| 2026-05-07 04:03:07 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | 0.568 | 🔺 Rising |
| 2026-05-07 03:05:51 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | 0.334 | 🔺 Rising |
| 2026-05-07 04:02:30 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | 0.326 | 🔺 Rising |
| 2026-05-06 22:14:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-05-07 04:03:13 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-05-07 04:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-07 02:33:22 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-07 04:01:17 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-07 04:01:25 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-07 01:01:19 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-07 03:03:54 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-07 03:11:15 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-07 03:04:23 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-07 04:00:49 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 18:05:19 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 03:10:30 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-07 03:04:59 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-07 04:01:11 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.003 |  |
| 2026-05-07 03:03:39 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.003 |  |
| 2026-05-07 04:00:59 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-07 03:02:11 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 04:00:58 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-05-07 04:03:27 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-07 04:02:15 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-06 18:02:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.010 |  |
| 2026-05-06 18:01:28 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-07 03:03:39 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-07 04:01:23 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-05-07 04:02:44 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.011 |  |
| 2026-05-07 04:01:27 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.011 |  |
| 2026-05-07 04:02:57 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-05-07 04:01:00 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-05-07 04:00:34 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.030 |  |
| 2026-05-07 04:02:44 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.085 |  |
| 2026-05-07 03:14:59 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.114 |  |
| 2026-05-07 04:02:09 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.146 |  |
| 2026-05-07 03:05:03 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.286 |  |
| 2026-05-07 03:01:49 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -2.082 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)