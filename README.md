# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--21_10:09:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **103,289 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 10:09:51 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-21 10:07:37 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:06:40 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:05:54 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:05:30 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.021 |  |
| 2026-03-21 10:05:13 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-03-21 10:05:08 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-21 10:04:52 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:04:43 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:04:32 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.017 |  |
| 2026-03-21 10:04:09 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-03-21 10:04:07 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:03:35 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:03:33 | Weraganthota (Mahaweli Ganga) | -1.93 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-03-21 10:03:18 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:03:16 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:03:09 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:03:09 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-21 10:03:05 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:02:52 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:02:49 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:02:45 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.127 |  |
| 2026-03-21 10:02:30 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:02:27 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.070 |  |
| 2026-03-21 10:02:23 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:02:13 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:02:12 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:02:11 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.060 |  |
| 2026-03-21 10:02:05 | Putupaula (Kalu Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-03-21 10:01:32 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-03-21 10:01:25 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:01:17 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:01:13 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:01:12 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-03-21 10:01:04 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-03-21 10:00:37 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 1.153 | 🔺 Rising |
| 2026-03-21 10:00:35 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-21 09:59:41 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-03-21 09:59:29 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:29:48 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.017 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 10:00:37 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 1.153 | 🔺 Rising |
| 2026-03-21 10:05:13 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-03-21 10:03:33 | Weraganthota (Mahaweli Ganga) | -1.93 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-03-21 10:03:09 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-21 10:09:51 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-21 10:03:16 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:01:13 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-21 09:01:54 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:02:23 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:02:11 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:04:52 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:04:43 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:02:13 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:03:05 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:03:18 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:01:17 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:03:35 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:03:09 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:06:40 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:02:30 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:02:12 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:04:07 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:02:49 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:05:54 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:01:25 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:07:37 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 10:05:08 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-21 10:04:09 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-03-21 10:00:35 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-21 10:01:04 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-03-21 09:59:41 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2026-03-21 10:01:12 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-03-21 10:04:32 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.017 |  |
| 2026-03-21 10:01:32 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-03-21 10:05:30 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.021 |  |
| 2026-03-21 10:02:05 | Putupaula (Kalu Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-03-21 10:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.060 |  |
| 2026-03-21 10:02:27 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.070 |  |
| 2026-03-21 10:02:45 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)