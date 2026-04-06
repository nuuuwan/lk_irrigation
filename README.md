# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_15:15:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,826 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 15:15:41 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:13:37 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:13:22 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:10:33 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:10:05 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | -0.009 |  |
| 2026-04-06 15:08:41 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:08:17 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:07:40 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:07:08 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | -0.010 |  |
| 2026-04-06 15:06:04 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | -0.018 |  |
| 2026-04-06 15:05:59 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.372 | 🔺 Rising |
| 2026-04-06 15:05:41 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 15:05:27 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:05:16 | Glencourse (Kelani Ganga) | 8.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-06 15:05:11 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-04-06 15:05:04 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:04:51 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:04:37 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:04:28 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:04:11 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 15:04:03 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-06 15:03:57 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:03:50 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:03:46 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 15:03:20 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-04-06 15:03:11 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-04-06 15:03:00 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.032 |  |
| 2026-04-06 15:02:57 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:02:28 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:02:18 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-04-06 15:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 15:02:09 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | -0.011 |  |
| 2026-04-06 15:02:06 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-04-06 15:01:49 | Manampitiya (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-06 15:01:49 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-04-06 15:01:42 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:01:00 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.273 |  |
| 2026-04-06 15:00:27 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.063 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 15:05:59 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.372 | 🔺 Rising |
| 2026-04-06 15:01:49 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-04-06 15:03:11 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-04-06 15:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-06 15:01:49 | Manampitiya (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-06 15:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 15:05:41 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 15:03:46 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 15:04:11 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 15:05:16 | Glencourse (Kelani Ganga) | 8.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-06 15:01:42 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:00:27 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:03:57 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:05:27 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:07:40 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:10:33 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:15:41 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:13:22 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:04:51 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:02:28 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:04:28 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:03:50 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:02:57 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:08:41 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:04:37 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:13:37 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-06 14:02:28 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:05:04 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-06 15:10:05 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | -0.009 |  |
| 2026-04-06 15:02:18 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-04-06 15:07:08 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | -0.010 |  |
| 2026-04-06 15:05:11 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-04-06 15:04:03 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-06 15:02:06 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-04-06 15:02:09 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | -0.011 |  |
| 2026-04-06 15:06:04 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | -0.018 |  |
| 2026-04-06 15:03:20 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-04-06 15:03:00 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.032 |  |
| 2026-04-06 15:01:00 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.273 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)