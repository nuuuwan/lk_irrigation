# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_17:01:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,735 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 17:01:59 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:01:57 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:01:50 | Giriulla (Maha Oya) | 3.04 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-05-14 17:01:25 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-05-14 17:01:05 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 17:00:55 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:00:28 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-05-14 17:00:06 | Horowpothana (Yan Oya) | 2.54 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-14 16:59:25 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-14 16:58:57 | Rathnapura (Kalu Ganga) | 4.59 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-05-14 16:24:59 | Magura (Kalu Ganga) | 4.92 | 🟡 Alert | 0.102 | 🔺 Rising |
| 2026-05-14 16:24:24 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-14 16:10:46 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.078 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 16:24:59 | Magura (Kalu Ganga) | 4.92 | 🟡 Alert | 0.102 | 🔺 Rising |
| 2026-05-14 16:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.46 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-05-14 16:04:42 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | 0.545 | 🔺 Rising |
| 2026-05-14 16:04:24 | Nawalapitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.467 | 🔺 Rising |
| 2026-05-14 16:06:37 | Holombuwa (Kelani Ganga) | 1.41 | 🟢 Normal | 0.342 | 🔺 Rising |
| 2026-05-14 16:04:04 | Deraniyagala (Kelani Ganga) | 3.81 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-05-14 16:07:26 | Dunamale (Aththanagalu Oya) | 3.06 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-05-14 16:04:13 | Hanwella (Kelani Ganga) | 2.52 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-05-14 17:01:50 | Giriulla (Maha Oya) | 3.04 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-05-14 16:58:57 | Rathnapura (Kalu Ganga) | 4.59 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-05-14 16:05:14 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-05-14 16:10:46 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-14 16:04:08 | Ellagawa (Kalu Ganga) | 8.28 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-14 16:07:11 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-14 17:00:06 | Horowpothana (Yan Oya) | 2.54 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-14 16:03:37 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-14 17:01:05 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 16:01:57 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 17:01:57 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.000 |  |
| 2026-05-14 16:02:19 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-14 16:08:28 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-14 16:02:59 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:01:59 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-14 16:01:46 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-14 16:02:09 | Katharagama (Menik Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:00:55 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-14 16:24:24 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-14 16:59:25 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-14 16:02:45 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-05-14 16:02:13 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-14 17:01:25 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-05-14 16:02:10 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-05-14 16:03:57 | Baddegama (Gin Ganga) | 3.15 | 🟢 Normal | -0.010 |  |
| 2026-05-14 16:04:52 | Moragaswewa (Deduru Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-05-14 17:00:28 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-05-14 16:06:31 | Panadugama (Nilwala Ganga) | 3.91 | 🟢 Normal | -0.031 |  |
| 2026-05-14 16:04:53 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.094 |  |
| 2026-05-14 16:06:50 | Thawalama (Gin Ganga) | 2.13 | 🟢 Normal | -0.141 |  |
| 2026-05-14 16:02:33 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)