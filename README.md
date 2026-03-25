# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--25_21:14:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **107,285 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 21:14:42 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-25 21:14:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | -0.009 |  |
| 2026-03-25 21:13:00 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.036 |  |
| 2026-03-25 21:11:16 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:09:54 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:09:48 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-03-25 21:09:20 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:07:36 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:06:52 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-25 21:06:29 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.168 |  |
| 2026-03-25 21:06:24 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:06:05 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.089 |  |
| 2026-03-25 21:05:55 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-25 21:05:49 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:05:06 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:04:57 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:04:38 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-25 21:04:30 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:04:25 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-25 21:04:09 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.166 |  |
| 2026-03-25 21:04:06 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | -0.011 |  |
| 2026-03-25 21:03:53 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:03:47 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:03:38 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:03:37 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:03:35 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-03-25 21:03:12 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:02:25 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:02:24 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:02:04 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:02:03 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:01:53 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:01:51 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:01:41 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.027 |  |
| 2026-03-25 21:01:28 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:01:21 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:00:44 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-25 21:00:19 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 21:04:25 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-25 21:14:42 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-25 21:05:55 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-25 21:04:38 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-25 21:02:25 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:01:21 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:01:51 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:00:19 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:03:47 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:03:38 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-25 18:00:29 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:09:20 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:06:24 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:01:28 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:05:06 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:04:30 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:03:12 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:02:24 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:03:37 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:05:49 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:11:16 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:07:36 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-25 18:02:01 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:02:04 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:09:54 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:01:53 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:03:53 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-25 21:14:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | -0.009 |  |
| 2026-03-25 21:06:52 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-25 21:03:35 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-03-25 21:09:48 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-03-25 21:00:44 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-25 21:04:06 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | -0.011 |  |
| 2026-03-25 21:01:41 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.027 |  |
| 2026-03-25 21:13:00 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.036 |  |
| 2026-03-25 18:01:39 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.060 |  |
| 2026-03-25 21:06:05 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.089 |  |
| 2026-03-25 21:04:09 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.166 |  |
| 2026-03-25 21:06:29 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.168 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)