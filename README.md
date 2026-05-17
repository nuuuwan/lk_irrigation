# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_15:17:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **154,396 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 15:17:25 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.009 |  |
| 2026-05-17 15:10:11 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-17 15:10:11 | Moragaswewa (Deduru Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:08:40 | Magura (Kalu Ganga) | 2.81 | 🟢 Normal | -0.133 |  |
| 2026-05-17 15:07:49 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:06:40 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | -0.011 |  |
| 2026-05-17 15:06:06 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:05:52 | Rathnapura (Kalu Ganga) | 2.87 | 🟢 Normal | -0.077 |  |
| 2026-05-17 15:05:38 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.114 |  |
| 2026-05-17 15:04:46 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:04:42 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-05-17 15:04:02 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:04:01 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:03:58 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | -0.021 |  |
| 2026-05-17 15:03:56 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:03:53 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-05-17 15:03:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.66 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-17 15:03:40 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | -0.012 |  |
| 2026-05-17 15:03:34 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:03:33 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:03:32 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 15:03:24 | Hanwella (Kelani Ganga) | 3.10 | 🟢 Normal | -0.030 |  |
| 2026-05-17 15:03:19 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.012 |  |
| 2026-05-17 15:03:11 | Galgamuwa (Mee Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:02:35 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.033 |  |
| 2026-05-17 15:02:31 | Moragaswewa (Deduru Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:02:30 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-05-17 15:02:07 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:02:00 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-05-17 15:01:49 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:01:48 | Ellagawa (Kalu Ganga) | 7.64 | 🟢 Normal | -0.040 |  |
| 2026-05-17 15:01:40 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:01:39 | Thanthirimale (Malwathu Oya) | 3.65 | 🟢 Normal | -0.012 |  |
| 2026-05-17 15:01:28 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.022 |  |
| 2026-05-17 15:01:27 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-05-17 15:01:20 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:01:08 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | -0.022 |  |
| 2026-05-17 15:00:59 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-17 15:00:42 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-05-17 15:00:37 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-05-17 15:00:25 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 15:03:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.66 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-17 15:02:00 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-05-17 15:00:59 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-17 15:03:32 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 15:10:11 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-17 15:01:49 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:10:11 | Moragaswewa (Deduru Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:01:40 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:04:02 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:03:11 | Galgamuwa (Mee Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:04:01 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:07:49 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:03:33 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:04:46 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:01:20 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:03:34 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:03:56 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:06:06 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-05-17 15:17:25 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.009 |  |
| 2026-05-17 15:04:42 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-05-17 15:02:30 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-05-17 15:00:25 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-05-17 15:01:27 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-05-17 15:06:40 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | -0.011 |  |
| 2026-05-17 15:03:40 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | -0.012 |  |
| 2026-05-17 15:01:39 | Thanthirimale (Malwathu Oya) | 3.65 | 🟢 Normal | -0.012 |  |
| 2026-05-17 15:03:19 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.012 |  |
| 2026-05-17 15:00:42 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-05-17 15:03:53 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-05-17 15:00:37 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-05-17 15:03:58 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | -0.021 |  |
| 2026-05-17 15:01:08 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | -0.022 |  |
| 2026-05-17 15:01:28 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.022 |  |
| 2026-05-17 15:03:24 | Hanwella (Kelani Ganga) | 3.10 | 🟢 Normal | -0.030 |  |
| 2026-05-17 15:02:35 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.033 |  |
| 2026-05-17 15:01:48 | Ellagawa (Kalu Ganga) | 7.64 | 🟢 Normal | -0.040 |  |
| 2026-05-17 15:05:52 | Rathnapura (Kalu Ganga) | 2.87 | 🟢 Normal | -0.077 |  |
| 2026-05-17 15:05:38 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.114 |  |
| 2026-05-17 15:08:40 | Magura (Kalu Ganga) | 2.81 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)