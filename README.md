# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_06:28:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,504 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 06:28:34 | Galgamuwa (Mee Oya) | 0.98 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-24 06:22:57 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-24 06:11:19 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-24 06:11:18 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-04-24 06:10:38 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-24 06:08:35 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-04-24 06:06:32 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 06:06:32 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | -0.030 |  |
| 2026-04-24 06:05:53 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-04-24 06:05:51 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-24 06:05:11 | Moraketiya (Walawe Ganga) | 1.24 | 🟢 Normal | -0.065 |  |
| 2026-04-24 06:04:25 | Katharagama (Menik Ganga) | 2.06 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-24 06:04:17 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-04-24 06:03:46 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 06:03:37 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.154 |  |
| 2026-04-24 06:03:20 | Glencourse (Kelani Ganga) | 9.64 | 🟢 Normal | -0.058 |  |
| 2026-04-24 06:03:18 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-24 06:03:05 | Thanamalwila (Kirindi Oya) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-04-24 06:03:00 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 06:02:58 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | -0.020 |  |
| 2026-04-24 06:02:38 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.068 |  |
| 2026-04-24 06:02:37 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-04-24 06:02:24 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 06:02:19 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.035 |  |
| 2026-04-24 06:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | -0.025 |  |
| 2026-04-24 06:02:09 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.031 |  |
| 2026-04-24 06:02:08 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -36.000 |  |
| 2026-04-24 06:02:07 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -36.000 |  |
| 2026-04-24 06:01:59 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-04-24 06:01:50 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.042 |  |
| 2026-04-24 06:01:42 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-04-24 06:01:33 | Kuda Oya (Kirindi Oya) | 2.14 | 🟢 Normal | -0.060 |  |
| 2026-04-24 06:01:12 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-04-24 06:01:11 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-04-24 06:00:54 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.046 |  |
| 2026-04-24 06:00:44 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.040 |  |
| 2026-04-24 06:00:28 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.221 |  |
| 2026-04-24 06:00:11 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-04-24 06:00:07 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 06:01:11 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-04-24 06:01:59 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-04-24 06:11:18 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-04-24 06:28:34 | Galgamuwa (Mee Oya) | 0.98 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-24 06:04:25 | Katharagama (Menik Ganga) | 2.06 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-24 06:05:51 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-24 06:06:32 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 18:03:04 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 06:01:12 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-04-24 06:02:24 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 06:03:00 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 06:22:57 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-24 06:03:46 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 06:00:07 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-24 06:11:19 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-24 06:03:18 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-24 06:00:11 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-04-24 06:01:42 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-04-24 06:03:05 | Thanamalwila (Kirindi Oya) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-04-24 06:08:35 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-04-24 06:02:37 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-04-24 06:04:17 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-04-24 06:02:58 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | -0.020 |  |
| 2026-04-24 06:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | -0.025 |  |
| 2026-04-24 06:06:32 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | -0.030 |  |
| 2026-04-24 06:05:53 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-04-24 06:02:09 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.031 |  |
| 2026-04-24 05:35:35 | Panadugama (Nilwala Ganga) | 3.19 | 🟢 Normal | -0.034 |  |
| 2026-04-24 06:02:19 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.035 |  |
| 2026-04-24 06:00:44 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.040 |  |
| 2026-04-24 06:01:50 | Nawalapitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.042 |  |
| 2026-04-24 06:00:54 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.046 |  |
| 2026-04-24 06:03:20 | Glencourse (Kelani Ganga) | 9.64 | 🟢 Normal | -0.058 |  |
| 2026-04-24 06:01:33 | Kuda Oya (Kirindi Oya) | 2.14 | 🟢 Normal | -0.060 |  |
| 2026-04-24 06:05:11 | Moraketiya (Walawe Ganga) | 1.24 | 🟢 Normal | -0.065 |  |
| 2026-04-24 06:02:38 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.068 |  |
| 2026-04-24 06:03:37 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.154 |  |
| 2026-04-24 06:00:28 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.221 |  |
| 2026-04-24 06:02:08 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)