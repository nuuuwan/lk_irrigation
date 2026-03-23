# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--23_09:08:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **105,043 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-23 09:08:22 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:07:03 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:06:58 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 129.273 | 🔺 Rising |
| 2026-03-23 09:06:52 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-03-23 09:06:36 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 129.273 | 🔺 Rising |
| 2026-03-23 09:04:54 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.082 |  |
| 2026-03-23 09:04:48 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.352 |  |
| 2026-03-23 09:04:46 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:03:58 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:03:52 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:03:44 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-03-23 09:03:44 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-23 09:03:38 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:03:38 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:03:35 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:03:28 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.141 |  |
| 2026-03-23 09:03:19 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:03:18 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:03:18 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-03-23 09:03:12 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:02:55 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:02:46 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-03-23 09:02:39 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-23 09:02:38 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.030 |  |
| 2026-03-23 09:02:37 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:02:29 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.061 |  |
| 2026-03-23 09:02:19 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:02:11 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.070 |  |
| 2026-03-23 09:01:55 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:01:53 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.031 |  |
| 2026-03-23 09:01:52 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:01:32 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-03-23 09:01:23 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:01:08 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.010 |  |
| 2026-03-23 09:00:38 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:00:10 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-03-23 08:38:44 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:14:23 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-03-23 08:14:21 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-23 09:06:58 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 129.273 | 🔺 Rising |
| 2026-03-23 09:01:32 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-03-23 09:00:10 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-03-23 09:03:18 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-03-23 08:08:48 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-23 09:02:39 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-23 09:03:44 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-23 09:02:11 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:01:23 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:04:46 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:03:12 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:01:52 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:03:35 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:00:12 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:00:38 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:03:38 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:03:38 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:14:21 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:03:18 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:07:03 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:03:52 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:02:37 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:02:19 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:08:22 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:02:55 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:03:58 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-23 08:03:45 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-23 09:03:44 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-03-23 09:01:08 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.010 |  |
| 2026-03-23 09:06:52 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-03-23 09:02:46 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-03-23 09:02:38 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.030 |  |
| 2026-03-23 09:01:53 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.031 |  |
| 2026-03-23 09:02:29 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.061 |  |
| 2026-03-23 09:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.070 |  |
| 2026-03-23 09:04:54 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.082 |  |
| 2026-03-23 08:03:17 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.125 |  |
| 2026-03-23 09:03:28 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.141 |  |
| 2026-03-23 09:04:48 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.352 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)