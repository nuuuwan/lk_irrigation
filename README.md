# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--10_13:19:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **94,371 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 13:19:43 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:12:17 | Dunamale (Aththanagalu Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:11:47 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:10:05 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:09:59 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:09:50 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:09:25 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:09:24 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:08:05 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 13:08:02 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | -0.028 |  |
| 2026-03-10 13:05:58 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:05:20 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.019 |  |
| 2026-03-10 13:04:24 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:04:23 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 13:04:15 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:04:12 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.019 |  |
| 2026-03-10 13:04:10 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:03:54 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:03:37 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 13:03:37 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:03:36 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:03:30 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-10 13:03:25 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:03:13 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:02:59 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.021 |  |
| 2026-03-10 13:02:46 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:02:35 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:02:23 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | -0.129 |  |
| 2026-03-10 13:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.29 | 🟢 Normal | -0.040 |  |
| 2026-03-10 13:02:00 | Glencourse (Kelani Ganga) | 8.19 | 🟢 Normal | -0.062 |  |
| 2026-03-10 13:01:55 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:01:47 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | -0.010 |  |
| 2026-03-10 13:01:34 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-10 13:01:31 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:01:27 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:01:20 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:01:00 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-10 13:00:52 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-03-10 13:00:41 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-03-10 12:57:45 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 13:03:30 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-10 13:00:41 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-03-10 13:01:34 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-10 13:01:00 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-10 13:08:05 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 13:03:37 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 13:04:23 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 13:02:35 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:01:55 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:01:20 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:04:24 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:03:13 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:09:24 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-10 12:04:23 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:04:10 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:01:27 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:03:37 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:02:46 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:03:25 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:03:36 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:12:17 | Dunamale (Aththanagalu Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:11:47 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:10:05 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:05:58 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:03:54 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:04:15 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:19:43 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:01:31 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:09:25 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-10 13:01:47 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | -0.010 |  |
| 2026-03-10 13:00:52 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-03-10 13:04:12 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.019 |  |
| 2026-03-10 13:05:20 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.019 |  |
| 2026-03-10 13:02:59 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.021 |  |
| 2026-03-10 12:57:45 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.022 |  |
| 2026-03-10 13:08:02 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | -0.028 |  |
| 2026-03-10 13:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.29 | 🟢 Normal | -0.040 |  |
| 2026-03-10 13:02:00 | Glencourse (Kelani Ganga) | 8.19 | 🟢 Normal | -0.062 |  |
| 2026-03-10 13:02:23 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)