# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_05:03:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,170 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 05:03:19 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-05-15 05:02:58 | Deraniyagala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.069 |  |
| 2026-05-15 05:02:57 | Giriulla (Maha Oya) | 3.78 | 🟢 Normal | -0.030 |  |
| 2026-05-15 05:02:51 | Horowpothana (Yan Oya) | 2.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 05:02:49 | Badalgama (Maha Oya) | 4.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-15 05:01:52 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-05-15 05:01:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.76 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-15 05:01:47 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.040 |  |
| 2026-05-15 05:01:12 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.130 |  |
| 2026-05-15 05:01:01 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.133 |  |
| 2026-05-15 05:00:37 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-15 04:51:59 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.130 |  |
| 2026-05-15 04:49:19 | Magura (Kalu Ganga) | 4.83 | 🟡 Alert | -0.026 |  |
| 2026-05-15 04:20:28 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-15 04:14:36 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | 0.049 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 04:06:59 | Dunamale (Aththanagalu Oya) | 4.59 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-05-15 05:01:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.76 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-15 04:49:19 | Magura (Kalu Ganga) | 4.83 | 🟡 Alert | -0.026 |  |
| 2026-05-15 04:05:44 | Moragaswewa (Deduru Oya) | 2.55 | 🟢 Normal | 0.478 | 🔺 Rising |
| 2026-05-15 04:03:41 | Hanwella (Kelani Ganga) | 6.20 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-15 04:02:22 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-15 04:14:36 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-15 04:04:06 | Thawalama (Gin Ganga) | 2.78 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-15 03:07:10 | Baddegama (Gin Ganga) | 3.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 05:02:49 | Badalgama (Maha Oya) | 4.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-15 05:02:51 | Horowpothana (Yan Oya) | 2.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 18:00:44 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.000 |  |
| 2026-05-15 05:00:37 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-15 04:08:13 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-05-15 04:03:27 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 03:03:34 | Katharagama (Menik Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-15 04:06:09 | Rathnapura (Kalu Ganga) | 4.84 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:03:16 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-15 04:00:39 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-15 03:16:08 | Putupaula (Kalu Ganga) | 2.57 | 🟢 Normal | -0.005 |  |
| 2026-05-15 04:07:41 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.009 |  |
| 2026-05-15 04:05:07 | Glencourse (Kelani Ganga) | 14.14 | 🟢 Normal | -0.010 |  |
| 2026-05-15 04:01:45 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-05-15 05:01:52 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-05-15 04:01:23 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-15 03:01:43 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.018 |  |
| 2026-05-15 03:04:21 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-05-15 04:02:12 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-05-15 05:03:19 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-05-15 05:02:57 | Giriulla (Maha Oya) | 3.78 | 🟢 Normal | -0.030 |  |
| 2026-05-15 04:03:29 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-05-15 04:03:24 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.035 |  |
| 2026-05-15 05:01:47 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.040 |  |
| 2026-05-15 04:10:05 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.048 |  |
| 2026-05-15 05:02:58 | Deraniyagala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.069 |  |
| 2026-05-15 04:07:52 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.074 |  |
| 2026-05-14 18:05:46 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.087 |  |
| 2026-05-15 05:01:12 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.130 |  |
| 2026-05-15 05:01:01 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)