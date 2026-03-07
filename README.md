# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--07_16:10:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **91,785 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 16:10:33 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-07 16:10:03 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-07 16:09:19 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:08:25 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:07:31 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:07:27 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:06:35 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:05:58 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:05:57 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:05:56 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-03-07 16:05:34 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 16:05:20 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-03-07 16:04:52 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-03-07 16:03:56 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.857 |  |
| 2026-03-07 16:03:48 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.039 |  |
| 2026-03-07 16:03:35 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:03:24 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | -0.010 |  |
| 2026-03-07 16:03:20 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-03-07 16:03:17 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-03-07 16:03:14 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | -0.857 |  |
| 2026-03-07 16:03:01 | Weraganthota (Mahaweli Ganga) | -1.85 | 🟢 Normal | -0.068 |  |
| 2026-03-07 16:02:57 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-03-07 16:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-03-07 16:02:30 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-03-07 16:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-03-07 16:02:17 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:02:03 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:01:37 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-07 16:01:30 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:01:27 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:01:24 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 16:01:22 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:01:10 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:01:03 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:01:03 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:00:39 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:00:32 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-07 16:00:22 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:00:19 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-07 16:00:12 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 16:03:17 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-03-07 16:01:37 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-07 16:10:03 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-07 16:00:32 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-07 16:01:24 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 16:05:34 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 16:10:33 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-07 16:01:27 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:00:39 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:01:03 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:01:30 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:01:22 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:02:03 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:09:19 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:01:03 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:05:58 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:03:35 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-07 14:03:12 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:07:27 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:00:22 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:02:17 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:06:35 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:01:10 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:08:25 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:07:31 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 16:05:56 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-03-07 16:04:52 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-03-07 16:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-03-07 16:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-03-07 16:02:30 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-03-07 16:03:24 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | -0.010 |  |
| 2026-03-07 16:00:12 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-03-07 16:00:19 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-07 16:05:20 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-03-07 16:02:57 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-03-07 16:03:20 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-03-07 16:03:48 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.039 |  |
| 2026-03-07 16:03:01 | Weraganthota (Mahaweli Ganga) | -1.85 | 🟢 Normal | -0.068 |  |
| 2026-03-07 16:03:56 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.857 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)