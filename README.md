# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--12_14:15:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **95,409 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 14:15:58 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:12:55 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:12:01 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:11:35 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-12 14:10:16 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-12 14:10:13 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-03-12 14:07:36 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-12 14:06:57 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-03-12 14:06:33 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:06:14 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:05:58 | Ellagawa (Kalu Ganga) | 0.50 | 🟢 Normal | -47.368 |  |
| 2026-03-12 14:05:33 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-12 14:05:18 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.042 |  |
| 2026-03-12 14:05:14 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:05:10 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-12 14:05:08 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:04:48 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:04:34 | Hanwella (Kelani Ganga) | 0.94 | 🟢 Normal | -0.059 |  |
| 2026-03-12 14:04:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | -0.019 |  |
| 2026-03-12 14:04:30 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.019 |  |
| 2026-03-12 14:04:30 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:03:55 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:03:45 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:03:12 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-03-12 14:02:54 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:02:40 | Manampitiya (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-12 14:02:21 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:02:12 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 14:02:09 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-03-12 14:02:09 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-03-12 14:02:08 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:01:58 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:01:53 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:01:51 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | -47.368 |  |
| 2026-03-12 14:01:43 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:01:39 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-03-12 14:01:25 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.031 |  |
| 2026-03-12 14:00:54 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:00:10 | Weraganthota (Mahaweli Ganga) | -2.57 | 🟢 Normal | -0.081 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 14:01:39 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-03-12 14:11:35 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-12 14:07:36 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-12 14:05:10 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-12 12:12:54 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-12 14:05:33 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-12 14:10:16 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-12 14:02:12 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 14:01:58 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:02:54 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:02:21 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:01:53 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:03:45 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:04:48 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:12:55 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:03:55 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:06:14 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:04:30 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:12:01 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:15:58 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:05:08 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:02:08 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:06:33 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:00:54 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:01:43 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:02:40 | Manampitiya (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-12 14:02:09 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-03-12 14:02:09 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-03-12 14:04:30 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.019 |  |
| 2026-03-12 14:04:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | -0.019 |  |
| 2026-03-12 14:03:12 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-03-12 14:10:13 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-03-12 14:06:57 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-03-12 14:01:25 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.031 |  |
| 2026-03-12 14:05:18 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.042 |  |
| 2026-03-12 14:04:34 | Hanwella (Kelani Ganga) | 0.94 | 🟢 Normal | -0.059 |  |
| 2026-03-12 14:00:10 | Weraganthota (Mahaweli Ganga) | -2.57 | 🟢 Normal | -0.081 |  |
| 2026-03-12 14:05:58 | Ellagawa (Kalu Ganga) | 0.50 | 🟢 Normal | -47.368 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)