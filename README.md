# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_08:27:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **122,872 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 08:27:10 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.041 |  |
| 2026-04-12 08:25:24 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.007 |  |
| 2026-04-12 08:23:03 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.024 |  |
| 2026-04-12 08:18:52 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.009 |  |
| 2026-04-12 08:15:18 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:10:03 | Baddegama (Gin Ganga) | 0.81 | 🟢 Normal | -0.027 |  |
| 2026-04-12 08:08:39 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-04-12 08:08:24 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:07:31 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.024 |  |
| 2026-04-12 08:07:04 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.018 |  |
| 2026-04-12 08:06:14 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:06:00 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-12 08:05:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.026 |  |
| 2026-04-12 08:05:04 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:04:59 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:04:47 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:04:04 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:04:03 | Weraganthota (Mahaweli Ganga) | -2.39 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-04-12 08:03:43 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 08:03:41 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 08:03:26 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 08:03:08 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-04-12 08:03:03 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 08:03:02 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 08:02:56 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:02:39 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 08:02:29 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:02:23 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:02:22 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.053 |  |
| 2026-04-12 08:02:03 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:01:41 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:01:39 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-12 08:01:20 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:00:54 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-04-12 08:00:44 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:00:42 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:00:32 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-04-12 07:41:44 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 08:03:08 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-04-12 08:04:03 | Weraganthota (Mahaweli Ganga) | -2.39 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-04-12 08:06:00 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-12 08:03:02 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 08:03:41 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 08:03:26 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 08:01:39 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-12 08:03:03 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 08:02:39 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 08:03:43 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 08:04:59 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:00:42 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:01:41 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:02:03 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:00:44 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:04:47 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:15:18 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:04:04 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:06:14 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:02:23 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:02:29 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:08:24 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:01:20 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:00:32 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:05:04 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:02:56 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-12 08:25:24 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.007 |  |
| 2026-04-12 07:15:09 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-04-12 08:18:52 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.009 |  |
| 2026-04-12 08:00:54 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-04-12 08:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-04-12 08:08:39 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-04-12 08:07:04 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.018 |  |
| 2026-04-12 08:23:03 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.024 |  |
| 2026-04-12 08:07:31 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.024 |  |
| 2026-04-12 08:05:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.026 |  |
| 2026-04-12 08:10:03 | Baddegama (Gin Ganga) | 0.81 | 🟢 Normal | -0.027 |  |
| 2026-04-12 08:27:10 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.041 |  |
| 2026-04-12 08:02:22 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.053 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)