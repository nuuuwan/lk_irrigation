# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_01:21:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,866 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 01:21:33 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-17 01:18:04 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-17 01:16:41 | Dunamale (Aththanagalu Oya) | 3.41 | 🟡 Alert | -0.016 |  |
| 2026-05-17 01:16:22 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | -0.024 |  |
| 2026-05-17 01:14:08 | Panadugama (Nilwala Ganga) | 3.16 | 🟢 Normal | -0.009 |  |
| 2026-05-17 01:11:19 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | -0.034 |  |
| 2026-05-17 01:09:28 | Hanwella (Kelani Ganga) | 3.39 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-17 01:08:04 | Putupaula (Kalu Ganga) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-05-17 01:07:51 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-05-17 01:07:07 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.023 |  |
| 2026-05-17 01:06:31 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 00:01:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.93 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-17 01:16:41 | Dunamale (Aththanagalu Oya) | 3.41 | 🟡 Alert | -0.016 |  |
| 2026-05-17 01:03:41 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-05-17 00:01:38 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-16 18:01:12 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-17 01:09:28 | Hanwella (Kelani Ganga) | 3.39 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-17 01:06:20 | Thawalama (Gin Ganga) | 2.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 01:01:57 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-17 01:03:09 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-16 23:02:36 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-17 01:02:24 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-17 01:00:23 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-17 01:21:33 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-17 01:00:43 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-17 00:04:54 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-17 01:02:08 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | 0.000 |  |
| 2026-05-17 01:07:51 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-05-17 01:03:50 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-17 01:18:04 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-17 01:02:17 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-17 01:02:33 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-17 01:14:08 | Panadugama (Nilwala Ganga) | 3.16 | 🟢 Normal | -0.009 |  |
| 2026-05-17 00:03:41 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-05-17 01:02:04 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-05-17 00:02:37 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-17 01:00:57 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-05-17 01:08:04 | Putupaula (Kalu Ganga) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-05-17 01:02:51 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-05-17 01:04:35 | Ellagawa (Kalu Ganga) | 8.06 | 🟢 Normal | -0.020 |  |
| 2026-05-17 01:06:31 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.020 |  |
| 2026-05-17 01:02:08 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-05-17 01:07:07 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.023 |  |
| 2026-05-17 01:16:22 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | -0.024 |  |
| 2026-05-17 00:02:41 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.024 |  |
| 2026-05-16 18:01:55 | Thanthirimale (Malwathu Oya) | 3.80 | 🟢 Normal | -0.030 |  |
| 2026-05-17 01:11:19 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | -0.034 |  |
| 2026-05-16 18:04:15 | Galgamuwa (Mee Oya) | 2.90 | 🟢 Normal | -0.048 |  |
| 2026-05-17 01:01:29 | Moragaswewa (Deduru Oya) | 2.36 | 🟢 Normal | -0.061 |  |
| 2026-05-17 01:06:00 | Rathnapura (Kalu Ganga) | 3.85 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)