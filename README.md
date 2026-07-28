# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--28_14:29:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **218,575 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-28 14:29:50 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:13:40 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:10:01 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-28 14:09:42 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:09:22 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-07-28 14:09:04 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.019 |  |
| 2026-07-28 14:08:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-07-28 14:07:57 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-28 14:07:23 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-28 14:06:48 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:06:10 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:05:26 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:04:04 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-07-28 14:04:00 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-28 14:03:38 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:03:38 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-28 14:03:32 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:03:31 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:03:26 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:03:24 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-07-28 14:03:14 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:03:12 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:03:07 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:02:58 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.063 |  |
| 2026-07-28 14:02:55 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:02:46 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:02:43 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:02:37 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:02:31 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:02:27 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:02:16 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:02:02 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.045 |  |
| 2026-07-28 14:01:47 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:01:46 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-28 14:01:32 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | -0.011 |  |
| 2026-07-28 14:01:26 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:01:24 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:01:04 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:00:53 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:00:31 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:00:09 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-28 14:09:22 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-07-28 14:03:38 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-28 14:01:46 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-28 14:07:23 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-28 14:04:00 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-28 14:07:57 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-28 14:10:01 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-28 14:03:32 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:01:24 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:02:46 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:01:47 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:02:43 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:03:38 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:02:37 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:02:55 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:13:40 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:06:10 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:03:12 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:00:31 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:06:48 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:01:26 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:01:04 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:03:26 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:05:26 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:02:31 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:00:53 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:03:07 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:29:50 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:09:42 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:02:27 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:03:14 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-28 14:03:24 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-07-28 14:00:09 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.010 |  |
| 2026-07-28 14:01:32 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | -0.011 |  |
| 2026-07-28 14:09:04 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.019 |  |
| 2026-07-28 14:08:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-07-28 14:04:04 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-07-28 14:02:02 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.045 |  |
| 2026-07-28 14:02:58 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)