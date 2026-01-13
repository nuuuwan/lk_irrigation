# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--14_05:14:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **45,053 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 05:14:26 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.055 |  |
| 2026-01-14 05:13:26 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-01-14 05:10:39 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | -0.068 |  |
| 2026-01-14 05:09:51 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-14 05:08:53 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-01-14 05:08:35 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:07:50 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.005 |  |
| 2026-01-14 05:07:44 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:07:31 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.018 |  |
| 2026-01-14 05:06:37 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:06:24 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.009 |  |
| 2026-01-14 05:06:01 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:04:52 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-14 05:04:50 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:04:46 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-14 05:04:20 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.018 |  |
| 2026-01-14 05:04:00 | Dunamale (Aththanagalu Oya) | 1.33 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-14 05:03:33 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-01-14 05:03:18 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:03:15 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:02:59 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:02:46 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-14 05:02:43 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-14 05:02:39 | Hanwella (Kelani Ganga) | 1.06 | 🟢 Normal | -0.021 |  |
| 2026-01-14 05:02:34 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:02:12 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:01:44 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:01:25 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-14 05:01:23 | Manampitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.022 |  |
| 2026-01-14 05:01:02 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.152 |  |
| 2026-01-14 04:31:09 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.018 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 05:04:46 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-14 05:04:52 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-14 05:04:00 | Dunamale (Aththanagalu Oya) | 1.33 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-14 05:01:25 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-14 05:09:51 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-14 05:02:43 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-14 05:04:50 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:02:59 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:02:12 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:03:18 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:08:35 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:03:54 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:03:37 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:03:15 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:07:44 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-14 04:01:54 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:02:34 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:06:37 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:06:01 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:10:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-14 05:07:50 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.005 |  |
| 2026-01-14 05:13:26 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-01-14 03:11:04 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-01-14 05:08:53 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-01-14 05:06:24 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.009 |  |
| 2026-01-14 04:06:24 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-01-14 05:02:46 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-14 05:03:33 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-01-14 05:04:20 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.018 |  |
| 2026-01-14 05:07:31 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.018 |  |
| 2026-01-13 18:03:19 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-01-14 05:02:39 | Hanwella (Kelani Ganga) | 1.06 | 🟢 Normal | -0.021 |  |
| 2026-01-14 05:01:23 | Manampitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.022 |  |
| 2026-01-14 04:00:09 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.022 |  |
| 2026-01-13 18:01:14 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.040 |  |
| 2026-01-14 05:14:26 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.055 |  |
| 2026-01-14 05:10:39 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | -0.068 |  |
| 2026-01-14 05:01:02 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.152 |  |
| 2026-01-14 04:05:22 | Horowpothana (Yan Oya) | 3.54 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)