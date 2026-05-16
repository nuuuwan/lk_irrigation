# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_18:05:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,620 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 18:05:51 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-16 18:05:47 | Baddegama (Gin Ganga) | 2.72 | 🟢 Normal | -0.021 |  |
| 2026-05-16 18:05:33 | Badalgama (Maha Oya) | 3.22 | 🟢 Normal | -0.031 |  |
| 2026-05-16 18:05:03 | Magura (Kalu Ganga) | 3.58 | 🟢 Normal | -0.075 |  |
| 2026-05-16 18:04:56 | Rathnapura (Kalu Ganga) | 3.89 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-05-16 18:04:54 | Ellagawa (Kalu Ganga) | 8.15 | 🟢 Normal | -0.036 |  |
| 2026-05-16 18:04:51 | Glencourse (Kelani Ganga) | 10.87 | 🟢 Normal | 0.000 |  |
| 2026-05-16 18:04:15 | Galgamuwa (Mee Oya) | 2.90 | 🟢 Normal | -0.048 |  |
| 2026-05-16 18:04:11 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-16 18:04:10 | Hanwella (Kelani Ganga) | 3.44 | 🟢 Normal | -0.030 |  |
| 2026-05-16 18:03:48 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | -0.010 |  |
| 2026-05-16 18:03:43 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-16 18:03:41 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-16 18:03:41 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 18:03:23 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-16 18:03:14 | Giriulla (Maha Oya) | 1.91 | 🟢 Normal | -0.040 |  |
| 2026-05-16 18:03:04 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 18:02:50 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | -0.020 |  |
| 2026-05-16 18:02:48 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-16 18:02:43 | Moragaswewa (Deduru Oya) | 2.90 | 🟢 Normal | -0.056 |  |
| 2026-05-16 18:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.95 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-16 18:02:17 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 18:02:16 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 18:02:10 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-16 18:02:02 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-16 18:01:55 | Thanthirimale (Malwathu Oya) | 3.80 | 🟢 Normal | -0.030 |  |
| 2026-05-16 18:01:18 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.100 |  |
| 2026-05-16 18:01:12 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-16 18:01:08 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-16 18:00:52 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-16 18:00:42 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | -0.020 |  |
| 2026-05-16 18:00:14 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:15:03 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:14:50 | Ellagawa (Kalu Ganga) | 8.18 | 🟢 Normal | -0.036 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 18:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.95 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-16 17:01:10 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | -0.109 |  |
| 2026-05-16 18:04:56 | Rathnapura (Kalu Ganga) | 3.89 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-05-16 18:02:02 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-16 18:04:11 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-16 18:03:41 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-16 18:03:23 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-16 17:04:02 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-16 18:01:12 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-16 18:03:41 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 18:02:16 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 18:03:04 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 17:04:00 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 18:02:48 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-16 18:00:14 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 18:01:08 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:03:11 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:01:07 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-16 18:04:51 | Glencourse (Kelani Ganga) | 10.87 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:03:08 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-16 18:03:43 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-16 18:02:10 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-16 18:05:51 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-16 17:15:03 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-16 18:00:52 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-16 18:02:17 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 18:03:48 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | -0.010 |  |
| 2026-05-16 18:02:50 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | -0.020 |  |
| 2026-05-16 18:00:42 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | -0.020 |  |
| 2026-05-16 18:05:47 | Baddegama (Gin Ganga) | 2.72 | 🟢 Normal | -0.021 |  |
| 2026-05-16 18:04:10 | Hanwella (Kelani Ganga) | 3.44 | 🟢 Normal | -0.030 |  |
| 2026-05-16 18:01:55 | Thanthirimale (Malwathu Oya) | 3.80 | 🟢 Normal | -0.030 |  |
| 2026-05-16 18:05:33 | Badalgama (Maha Oya) | 3.22 | 🟢 Normal | -0.031 |  |
| 2026-05-16 18:04:54 | Ellagawa (Kalu Ganga) | 8.15 | 🟢 Normal | -0.036 |  |
| 2026-05-16 18:03:14 | Giriulla (Maha Oya) | 1.91 | 🟢 Normal | -0.040 |  |
| 2026-05-16 18:04:15 | Galgamuwa (Mee Oya) | 2.90 | 🟢 Normal | -0.048 |  |
| 2026-05-16 18:02:43 | Moragaswewa (Deduru Oya) | 2.90 | 🟢 Normal | -0.056 |  |
| 2026-05-16 18:05:03 | Magura (Kalu Ganga) | 3.58 | 🟢 Normal | -0.075 |  |
| 2026-05-16 18:01:18 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)