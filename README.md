# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--29_14:15:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **219,462 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-29 14:15:27 | Thanthirimale (Malwathu Oya) | 0.86 | 🟢 Normal | -0.008 |  |
| 2026-07-29 14:14:04 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-07-29 14:10:46 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:09:58 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.159 |  |
| 2026-07-29 14:09:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-29 14:08:06 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-29 14:07:44 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-29 14:07:43 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:06:24 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:06:07 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:05:03 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:04:47 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.034 |  |
| 2026-07-29 14:04:36 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-07-29 14:04:14 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-07-29 14:03:55 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:03:55 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-07-29 14:03:52 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:03:49 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-29 14:03:37 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.012 |  |
| 2026-07-29 14:03:19 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:03:19 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-29 14:03:03 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-07-29 14:03:02 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-07-29 14:03:02 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:03:00 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:02:55 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:02:42 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 14:02:35 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:02:24 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:02:08 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:01:39 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:01:20 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-07-29 14:01:19 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.020 |  |
| 2026-07-29 14:01:08 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-07-29 14:00:47 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:00:43 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:00:38 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:00:31 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-29 14:01:20 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-07-29 14:04:36 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-07-29 14:01:08 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-07-29 14:14:04 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-07-29 14:09:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-29 14:08:06 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-29 14:03:49 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-29 14:07:44 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-29 14:03:55 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-07-29 14:03:19 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-07-29 14:02:42 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 14:03:19 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:00:31 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:07:43 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:00:38 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:10:46 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:03:55 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:03:00 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:06:07 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:03:02 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-29 13:23:21 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:03:52 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:00:43 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:01:39 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:02:35 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:05:03 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:02:55 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:00:47 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:06:24 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:02:24 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:02:08 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-29 14:15:27 | Thanthirimale (Malwathu Oya) | 0.86 | 🟢 Normal | -0.008 |  |
| 2026-07-29 14:04:14 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-07-29 14:03:03 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-07-29 14:03:37 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.012 |  |
| 2026-07-29 14:01:19 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.020 |  |
| 2026-07-29 14:03:02 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-07-29 14:04:47 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.034 |  |
| 2026-07-29 14:09:58 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.159 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)