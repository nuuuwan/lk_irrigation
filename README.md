# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_14:18:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,470 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 14:18:31 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-16 14:18:27 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.383 |  |
| 2026-05-16 14:16:00 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-16 14:12:05 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | -0.045 |  |
| 2026-05-16 14:10:40 | Moragaswewa (Deduru Oya) | 3.01 | 🟢 Normal | 0.000 |  |
| 2026-05-16 14:09:46 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-16 14:09:29 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-05-16 14:09:18 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-16 14:08:26 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.027 |  |
| 2026-05-16 14:07:47 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.009 |  |
| 2026-05-16 14:07:38 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 14:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-16 14:06:37 | Dunamale (Aththanagalu Oya) | 4.08 | 🟡 Alert | -0.096 |  |
| 2026-05-16 14:05:43 | Glencourse (Kelani Ganga) | 10.87 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-16 14:04:54 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-16 14:03:34 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-16 14:05:51 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-16 14:01:54 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 14:10:40 | Moragaswewa (Deduru Oya) | 3.01 | 🟢 Normal | 0.000 |  |
| 2026-05-16 14:01:32 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-16 14:09:46 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-16 14:03:52 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-16 14:18:31 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-16 14:04:49 | Rathnapura (Kalu Ganga) | 3.41 | 🟢 Normal | 0.000 |  |
| 2026-05-16 14:09:29 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-05-16 14:07:38 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-05-16 14:09:18 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-16 14:16:00 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-16 14:00:12 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-16 14:02:09 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 14:07:47 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.009 |  |
| 2026-05-16 14:02:21 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-16 14:00:33 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-05-16 14:01:23 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.010 |  |
| 2026-05-16 14:02:19 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-05-16 14:01:58 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | -0.011 |  |
| 2026-05-16 14:03:21 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-05-16 14:05:52 | Ellagawa (Kalu Ganga) | 8.28 | 🟢 Normal | -0.019 |  |
| 2026-05-16 14:03:18 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | -0.021 |  |
| 2026-05-16 14:08:26 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.027 |  |
| 2026-05-16 14:04:07 | Thanthirimale (Malwathu Oya) | 3.95 | 🟢 Normal | -0.031 |  |
| 2026-05-16 14:03:46 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.031 |  |
| 2026-05-16 14:06:33 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.031 |  |
| 2026-05-16 14:05:05 | Baddegama (Gin Ganga) | 2.81 | 🟢 Normal | -0.031 |  |
| 2026-05-16 14:03:39 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | -0.040 |  |
| 2026-05-16 14:12:05 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | -0.045 |  |
| 2026-05-16 14:03:24 | Hanwella (Kelani Ganga) | 3.56 | 🟢 Normal | -0.061 |  |
| 2026-05-16 14:06:55 | Galgamuwa (Mee Oya) | 3.29 | 🟢 Normal | -0.065 |  |
| 2026-05-16 14:07:13 | Badalgama (Maha Oya) | 3.36 | 🟢 Normal | -0.068 |  |
| 2026-05-16 14:18:27 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | -0.383 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)