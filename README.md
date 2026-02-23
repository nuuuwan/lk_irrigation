# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--23_06:10:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,626 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 06:10:46 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.076 |  |
| 2026-02-23 06:10:37 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 06:09:25 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.083 |  |
| 2026-02-23 06:08:40 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-02-23 06:07:17 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 06:07:09 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.040 |  |
| 2026-02-23 06:06:27 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-02-23 06:06:10 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-23 06:06:09 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -0.009 |  |
| 2026-02-23 06:06:08 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.047 |  |
| 2026-02-23 06:05:55 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-02-23 06:05:38 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.000 |  |
| 2026-02-23 06:05:32 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | -0.018 |  |
| 2026-02-23 06:04:53 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-02-23 06:04:51 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | -0.221 |  |
| 2026-02-23 06:04:46 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | -0.009 |  |
| 2026-02-23 06:04:27 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.133 |  |
| 2026-02-23 06:03:50 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-02-23 06:03:30 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-02-23 06:03:23 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-23 06:03:21 | Manampitiya (Mahaweli Ganga) | 2.56 | 🟢 Normal | -0.041 |  |
| 2026-02-23 06:03:04 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.066 |  |
| 2026-02-23 06:03:01 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-02-23 06:03:00 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-23 06:02:48 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.012 |  |
| 2026-02-23 06:02:39 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.091 |  |
| 2026-02-23 06:02:37 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-02-23 06:02:26 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.000 |  |
| 2026-02-23 06:01:29 | Weraganthota (Mahaweli Ganga) | -1.49 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-02-23 06:01:18 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-02-23 06:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.11 | 🟢 Normal | -1.093 |  |
| 2026-02-23 06:00:57 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-02-23 06:00:40 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-02-23 06:00:21 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.026 |  |
| 2026-02-23 05:51:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.28 | 🟢 Normal | -1.093 |  |
| 2026-02-23 05:51:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.41 | 🟢 Normal | -1.093 |  |
| 2026-02-23 05:37:03 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-23 05:27:09 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 18:04:47 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-23 06:01:29 | Weraganthota (Mahaweli Ganga) | -1.49 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-02-23 06:00:40 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-02-23 06:03:23 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-23 06:10:37 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 05:16:50 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:01:10 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 06:07:17 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 06:05:38 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.000 |  |
| 2026-02-23 06:03:00 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-23 06:06:10 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-23 05:24:07 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-23 06:01:18 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-02-23 06:08:40 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-02-23 05:06:10 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-02-23 06:04:46 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | -0.009 |  |
| 2026-02-23 06:06:09 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -0.009 |  |
| 2026-02-23 06:04:53 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-02-23 05:02:35 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-02-23 06:06:27 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-02-23 06:02:48 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.012 |  |
| 2026-02-23 06:05:32 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | -0.018 |  |
| 2026-02-23 06:02:37 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-02-23 06:00:57 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-02-23 06:05:55 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-02-23 06:03:50 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-02-23 06:03:30 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-02-23 06:00:21 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.026 |  |
| 2026-02-23 06:03:01 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-02-23 06:07:09 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.040 |  |
| 2026-02-23 06:03:21 | Manampitiya (Mahaweli Ganga) | 2.56 | 🟢 Normal | -0.041 |  |
| 2026-02-23 06:06:08 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.047 |  |
| 2026-02-23 06:03:04 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.066 |  |
| 2026-02-23 06:10:46 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.076 |  |
| 2026-02-23 06:09:25 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.083 |  |
| 2026-02-23 06:02:39 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.091 |  |
| 2026-02-23 06:04:27 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.133 |  |
| 2026-02-23 06:04:51 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | -0.221 |  |
| 2026-02-23 06:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.11 | 🟢 Normal | -1.093 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)