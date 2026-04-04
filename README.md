# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_13:04:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,937 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 13:04:01 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.058 |  |
| 2026-04-04 13:04:00 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-04 13:03:50 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-04-04 13:03:49 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-04-04 13:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | -0.060 |  |
| 2026-04-04 13:03:09 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 13:02:49 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:02:42 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 13:02:36 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.051 |  |
| 2026-04-04 13:02:18 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:02:12 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.033 |  |
| 2026-04-04 13:01:53 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:01:52 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:01:52 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:01:20 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-04 13:00:46 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:00:46 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-04 13:00:41 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.216 |  |
| 2026-04-04 13:00:37 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-04-04 13:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-04 13:00:14 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-04-04 12:59:03 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:10:55 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-04 12:09:16 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.171 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 12:09:16 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-04-04 13:03:49 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-04-04 13:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-04 13:04:00 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-04 13:01:20 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-04 12:05:05 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 13:00:46 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-04 13:03:09 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 12:02:04 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 13:02:42 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 12:05:09 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 13:01:52 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:02:18 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:01:53 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:02:10 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:06:10 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:02:49 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:59:03 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:00:46 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:03:17 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:00:40 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:01:52 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:04:47 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-04 13:00:37 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-04-04 12:02:17 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-04-04 13:00:14 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-04-04 12:10:55 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-04 12:06:00 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.011 |  |
| 2026-04-04 13:03:50 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-04-04 12:07:29 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.028 |  |
| 2026-04-04 12:02:30 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-04-04 12:01:40 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-04-04 13:02:12 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.033 |  |
| 2026-04-04 12:01:49 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.040 |  |
| 2026-04-04 13:02:36 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.051 |  |
| 2026-04-04 12:05:22 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.057 |  |
| 2026-04-04 13:04:01 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.058 |  |
| 2026-04-04 13:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | -0.060 |  |
| 2026-04-04 13:00:41 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.216 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)