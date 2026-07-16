# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--16_15:12:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **207,888 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-16 15:12:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:11:57 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:10:46 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:09:36 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:06:02 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:05:22 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:05:08 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:05:07 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:04:49 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.005 |  |
| 2026-07-16 15:04:45 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:04:25 | Hanwella (Kelani Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-07-16 15:04:06 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:03:57 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:03:39 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-07-16 15:03:34 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-07-16 15:03:22 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:03:04 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | -0.045 |  |
| 2026-07-16 15:03:03 | Thalgahagoda (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-16 15:02:49 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:02:38 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-07-16 15:02:37 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:02:37 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-16 15:02:36 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:02:35 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:02:29 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-07-16 15:02:28 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:02:25 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-07-16 15:02:21 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-07-16 15:02:19 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:02:13 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:02:09 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | -0.050 |  |
| 2026-07-16 15:02:04 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:01:57 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2026-07-16 15:01:49 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-16 15:01:27 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.117 |  |
| 2026-07-16 15:01:25 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:01:17 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:00:42 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.021 |  |
| 2026-07-16 15:00:14 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-16 15:01:57 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2026-07-16 15:02:21 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-07-16 15:03:34 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-07-16 15:02:37 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-16 15:03:03 | Thalgahagoda (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-16 15:01:49 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-16 15:02:29 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-07-16 15:01:17 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:02:04 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:11:57 | Moragaswewa (Deduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:01:25 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:02:35 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:00:14 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:03:57 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:05:22 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:02:28 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:05:07 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:02:19 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:03:22 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:02:13 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:10:46 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:04:06 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:04:45 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:05:08 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:02:36 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:09:36 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:02:49 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:02:37 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:12:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-07-16 15:04:49 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.005 |  |
| 2026-07-16 15:03:39 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-07-16 15:02:38 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-07-16 15:04:25 | Hanwella (Kelani Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-07-16 15:02:25 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-07-16 15:00:42 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.021 |  |
| 2026-07-16 15:03:04 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | -0.045 |  |
| 2026-07-16 15:02:09 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | -0.050 |  |
| 2026-07-16 15:01:27 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)