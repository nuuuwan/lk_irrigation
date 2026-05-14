# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_04:06:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,150 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 04:06:45 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-05-15 04:06:09 | Rathnapura (Kalu Ganga) | 4.84 | 🟢 Normal | 0.000 |  |
| 2026-05-15 04:05:44 | Moragaswewa (Deduru Oya) | 2.55 | 🟢 Normal | 0.478 | 🔺 Rising |
| 2026-05-15 04:05:42 | Badalgama (Maha Oya) | 4.75 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-15 04:05:07 | Glencourse (Kelani Ganga) | 14.14 | 🟢 Normal | -0.010 |  |
| 2026-05-15 04:04:06 | Thawalama (Gin Ganga) | 2.78 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-15 04:03:41 | Hanwella (Kelani Ganga) | 6.20 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-15 04:03:29 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-05-15 04:03:27 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 04:03:24 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.035 |  |
| 2026-05-15 04:02:58 | Giriulla (Maha Oya) | 3.81 | 🟢 Normal | -0.060 |  |
| 2026-05-15 04:02:47 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-05-15 04:02:22 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-15 04:02:12 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-05-15 04:02:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.78 | 🟠 Minor Flood | 0.066 | 🔺 Rising |
| 2026-05-15 04:01:45 | Horowpothana (Yan Oya) | 2.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 04:01:45 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-05-15 04:01:41 | Deraniyagala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.062 |  |
| 2026-05-15 04:01:23 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-15 04:01:03 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.088 |  |
| 2026-05-15 04:00:39 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-15 03:17:35 | Hanwella (Kelani Ganga) | 6.15 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-15 03:17:30 | Magura (Kalu Ganga) | 4.87 | 🟡 Alert | -0.139 |  |
| 2026-05-15 03:16:59 | Rathnapura (Kalu Ganga) | 4.84 | 🟢 Normal | 0.000 |  |
| 2026-05-15 03:16:08 | Putupaula (Kalu Ganga) | 2.57 | 🟢 Normal | -0.005 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 04:02:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.78 | 🟠 Minor Flood | 0.066 | 🔺 Rising |
| 2026-05-15 03:03:46 | Dunamale (Aththanagalu Oya) | 4.58 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-15 03:17:30 | Magura (Kalu Ganga) | 4.87 | 🟡 Alert | -0.139 |  |
| 2026-05-15 04:05:44 | Moragaswewa (Deduru Oya) | 2.55 | 🟢 Normal | 0.478 | 🔺 Rising |
| 2026-05-15 04:03:41 | Hanwella (Kelani Ganga) | 6.20 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-15 04:02:22 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-15 03:13:48 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-15 03:01:49 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-15 04:05:42 | Badalgama (Maha Oya) | 4.75 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-15 04:04:06 | Thawalama (Gin Ganga) | 2.78 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-15 03:07:10 | Baddegama (Gin Ganga) | 3.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 04:01:45 | Horowpothana (Yan Oya) | 2.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 04:02:47 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:00:44 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.000 |  |
| 2026-05-15 04:03:27 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 03:03:34 | Katharagama (Menik Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-15 04:06:09 | Rathnapura (Kalu Ganga) | 4.84 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:03:16 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-15 04:00:39 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-15 03:16:08 | Putupaula (Kalu Ganga) | 2.57 | 🟢 Normal | -0.005 |  |
| 2026-05-15 04:06:45 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-05-15 04:05:07 | Glencourse (Kelani Ganga) | 14.14 | 🟢 Normal | -0.010 |  |
| 2026-05-15 03:02:49 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-05-15 04:01:45 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-05-15 04:01:23 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-15 03:03:39 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | -0.011 |  |
| 2026-05-15 03:01:43 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.018 |  |
| 2026-05-15 03:04:21 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-05-15 04:02:12 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-05-15 03:04:45 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | -0.021 |  |
| 2026-05-15 04:03:29 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-05-15 04:03:24 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.035 |  |
| 2026-05-15 03:00:14 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.040 |  |
| 2026-05-15 04:02:58 | Giriulla (Maha Oya) | 3.81 | 🟢 Normal | -0.060 |  |
| 2026-05-15 04:01:41 | Deraniyagala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.062 |  |
| 2026-05-15 03:03:12 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.062 |  |
| 2026-05-14 18:05:46 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.087 |  |
| 2026-05-15 04:01:03 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.088 |  |
| 2026-05-15 03:07:37 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)