# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--10_06:16:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **202,162 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-10 06:16:46 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-07-10 06:15:07 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:11:10 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:07:29 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 06:06:43 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:06:32 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-07-10 06:06:09 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:05:33 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:05:05 | Yaka Wewa (Ma Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:04:40 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 06:04:34 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:04:21 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:04:12 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-07-10 06:04:07 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:04:07 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:04:05 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:03:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.068 |  |
| 2026-07-10 06:03:52 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:03:48 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-10 06:03:31 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.013 |  |
| 2026-07-10 06:03:30 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:03:27 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | -0.074 |  |
| 2026-07-10 06:03:25 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:02:30 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.031 |  |
| 2026-07-10 06:02:21 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-07-10 06:02:20 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:02:08 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:02:06 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:01:56 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:01:30 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:01:28 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:01:23 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-10 06:01:11 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-07-10 06:01:09 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:00:54 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 06:00:47 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:00:21 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-10 05:42:25 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-10 06:16:46 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-07-10 06:01:11 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-07-10 06:06:32 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-07-10 06:03:48 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-10 06:01:23 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-10 06:00:54 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 06:07:29 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 06:04:40 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 06:00:21 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-10 05:01:45 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:01:28 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:05:05 | Yaka Wewa (Ma Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:03:52 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:04:21 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:11:10 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:03:30 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:04:21 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:03:25 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:06:43 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:15:07 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:04:07 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:01:09 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:02:20 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:02:08 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:06:09 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:05:33 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:04:07 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:01:30 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-09 18:01:40 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:04:34 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:01:56 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:02:06 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:04:05 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-10 06:04:12 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-07-10 06:02:21 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-07-10 06:03:31 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.013 |  |
| 2026-07-10 06:02:30 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.031 |  |
| 2026-07-10 06:03:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.068 |  |
| 2026-07-10 06:03:27 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)