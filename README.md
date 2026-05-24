# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--24_16:34:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **160,488 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 16:34:57 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.007 |  |
| 2026-05-24 16:11:57 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:10:50 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:10:24 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:09:51 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-24 16:09:01 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:08:59 | Glencourse (Kelani Ganga) | 10.63 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-24 16:08:08 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-05-24 16:07:43 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.018 |  |
| 2026-05-24 16:07:30 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:07:27 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:06:43 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | -0.020 |  |
| 2026-05-24 16:04:55 | Ellagawa (Kalu Ganga) | 9.71 | 🟢 Normal | -0.078 |  |
| 2026-05-24 16:04:44 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-05-24 16:04:43 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.030 |  |
| 2026-05-24 16:04:34 | Hanwella (Kelani Ganga) | 4.10 | 🟢 Normal | -0.079 |  |
| 2026-05-24 16:04:32 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-05-24 16:04:30 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 16:01:49 | Putupaula (Kalu Ganga) | 3.27 | 🟡 Alert | 0.000 |  |
| 2026-05-24 15:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.34 | 🟡 Alert | -0.021 |  |
| 2026-05-24 16:04:11 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | 1.189 | 🔺 Rising |
| 2026-05-24 16:04:32 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-05-24 16:09:51 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-24 16:08:59 | Glencourse (Kelani Ganga) | 10.63 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-24 16:00:55 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 16:04:30 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:01:44 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:07:27 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:01:41 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:00:39 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:11:57 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:10:50 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:02:51 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:01:38 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:10:24 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:00:23 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:00:13 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:07:30 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:09:01 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:00:26 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:02:17 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 16:34:57 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.007 |  |
| 2026-05-24 16:08:08 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-05-24 16:03:47 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-05-24 16:03:42 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-05-24 16:01:09 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-05-24 16:00:35 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-05-24 16:00:26 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-05-24 16:02:00 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-05-24 16:07:43 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.018 |  |
| 2026-05-24 16:06:43 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | -0.020 |  |
| 2026-05-24 16:04:44 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-05-24 16:04:43 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.030 |  |
| 2026-05-24 16:04:15 | Rathnapura (Kalu Ganga) | 3.87 | 🟢 Normal | -0.059 |  |
| 2026-05-24 16:02:29 | Dunamale (Aththanagalu Oya) | 3.22 | 🟢 Normal | -0.060 |  |
| 2026-05-24 16:04:55 | Ellagawa (Kalu Ganga) | 9.71 | 🟢 Normal | -0.078 |  |
| 2026-05-24 16:04:34 | Hanwella (Kelani Ganga) | 4.10 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)