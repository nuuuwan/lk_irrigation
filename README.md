# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_10:18:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,985 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 10:18:10 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.024 |  |
| 2026-05-09 10:16:23 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 10:09:07 | Baddegama (Gin Ganga) | 1.99 | 🟢 Normal | -0.069 |  |
| 2026-05-09 10:08:52 | Rathnapura (Kalu Ganga) | 3.36 | 🟢 Normal | -0.241 |  |
| 2026-05-09 10:08:30 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-09 10:08:27 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-09 10:08:25 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.063 |  |
| 2026-05-09 10:08:20 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.086 |  |
| 2026-05-09 10:07:13 | Moragaswewa (Deduru Oya) | 3.15 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-09 10:07:06 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-09 10:06:46 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-09 10:06:23 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.047 |  |
| 2026-05-09 10:06:11 | Glencourse (Kelani Ganga) | 9.68 | 🟢 Normal | -0.070 |  |
| 2026-05-09 10:05:59 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.049 |  |
| 2026-05-09 10:05:59 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.031 |  |
| 2026-05-09 10:05:36 | Galgamuwa (Mee Oya) | 2.74 | 🟢 Normal | -0.052 |  |
| 2026-05-09 10:05:19 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | -0.048 |  |
| 2026-05-09 10:04:59 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.039 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 10:04:26 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | 42.353 | 🔺 Rising |
| 2026-05-09 10:03:51 | Katharagama (Menik Ganga) | 2.30 | 🟢 Normal | 0.315 | 🔺 Rising |
| 2026-05-09 10:04:17 | Kuda Oya (Kirindi Oya) | 2.87 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-05-09 10:00:53 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-09 10:01:35 | Ellagawa (Kalu Ganga) | 6.38 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-09 10:07:13 | Moragaswewa (Deduru Oya) | 3.15 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-09 10:08:30 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-09 10:07:06 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-09 10:06:46 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-09 10:00:29 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-09 10:01:18 | Thanthirimale (Malwathu Oya) | 3.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 10:08:27 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-09 10:02:34 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 10:16:23 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 10:01:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.83 | 🟢 Normal | 0.000 |  |
| 2026-05-09 10:02:48 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-05-09 10:00:47 | Weraganthota (Mahaweli Ganga) | -2.64 | 🟢 Normal | -0.010 |  |
| 2026-05-09 10:02:29 | Wellawaya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.019 |  |
| 2026-05-09 10:02:14 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-05-09 10:04:36 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-05-09 10:18:10 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.024 |  |
| 2026-05-09 10:01:42 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.026 |  |
| 2026-05-09 10:03:26 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | -0.030 |  |
| 2026-05-09 10:01:33 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-05-09 10:05:59 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.031 |  |
| 2026-05-09 10:04:59 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.039 |  |
| 2026-05-09 10:03:27 | Thanamalwila (Kirindi Oya) | 2.50 | 🟢 Normal | -0.041 |  |
| 2026-05-09 10:03:09 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.041 |  |
| 2026-05-09 10:06:23 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.047 |  |
| 2026-05-09 10:05:19 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | -0.048 |  |
| 2026-05-09 10:05:59 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.049 |  |
| 2026-05-09 10:05:36 | Galgamuwa (Mee Oya) | 2.74 | 🟢 Normal | -0.052 |  |
| 2026-05-09 10:08:25 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.063 |  |
| 2026-05-09 10:04:37 | Panadugama (Nilwala Ganga) | 3.04 | 🟢 Normal | -0.066 |  |
| 2026-05-09 10:09:07 | Baddegama (Gin Ganga) | 1.99 | 🟢 Normal | -0.069 |  |
| 2026-05-09 10:06:11 | Glencourse (Kelani Ganga) | 9.68 | 🟢 Normal | -0.070 |  |
| 2026-05-09 10:08:20 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.086 |  |
| 2026-05-09 10:03:35 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.138 |  |
| 2026-05-09 10:08:52 | Rathnapura (Kalu Ganga) | 3.36 | 🟢 Normal | -0.241 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)