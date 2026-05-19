# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_12:04:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **156,050 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 12:04:12 | Hanwella (Kelani Ganga) | 1.92 | 🟢 Normal | -0.040 |  |
| 2026-05-19 12:04:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.77 | 🟢 Normal | -0.060 |  |
| 2026-05-19 12:03:55 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:03:50 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:03:43 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-19 12:03:40 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-05-19 12:03:36 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-05-19 12:03:14 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | -0.021 |  |
| 2026-05-19 12:03:09 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-19 12:03:04 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:03:03 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:02:37 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:02:19 | Thanthirimale (Malwathu Oya) | 2.34 | 🟢 Normal | -0.041 |  |
| 2026-05-19 12:02:11 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:02:08 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:02:08 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-19 12:01:59 | Ellagawa (Kalu Ganga) | 5.51 | 🟢 Normal | -0.031 |  |
| 2026-05-19 12:01:44 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:01:43 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-05-19 12:01:43 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.021 |  |
| 2026-05-19 12:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-19 12:01:22 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:01:17 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:01:14 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:00:53 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:00:15 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-19 12:00:11 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:00:11 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-19 11:30:57 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-19 11:23:26 | Ellagawa (Kalu Ganga) | 5.53 | 🟢 Normal | -0.031 |  |
| 2026-05-19 11:22:21 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 12:01:43 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-05-19 12:00:15 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-19 11:30:57 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-19 12:02:08 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-19 12:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-19 12:03:43 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-19 11:05:33 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 12:01:22 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:00:11 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:00:53 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:02:08 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-19 11:06:08 | Galgamuwa (Mee Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:02:37 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:01:44 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:03:50 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:00:11 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:01:17 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:02:11 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:03:55 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:03:03 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:01:14 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-19 11:22:21 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:03:04 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-19 12:03:40 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-05-19 11:05:32 | Glencourse (Kelani Ganga) | 9.86 | 🟢 Normal | -0.010 |  |
| 2026-05-19 11:00:14 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.010 |  |
| 2026-05-19 12:03:09 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-19 11:00:40 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-05-19 11:03:08 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-05-19 11:01:37 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-05-19 12:03:36 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-05-19 11:06:23 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-05-19 12:03:14 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | -0.021 |  |
| 2026-05-19 12:01:43 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.021 |  |
| 2026-05-19 11:01:00 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | -0.030 |  |
| 2026-05-19 12:01:59 | Ellagawa (Kalu Ganga) | 5.51 | 🟢 Normal | -0.031 |  |
| 2026-05-19 12:04:12 | Hanwella (Kelani Ganga) | 1.92 | 🟢 Normal | -0.040 |  |
| 2026-05-19 12:02:19 | Thanthirimale (Malwathu Oya) | 2.34 | 🟢 Normal | -0.041 |  |
| 2026-05-19 12:04:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.77 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)