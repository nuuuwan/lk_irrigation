# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_03:12:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **129,808 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 03:12:48 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:08:25 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.013 |  |
| 2026-04-20 03:08:10 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:07:08 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 03:06:53 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-04-20 03:06:52 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-04-20 03:06:50 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-04-20 03:06:32 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:06:23 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 03:05:42 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.149 |  |
| 2026-04-20 03:05:37 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-04-20 03:05:20 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-20 03:04:14 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:03:59 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.602 | 🔺 Rising |
| 2026-04-20 03:03:44 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:03:34 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 03:03:29 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:03:18 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:03:16 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:03:05 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-04-20 03:03:02 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:03:02 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-04-20 03:02:54 | Manampitiya (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2026-04-20 03:02:51 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-04-20 03:02:49 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 03:02:30 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-04-20 03:02:16 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 03:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.032 |  |
| 2026-04-20 03:02:06 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:01:47 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-20 03:01:42 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:00:51 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:00:30 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.022 |  |
| 2026-04-20 03:00:27 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-20 02:43:03 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.602 | 🔺 Rising |
| 2026-04-20 02:38:05 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-04-20 02:37:08 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 03:06:53 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-04-20 02:04:20 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.797 | 🔺 Rising |
| 2026-04-20 03:03:59 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.602 | 🔺 Rising |
| 2026-04-20 03:03:05 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-04-20 03:02:30 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-04-20 03:05:20 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-19 18:00:27 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-20 03:01:47 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-20 03:03:34 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 03:02:16 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 03:02:49 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 03:06:23 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 03:07:08 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 03:02:51 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-04-20 03:00:27 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:00:51 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:01:42 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:04:14 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:03:44 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:06:32 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:03:18 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:02:06 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:03:29 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:08:10 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 00:02:42 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:03:02 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:12:48 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:02:04 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-20 03:08:25 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.013 |  |
| 2026-04-19 21:20:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.017 |  |
| 2026-04-20 03:03:02 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-04-20 03:05:37 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-04-20 03:00:30 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.022 |  |
| 2026-04-20 03:02:54 | Manampitiya (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.029 |  |
| 2026-04-20 03:06:50 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-04-20 03:02:15 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.032 |  |
| 2026-04-20 02:11:12 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | -0.034 |  |
| 2026-04-19 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.068 |  |
| 2026-04-20 03:05:42 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)