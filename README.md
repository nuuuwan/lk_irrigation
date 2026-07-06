# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--06_10:05:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **198,728 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 10:05:00 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-07-06 10:04:42 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:04:14 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 10:04:13 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:04:11 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-07-06 10:03:52 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:03:50 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.029 |  |
| 2026-07-06 10:03:27 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | -0.020 |  |
| 2026-07-06 10:03:17 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:03:15 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-07-06 10:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | -0.069 |  |
| 2026-07-06 10:03:09 | Glencourse (Kelani Ganga) | 10.01 | 🟢 Normal | -0.030 |  |
| 2026-07-06 10:03:07 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:03:04 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.299 |  |
| 2026-07-06 10:03:04 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:02:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:02:33 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:02:22 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.032 |  |
| 2026-07-06 10:02:07 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-07-06 10:01:59 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:01:23 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.031 |  |
| 2026-07-06 10:01:14 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:01:11 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-07-06 10:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:00:42 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:00:24 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:00:06 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 09:01:09 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-07-06 10:04:14 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 09:03:51 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 10:00:24 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:00:06 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 09:13:46 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:02:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:01:14 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-06 08:06:04 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:03:17 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:02:33 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:04:13 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:03:04 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-06 09:15:16 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:03:52 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:03:07 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-06 09:04:47 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:04:42 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:00:42 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-06 09:02:18 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-06 10:03:15 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-07-06 10:01:11 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-07-06 09:02:40 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.011 |  |
| 2026-07-06 09:05:56 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-07-06 10:04:11 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-07-06 10:02:07 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-07-06 10:03:27 | Hanwella (Kelani Ganga) | 1.89 | 🟢 Normal | -0.020 |  |
| 2026-07-06 09:02:36 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | -0.020 |  |
| 2026-07-06 10:03:50 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.029 |  |
| 2026-07-06 10:05:00 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-07-06 10:03:09 | Glencourse (Kelani Ganga) | 10.01 | 🟢 Normal | -0.030 |  |
| 2026-07-06 10:01:23 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.031 |  |
| 2026-07-06 10:02:22 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.032 |  |
| 2026-07-06 09:01:59 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.033 |  |
| 2026-07-06 09:07:58 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.060 |  |
| 2026-07-06 09:03:24 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.063 |  |
| 2026-07-06 10:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | -0.069 |  |
| 2026-07-06 10:03:04 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.299 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)