# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_12:06:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,911 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 12:06:10 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:06:00 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.011 |  |
| 2026-04-04 12:05:33 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 12:05:22 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.057 |  |
| 2026-04-04 12:05:09 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 12:05:05 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 12:04:51 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.040 |  |
| 2026-04-04 12:04:47 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-04 12:03:17 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:03:12 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.049 |  |
| 2026-04-04 12:03:07 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-04-04 12:03:04 | Thanthirimale (Malwathu Oya) | 2.57 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-04 12:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.12 | 🟢 Normal | -0.050 |  |
| 2026-04-04 12:02:55 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 12:02:30 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-04-04 12:02:19 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-04 12:02:17 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-04-04 12:02:15 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | -0.225 |  |
| 2026-04-04 12:02:10 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:02:08 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:02:07 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:02:04 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 12:01:57 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-04-04 12:01:54 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 12:01:49 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.040 |  |
| 2026-04-04 12:01:42 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:01:40 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-04-04 12:01:36 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-04-04 12:01:26 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.063 |  |
| 2026-04-04 12:01:24 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:01:16 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:00:40 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:00:22 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-04-04 11:17:50 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-04 11:16:02 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:13:42 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.054 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 12:01:36 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-04-04 11:05:10 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-04-04 12:02:19 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-04 12:05:05 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 12:03:04 | Thanthirimale (Malwathu Oya) | 2.57 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-04 12:05:33 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 12:01:54 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 12:02:55 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 12:02:04 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 12:05:09 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 12:01:24 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:02:20 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:01:16 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:02:10 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:06:10 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:01:42 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:02:07 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:03:17 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:00:40 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:02:08 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:01:57 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-04-04 12:04:47 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-04 12:02:17 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-04-04 12:06:00 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.011 |  |
| 2026-04-04 12:00:22 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-04-04 11:07:42 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-04-04 12:03:07 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-04-04 12:02:30 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-04-04 12:01:40 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-04-04 12:01:49 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.040 |  |
| 2026-04-04 12:04:51 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.040 |  |
| 2026-04-04 11:04:12 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.042 |  |
| 2026-04-04 12:03:12 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.049 |  |
| 2026-04-04 12:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.12 | 🟢 Normal | -0.050 |  |
| 2026-04-04 11:13:42 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.054 |  |
| 2026-04-04 12:05:22 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.057 |  |
| 2026-04-04 12:01:26 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.063 |  |
| 2026-04-04 12:02:15 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | -0.225 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)