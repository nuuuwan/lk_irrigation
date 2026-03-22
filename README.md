# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--22_15:18:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **104,390 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 15:18:57 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:12:14 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:12:08 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-03-22 15:11:30 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:10:03 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | -0.019 |  |
| 2026-03-22 15:08:43 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.029 |  |
| 2026-03-22 15:07:44 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | -0.009 |  |
| 2026-03-22 15:07:36 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:07:21 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:06:44 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | -0.018 |  |
| 2026-03-22 15:06:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.040 |  |
| 2026-03-22 15:06:36 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:05:26 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-22 15:05:17 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-03-22 15:04:22 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:04:20 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:04:20 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-03-22 15:04:20 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.019 |  |
| 2026-03-22 15:04:15 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-03-22 15:03:59 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:03:57 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.019 |  |
| 2026-03-22 15:03:48 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-03-22 15:03:31 | Weraganthota (Mahaweli Ganga) | -2.64 | 🟢 Normal | -0.094 |  |
| 2026-03-22 15:03:23 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | -0.011 |  |
| 2026-03-22 15:03:08 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:03:02 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-03-22 15:02:48 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:02:35 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:02:27 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:02:25 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-22 15:02:18 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 15:02:04 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:01:58 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.054 |  |
| 2026-03-22 15:01:55 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:01:55 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:01:44 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:01:38 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.052 |  |
| 2026-03-22 15:01:25 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-03-22 15:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:00:13 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 15:04:20 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-03-22 15:04:15 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-03-22 15:12:08 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-03-22 15:05:26 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-22 15:02:25 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-22 15:02:18 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 15:02:27 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:01:55 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:02:48 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:06:36 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:01:55 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:18:57 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:11:30 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:04:20 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:07:36 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:02:35 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:00:13 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:04:22 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:03:59 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:12:14 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:07:21 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:02:04 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:03:08 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-22 15:07:44 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | -0.009 |  |
| 2026-03-22 15:03:02 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-03-22 15:03:48 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-03-22 15:03:23 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | -0.011 |  |
| 2026-03-22 15:06:44 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | -0.018 |  |
| 2026-03-22 15:10:03 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | -0.019 |  |
| 2026-03-22 15:04:20 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.019 |  |
| 2026-03-22 15:03:57 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.019 |  |
| 2026-03-22 15:01:25 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-03-22 15:05:17 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-03-22 15:08:43 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.029 |  |
| 2026-03-22 15:06:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | -0.040 |  |
| 2026-03-22 15:01:38 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.052 |  |
| 2026-03-22 15:01:58 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.054 |  |
| 2026-03-22 15:03:31 | Weraganthota (Mahaweli Ganga) | -2.64 | 🟢 Normal | -0.094 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)