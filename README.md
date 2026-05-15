# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_09:37:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,357 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **9** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 09:37:43 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | -1.440 |  |
| 2026-05-15 09:36:03 | Thawalama (Gin Ganga) | 2.64 | 🟢 Normal | -1.440 |  |
| 2026-05-15 09:17:05 | Panadugama (Nilwala Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-05-15 09:11:08 | Baddegama (Gin Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-05-15 09:10:48 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 09:09:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.93 | 🟠 Minor Flood | 0.035 | 🔺 Rising |
| 2026-05-15 09:09:18 | Galgamuwa (Mee Oya) | 3.50 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-15 09:07:51 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-15 09:07:32 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -1.440 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 09:09:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.93 | 🟠 Minor Flood | 0.035 | 🔺 Rising |
| 2026-05-15 09:05:45 | Dunamale (Aththanagalu Oya) | 4.72 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 09:06:59 | Magura (Kalu Ganga) | 4.78 | 🟡 Alert | -0.020 |  |
| 2026-05-15 09:04:48 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-05-15 09:04:34 | Nagalagam Street (Kelani Ganga) | 0.96 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-05-15 09:09:18 | Galgamuwa (Mee Oya) | 3.50 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-15 09:01:18 | Thanthirimale (Malwathu Oya) | 3.88 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-15 09:04:23 | Moragaswewa (Deduru Oya) | 3.78 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-15 09:00:23 | Horowpothana (Yan Oya) | 2.95 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-15 09:02:20 | Putupaula (Kalu Ganga) | 2.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 09:01:03 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 09:02:51 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-15 09:04:28 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-15 09:01:49 | Ellagawa (Kalu Ganga) | 8.69 | 🟢 Normal | 0.000 |  |
| 2026-05-15 09:11:08 | Baddegama (Gin Ganga) | 3.30 | 🟢 Normal | 0.000 |  |
| 2026-05-15 09:17:05 | Panadugama (Nilwala Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-05-15 09:10:48 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 09:04:00 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-15 09:02:31 | Katharagama (Menik Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-15 09:07:51 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-15 09:02:59 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-15 09:04:09 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-15 09:04:19 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-15 09:02:12 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-15 09:04:23 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-05-15 09:02:23 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-05-15 09:00:19 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.011 |  |
| 2026-05-15 09:00:30 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-05-15 09:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-05-15 09:00:40 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.021 |  |
| 2026-05-15 09:00:18 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.030 |  |
| 2026-05-15 09:05:11 | Badalgama (Maha Oya) | 4.62 | 🟢 Normal | -0.040 |  |
| 2026-05-15 09:02:43 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.040 |  |
| 2026-05-15 09:05:25 | Rathnapura (Kalu Ganga) | 4.72 | 🟢 Normal | -0.050 |  |
| 2026-05-15 09:03:11 | Hanwella (Kelani Ganga) | 6.12 | 🟢 Normal | -0.050 |  |
| 2026-05-15 09:04:56 | Giriulla (Maha Oya) | 3.51 | 🟢 Normal | -0.076 |  |
| 2026-05-15 09:04:30 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.142 |  |
| 2026-05-15 09:05:17 | Glencourse (Kelani Ganga) | 13.22 | 🟢 Normal | -0.189 |  |
| 2026-05-15 09:37:43 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | -1.440 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)