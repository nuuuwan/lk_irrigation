# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--15_14:13:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **206,959 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-15 14:13:25 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:10:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 0.876 | 🔺 Rising |
| 2026-07-15 14:09:00 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:08:37 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:07:16 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.009 |  |
| 2026-07-15 14:06:21 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:05:56 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-15 14:05:43 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-15 14:05:40 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:04:53 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-07-15 14:04:53 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-07-15 14:04:48 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-07-15 14:04:12 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:03:54 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2026-07-15 14:03:53 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-07-15 14:03:51 | Thalgahagoda (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-15 14:03:40 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:03:29 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:02:57 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:02:42 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:02:41 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:02:35 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-07-15 14:02:27 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:02:25 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:02:17 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-15 14:02:09 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:02:09 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:02:07 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-15 14:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:01:48 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:01:47 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:01:45 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:01:41 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:01:40 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:01:17 | Thanthirimale (Malwathu Oya) | 0.88 | 🟢 Normal | -0.014 |  |
| 2026-07-15 14:01:04 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:00:59 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:00:40 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-07-15 14:00:39 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-15 13:57:10 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-15 14:10:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 0.876 | 🔺 Rising |
| 2026-07-15 14:03:54 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.298 | 🔺 Rising |
| 2026-07-15 14:03:53 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-07-15 14:04:53 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-07-15 14:02:17 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-15 14:05:56 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-15 14:02:07 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-15 14:03:51 | Thalgahagoda (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-15 14:05:43 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-15 14:00:59 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:03:29 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:01:41 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:02:25 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:01:04 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:01:45 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:02:41 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:08:37 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:02:27 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:02:42 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:02:09 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2026-07-15 12:59:36 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:02:57 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:13:25 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:04:12 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:05:40 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:00:39 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:01:40 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:06:21 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:01:48 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:03:40 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:09:00 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:02:09 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-15 14:07:16 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.009 |  |
| 2026-07-15 14:02:35 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-07-15 14:00:40 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-07-15 14:01:17 | Thanthirimale (Malwathu Oya) | 0.88 | 🟢 Normal | -0.014 |  |
| 2026-07-15 14:04:53 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-07-15 14:04:48 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.030 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)