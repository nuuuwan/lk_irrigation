# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--28_04:10:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **218,176 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-28 04:10:43 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-07-28 04:10:18 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:08:40 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:07:44 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | -36.000 |  |
| 2026-07-28 04:07:43 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | -36.000 |  |
| 2026-07-28 04:07:40 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-28 04:05:39 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.009 |  |
| 2026-07-28 04:05:29 | Glencourse (Kelani Ganga) | 9.06 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-28 04:05:15 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.399 |  |
| 2026-07-28 04:04:32 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:04:25 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:04:15 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:03:53 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:03:21 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:03:16 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:02:43 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:02:26 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-28 04:02:05 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.060 |  |
| 2026-07-28 04:02:04 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:01:53 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:01:51 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:01:38 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:01:37 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:01:36 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.192 |  |
| 2026-07-28 04:01:21 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:01:09 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:01:03 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.040 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-28 01:16:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-07-28 04:05:29 | Glencourse (Kelani Ganga) | 9.06 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-28 04:01:03 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-28 04:10:43 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-07-28 04:02:26 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-28 04:07:40 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-28 03:13:39 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-07-28 03:01:01 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:08:40 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:10:18 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:01:38 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:01:37 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:03:16 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-28 03:06:33 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:03:06 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:03:53 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:02:43 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:04:25 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-28 03:03:20 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:01:09 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:01:21 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:02:04 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:01:53 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:03:21 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:04:32 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-07-27 18:00:30 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-28 03:08:31 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-28 03:22:08 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:01:51 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:04:15 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-28 04:05:39 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.009 |  |
| 2026-07-27 18:01:36 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.020 |  |
| 2026-07-28 03:02:18 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.021 |  |
| 2026-07-28 03:04:47 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.058 |  |
| 2026-07-28 04:02:05 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.060 |  |
| 2026-07-28 04:01:36 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.192 |  |
| 2026-07-28 03:09:11 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.194 |  |
| 2026-07-28 04:05:15 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.399 |  |
| 2026-07-28 04:07:44 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)