# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--21_03:11:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **211,861 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-21 03:11:28 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:11:25 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:10:47 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:07:37 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:07:35 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:06:47 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -1.200 |  |
| 2026-07-21 03:06:17 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -1.200 |  |
| 2026-07-21 03:06:17 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.019 |  |
| 2026-07-21 03:06:02 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.375 |  |
| 2026-07-21 03:05:31 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.018 |  |
| 2026-07-21 03:05:24 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:05:14 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:05:07 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:05:00 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:04:01 | Glencourse (Kelani Ganga) | 9.37 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-07-21 03:03:47 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-21 03:03:37 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:03:06 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | -0.088 |  |
| 2026-07-21 03:02:54 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-21 03:02:46 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:02:29 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-07-21 03:02:25 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-07-21 03:02:07 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:02:06 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.021 |  |
| 2026-07-21 03:01:59 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:01:49 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:01:10 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.010 |  |
| 2026-07-21 03:01:07 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:00:56 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:00:42 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:00:10 | Thalgahagoda (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-21 02:26:10 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 234.000 | 🔺 Rising |
| 2026-07-21 03:02:25 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-07-21 03:04:01 | Glencourse (Kelani Ganga) | 9.37 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-07-21 02:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-21 03:03:47 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-21 03:02:54 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-21 03:02:07 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-21 02:09:18 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:01:59 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:11:28 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:00:42 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:03:25 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:05:07 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-20 23:30:18 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:05:00 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:00:56 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:07:35 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:01:07 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:02:46 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:05:24 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:01:49 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:10:47 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:11:25 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:07:37 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:01:29 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:00:10 | Thalgahagoda (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:03:37 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:05:14 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-21 03:01:10 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.010 |  |
| 2026-07-21 03:02:29 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-07-21 02:02:34 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | -0.011 |  |
| 2026-07-21 03:05:31 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.018 |  |
| 2026-07-21 03:06:17 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.019 |  |
| 2026-07-21 02:04:26 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-07-21 03:02:06 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.021 |  |
| 2026-07-20 18:01:44 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.050 |  |
| 2026-07-21 03:03:06 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | -0.088 |  |
| 2026-07-21 03:06:02 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.375 |  |
| 2026-07-21 03:06:47 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -1.200 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)