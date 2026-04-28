# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_13:04:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,332 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 13:04:50 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:04:29 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.020 |  |
| 2026-04-28 13:04:03 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-28 13:04:00 | Hanwella (Kelani Ganga) | 1.07 | 🟢 Normal | -0.059 |  |
| 2026-04-28 13:03:58 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | -0.071 |  |
| 2026-04-28 13:03:27 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-04-28 13:03:22 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-04-28 13:03:21 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-04-28 13:03:18 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:03:07 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-28 13:03:03 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:03:02 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:02:58 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | -0.020 |  |
| 2026-04-28 13:02:39 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:02:39 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-04-28 13:02:27 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:02:19 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.054 |  |
| 2026-04-28 13:02:09 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.060 |  |
| 2026-04-28 13:01:47 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:01:31 | Manampitiya (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-28 13:00:47 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:00:36 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.020 |  |
| 2026-04-28 13:00:06 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-28 12:59:48 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:18:00 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:13:08 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | -0.071 |  |
| 2026-04-28 12:12:38 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 13:00:06 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-28 13:04:03 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-28 12:01:24 | Thanthirimale (Malwathu Oya) | 2.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-28 13:03:03 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:00:47 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:02:17 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-28 11:58:50 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:01:47 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:04:50 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:03:02 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:03:18 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:18:00 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:59:48 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:02:27 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-28 13:02:39 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:12:38 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:01:24 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:04:32 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:03:09 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:09:46 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-04-28 12:04:22 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-04-28 13:03:22 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-04-28 13:03:21 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-04-28 13:03:07 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-28 13:01:31 | Manampitiya (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-28 12:00:54 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-28 13:02:39 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-04-28 12:03:27 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.016 |  |
| 2026-04-28 13:03:27 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-04-28 13:00:36 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.020 |  |
| 2026-04-28 13:02:58 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | -0.020 |  |
| 2026-04-28 12:02:55 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.020 |  |
| 2026-04-28 13:04:29 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.020 |  |
| 2026-04-28 12:06:27 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.049 |  |
| 2026-04-28 13:02:19 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.054 |  |
| 2026-04-28 13:04:00 | Hanwella (Kelani Ganga) | 1.07 | 🟢 Normal | -0.059 |  |
| 2026-04-28 13:02:09 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.060 |  |
| 2026-04-28 13:03:58 | Dunamale (Aththanagalu Oya) | 1.72 | 🟢 Normal | -0.071 |  |
| 2026-04-28 12:07:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.078 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)