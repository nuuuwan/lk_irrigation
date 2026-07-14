# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14_23:33:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **206,393 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-14 23:33:29 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.007 |  |
| 2026-07-14 23:14:27 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:14:14 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:14:05 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:11:12 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | -0.012 |  |
| 2026-07-14 23:09:40 | Putupaula (Kalu Ganga) | 0.14 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-14 23:09:27 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-14 23:08:40 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.027 |  |
| 2026-07-14 23:08:25 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:08:07 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-07-14 23:07:39 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:07:18 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:06:12 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:06:01 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:05:53 | Glencourse (Kelani Ganga) | 9.19 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-07-14 23:05:52 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.021 |  |
| 2026-07-14 23:04:14 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:03:50 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:03:45 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:03:24 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:03:22 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:03:06 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:03:02 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:02:54 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-07-14 23:02:45 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:02:40 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | -0.012 |  |
| 2026-07-14 23:02:26 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:02:21 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:02:17 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-14 23:02:16 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:02:00 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-07-14 23:01:46 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:01:08 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-07-14 23:01:08 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:00:43 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:00:38 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-14 22:01:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-07-14 23:05:53 | Glencourse (Kelani Ganga) | 9.19 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-07-14 18:02:37 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-14 23:02:17 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-14 23:09:40 | Putupaula (Kalu Ganga) | 0.14 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-14 23:09:27 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-14 23:02:21 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:00:43 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:01:46 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:03:06 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:03:02 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:00:38 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 18:03:13 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:06:01 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:06:12 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:04:14 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:08:25 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:14:27 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:07:18 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:02:45 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-07-14 22:00:06 | Siyambalanduwa (Heda Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:03:24 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:03:22 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:02:26 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-14 18:01:22 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:07:39 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:14:14 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:03:50 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:01:08 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:02:16 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-14 23:33:29 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.007 |  |
| 2026-07-14 23:08:07 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-07-14 23:11:12 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | -0.012 |  |
| 2026-07-14 23:02:40 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | -0.012 |  |
| 2026-07-14 23:02:00 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-07-14 23:02:54 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-07-14 23:01:08 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-07-14 23:05:52 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.021 |  |
| 2026-07-14 23:08:40 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.027 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)