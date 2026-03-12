# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--12_15:15:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **95,446 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 15:15:30 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:11:17 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.036 |  |
| 2026-03-12 15:10:27 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:09:45 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-12 15:08:27 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.019 |  |
| 2026-03-12 15:07:31 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:07:10 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:06:43 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-03-12 15:05:43 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:05:29 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:05:15 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:05:14 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:05:05 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-03-12 15:04:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | -0.040 |  |
| 2026-03-12 15:04:23 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:04:21 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.019 |  |
| 2026-03-12 15:04:13 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | 3.348 | 🔺 Rising |
| 2026-03-12 15:04:13 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:04:09 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.004 |  |
| 2026-03-12 15:03:46 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:03:23 | Hanwella (Kelani Ganga) | 0.87 | 🟢 Normal | -0.071 |  |
| 2026-03-12 15:03:22 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-03-12 15:03:04 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:02:38 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:02:33 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-12 15:02:20 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:02:15 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:02:01 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:01:49 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-12 15:01:36 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:01:36 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:01:32 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:01:03 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 15:04:13 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | 3.348 | 🔺 Rising |
| 2026-03-12 15:05:05 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-03-12 15:01:49 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-12 15:02:33 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-12 15:09:45 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-12 15:04:09 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.004 |  |
| 2026-03-12 15:03:04 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:02:01 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:02:21 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:04:23 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:01:32 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:01:36 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:05:15 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:10:27 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 14:04:48 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:07:10 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:02:20 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:04:13 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:05:43 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:03:46 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:00:15 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:05:14 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:01:03 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:05:29 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:02:38 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:07:31 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:15:30 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:01:36 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:00:36 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:00:32 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:02:15 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 15:03:22 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-03-12 15:06:43 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-03-12 15:08:27 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.019 |  |
| 2026-03-12 15:04:21 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.019 |  |
| 2026-03-12 15:11:17 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.036 |  |
| 2026-03-12 15:04:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | -0.040 |  |
| 2026-03-12 15:00:39 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | -0.060 |  |
| 2026-03-12 15:03:23 | Hanwella (Kelani Ganga) | 0.87 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)