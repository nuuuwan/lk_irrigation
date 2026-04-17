# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_22:10:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **127,879 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 22:10:30 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.074 |  |
| 2026-04-17 22:10:05 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-04-17 22:10:05 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:07:38 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-04-17 22:07:26 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.667 | 🔺 Rising |
| 2026-04-17 22:07:13 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-17 22:06:48 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-17 22:06:34 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.047 |  |
| 2026-04-17 22:06:32 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.667 | 🔺 Rising |
| 2026-04-17 22:06:24 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-17 22:06:16 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:05:57 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-17 22:05:49 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:05:04 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:04:10 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:04:03 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:03:52 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:03:52 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.011 |  |
| 2026-04-17 22:03:32 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-17 22:03:26 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:03:14 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:03:03 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.315 | 🔺 Rising |
| 2026-04-17 22:02:55 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:02:44 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | -0.020 |  |
| 2026-04-17 22:02:20 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-17 22:02:09 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.264 |  |
| 2026-04-17 22:02:06 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:01:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-04-17 22:01:40 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:01:19 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:01:17 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:01:12 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 22:01:07 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | -0.010 |  |
| 2026-04-17 22:01:02 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:00:44 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:00:32 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-17 21:59:24 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 22:07:26 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.667 | 🔺 Rising |
| 2026-04-17 22:03:03 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.315 | 🔺 Rising |
| 2026-04-17 22:07:13 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-17 22:05:57 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-17 22:06:48 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-17 22:02:20 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-17 22:01:12 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 18:04:21 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:03:14 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:00:32 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:01:19 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:02:06 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:01:40 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:00:44 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:02:55 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:10:05 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:05:49 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:01:02 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:01:17 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:04:03 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:04:10 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:05:04 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:03:52 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:06:16 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:00:41 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:03:26 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:02:55 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:10:05 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-04-17 22:07:38 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-04-17 22:03:32 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-17 22:06:24 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-17 22:01:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-04-17 22:01:07 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | -0.010 |  |
| 2026-04-17 22:03:52 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.011 |  |
| 2026-04-17 22:02:44 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | -0.020 |  |
| 2026-04-17 21:02:47 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.030 |  |
| 2026-04-17 22:06:34 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.047 |  |
| 2026-04-17 22:10:30 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.074 |  |
| 2026-04-17 22:02:09 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.264 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)