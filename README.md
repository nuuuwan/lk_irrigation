# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--21_10:13:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **51,553 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 10:13:54 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:13:10 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:09:11 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-01-21 10:08:32 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:08:30 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-21 10:08:22 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:08:08 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-21 10:08:01 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:05:39 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:05:29 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-01-21 10:05:03 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-21 10:05:02 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:04:52 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:04:25 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-21 10:04:16 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:04:10 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:03:53 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 10:03:48 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-01-21 10:03:38 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:03:31 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-01-21 10:03:19 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:03:19 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.059 |  |
| 2026-01-21 10:03:00 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-01-21 10:02:55 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:02:52 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:02:33 | Putupaula (Kalu Ganga) | 0.27 | 🟢 Normal | -0.081 |  |
| 2026-01-21 10:02:29 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:02:19 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:02:19 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.050 |  |
| 2026-01-21 10:02:06 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-21 10:02:01 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:01:52 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:01:33 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:01:22 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:01:17 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:00:32 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:00:22 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:00:07 | Padiyathalawa (Maduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 10:09:11 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-01-21 10:02:06 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-21 10:04:25 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-21 10:08:30 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-21 10:05:03 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-21 10:08:08 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-21 10:03:53 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 10:01:22 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:02:55 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:00:32 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:00:22 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:05:02 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:08:22 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:13:54 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:04:52 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:08:01 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:01:17 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:04:16 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:02:01 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:03:38 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:00:07 | Padiyathalawa (Maduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:03:19 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:01:52 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:05:39 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:02:52 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:01:33 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:02:19 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:08:32 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:04:10 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:13:10 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:02:29 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-21 10:05:29 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-01-21 10:03:31 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-01-21 10:03:00 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-01-21 10:03:48 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-01-21 09:12:33 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.044 |  |
| 2026-01-21 10:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.050 |  |
| 2026-01-21 10:03:19 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.059 |  |
| 2026-01-21 10:02:33 | Putupaula (Kalu Ganga) | 0.27 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)