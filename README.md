# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_13:19:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,430 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 13:19:24 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:11:37 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-05-16 13:08:54 | Manampitiya (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-05-16 13:08:08 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-16 13:07:09 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.027 |  |
| 2026-05-16 13:06:48 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:06:47 | Baddegama (Gin Ganga) | 2.84 | 🟢 Normal | -0.020 |  |
| 2026-05-16 13:06:22 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | -0.025 |  |
| 2026-05-16 13:06:05 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | -0.045 |  |
| 2026-05-16 13:05:38 | Badalgama (Maha Oya) | 3.43 | 🟢 Normal | -0.067 |  |
| 2026-05-16 13:05:30 | Thanthirimale (Malwathu Oya) | 3.98 | 🟢 Normal | -0.019 |  |
| 2026-05-16 13:05:20 | Magura (Kalu Ganga) | 3.83 | 🟢 Normal | -0.030 |  |
| 2026-05-16 13:05:14 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | -0.021 |  |
| 2026-05-16 13:05:04 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-05-16 13:04:48 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:04:35 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:04:34 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | -0.019 |  |
| 2026-05-16 13:04:18 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:04:02 | Giriulla (Maha Oya) | 2.14 | 🟢 Normal | -0.070 |  |
| 2026-05-16 13:04:02 | Hanwella (Kelani Ganga) | 3.62 | 🟢 Normal | -0.061 |  |
| 2026-05-16 13:03:49 | Dunamale (Aththanagalu Oya) | 4.18 | 🟡 Alert | -0.041 |  |
| 2026-05-16 13:03:35 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.019 |  |
| 2026-05-16 13:03:20 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:03:10 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:02:51 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:02:45 | Galgamuwa (Mee Oya) | 3.36 | 🟢 Normal | -0.041 |  |
| 2026-05-16 13:02:26 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.020 |  |
| 2026-05-16 13:02:23 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-16 13:02:13 | Nagalagam Street (Kelani Ganga) | 0.90 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-16 13:02:08 | Rathnapura (Kalu Ganga) | 3.41 | 🟢 Normal | -0.010 |  |
| 2026-05-16 13:02:04 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:02:00 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:01:53 | Moragaswewa (Deduru Oya) | 3.01 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:01:45 | Ellagawa (Kalu Ganga) | 8.30 | 🟢 Normal | -0.050 |  |
| 2026-05-16 13:01:37 | Yaka Wewa (Ma Oya) | 1.20 | 🟢 Normal | 0.581 | 🔺 Rising |
| 2026-05-16 13:01:29 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:01:26 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-16 13:01:08 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-16 12:59:49 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 13:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-16 13:03:49 | Dunamale (Aththanagalu Oya) | 4.18 | 🟡 Alert | -0.041 |  |
| 2026-05-16 13:01:37 | Yaka Wewa (Ma Oya) | 1.20 | 🟢 Normal | 0.581 | 🔺 Rising |
| 2026-05-16 13:05:04 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-05-16 13:01:26 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-16 13:01:08 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-16 13:02:13 | Nagalagam Street (Kelani Ganga) | 0.90 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-16 13:02:04 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:02:00 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:01:53 | Moragaswewa (Deduru Oya) | 3.01 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:04:18 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:01:29 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:19:24 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:04:35 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:03:10 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:02:51 | Putupaula (Kalu Ganga) | 2.91 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:06:48 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:03:20 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:04:48 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:02:23 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 13:08:54 | Manampitiya (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-05-16 13:11:37 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-05-16 13:08:08 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-16 13:02:08 | Rathnapura (Kalu Ganga) | 3.41 | 🟢 Normal | -0.010 |  |
| 2026-05-16 13:05:30 | Thanthirimale (Malwathu Oya) | 3.98 | 🟢 Normal | -0.019 |  |
| 2026-05-16 13:03:35 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.019 |  |
| 2026-05-16 13:04:34 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | -0.019 |  |
| 2026-05-16 13:02:26 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.020 |  |
| 2026-05-16 13:06:47 | Baddegama (Gin Ganga) | 2.84 | 🟢 Normal | -0.020 |  |
| 2026-05-16 13:05:14 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | -0.021 |  |
| 2026-05-16 13:06:22 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | -0.025 |  |
| 2026-05-16 13:07:09 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.027 |  |
| 2026-05-16 13:05:20 | Magura (Kalu Ganga) | 3.83 | 🟢 Normal | -0.030 |  |
| 2026-05-16 13:02:45 | Galgamuwa (Mee Oya) | 3.36 | 🟢 Normal | -0.041 |  |
| 2026-05-16 13:06:05 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | -0.045 |  |
| 2026-05-16 13:01:45 | Ellagawa (Kalu Ganga) | 8.30 | 🟢 Normal | -0.050 |  |
| 2026-05-16 13:04:02 | Hanwella (Kelani Ganga) | 3.62 | 🟢 Normal | -0.061 |  |
| 2026-05-16 13:05:38 | Badalgama (Maha Oya) | 3.43 | 🟢 Normal | -0.067 |  |
| 2026-05-16 13:04:02 | Giriulla (Maha Oya) | 2.14 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)