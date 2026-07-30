# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_05:04:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **220,877 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 05:04:21 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 05:04:03 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-31 05:04:01 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 05:03:24 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-07-31 05:03:18 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-31 05:03:12 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-31 05:03:11 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-31 05:03:10 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-31 05:03:08 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.518 | 🔺 Rising |
| 2026-07-31 05:03:03 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-07-31 05:02:54 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-31 05:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.060 |  |
| 2026-07-31 05:02:24 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | -0.014 |  |
| 2026-07-31 05:02:16 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 05:01:51 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 05:01:46 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-31 05:00:29 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-31 05:00:24 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-07-31 05:00:13 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-31 04:51:04 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 04:50:45 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-07-31 04:50:37 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 04:45:25 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 04:29:12 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-31 04:27:27 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-31 04:26:22 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-07-31 04:24:30 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-07-31 04:20:48 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 05:03:08 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.518 | 🔺 Rising |
| 2026-07-31 05:00:24 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-07-31 04:05:42 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-31 05:03:11 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-31 05:04:03 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-31 04:07:43 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-07-31 05:04:01 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 04:24:30 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-07-31 04:45:25 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 05:01:51 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 04:06:36 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 05:02:16 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 18:04:12 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 04:50:45 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-07-31 04:29:12 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-31 05:03:10 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-31 04:10:38 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2026-07-31 05:00:29 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-31 05:04:21 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 05:03:12 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-31 04:03:26 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.000 |  |
| 2026-07-31 04:02:40 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-31 05:00:13 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-31 04:02:20 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-31 05:02:54 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-31 05:03:18 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-31 04:10:57 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-31 03:05:59 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-31 04:03:16 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 05:01:46 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-31 04:03:00 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-31 05:03:03 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-07-30 18:01:03 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-07-31 05:03:24 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-07-31 04:02:15 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-07-31 05:02:24 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | -0.014 |  |
| 2026-07-31 05:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.060 |  |
| 2026-07-30 18:00:15 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.060 |  |
| 2026-07-31 04:05:18 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.207 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)