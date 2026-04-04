# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_13:47:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,953 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 13:47:30 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:14:07 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-04 13:13:28 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:13:13 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.046 |  |
| 2026-04-04 13:10:30 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:09:25 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.066 |  |
| 2026-04-04 13:09:21 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-04-04 13:08:27 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-04-04 13:08:08 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-04-04 13:07:27 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:06:37 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | -0.028 |  |
| 2026-04-04 13:05:32 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 13:03:49 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-04-04 13:08:27 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-04-04 13:14:07 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-04 13:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-04 13:04:00 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-04 13:01:20 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-04 13:05:32 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-04 13:00:46 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-04 13:03:09 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 13:02:42 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 13:05:16 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 13:01:52 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:02:18 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:01:53 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:47:30 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:04:47 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:02:49 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-04 12:59:03 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:00:46 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:13:28 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:07:27 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:10:30 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:04:09 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:01:52 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-04 13:08:08 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-04-04 13:09:21 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-04-04 13:00:37 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-04-04 13:00:14 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-04-04 13:04:59 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-04-04 13:03:50 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-04-04 13:06:37 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | -0.028 |  |
| 2026-04-04 13:02:12 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.033 |  |
| 2026-04-04 12:01:49 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.040 |  |
| 2026-04-04 13:13:13 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.046 |  |
| 2026-04-04 13:02:36 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.051 |  |
| 2026-04-04 13:04:01 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.058 |  |
| 2026-04-04 13:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | -0.060 |  |
| 2026-04-04 13:09:25 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.066 |  |
| 2026-04-04 13:00:41 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.216 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)