# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_13:24:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,092 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 13:24:12 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-21 13:21:22 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.008 |  |
| 2026-04-21 13:16:16 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-21 13:13:12 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.030 |  |
| 2026-04-21 13:13:04 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-21 13:11:54 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-21 13:07:54 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.021 |  |
| 2026-04-21 13:07:40 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.018 |  |
| 2026-04-21 13:07:29 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | -0.103 |  |
| 2026-04-21 13:07:05 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.123 |  |
| 2026-04-21 13:07:03 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-21 13:06:43 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-04-21 13:06:23 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.047 |  |
| 2026-04-21 13:06:17 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-21 13:06:01 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-21 13:05:59 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-21 13:05:50 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.105 |  |
| 2026-04-21 13:05:45 | Galgamuwa (Mee Oya) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-04-21 13:05:38 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-21 13:05:22 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.022 |  |
| 2026-04-21 13:05:22 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-04-21 13:05:10 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-04-21 13:05:10 | Ellagawa (Kalu Ganga) | 6.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 13:05:02 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.082 |  |
| 2026-04-21 13:04:45 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-21 13:03:24 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.080 |  |
| 2026-04-21 13:03:06 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-21 13:03:03 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.052 |  |
| 2026-04-21 13:02:13 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-21 13:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.060 |  |
| 2026-04-21 13:02:13 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.041 |  |
| 2026-04-21 13:02:10 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | -0.040 |  |
| 2026-04-21 13:02:02 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-21 13:01:37 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 13:01:27 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 13:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-04-21 13:01:08 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 13:00:55 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-21 13:00:11 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 13:05:22 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-04-21 13:03:06 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-21 13:11:54 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-21 12:00:41 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-04-21 13:06:01 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-21 13:05:59 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-21 13:02:13 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-21 13:01:27 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 13:01:08 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 13:05:10 | Ellagawa (Kalu Ganga) | 6.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 13:02:02 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-21 13:13:04 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-21 13:01:37 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 13:00:55 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-21 13:05:38 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-21 13:16:16 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-21 13:06:17 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-21 13:07:03 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-21 13:24:12 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-21 13:21:22 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.008 |  |
| 2026-04-21 13:06:43 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-04-21 13:05:10 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-04-21 13:07:40 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.018 |  |
| 2026-04-21 13:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-04-21 13:00:11 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | -0.020 |  |
| 2026-04-21 13:07:54 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.021 |  |
| 2026-04-21 13:05:45 | Galgamuwa (Mee Oya) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-04-21 13:05:22 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.022 |  |
| 2026-04-21 13:13:12 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.030 |  |
| 2026-04-21 13:02:10 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | -0.040 |  |
| 2026-04-21 13:02:13 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.041 |  |
| 2026-04-21 13:06:23 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.047 |  |
| 2026-04-21 13:03:03 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.052 |  |
| 2026-04-21 13:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.060 |  |
| 2026-04-21 13:03:24 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.080 |  |
| 2026-04-21 13:05:02 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.082 |  |
| 2026-04-21 13:07:29 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | -0.103 |  |
| 2026-04-21 13:05:50 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.105 |  |
| 2026-04-21 13:07:05 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)