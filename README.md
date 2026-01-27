# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--27_23:38:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **57,436 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-27 23:38:55 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:15:02 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.018 |  |
| 2026-01-27 23:11:33 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:08:44 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:08:13 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:08:09 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:07:08 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:06:08 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.010 |  |
| 2026-01-27 23:06:07 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:05:52 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:05:45 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:04:57 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 23:04:38 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 23:04:20 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-27 23:03:53 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:03:50 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:03:48 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:03:48 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:03:20 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.081 |  |
| 2026-01-27 23:03:17 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:02:22 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.149 |  |
| 2026-01-27 23:02:21 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:02:17 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:02:01 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:01:53 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:01:34 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:01:25 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2026-01-27 23:01:21 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:01:21 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:01:13 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:00:52 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-01-27 23:00:48 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:00:46 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:00:39 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-01-27 23:00:08 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-27 23:00:52 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-01-27 18:01:37 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-27 23:04:20 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-27 23:04:57 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 23:04:38 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 23:03:50 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:00:08 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:38:55 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:01:21 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:03:53 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:00:46 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:05:52 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:07:08 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:03:48 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:11:33 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:03:48 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-27 22:05:46 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:06:07 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:01:21 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:08:13 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:02:21 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:05:45 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:02:17 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:02:01 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:01:34 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:00:48 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:03:17 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:08:44 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:01:13 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:08:09 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-27 23:00:39 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-01-27 23:06:08 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.010 |  |
| 2026-01-27 17:06:09 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-01-27 23:15:02 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.018 |  |
| 2026-01-27 18:02:53 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-01-27 22:01:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | -0.021 |  |
| 2026-01-27 23:01:25 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2026-01-27 23:03:20 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.081 |  |
| 2026-01-27 23:02:22 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)