# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14_16:29:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **206,131 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-14 16:29:02 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:24:24 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:23:13 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | -0.008 |  |
| 2026-07-14 16:19:51 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-07-14 16:14:46 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-14 16:11:51 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:10:33 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:10:29 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:10:12 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:09:13 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:09:08 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-14 16:08:21 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.112 |  |
| 2026-07-14 16:08:16 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-07-14 16:08:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | -0.054 |  |
| 2026-07-14 16:07:27 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-14 16:07:21 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:07:09 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:06:37 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:06:00 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-07-14 16:05:36 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:05:12 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:04:31 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.078 |  |
| 2026-07-14 16:03:58 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:03:21 | Hanwella (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:03:08 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-07-14 16:02:57 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:02:51 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-07-14 16:02:44 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.039 |  |
| 2026-07-14 16:02:44 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:02:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:02:36 | Glencourse (Kelani Ganga) | 9.17 | 🟢 Normal | -0.031 |  |
| 2026-07-14 16:02:09 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:02:08 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:01:22 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-14 16:01:18 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:01:12 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | -0.051 |  |
| 2026-07-14 16:00:52 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:00:41 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-14 16:19:51 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-07-14 15:05:49 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-14 16:07:27 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-14 16:01:22 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-14 16:14:46 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-14 16:09:08 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-14 16:10:33 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:00:41 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:29:02 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:10:29 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:02:08 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:24:24 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:02:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:02:44 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:03:21 | Hanwella (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:05:36 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:07:09 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:09:13 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:02:57 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:10:12 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:03:58 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:02:09 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:05:12 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:00:52 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:07:21 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:06:37 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:11:51 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:01:18 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-14 16:23:13 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | -0.008 |  |
| 2026-07-14 16:06:00 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-07-14 16:02:51 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-07-14 16:03:08 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-07-14 16:08:16 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-07-14 16:02:36 | Glencourse (Kelani Ganga) | 9.17 | 🟢 Normal | -0.031 |  |
| 2026-07-14 16:02:44 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.039 |  |
| 2026-07-14 16:01:12 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | -0.051 |  |
| 2026-07-14 16:08:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | -0.054 |  |
| 2026-07-14 16:04:31 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.078 |  |
| 2026-07-14 16:08:21 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)