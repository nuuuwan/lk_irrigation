# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_10:16:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **154,194 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 10:16:06 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:11:54 | Moragaswewa (Deduru Oya) | 1.37 | 🟢 Normal | -0.027 |  |
| 2026-05-17 10:09:34 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-17 10:09:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.75 | 🟠 Minor Flood | -0.018 |  |
| 2026-05-17 10:09:03 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:08:47 | Badalgama (Maha Oya) | 3.04 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:08:22 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-17 10:07:45 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.018 |  |
| 2026-05-17 10:06:59 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-05-17 10:06:38 | Panadugama (Nilwala Ganga) | 3.12 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:06:33 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:06:03 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-05-17 10:05:32 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-05-17 10:05:31 | Magura (Kalu Ganga) | 3.13 | 🟢 Normal | -0.053 |  |
| 2026-05-17 10:05:28 | Dunamale (Aththanagalu Oya) | 3.06 | 🟢 Normal | -0.041 |  |
| 2026-05-17 10:05:16 | Hanwella (Kelani Ganga) | 3.28 | 🟢 Normal | -0.029 |  |
| 2026-05-17 10:05:10 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | -0.021 |  |
| 2026-05-17 10:04:56 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-17 10:04:32 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-05-17 10:04:27 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-05-17 10:04:08 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:04:06 | Putupaula (Kalu Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:04:05 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:03:51 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:03:24 | Rathnapura (Kalu Ganga) | 3.27 | 🟢 Normal | -0.070 |  |
| 2026-05-17 10:03:04 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.019 |  |
| 2026-05-17 10:03:02 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:02:54 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-05-17 10:02:08 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:01:48 | Galgamuwa (Mee Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:01:47 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:01:28 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 10:01:25 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.101 |  |
| 2026-05-17 10:01:23 | Ellagawa (Kalu Ganga) | 7.84 | 🟢 Normal | -0.020 |  |
| 2026-05-17 10:01:19 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:01:05 | Thanthirimale (Malwathu Oya) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:00:19 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 10:09:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.75 | 🟠 Minor Flood | -0.018 |  |
| 2026-05-17 10:09:34 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-17 10:08:22 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-17 10:01:28 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 10:04:56 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-17 10:04:05 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-17 09:03:11 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:01:47 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:01:48 | Galgamuwa (Mee Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:06:38 | Panadugama (Nilwala Ganga) | 3.12 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:04:08 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:03:51 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:03:02 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:02:08 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:06:33 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:04:06 | Putupaula (Kalu Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:08:47 | Badalgama (Maha Oya) | 3.04 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:01:19 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:01:05 | Thanthirimale (Malwathu Oya) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:09:03 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:16:06 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-17 10:06:59 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-05-17 10:04:32 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-05-17 10:05:32 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-05-17 09:00:11 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-05-17 10:00:19 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-05-17 10:02:54 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-05-17 10:07:45 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.018 |  |
| 2026-05-17 10:06:03 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-05-17 10:03:04 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.019 |  |
| 2026-05-17 10:04:27 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-05-17 10:01:23 | Ellagawa (Kalu Ganga) | 7.84 | 🟢 Normal | -0.020 |  |
| 2026-05-17 10:05:10 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | -0.021 |  |
| 2026-05-17 10:11:54 | Moragaswewa (Deduru Oya) | 1.37 | 🟢 Normal | -0.027 |  |
| 2026-05-17 10:05:16 | Hanwella (Kelani Ganga) | 3.28 | 🟢 Normal | -0.029 |  |
| 2026-05-17 10:05:28 | Dunamale (Aththanagalu Oya) | 3.06 | 🟢 Normal | -0.041 |  |
| 2026-05-17 10:05:31 | Magura (Kalu Ganga) | 3.13 | 🟢 Normal | -0.053 |  |
| 2026-05-17 10:03:24 | Rathnapura (Kalu Ganga) | 3.27 | 🟢 Normal | -0.070 |  |
| 2026-05-17 10:01:25 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)