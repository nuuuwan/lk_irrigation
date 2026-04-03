# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_13:18:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,044 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 13:18:41 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:18:13 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:16:12 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-03 13:14:47 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.017 |  |
| 2026-04-03 13:12:05 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:08:59 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.037 |  |
| 2026-04-03 13:08:43 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-03 13:08:26 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:08:11 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:06:48 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-04-03 13:06:02 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:05:20 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-04-03 13:05:16 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | -0.067 |  |
| 2026-04-03 13:05:15 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-03 13:04:56 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 13:04:02 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.013 |  |
| 2026-04-03 13:03:55 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-04-03 13:03:53 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.030 |  |
| 2026-04-03 13:03:49 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-04-03 13:03:39 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-03 13:03:39 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:03:32 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.011 |  |
| 2026-04-03 13:03:29 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | -0.020 |  |
| 2026-04-03 13:03:29 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.005 |  |
| 2026-04-03 13:03:16 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:03:03 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:02:49 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 13:02:33 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:02:23 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-04-03 13:01:43 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:01:40 | Thanthirimale (Malwathu Oya) | 3.14 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-03 13:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 13:01:17 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:01:17 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:00:51 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:00:33 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:00:23 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.359 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 13:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-04-03 13:05:20 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-04-03 13:06:48 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-04-03 13:01:40 | Thanthirimale (Malwathu Oya) | 3.14 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-03 13:05:15 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-03 13:16:12 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-03 13:03:39 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-03 13:02:49 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 13:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 13:04:56 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 12:06:01 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:02:33 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:18:41 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:00:51 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:01:17 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:08:26 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:03:16 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:18:13 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:03:39 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:00:33 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:01:43 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:08:11 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:01:17 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:03:03 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:06:02 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:02:23 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 13:03:29 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.005 |  |
| 2026-04-03 13:03:55 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-04-03 13:08:43 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-03 13:03:32 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.011 |  |
| 2026-04-03 13:04:02 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.013 |  |
| 2026-04-03 13:14:47 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.017 |  |
| 2026-04-03 13:03:29 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | -0.020 |  |
| 2026-04-03 13:03:53 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.030 |  |
| 2026-04-03 13:03:49 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-04-03 13:08:59 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.037 |  |
| 2026-04-03 12:13:15 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.058 |  |
| 2026-04-03 13:05:16 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | -0.067 |  |
| 2026-04-03 13:00:23 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.359 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)