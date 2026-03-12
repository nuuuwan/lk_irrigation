# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--12_06:31:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **95,098 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 06:31:56 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:21:06 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:19:22 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:15:48 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-12 06:08:01 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-12 06:07:30 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-03-12 06:06:21 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.065 |  |
| 2026-03-12 06:06:17 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-03-12 06:05:56 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:05:56 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:05:34 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:05:24 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:05:11 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 06:04:47 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:04:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | -0.026 |  |
| 2026-03-12 06:04:24 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:04:23 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:04:18 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-12 06:04:17 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-12 06:03:46 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.052 |  |
| 2026-03-12 06:03:37 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:03:28 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.039 |  |
| 2026-03-12 06:03:06 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-03-12 06:03:01 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:02:59 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:02:57 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:02:41 | Moraketiya (Walawe Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:02:39 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:02:32 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-12 06:02:31 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:02:02 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 06:01:44 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:01:37 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-12 06:01:31 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.065 |  |
| 2026-03-12 06:01:27 | Weraganthota (Mahaweli Ganga) | -2.68 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-03-12 06:01:11 | Badalgama (Maha Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:00:42 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-03-12 06:00:32 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-12 05:51:34 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 06:07:30 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-03-12 06:00:42 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-03-12 06:15:48 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-12 06:04:17 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-12 06:01:37 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-12 06:02:02 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 06:05:11 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 06:08:01 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-12 06:01:27 | Weraganthota (Mahaweli Ganga) | -2.68 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-03-12 05:51:34 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:02:57 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:02:39 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:05:56 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:00:32 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:31:56 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:02:31 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:04:23 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:19:22 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:03:01 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:02:41 | Moraketiya (Walawe Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:05:24 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:03:37 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:04:24 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:01:11 | Badalgama (Maha Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:05:56 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:05:34 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-10 18:00:47⌛ | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:21:06 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:01:44 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:04:47 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-12 06:04:18 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-12 06:02:32 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-12 06:03:06 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-03-12 06:04:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.49 | 🟢 Normal | -0.026 |  |
| 2026-03-12 06:06:17 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-03-12 06:03:28 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.039 |  |
| 2026-03-12 06:03:46 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.052 |  |
| 2026-03-12 06:01:31 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.065 |  |
| 2026-03-12 06:06:21 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)