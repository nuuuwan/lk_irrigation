# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--01_16:12:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **194,488 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 16:12:07 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:10:03 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:09:41 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-01 16:09:10 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | -0.053 |  |
| 2026-07-01 16:08:59 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.018 |  |
| 2026-07-01 16:08:30 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-07-01 16:07:26 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:07:16 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-07-01 16:07:07 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.028 |  |
| 2026-07-01 16:06:45 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-07-01 16:06:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.05 | 🟢 Normal | -0.086 |  |
| 2026-07-01 16:05:33 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.011 |  |
| 2026-07-01 16:05:31 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:05:26 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | -0.005 |  |
| 2026-07-01 16:05:18 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:05:06 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:04:54 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:04:47 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-07-01 16:04:47 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:04:24 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:04:14 | Hanwella (Kelani Ganga) | 1.84 | 🟢 Normal | -0.030 |  |
| 2026-07-01 16:03:46 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:03:44 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | -0.019 |  |
| 2026-07-01 16:03:15 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.029 |  |
| 2026-07-01 16:03:07 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-07-01 16:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:02:42 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:02:41 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-07-01 16:02:41 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:02:36 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 16:02:35 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:02:23 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:02:15 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-07-01 16:02:13 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 16:01:56 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 16:01:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:01:14 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:01:04 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.011 |  |
| 2026-07-01 16:01:03 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 16:04:47 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-07-01 16:09:41 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-01 16:02:13 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 16:01:56 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 16:02:36 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 16:02:41 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:02:35 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:05:18 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:01:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:05:31 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:01:03 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:05:06 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:04:47 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:02:23 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:03:46 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:02:42 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:04:24 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:07:26 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:10:03 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:12:07 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:01:14 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-01 16:05:26 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | -0.005 |  |
| 2026-07-01 16:06:45 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-07-01 16:07:16 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-07-01 16:08:30 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-07-01 16:02:41 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-07-01 16:02:15 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-07-01 16:03:07 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-07-01 16:05:33 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.011 |  |
| 2026-07-01 16:01:04 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.011 |  |
| 2026-07-01 16:08:59 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.018 |  |
| 2026-07-01 16:03:44 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | -0.019 |  |
| 2026-07-01 15:00:42 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | -0.027 |  |
| 2026-07-01 16:07:07 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.028 |  |
| 2026-07-01 16:03:15 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.029 |  |
| 2026-07-01 16:04:14 | Hanwella (Kelani Ganga) | 1.84 | 🟢 Normal | -0.030 |  |
| 2026-07-01 16:09:10 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | -0.053 |  |
| 2026-07-01 16:06:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.05 | 🟢 Normal | -0.086 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)