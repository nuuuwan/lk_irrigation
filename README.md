# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--17_11:09:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **99,740 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 11:09:27 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:09:16 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:06:52 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:06:22 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:06:14 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:05:56 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-17 11:05:43 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:05:40 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:04:53 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:03:37 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | -0.156 |  |
| 2026-03-17 11:03:28 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:03:26 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-03-17 11:03:23 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:03:18 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:03:11 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.049 |  |
| 2026-03-17 11:03:05 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:02:59 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.050 |  |
| 2026-03-17 11:02:59 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | -0.011 |  |
| 2026-03-17 11:02:50 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 11:02:47 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 11:02:34 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-03-17 11:02:33 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-17 11:02:15 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-03-17 11:01:48 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.044 |  |
| 2026-03-17 11:01:41 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:01:37 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-03-17 11:01:21 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:01:16 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:00:58 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:00:43 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:00:31 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:00:09 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | -0.067 |  |
| 2026-03-17 10:16:57 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 11:03:26 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-03-17 11:02:34 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-03-17 11:02:15 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-03-17 11:02:33 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-17 11:05:56 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-17 11:02:50 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 11:02:47 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 11:03:18 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:01:16 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:00:31 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:03:05 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:03:28 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:03:10 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:00:58 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:08:35 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:09:16 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:03:11 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:07:00 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:03:23 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:05:40 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:01:41 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:01:21 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:05:43 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:06:14 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:06:22 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:09:27 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:00:43 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:06:52 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-17 10:02:35 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:04:53 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-17 11:01:37 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-03-17 10:03:15 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | -0.011 |  |
| 2026-03-17 11:02:59 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | -0.011 |  |
| 2026-03-17 10:03:45 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | -0.021 |  |
| 2026-03-17 11:01:48 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.044 |  |
| 2026-03-17 11:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.049 |  |
| 2026-03-17 11:02:59 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.050 |  |
| 2026-03-17 11:00:09 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | -0.067 |  |
| 2026-03-17 11:03:37 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | -0.156 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)