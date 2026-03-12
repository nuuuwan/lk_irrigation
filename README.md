# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--12_08:27:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **95,175 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 08:27:01 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:24:48 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-03-12 08:19:33 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-12 08:17:25 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:14:40 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-12 08:10:41 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:10:37 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-03-12 08:07:34 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.018 |  |
| 2026-03-12 08:06:54 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.065 |  |
| 2026-03-12 08:06:43 | Moraketiya (Walawe Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:06:42 | Badalgama (Maha Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:05:39 | Glencourse (Kelani Ganga) | 9.26 | 🟢 Normal | -0.142 |  |
| 2026-03-12 08:05:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-03-12 08:04:49 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 08:04:23 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:04:05 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:04:02 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-03-12 08:03:56 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-12 08:03:50 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:03:29 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.110 |  |
| 2026-03-12 08:03:20 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:03:08 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.050 |  |
| 2026-03-12 08:02:54 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:02:48 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -0.069 |  |
| 2026-03-12 08:02:32 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-12 08:02:32 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:02:28 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 08:02:28 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:02:14 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:02:13 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:02:08 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:01:47 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:01:43 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:01:38 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:01:29 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.041 |  |
| 2026-03-12 08:01:16 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:00:55 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.101 |  |
| 2026-03-12 08:00:22 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 08:24:48 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-03-12 08:10:37 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-03-12 08:04:02 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-03-12 08:02:32 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-12 08:19:33 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-12 08:14:40 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-12 08:02:28 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 08:04:49 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 08:02:13 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:02:08 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:01:38 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:01:43 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:03:20 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:17:25 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:10:41 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:01:16 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:03:50 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:27:01 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:06:43 | Moraketiya (Walawe Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:02:28 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:02:54 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:04:05 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:06:42 | Badalgama (Maha Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:02:32 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:00:55 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:04:23 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:01:47 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:02:14 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-12 08:03:56 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-12 08:00:22 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | -0.012 |  |
| 2026-03-12 08:07:34 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.018 |  |
| 2026-03-12 08:05:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-03-12 08:01:29 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.041 |  |
| 2026-03-12 08:03:08 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.050 |  |
| 2026-03-12 08:06:54 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.065 |  |
| 2026-03-12 08:02:48 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -0.069 |  |
| 2026-03-12 08:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.101 |  |
| 2026-03-12 08:03:29 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.110 |  |
| 2026-03-12 08:05:39 | Glencourse (Kelani Ganga) | 9.26 | 🟢 Normal | -0.142 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)