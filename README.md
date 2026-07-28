# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--28_19:13:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **218,764 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-28 19:13:43 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.214 |  |
| 2026-07-28 19:12:17 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-07-28 19:10:58 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:10:24 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-07-28 19:10:14 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:09:49 | Thalgahagoda (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:09:02 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:08:43 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:08:08 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:07:06 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-07-28 19:06:58 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:06:10 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.655 | 🔺 Rising |
| 2026-07-28 19:05:48 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:05:46 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:05:36 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:05:33 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:05:27 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.057 |  |
| 2026-07-28 19:05:04 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:04:51 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:04:43 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.063 |  |
| 2026-07-28 19:04:01 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:03:30 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-28 19:03:20 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:02:48 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:02:48 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:02:45 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-28 19:02:28 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-07-28 19:02:27 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:02:11 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-07-28 19:02:10 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:02:09 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:00:44 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.061 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-28 19:06:10 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.655 | 🔺 Rising |
| 2026-07-28 19:02:28 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-07-28 19:10:24 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-07-28 19:07:06 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-07-28 19:12:17 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-07-28 19:03:30 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-28 19:02:45 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-28 19:02:27 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:10:58 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:08:08 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:04:01 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:05:33 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:02:10 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-28 18:03:13 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-28 18:02:26 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:03:20 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:05:46 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-07-28 18:03:53 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:05:48 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:04:51 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:05:36 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:09:02 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:06:58 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:05:04 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:10:14 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-28 18:00:50 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:02:48 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:08:43 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:09:49 | Thalgahagoda (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:02:48 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-28 19:02:09 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-28 18:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-07-28 19:02:11 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-07-28 18:00:11 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.030 |  |
| 2026-07-28 19:05:27 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.057 |  |
| 2026-07-28 19:00:44 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.061 |  |
| 2026-07-28 19:04:43 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.063 |  |
| 2026-07-28 19:13:43 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.214 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)