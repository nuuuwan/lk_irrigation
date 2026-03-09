# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--09_16:14:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **93,590 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 16:14:18 | Baddegama (Gin Ganga) | 0.75 | 🟢 Normal | -0.033 |  |
| 2026-03-09 16:11:35 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:10:05 | Dunamale (Aththanagalu Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:09:22 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:09:15 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:09:03 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.009 |  |
| 2026-03-09 16:07:01 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:06:49 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:05:30 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:04:54 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-03-09 16:04:21 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-09 16:04:18 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:04:04 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.039 |  |
| 2026-03-09 16:03:56 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:03:53 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-03-09 16:03:42 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:03:35 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:03:31 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 16:03:30 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-03-09 16:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:02:48 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 16:02:45 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.032 |  |
| 2026-03-09 16:02:39 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.020 |  |
| 2026-03-09 16:02:28 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:02:22 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-03-09 16:02:20 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:02:18 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:02:13 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 16:02:08 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:01:46 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-03-09 16:01:45 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-03-09 16:01:43 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:01:27 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:01:14 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-09 16:00:41 | Thanthirimale (Malwathu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:00:22 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 16:03:30 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-03-09 16:04:54 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-03-09 16:01:46 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-03-09 15:07:38 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-09 16:02:48 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 16:02:13 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 16:03:31 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 16:02:18 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:00:22 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:05:30 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:01:27 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:03:42 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:03:56 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:09:15 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:19:12 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:11:35 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-09 15:08:51 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:02:28 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:01:43 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:02:08 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:10:05 | Dunamale (Aththanagalu Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:03:35 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:07:01 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:04:18 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:00:41 | Thanthirimale (Malwathu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:09:22 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:02:20 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-03-09 16:09:03 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.009 |  |
| 2026-03-09 16:02:22 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-03-09 16:01:45 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-03-09 16:04:21 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-09 16:01:14 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-09 16:02:39 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.020 |  |
| 2026-03-09 16:03:53 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-03-09 16:02:45 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.032 |  |
| 2026-03-09 16:14:18 | Baddegama (Gin Ganga) | 0.75 | 🟢 Normal | -0.033 |  |
| 2026-03-09 16:04:04 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.039 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)