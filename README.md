# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--25_07:23:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **55,039 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 07:23:51 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:20:15 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:15:03 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:13:22 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:12:44 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:12:30 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:12:13 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:11:30 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:10:28 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:10:19 | Yaka Wewa (Ma Oya) | 1.35 | 🟢 Normal | -0.027 |  |
| 2026-01-25 07:10:18 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-25 07:10:11 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-01-25 07:09:17 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.060 |  |
| 2026-01-25 07:08:35 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.080 |  |
| 2026-01-25 07:08:11 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:07:55 | Thawalama (Gin Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-25 07:07:54 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:05:57 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:04:55 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-25 07:04:44 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:04:44 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:04:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:04:25 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:04:15 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-25 07:04:13 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 07:03:43 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 07:03:39 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-01-25 07:03:19 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-01-25 07:03:16 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-25 07:03:08 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:02:58 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:02:42 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:02:26 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-25 07:02:23 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.122 |  |
| 2026-01-25 07:02:18 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:01:47 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:00:19 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-25 07:00:10 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | -0.062 |  |
| 2026-01-25 07:00:05 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:54:59 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.208 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 07:03:39 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-01-25 07:03:19 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-01-25 07:02:26 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-25 07:00:19 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-25 07:03:16 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-25 07:04:15 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-25 07:03:43 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 07:04:13 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 07:10:18 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-25 07:04:55 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-25 07:00:05 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:15:03 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:11:30 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:02:18 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:10:28 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:12:30 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:23:51 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:07:54 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:04:44 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:02:42 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:12:13 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:08:11 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:02:58 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:05:57 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:13:22 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:04:25 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:04:44 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:20:15 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:01:47 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:03:08 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 07:04:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:30:46 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | -0.002 |  |
| 2026-01-25 07:07:55 | Thawalama (Gin Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-25 07:10:11 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-01-25 07:10:19 | Yaka Wewa (Ma Oya) | 1.35 | 🟢 Normal | -0.027 |  |
| 2026-01-25 07:09:17 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.060 |  |
| 2026-01-25 07:00:10 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | -0.062 |  |
| 2026-01-25 07:08:35 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.080 |  |
| 2026-01-25 07:02:23 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)