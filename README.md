# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_02:15:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,224 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 02:15:49 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-16 02:08:51 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:08:23 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.047 |  |
| 2026-04-16 02:06:42 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-16 02:05:48 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.057 |  |
| 2026-04-16 02:04:34 | Glencourse (Kelani Ganga) | 8.99 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-04-16 02:04:30 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:04:21 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:04:14 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:04:01 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-04-16 02:03:42 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:03:09 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:03:02 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.145 |  |
| 2026-04-16 02:02:52 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:02:49 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 1485.000 | 🔺 Rising |
| 2026-04-16 02:02:45 | Badalgama (Maha Oya) | 0.24 | 🟢 Normal | 1485.000 | 🔺 Rising |
| 2026-04-16 02:02:39 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:02:30 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-16 02:02:16 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:02:08 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:02:05 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:02:04 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-16 02:02:00 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.030 |  |
| 2026-04-16 02:01:35 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:01:26 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:01:19 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.010 |  |
| 2026-04-16 02:01:15 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-16 02:00:47 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-16 01:55:43 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.047 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 02:02:49 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 1485.000 | 🔺 Rising |
| 2026-04-16 00:24:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 2.700 | 🔺 Rising |
| 2026-04-16 01:14:14 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | 0.903 | 🔺 Rising |
| 2026-04-16 02:04:01 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-04-16 02:04:34 | Glencourse (Kelani Ganga) | 8.99 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-04-16 00:03:09 | Magura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-16 00:09:08 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-16 02:02:30 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-16 02:06:42 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-16 02:00:47 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-16 02:02:04 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-16 02:15:49 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-16 01:02:56 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 02:02:39 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:01:26 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:01:35 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:02:05 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:00:07 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-15 23:01:48 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:02:16 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:04:14 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-16 01:31:17 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:02:08 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:02:52 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:03:42 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:03:09 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:04:21 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:08:51 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:04:30 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-16 02:01:19 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.010 |  |
| 2026-04-16 02:01:15 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-16 01:03:34 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-04-16 02:02:00 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.030 |  |
| 2026-04-15 18:05:24 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.038 |  |
| 2026-04-16 02:08:23 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.047 |  |
| 2026-04-16 02:05:48 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.057 |  |
| 2026-04-15 18:01:03 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.062 |  |
| 2026-04-16 02:03:02 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.145 |  |
| 2026-04-16 00:00:12 | Wellawaya (Kirindi Oya) | 1.70 | 🟢 Normal | -0.240 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)