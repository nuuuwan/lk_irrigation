# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_14:01:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **138,242 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 14:01:49 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-04-29 14:01:36 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:01:35 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:01:04 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-04-29 14:00:48 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | -0.036 |  |
| 2026-04-29 14:00:38 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:00:30 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-29 13:36:28 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:17:18 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:13:56 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:12:28 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:12:13 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:10:21 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | -0.011 |  |
| 2026-04-29 13:10:13 | Thanthirimale (Malwathu Oya) | 1.90 | 🟢 Normal | -0.036 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 14:01:49 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-04-29 13:04:19 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-04-29 14:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-29 13:08:34 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-04-29 13:01:13 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:01:35 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:02:31 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:05:06 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:00:38 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:07:57 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:13:56 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:03:15 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:03:13 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:03:28 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:17:18 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:07:26 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:00:56 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:02:43 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:12:13 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:02:29 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:05:25 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:01:36 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:08:08 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:12:28 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-29 14:00:30 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-29 13:07:32 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-04-29 13:01:33 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.010 |  |
| 2026-04-29 14:01:04 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-04-29 13:01:55 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-04-29 13:10:21 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | -0.011 |  |
| 2026-04-29 13:05:13 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.019 |  |
| 2026-04-29 13:07:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.019 |  |
| 2026-04-29 13:04:59 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-04-29 13:02:43 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-04-29 13:04:20 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.033 |  |
| 2026-04-29 14:00:48 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | -0.036 |  |
| 2026-04-29 13:08:50 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.036 |  |
| 2026-04-29 13:01:27 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.042 |  |
| 2026-04-29 13:02:33 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)