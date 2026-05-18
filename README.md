# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_03:44:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **155,720 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 03:44:18 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.012 |  |
| 2026-05-19 03:27:33 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.012 |  |
| 2026-05-19 03:25:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.44 | 🟢 Normal | -0.068 |  |
| 2026-05-19 03:11:33 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-19 03:09:59 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-19 03:09:28 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-05-19 03:09:23 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | -0.012 |  |
| 2026-05-19 03:07:55 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.018 |  |
| 2026-05-19 03:07:08 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-19 03:06:45 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-19 03:06:29 | Hanwella (Kelani Ganga) | 1.95 | 🟢 Normal | -0.040 |  |
| 2026-05-19 03:06:13 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.029 |  |
| 2026-05-19 03:05:55 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-19 03:05:22 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-19 03:04:40 | Ellagawa (Kalu Ganga) | 5.63 | 🟢 Normal | -0.029 |  |
| 2026-05-19 03:04:36 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -2.000 |  |
| 2026-05-19 03:04:18 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -2.000 |  |
| 2026-05-19 03:04:16 | Dunamale (Aththanagalu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-05-19 03:04:15 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-19 03:04:03 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-05-19 03:03:59 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-19 03:03:56 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-19 03:03:43 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-19 03:03:36 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-19 03:03:32 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 1.333 | 🔺 Rising |
| 2026-05-19 03:03:32 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-05-19 03:03:19 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | -0.045 |  |
| 2026-05-19 03:03:10 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.041 |  |
| 2026-05-19 03:03:05 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 1.333 | 🔺 Rising |
| 2026-05-19 03:02:51 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-05-19 03:02:50 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-19 03:02:47 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-19 03:02:37 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-05-19 03:01:49 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-05-19 03:01:37 | Moraketiya (Walawe Ganga) | 1.88 | 🟢 Normal | -0.154 |  |
| 2026-05-19 03:00:45 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-05-19 03:00:43 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 03:03:32 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 1.333 | 🔺 Rising |
| 2026-05-19 03:03:56 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-19 03:03:59 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-19 03:09:59 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-19 03:05:22 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-19 02:01:21 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-18 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-19 03:00:43 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 03:11:33 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-19 02:04:22 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 03:03:36 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-19 03:07:08 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-19 03:04:15 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-19 03:04:16 | Dunamale (Aththanagalu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-05-19 03:02:50 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-05-19 03:06:45 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-19 03:02:51 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-05-19 03:04:03 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-05-19 03:00:45 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-05-19 03:02:37 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-05-19 03:01:49 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-05-19 03:27:33 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.012 |  |
| 2026-05-19 03:44:18 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.012 |  |
| 2026-05-19 03:09:23 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | -0.012 |  |
| 2026-05-19 03:07:55 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | -0.018 |  |
| 2026-05-19 03:09:28 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-05-19 03:03:32 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | -0.020 |  |
| 2026-05-19 01:03:56 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.022 |  |
| 2026-05-19 02:46:59 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | -0.023 |  |
| 2026-05-19 03:04:40 | Ellagawa (Kalu Ganga) | 5.63 | 🟢 Normal | -0.029 |  |
| 2026-05-19 03:06:13 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.029 |  |
| 2026-05-18 18:01:53 | Galgamuwa (Mee Oya) | 1.67 | 🟢 Normal | -0.033 |  |
| 2026-05-19 03:06:29 | Hanwella (Kelani Ganga) | 1.95 | 🟢 Normal | -0.040 |  |
| 2026-05-19 03:03:10 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.041 |  |
| 2026-05-19 03:03:19 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | -0.045 |  |
| 2026-05-19 03:25:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.44 | 🟢 Normal | -0.068 |  |
| 2026-05-18 18:01:24 | Thanthirimale (Malwathu Oya) | 2.75 | 🟢 Normal | -0.082 |  |
| 2026-05-19 03:01:37 | Moraketiya (Walawe Ganga) | 1.88 | 🟢 Normal | -0.154 |  |
| 2026-05-19 03:04:36 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -2.000 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)