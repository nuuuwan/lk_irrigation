# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_14:01:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,077 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 14:01:50 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 14:01:44 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-12 14:01:35 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-12 14:01:22 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-12 14:01:20 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-12 14:01:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.021 |  |
| 2026-04-12 14:00:58 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | -0.020 |  |
| 2026-04-12 14:00:43 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-12 14:00:32 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-12 14:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-12 14:00:17 | Weraganthota (Mahaweli Ganga) | -2.81 | 🟢 Normal | -0.124 |  |
| 2026-04-12 13:16:47 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-12 13:15:35 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-04-12 13:12:16 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 13:10:52 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-12 13:10:42 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-12 13:10:12 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 13:08:54 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.012 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 13:01:05 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-04-12 13:08:20 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-04-12 13:10:42 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-12 13:03:23 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-12 13:06:15 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-12 14:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-12 14:01:50 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 13:01:44 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 12:16:44 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-12 13:03:14 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-12 14:01:35 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-12 14:01:22 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-12 13:05:46 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 13:05:19 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-12 14:00:32 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-12 13:08:07 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-12 13:15:35 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-04-12 13:12:16 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 13:05:09 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-12 13:03:36 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-12 13:02:57 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-12 13:10:12 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 13:07:10 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-12 13:06:48 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-04-12 14:00:43 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-12 13:07:46 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-12 13:04:05 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-12 14:01:44 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-12 13:04:01 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-04-12 14:01:20 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-12 13:06:01 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-04-12 13:06:27 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-04-12 14:00:58 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | -0.020 |  |
| 2026-04-12 14:01:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.021 |  |
| 2026-04-12 12:07:31 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.021 |  |
| 2026-04-12 12:04:48 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.021 |  |
| 2026-04-12 13:03:35 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.079 |  |
| 2026-04-12 14:00:17 | Weraganthota (Mahaweli Ganga) | -2.81 | 🟢 Normal | -0.124 |  |
| 2026-04-12 13:05:16 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)