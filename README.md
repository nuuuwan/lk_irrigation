# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--25_06:12:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **54,995 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 06:12:26 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:10:07 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-01-25 06:09:31 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:08:56 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-01-25 06:08:44 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.108 |  |
| 2026-01-25 06:08:25 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | -0.012 |  |
| 2026-01-25 06:07:50 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.012 |  |
| 2026-01-25 06:07:39 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:07:39 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:07:23 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:06:59 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:06:23 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | -0.018 |  |
| 2026-01-25 06:05:42 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:04:56 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-25 06:04:42 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:04:30 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:04:04 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-25 06:03:46 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:03:42 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 06:03:37 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:03:32 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:03:22 | Yaka Wewa (Ma Oya) | 1.38 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-01-25 06:02:53 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 06:02:32 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:02:12 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-01-25 06:02:05 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-25 06:01:56 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:01:49 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:01:19 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-25 06:00:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-01-25 06:00:50 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:00:48 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | -0.011 |  |
| 2026-01-25 06:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:53:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-01-25 05:50:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-01-25 05:45:29 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:40:17 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:23:21 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:22:35 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.075 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 06:00:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-01-25 06:03:22 | Yaka Wewa (Ma Oya) | 1.38 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-01-25 06:08:56 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-01-25 05:22:35 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-01-25 06:04:04 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-25 06:02:05 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-25 06:01:19 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-25 06:04:56 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-25 06:02:53 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 06:03:42 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 23:03:01 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:07:23 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:03:46 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:01:49 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:03:37 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:03:22 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:05:47 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:04:30 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:04:42 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:01:56 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:07:39 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:12:26 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:09:31 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:06:59 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:02:32 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:07:39 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-25 05:01:30 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:03:32 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:05:42 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 06:10:07 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-01-24 18:01:40 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-25 06:00:48 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | -0.011 |  |
| 2026-01-25 06:08:25 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | -0.012 |  |
| 2026-01-25 06:07:50 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.012 |  |
| 2026-01-25 06:06:23 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | -0.018 |  |
| 2026-01-25 06:02:12 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-01-25 06:08:44 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.108 |  |
| 2026-01-25 05:01:42 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)